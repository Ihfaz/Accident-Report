# url_for -- searches for a file in a folder like templates/static
# Markup -- converts strings to HTML tags

from flask import Flask, render_template, url_for, Markup, flash, redirect, request, Response
from forms import RegistrationForm, LoginForm
from pymongo import MongoClient
from flask import jsonify
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b924439ea2514672da218f4a7fba3f0e'

# Database access
# client = MongoClient("mongodb+srv://admin:utdallas123@accidentreport-qad27.mongodb.net/test?retryWrites=true&w=majority")
# db = client['accident_reports']
# accident = db['accident']

# Report page
#@app.route("/")
@app.route("/report")
def report():
    client = __get_mongo_client()
    db = client['accident_reports']
    accident = db['accident']

    i_content = 'assets/insta_demo.jpg'    # Instagram content
    
    # Twitter content

    # Tesla tweet --
    # tesla_solar = '<blockquote class="twitter-tweet" data-width="550"><p lang="en" dir="ltr">Get Tesla Solar plus Powerwall battery for 24/7 clean power &amp; no more blackouts! <a href="https://t.co/mDoPO17YB9">https://t.co/mDoPO17YB9</a></p>&mdash; Elon Musk (@elonmusk) <a href="https://twitter.com/elonmusk/status/1182812717083611138?ref_src=twsrc%5Etfw">October 12, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    # # DFW Accident --
    # dfw_accident = '<blockquote class="twitter-tweet"><p lang="en" dir="ltr">CLEARED - accident:I-30 westbound IH35E Dallas various Lns blocked</p>&mdash; 511DFW_Dallas (@511DFWDallas) <a href="https://twitter.com/511DFWDallas/status/1188683916070313984?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    # # twitter_embed = 
    # t_content = Markup(tesla_solar)
    
    
    # TODO -- pull this data from DB
    data = accident.find_one()
    if data is None:
        return "<h1>Error 404: Content Not Found</h1>"


    tweets = sorted(data['related_tweets'], key=lambda k: k['relevancy_score'], reverse=True)   # Sort tweets according to relevancy
    insta = sorted(data['instagram_posts'], key=lambda k: k['relevancy_score'], reverse=True)   # Sort insta posts according to relevancy
      
    summary = data['summary']+"\nType of injury: "+data['type_of_injury']+"\nNumber of people affected: "+str(data['num_people_affected'])+"\nTime of occurence: "+data['occur_time']    # Summary content
    lat = data['geolocation']['latitude']
    long = data['geolocation']['longitude']
    
    loc_link = "window.open('https://www.latlong.net/c/?lat=%s&long=%s');" %(lat, long)

    client.close
    return render_template('report_layout.html', insta=insta, tweets=tweets, summary=summary, i_content=i_content, loc_link=loc_link)


@app.route("/search")
def search():
    return render_template('search.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    username = form.username.data
    if form.validate_on_submit():
        flash('Account created for %s!' %username, 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Registration', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Dummy login validation
        if form.email.data == 'ihfaz@utdallas.edu' and form.password.data == '1234':
            # flash('Successful login!', 'success')
            return redirect(url_for('search'))
        else:
            flash('Login unsuccessful', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route('/upload', methods=["POST"])
def upload_data():
    client = __get_mongo_client()
    db = client['accident_reports']
    accident = db['accident']

    data = request.data
    #data = json.loads(data)
    data = request.get_json('data')
    # return Response(200)

    newID = data['_id']
    # If the document already exists
    if accident.find({ '_id': newID}).count() > 0:
        accident.update({'_id': newID}, {'$set': data})
        #return jsonify(success=True) #have to return a response
        return "<h1>UPDATED -- ID: %s</h1>" %newID
    else:
        accident.insert_one(data)
        client.close()
	#return jsonify(success=True) #have to return a response
        return "<h1>NEW ENTRY -- ID: %s</h1>" %newID
  
        
    client.close()#never reaches this statement
    #return jsonify(success=True) #have to return a response
    return ""

def __get_mongo_client():
    MONGO_SERVER_IP = "172.29.100.22"
    MONGO_PORT = "3154"
    MONGO_USER = "event_reader"
    MONGO_PSWD = "dml2016"
    NUM_ARTICLES = 1000

    password = MONGO_PSWD
    #return MongoClient('mongodb://' + MONGO_USER + ':' + password + '@' + MONGO_SERVER_IP + ":" + MONGO_PORT)
    return MongoClient(port=3154)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
# url_for -- searches for a file in a folder like templates/static
# Markup -- converts strings to HTML tags

from flask import Flask, render_template, url_for, Markup, flash, redirect, request, Response
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b924439ea2514672da218f4a7fba3f0e'

# Report page
@app.route("/")
@app.route("/report")
def report():
    i_content = 'assets/insta_demo.jpg'    # Instagram content
    
    # Twitter content

    # Tesla tweet --
    tesla_solar = '<blockquote class="twitter-tweet" data-width="550"><p lang="en" dir="ltr">Get Tesla Solar plus Powerwall battery for 24/7 clean power &amp; no more blackouts! <a href="https://t.co/mDoPO17YB9">https://t.co/mDoPO17YB9</a></p>&mdash; Elon Musk (@elonmusk) <a href="https://twitter.com/elonmusk/status/1182812717083611138?ref_src=twsrc%5Etfw">October 12, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    # DFW Accident --
    dfw_accident = '<blockquote class="twitter-tweet"><p lang="en" dir="ltr">CLEARED - accident:I-30 westbound IH35E Dallas various Lns blocked</p>&mdash; 511DFW_Dallas (@511DFWDallas) <a href="https://twitter.com/511DFWDallas/status/1188683916070313984?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    # # twitter_embed = 
    # t_content = Markup(tesla_solar)
    
    
    # TODO -- pull this data from DB
    data = {
            "id": "1234",
            "summary": "Some summary",
            "type_of_injury": "Severe",
            "num_people_affected": 3,
            "reported_locations": ["Lagos", "Lagos-Ibadan expy"],
            "occur_time": "1620",
            "related_tweets": [
                {
                    "username":"ihfaz98",
                    "message": "Accident on I-35 highway. Police have arrived on site.",
                    "relevancy_score": 0.0,
                    "key_terms": ["a", "b", "c"]
                },
                {
                    "username":"zunayed98",
                    "message": "Car crash on highway. Seems like 4 people were injured.",
                    "relevancy_score": 1.0,
                    "key_terms": ["a", "d", "c"]
                },
                {
                    "username":"zunayed98",
                    "message": "Car crash on highway. Seems like 4 people were injured.",
                    "relevancy_score": 1.0,
                    "key_terms": ["a", "d", "c"]
                },
                {
                    "username":"zunayed98",
                    "message": "Car crash on highway. Seems like 4 people were injured.",
                    "relevancy_score": 1.0,
                    "key_terms": ["a", "d", "c"]
                },
                {
                    "username":"zunayed98",
                    "message": "Car crash on highway. Seems like 4 people were injured.",
                    "relevancy_score": 1.0,
                    "key_terms": ["a", "d", "c"]
                },
                {
                    "username":"zunayed98",
                    "message": "Car crash on highway. Seems like 4 people were injured.",
                    "relevancy_score": 1.0,
                    "key_terms": ["a", "d", "c"]
                }

            ],

            "instagram_posts": [
                {
                    "username": "ihfaz98",
                    "relevancy_score": 0.0,
                    "images": [
                        {
                        "image_url": "",
                        "caption": "Image caption 1"
                        },
                        {
                        "image_url": "",
                        "caption": "Image caption 2"
                        }
                    ],
                    "key_terms": ["s", "d"]
                }
            ]

        }


    tweets = sorted(data['related_tweets'], key=lambda k: k['relevancy_score'], reverse=True)   # Sort tweets according to relevancy
      
    summary = Markup('<p>*Summary about recent accident*</p>')    # Summary content

    return render_template('report_layout.html', i_content=i_content, tweets=tweets, summary=summary)


@app.route("/search")
def search():
    return render_template('search.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
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


@app.route('/upload', methods=['POST'])
def upload_data():
    # data = request.args.get('data')
    data = request.get_json('data')
    process_data(data)
    return f"<h1>DATA = {data}</h1>"
    # return Response(200)


def process_data(data):
    print(data['id'])


if __name__ == '__main__':
    app.run(debug=True)
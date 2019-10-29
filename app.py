# url_for -- searches for a file in a folder like templates/static
# Markup -- converts strings to HTML tags

from flask import Flask, render_template, url_for, Markup
app = Flask(__name__)

# Report page
@app.route("/")
@app.route("/report")
def report():
    i_file = 'assets/insta_demo.jpg'    # Instagram content

    # Twitter content

    # Tesla tweet --
    tesla_solar = '<blockquote class="twitter-tweet" data-width="550"><p lang="en" dir="ltr">Get Tesla Solar plus Powerwall battery for 24/7 clean power &amp; no more blackouts! <a href="https://t.co/mDoPO17YB9">https://t.co/mDoPO17YB9</a></p>&mdash; Elon Musk (@elonmusk) <a href="https://twitter.com/elonmusk/status/1182812717083611138?ref_src=twsrc%5Etfw">October 12, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    # DFW Accident --
    dfw_accident = '<blockquote class="twitter-tweet"><p lang="en" dir="ltr">CLEARED - accident:I-30 westbound IH35E Dallas various Lns blocked</p>&mdash; 511DFW_Dallas (@511DFWDallas) <a href="https://twitter.com/511DFWDallas/status/1188683916070313984?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'

    # twitter_embed =
    t_content = Markup(tesla_solar)
    # Summary content
    summary = Markup('<p>*Summary about beaudy accident*</p>')

    return render_template('report_layout.html', i_file=i_file, t_content=t_content, summary=summary)

# Search page
@app.route("/search")
def search():
    return render_template('search.html', Z=name)


if __name__ == '__main__':
    app.run(debug=True)

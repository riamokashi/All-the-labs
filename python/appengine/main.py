import webapp2
import jinja2
import os
from files import MemeInfo
from google.appengine.api import urlfetch
import json
#this initializes the jinja2 environment
#this is going to be the same for every app you build!!
#jinja2.Environment if a constructor

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



#the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):
        api_url = "https://api.imgflip.com/get_memes"
        imgflip_response = urlfetch.fetch(api_url).content
        imgflip_response_json = json.loads(imgflip_response)
        print(imgflip_response_json['data']['memes'])
        meme_templates = []
        for meme_template in imgflip_response_json['data']['memes']:
            meme_templates.append(meme_template["url"])
        meme_dict = {
        "imgs": meme_templates
        }
        welcome_template = jinja_env.get_template('welcome.html')
        self.response.write(welcome_template.render(meme_dict))
    def post(self):
        top_line = self.request.get("top-line")
        print(top_line)
        bottom_line = self.request.get("bottom-line")
        print(bottom_line)

class ResultPage(webapp2.RequestHandler):
    def post(self):
        top_line = self.request.get("top-line")
        bottom_line = self.request.get("bottom-line")
        meme_url = self.request.get("template")
        data_dict = {
        "top": top_line,
        "bottom": bottom_line,
        "url": meme_url
        }

        #creates meme object and stores it into datastore
        meme1 = MemeInfo(memeUrl=meme_url, memeTop=top_line, memeBottom=bottom_line)
        meme1.put()
        result_template = jinja_env.get_template("result.html")
        self.response.write(result_template.render(data_dict))

class AllMemesPage(webapp2.RequestHandler):
    def get(self):
        all_memes = MemeInfo.query().fetch()
        meme_dict = {
            "memes": all_memes
        }
        result_template = jinja_env.get_template("allmemes.html")
        self.response.write(result_template.render(meme_dict))





#the app configuration section
app = webapp2.WSGIApplication(
    [
    ('/', MainPage),
    ('/result', ResultPage),
    ('/allmemes', AllMemesPage)
    ],
    debug = True
)

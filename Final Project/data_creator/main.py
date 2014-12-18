
import logging
import json
import os
import webapp2

from google.appengine.ext.webapp import template

class Main(webapp2.RequestHandler):
    def get(self):
        logging.debug('Serving main page')
        path = os.path.join(os.path.dirname(__file__), "index.html")
        self.response.out.write(template.render(path, {}))


application = webapp2.WSGIApplication([
    ('/.*', Main)
], debug=True)


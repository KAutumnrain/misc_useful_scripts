from defusedxml.ElementTree import parse
from flask import Flask
from flask import request
import gunicorn
import os
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

#----------------------------------#
#                                  |
#      XML translation script      |
#      Written by KAutumnrain      |
#                                  |
#----------------------------------#

# Warning; the other purpose of this
# script, being to actually take this 
# data somewhere else, hasn't been 
# implemented yet, but once I have a 
# more-complete picture  


# We're using a flask app for this because
# it's easier :3
app = Flask(__name__)

# Requests will go to <ip>:<port>/listener
@app.route("/listener", methods=['GET','POST'])
def xml_listen():
	# Don't load your JSON too many times, kiddos!
	postXmlData = json2xml.Json2xml(request.get_json()).to_xml()
	return postXmlData
	




if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 1337)))

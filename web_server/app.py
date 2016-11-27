import subprocess
import flask
from subprocess import check_output
from flask import Flask, render_template, Response, request
import re

app = Flask(__name__)

def get_data():
    try:
	p = check_output(["~/openface/demos/classifier_mod.py infer '/root/openface/generated-embeddings/classifier_RadialSvm.pkl' '/root/openface/shared/1.jpg'"], shell=True)
    	return p
    except subprocess.CalledProcessError, e:
	print  e.output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def upload_files():
    resp = flask.make_response()
    request.files['image'].save('/root/openface/shared/1.jpg')
    resp.status_code = 204
    result = get_data()
    result = result.split(',',1)
    result[0] = re.sub(r'\s===.+===\s','', result[0])
    result[1] = str(float(result[1][:7])*100)
    if float(result[1]) > 60.0:
    	guess_message = "I see " + result[0] + " with " + result[1] + "% confidence."
    else:
	guess_message = "I'm not sure!"

    return render_template('index.html', guess = guess_message)

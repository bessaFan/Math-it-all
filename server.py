import json
import time
import glob
import os
from tsne_lib import tsne_script
from shutil import copyfile
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import uuid
from IPython import embed

#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = 'static/uploads'
#app.config['MAX_CONTENT_LENGTH'] = 300 * 1024 * 1024 # Allow 300 MiB maximum upload for all images at once
#FILE_SIZE_LIMIT = 3 * 1024 * 1024 # 3 MiB
#NUM_IMAGES_LIMIT = 100

@app.route("/")
def main():
    return render_template('main.html')


@app.route("/calculation", methods=['POST', 'GET'])
def calculation():
    CommonDifference = int (request.args.get('CommonDifference'))
    FirstTerm = int (request.args.get('FirstTerm'))
    TermNumber = int (request.args.get('TermNumber'))
    #colors_text = colors_text.replace("'",'"')
    #colors_dict = json.loads(colors_text)
    #tsne_data = tsne_script.tsne_images(session_id, colors_dict, resolution, perplexity,early_exaggeration, learning_rate, DotsPerInchs,CanvasSize, colors)
    
    return redirect('/?session=%s' % session_id)

if __name__ == "__main__":
    app.run(debug = True, port=2000)

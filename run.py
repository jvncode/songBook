from flask import render_template, redirect, url_for, request
from flask import Flask
from controller.apiData import apiConnect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('home.html')
    if request.method == "POST":
        search = request.form.get('letter')
        message = ""
        if search == "":
            message = "Introduce alguna canción para poder ayudarte..."
            return render_template('home.html', message=message)
        return redirect(url_for('results', search=search))


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == "GET":
        apiController = apiConnect(request.args.get('search'))
        dataShazam = apiController.getShazam()
        #dataMusix = apiController.getMusixMatch()
        #dataLAST = apiController.getLastFM()
        dictShazam = {}
        for ix in range(len(dataShazam['tracks']['hits'])):
            dictShazam[ix] = {'id': ix,
                              'song': dataShazam['tracks']['hits'][ix]['track']['title'],
                              'artist': dataShazam['tracks']['hits'][ix]['track']['subtitle'],
                              'image': dataShazam['tracks']['hits'][ix]['track']['share']['image'],
                              'video': dataShazam['tracks']['hits'][ix]['track']['share']['href']
                              }
            numHits = len(dictShazam)
        return render_template('resultSongs.html',
                               dataShazam=dictShazam,
                               numHits=numHits,
                               # dataMusix=dataMusix,
                               # dataLAST=dataLAST
                               )
    if request.method == "POST":
        return redirect(url_for('home'))


app.run(debug=True)

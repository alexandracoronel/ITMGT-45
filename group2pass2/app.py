from flask import Flask, redirect
from flask import render_template
from flask import request
import database as db
import os

app = Flask(__name__)

picsFolder =os.path.join('static', 'pics')

app.config['UPLOAD_FOLDER'] = picsFolder

@app.route('/')
def index():
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png') #logophoto #logophoto
    pics6 = os.path.join(app.config['UPLOAD_FOLDER'], 'button1.jpg')
    pics7 = os.path.join(app.config['UPLOAD_FOLDER'], 'button2.png')
    pics8 = os.path.join(app.config['UPLOAD_FOLDER'], 'button3.png')
    return render_template('home.html', user_images1=pics1, user_images7=pics7, user_images8=pics8, user_images6=pics6)

@app.route('/roster')
def roster():
    pics2 = os.path.join(app.config['UPLOAD_FOLDER'], 'currystats.png')
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png')
    return render_template('roster.html', user_images2 = pics2, user_images1 = pics1)

@app.route('/curryroster')
def curryroster():
    pics2 = os.path.join(app.config['UPLOAD_FOLDER'], 'currystats.png')
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png')
    return render_template('curryroster.html', user_images2 = pics2, user_images1 = pics1)


@app.route('/jamesroster')
def jamesroster():
    pics3 = os.path.join(app.config['UPLOAD_FOLDER'], 'ljamesstats.png')
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png') 
    return render_template('jamesroster.html', user_images3 = pics3, user_images1 = pics1)

@app.route('/giannisroster')
def giannisroster():
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png') 
    pics4 = os.path.join(app.config['UPLOAD_FOLDER'], 'giannis.png')
    return render_template('giannisroster.html', user_images4=pics4, user_images1 = pics1)

@app.route('/ldoncicroster')
def ldoncicroster():
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png') 
    pics5 = os.path.join(app.config['UPLOAD_FOLDER'], 'ldoncic.png')
    return render_template('ldoncic.html', user_images1=pics1, user_images5=pics5)

@app.route('/njokicroster')
def njokicroster():
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png') 
    pics6 = os.path.join(app.config['UPLOAD_FOLDER'], 'njokicroster.png')
    return render_template('njokicroster.html', user_images1=pics1, user_images6=pics6)

@app.route('/home')
def home():
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png') 
    pics6 = os.path.join(app.config['UPLOAD_FOLDER'], 'button1.jpg')
    pics7 = os.path.join(app.config['UPLOAD_FOLDER'], 'button2.png')
    pics8 = os.path.join(app.config['UPLOAD_FOLDER'], 'button3.png')
    return render_template('home.html', user_images1 = pics1, user_images7=pics7, user_images8=pics8, user_images6=pics6)

@app.route('/yummy')
def yummy():
    return render_template('yummy.html')

@app.route('/profile')
def profile():
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png') 
    return render_template('profile.html', user_images1=pics1)


@app.route('/standings')
def branches():
    branch_list = db.get_branches()
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png') 
    return render_template('standings.html', page="Branches",  user_images1=pics1, branch_list=branch_list)

@app.route('/matchups')
def matchups():
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png')
    m1 = os.path.join(app.config['UPLOAD_FOLDER'], 'teamgiannis.png')
    m2 = os.path.join(app.config['UPLOAD_FOLDER'], 'teammagic.png')
    return render_template('matchups.html', page="matchups",  user_images1=pics1, m1=m1, m2=m2)

@app.route('/messages')
def messages():
    pics1 = os.path.join(app.config['UPLOAD_FOLDER'], 'nba (1).png')
    pfp1 = os.path.join(app.config['UPLOAD_FOLDER'], 'teamrocket.png')
    pfp2 = os.path.join(app.config['UPLOAD_FOLDER'], 'dog.png')
    pfp3 = os.path.join(app.config['UPLOAD_FOLDER'], 'cat.jpeg')
    pfp4 = os.path.join(app.config['UPLOAD_FOLDER'], 'kanye.jpeg')
    pfp5 = os.path.join(app.config['UPLOAD_FOLDER'], 'edward.jpeg')
    pfp6 = os.path.join(app.config['UPLOAD_FOLDER'], 'meme.jpeg')
    pfp7 = os.path.join(app.config['UPLOAD_FOLDER'], 'mike.jpeg')
    return render_template('messages.html', page="matchups",  user_images1=pics1, pfp1=pfp1, pfp2=pfp2, pfp3=pfp3, pfp4=pfp4, pfp5=pfp5, pfp6=pfp6, pfp7=pfp7 )



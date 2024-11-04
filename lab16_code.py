from flask import Flask, render_template , send_file
from flask_bootstrap import Bootstrap5
from dog_fav import dogs_favorite_toy
from PIL import Image, ImageOps 
import random

app = Flask(__name__)

image_paths = [ "static/dog_1.jpg", "static/dog_2.jpg", "static/dog_3.jpg" ] 
images = [Image.open(path) for path in image_paths]

@app.route('/')
def t_test():
   return render_template('my_template_1.html', toys=dogs_favorite_toy)

@app.route('/random')
def ran_img():
   ran_select_img= random.choice(images)
   neg_ran_select_img= ImageOps.invert(ran_select_img.convert("RGB"))
   temp_path = "static/temp_negative.jpg" 
   neg_ran_select_img.save(temp_path) 
   return send_file(temp_path, mimetype='image/jpeg')

bootstrap = Bootstrap5(app)
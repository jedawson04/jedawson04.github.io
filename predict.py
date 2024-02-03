# python file for predicting on the input data accessed through PyScript

# here we can load the models and predict on them

"""
might look something like this -- assuming the sentiment model and classification model are stored in a models folder

sentiment = load_learner(./Models/Sentiment)
class = load_learner(./Models/Classification)

sentiment.predict(data)
class.predict(data)

depending on how these outputs look we can do something with them and then send them back to the js file somehow
"""
from fastai.text.all import *
from fastai.learner import * # put these in the json file
from pyscript import document 

def predict(event):
    input_text = document.querySelector("#prediction") # grabs the users entered text to predict on
    data = input_text.value 
    output_div = document.querySelector("#output")
    output_div.innerText = data # currently spits the data back out


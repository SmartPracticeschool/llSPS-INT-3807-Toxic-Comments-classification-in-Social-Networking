# llSPS-INT-3807-Toxic-Comments-classification-in-Social-Networking
# Toxic Comments classification in Social Networking
---

## Overview:
	The threat of abuse and harassment online prevent many people from expressing themselves and make them give up on seeking different opinions. Platforms struggle to effectively facilitate conversations, leading many communities to limit or completely shut down user comments. Therefore, we have built a model using Convolutional Neural Network (CNN) and Natural Language Processing (NLP) that can predict the toxicity of these comments.
---

## Dataset:
	The dataset we are using consists of comments from Wikipedia’s talk page edits. These comments have been labeled by human raters for toxic behavior. The types of toxicity are:
- toxic
- severe_toxic
- obscene
- threat
- insult
- identity_hate
---

## Software requirements:
- Text editor / IDE: Jupyter Notebook / Spyder
- Language: Python, HTML, CSS
- Distribution software: Anaconda
- Framework: Flask
---

## Libraries required:
- numpy
- pandas
- matplotlib.pyplot
- seaborn
- re
- string
- nltk
- itertools
- tensorflow.keras
- sklearn
- joblib
	These libraries can be installed using the package manager pip.
---

## Steps involved in building the project:
- Install and import the required libraries.
- Load the test and train datasets.
- Preprocess the data.
- Perform data visualization.
- Clean the raw comments using NLP techniques.
- Tokenize the comments.
- Build a CNN model to make the predictions.
- Train and save the model.
- Design a web application using Flask and integrate the saved model.
---

## Running the project:
- Install all the required libraries.
- Unzip the dataset file in the project directory.
- Open the TCC-CNN.ipynb file in your Jupyter Notebook and run all cells. The trained model will be saved in your directory.
- Open Anaconda Prompt. Navigate to the project directory path and run the following command:
  	python app.py
- Copy paste the URL in the browser to open the web application.
- Enter the comment and click on Predict to get the output.
---

## Project Associates:
- Sonika Prakash
- Poornima G B
- Spoorthi R S
- Anu Bai B
- Ramyashree G T

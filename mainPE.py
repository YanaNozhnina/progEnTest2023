import io
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions

from bs4 import BeautifulSoup
import requests


@st.cache(allow_output_mutation=True)
def load_model():
    return EfficientNetB0(weights='imagenet')


def preprocess_image(img):
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x


def load_image():
    uploaded_file = st.file_uploader(label='Choose image')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None


def print_predictions(preds):
    classes = decode_predictions(preds, top=3)[0]
    for cl in classes:
        st.write(cl[1], cl[2])

def getContent_1(thingNameLst):
	thingName = ''
	firstWord = True
	for word in thingNameLst:
		if firstWord:
			thingName = thingName + word
			firstWord = False
		else:
			thingName = thingName + '+' + word
	
	url = f'https://diyprojects.com/?s={thingName}'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	page = requests.get(url, headers=headers, verify=False)
	
	filteredData = []
	allData = []
	
	soup = BeautifulSoup(page.text, "html.parser")
	
	allData = soup.findAll('article')
	for data in allData:
		filtered = []
		if data.find('a', attrs={'class': 'entry-title-link'}) is not None:
			filtered.append(data.find('a', attrs={'class': 'entry-title-link'}).get('href'))
			filtered.append(data.find('a', attrs={'class': 'entry-title-link'}).text)
			filtered.append(data.find('img', attrs={'class': 'alignleft post-image entry-image'}).get('src'))
			filtered.append(data.find('div', attrs={'class': 'entry-content'}).find('p').text)
			filteredData.append(filtered)
	
	return filteredData

def getContent_2(thingNameLst):
	thingName = ''
	firstWord = True
	for word in thingNameLst:
		if firstWord:
			thingName = thingName + word
			firstWord = False
		else:
			thingName = thingName + '%20' + word
	
	url = f'https://www.hometalk.com/search/all?filter={thingName}'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	page = requests.get(url, headers=headers)
	
	filteredData = []
	allData = []
	
	soup = BeautifulSoup(page.text, "html.parser")
	
	allData = soup.find_all('div', {'class': 'media-component relative js-pin-item'})
	for data in allData:
		filtered = []
		if (data.find('a', attrs={'class': 'js-card-img'}) is not None) and ((data.find('img') is not None)):
			filtered.append('https://www.hometalk.com' + data.find('a', attrs={'class': 'js-card-img'}).get('href'))
			filtered.append(data.find('img').get('alt'))
			#filtered.append(data.find('div', {'class': 'post-body'}).find('a').text)
			filtered.append(data.find('img').get('data-src'))
			filtered.append(None)
			filteredData.append(filtered)
			
	return filteredData

def getContent_3(thingNameLst):
	thingName = ''
	firstWord = True
	for word in thingNameLst:
		if firstWord:
			thingName = thingName + word
			firstWord = False
		else:
			thingName = thingName + '+' + word
	
	url = f'https://diyjoy.com/?s={thingName}'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	page = requests.get(url, headers=headers)
	
	filteredData = []
	allData = []
	
	soup = BeautifulSoup(page.text, "html.parser")
	
	allData = soup.findAll('article')
	for data in allData:
		filtered = []
		if data.find('a', attrs={'class': 'video-index-block-img-link'}) is not None:
			filtered.append(data.find('a', attrs={'class': 'video-index-block-img-link'}).get('href'))
			filtered.append(data.find('a', attrs={'class': 'video-index-block-img-link'}).get('title'))
			filtered.append(data.find('img').get('src'))
			filtered.append(data.find('div', attrs={'class': 'entry-summary'}).find('p').text)
			filteredData.append(filtered)
	
	return filteredData



def showMap():
	data = [56.8519, 60.6122]
	df = pd.DataFrame(data,
    columns=['lat', 'lon'])
	st.map(df)

def printDiyData(thingNameLst):
	diyData = getContent_1(thingNameLst) + getContent_2(thingNameLst) + getContent_3(thingNameLst) 
	if len(diyData) < 10:
		x = len(diyData)
	else:
		x = 10
	for i in range(x):
		st.header(diyData[i][1])
		st.write(diyData[i][0])
		st.image(diyData[i][2])
		if diyData[i][3] != None:
			st.write(diyData[i][3])
		st.write('------------------')
	
def diyButton(img, model, candidateId): # Не используется
	if candidateId < 2: 
		candidateId += 1
		x = preprocess_image(img)
		preds = model.predict(x)
		classes = decode_predictions(preds, top=3)[0]
		thingNameLst = classes[candidateId][1].split('_')
		printDiyData(thingNameLst)
		diyButton(img, model, candidateId)
		showMap()
	else:
		st.write("sorry, don't know what it is.")

def predict(img, model, candidateId):
	switch = candidateId
	x = preprocess_image(img)
	preds = model.predict(x)
	#st.write('**Результаты распознавания:**')
	#print_predictions(preds)
	classes = decode_predictions(preds, top=3)[0]
	st.subheader(f'it is a {classes[candidateId][1]}')
	thingNameLst = classes[candidateId][1].split('_')
	printDiyData(thingNameLst)
	return switch
	

model = load_model()


st.title('Give it a chance!')
img = load_image()
result = st.button('Scan image')
switch = 1
giveInstructions = True
if result:
	candidateId = 0
	switch = predict(img, model, candidateId)
	giveInstructions = False
#st.write(switch)
	
if st.button('No, it\'s NOT.'):
	candidateId = 1
	switch = predict(img, model, candidateId)
	giveInstructions = False
#st.write(switch)

if switch == 1:
	if st.button('No! You are wrong!'):
		candidateId = 2
		predict(img, model, candidateId)
		giveInstructions = True

if giveInstructions:
	if st.button('How do I utilize it?'):
		st.write('this is a placeholder')
		

	
	

import os
import sys
import json
from flask import Flask, render_template, request,redirect,url_for,send_from_directory
from werkzeug import secure_filename
app = Flask(__name__)
#from GoogleSpeechToText import run_quickstart
#from PIL import Image
#import pygal
import numpy as np
UPLOAD_FOLDER = '/home/gajendra/Singularity/singularity/Audio'
ALLOWED_EXTENSIONS = set(['wav','mp4'])
#rootdir = '/home/gajendra/Images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#jsonoutput={"text": "", "value": ""}
global SentimentCount
#SentimentCount=[]
@app.route('/upload')
def hello_world():
    return render_template('index.html')
@app.route('/uploader',methods = ['POST'])
def uploader_files():
    #print("1")
    jsonoutput={"text": "", "value": ""}
    #jsonoutput={}
    if request.method == 'POST':
        #jsonoutput.clear()
        f = request.files['file']
        #jsonoutput={}
        #print(request.files)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        test_audio_path =  os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        #print("test_audio_path",test_audio_path)
        from GoogleSpeechToText import run_quickstart
        ToxicityLevel,output=run_quickstart(test_audio_path)
        #print("ToxicityLevel",ToxicityLevel)
        #jsonoutput[output]=ToxicityLevel
        jsonoutput["text"]=output
        jsonoutput["value"]=ToxicityLevel
    #print("jsonoutput",jsonoutput["text"])
    jsonoutput1=json.dumps(jsonoutput,indent=2)
    jsonoutput1 = json.loads(jsonoutput1)
    jsonoutput.clear()
    #print("jsonoutput1",jsonoutput1)
    return render_template('Display.html',Output=jsonoutput1)

@app.route('/fileuploader')
def upload_files():
	#jsonoutput={"text": "", "value": ""}
	jsonoutput={}
	global SentimentCount
	SentimentCount=[]
	from GoogleSpeechToText import run_quickstart
	for dirpath, dirnames, filenames in os.walk('/home/gajendra/Singularity/singularity/Audio'):
		for indivisualfile in filenames:
			test_audio_path=os.path.join(dirpath,indivisualfile)
			print("test_audio_path",test_audio_path)
			textvalue=[]
			ToxicityLevel,output=run_quickstart(test_audio_path)
			textvalue.append(output)
			textvalue.append(ToxicityLevel)
			SentimentCount.append(ToxicityLevel)
			#jsonoutput["text"]=output
			#jsonoutput["value"]=ToxicityLevel
			jsonoutput[indivisualfile]=textvalue
	#print("jsonoutput",jsonoutput)
	jsonoutput1=json.dumps(jsonoutput,indent=2)
	jsonoutput1 = json.loads(jsonoutput1)
	jsonoutput.clear()
    #print("jsonoutput1",jsonoutput1)
	return render_template('Displayfile.html',Output=jsonoutput1)

@app.route('/DisplayPercentageSentiment')
def display_head():
	labels = "Satisfied","Not Satisfied","Very Satisfied","Very UnSatisfied"
	colors = ['green', 'red',"yellow","blue"]
	SatisfiedCount = SentimentCount.count("Satisfied")
	NotSatisfiedCount = SentimentCount.count("Not Satisfied")
	VerySatisfiedCount = SentimentCount.count("Very Satisfied")
	VeryUnSatisfiedCount = SentimentCount.count("Very UnSatisfied")
	values=[SatisfiedCount,NotSatisfiedCount,VerySatisfiedCount,VeryUnSatisfiedCount]
	#labels = [
	#'JAN', 'FEB', 'MAR', 'APR',
	#'MAY', 'JUN', 'JUL', 'AUG',
	#'SEP', 'OCT', 'NOV', 'DEC']
	#values = [
	#967.67, 1190.89, 1079.75, 1349.19,
	#2328.91, 2504.28, 2873.83, 4764.87,
	#4349.29, 6458.30, 9907, 16297]

	#colors = [
	#"#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
	#"#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
	#"#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
	#values=[1, 1, 1, 1]
	values=[SatisfiedCount,NotSatisfiedCount,VerySatisfiedCount,VeryUnSatisfiedCount]
	print("SatisfiedCount=", SatisfiedCount)

	#return render_template('chart.html', max=17000,set=zip(values, labels, colors))
	return render_template('chart.html', max=17000,values=values, labels=labels, colors=colors)
	#sizes = [SatisfiedCount, NotSatisfiedCount,VerySatisfiedCount,VeryUnSatisfiedCount]
	#explode = (0, 0.1,0,0)
	#label=["Satisfied= %s" %SatisfiedCount,"Not Satisfied= %s" %NotSatisfiedCount,"Very Satisfied= %s" %VerySatisfiedCount,"Very UnSatisfied= %s" %VeryUnSatisfiedCount]
	#fig1, ax1 = plt.subplots()
	#ax1.pie(sizes, explode=explode, labels=labels,colors=colors,autopct='%1.1f%%',shadow=True, startangle=90)
	#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	#ax1.legend(label,loc="upper right")
	#ax1.set_title('Sentiment Visualization')
	#plt.show()
	
	#return "Successfully Displayed"
if __name__ == '__main__':
    app.debug = True
    app.run(host='10.142.56.96')



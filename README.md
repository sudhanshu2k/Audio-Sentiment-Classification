# Audio-Sentiment-Classification

# Installation
    apt-get -y update
    apt-get install -y software-properties-common
    apt-get install -y python3.5 python3-pip
    apt install -y python3-numpy
		pip3 install Flask
		pip3 install --upgrade google-cloud-speech
		pip3 install pydub
		pip3 install -U textblob
		python3 -m textblob.download_corpora
		
# Environment
 export GOOGLE_APPLICATION_CREDENTIALS="/Speech-fbc4fe2b0e6c.json"

# Run the application

Modify IP in view.py with the IP of your system or replace it with local host
Use the following command to run python file:
python3 views.py

To upload Audio file from your system.Paste following URL into your browser:
http://localhost:5000/upload

To Test the application on set of Audio file placed inside folder:
http://localhost:5000/fileuploader



 


#SpeechtoText={}
#Output=[]
#Chunkfile=[]
def run_quickstart(file_name):
	SpeechtoText={}
	Output=[]
	Chunkfile=[]
	# [START speech_quickstart]
	import io
	import os
	# Imports the Google Cloud client library
	# [START speech_python_migration_imports]
	from google.cloud import speech
	from google.cloud.speech import enums
	from google.cloud.speech import types
	# [END speech_python_migration_imports]
	# Instantiates a client
	# [START speech_python_migration_client]
	client = speech.SpeechClient()
	# [END speech_python_migration_client]
	# The name of the audio file to transcribe
	# file_name = os.path.join(
		# os.path.dirname(__file__),
	# 'resources',
	# 'audio.raw')
	#file_name='Vaishali_1_Hate.mp3'
	# Loads the audio into memory
	from pydub import AudioSegment
	from pydub.utils import make_chunks
	myaudio = AudioSegment.from_file(file_name,"wav")
	chunk_length_ms = 20000 # pydub calculates in millisec
	chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec
	#Export all of the individual chunks as wav files
	for i, chunk in enumerate(chunks):
		chunk_name = "chunk{0}.wav".format(i)
		print("exporting", chunk_name)
		Chunkfile.append('../CutAudio/'+chunk_name)
		chunk.export('../CutAudio/'+chunk_name, format="wav")
	#print("Chunkfile",Chunkfile)
	for i in Chunkfile:
		with io.open(i, 'rb') as audio_file:
			content = audio_file.read()
			audio = types.RecognitionAudio(content=content)
		config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,sample_rate_hertz=16000,language_code='en-US',use_enhanced=True,model='phone_call')
		#print("config",config)
	# Detects speech in the audio file
		response = client.recognize(config, audio)
		#print("response",type(response))
		for result in response.results:
			print('Transcript: {}'.format(result.alternatives[0].transcript))
			output=result.alternatives[0].transcript
		#print("output",output)
			Output.append(output)
	Chunkfile.clear()
	#print("Output",type(Output))
	#from toxicCommentPrediction import toxicity_level
	from sentiment import Sentiment
	#from DisplayPrediction import DisplayOutput
	listToStr = ' '.join([str(elem) for elem in Output])
	prediction=Sentiment(listToStr)
	#prediction=toxicity_level(listToStr)
	SpeechtoText[listToStr]=prediction
	#print("SpeechtoText",SpeechtoText)
	#ToxicityLevel=DisplayOutput(SpeechtoText)
	Output.clear()
	SpeechtoText.clear()
	return  prediction,listToStr
if __name__ == '__main__':
	file_name='Vaishali_1_Hate.wav'
	run_quickstart(file_name)

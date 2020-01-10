from textblob import TextBlob
def Sentiment(listToStr):
    analysis=TextBlob(listToStr)
    #print("analysis",type(analysis))
    #for words, tag in analysis.tags:
    #	print(words,tag)
    sentimentscore=analysis.sentiment.polarity
    subjectivity=analysis.sentiment.subjectivity
    print("sentimentscore",sentimentscore)
    if sentimentscore > 0.5:
        return "Very Satisfied"
    elif 0.2<= sentimentscore <= 0.5:
        return "Satisfied"
    elif -0.2 <= sentimentscore < 0.2:
        return "Not Satisfied"
    elif sentimentscore <-0.2:
        return "Very UnSatisfied"
#analysis = TextBlob("Good Morning mam. Good Morning. I am ABC Calling from FAB Hotel. As per our record,You have recently stayed in our Hotel for 3 days.As a part of quality test,We want to know,How was your stay with us?I had few issues with the hotel.kids were shouting and making noises outside my room.I called reception to get security to come and do something and tried to sleep. No one came.The rooms are not good soundproof and I could hear the telephone ringing everytime it goes off.No free wifi in the hotel.I am extremly sorry for inconvenice.Will take care in future.") 
    #print(analysis.sentiment.polarity)
    #return sentimentscore
#Good Morning Sir.Good Morning.How is the service of our company?I just hate service of your company.All your staff are disgusting.Hate is very small word for your company.I would not like to continue service of your comapny.Will take care of this in future sir?

#Good Morning Sir.Good Morning.How is the service of our company?I love service of your company.Behaviour of all your staff is  good.Love is very small word for them.I would like to continue service of your comapny and I will recommend it to others.Thank you sir


#How dare you to cheat me.I was making a friend smile, and you ruined it. In doing that, you also ruined my life. And my friends life. I'm going to cut your dog in half.

#I have sent numerous emails to the company.I still have not gotten any kind of response. What kind of customer service is that? No one will help me with this problem. My advice - don't waste your money!

if __name__ == '__main__':
    #app.debug = True
	#Response=Sentiment("Poor quality, horrible customer care")
    #Response=Sentiment("Not upto the expectation.Poor quality.horrible customer care.Not upto the expectation")
    Response=Sentiment("I am Kumar calling from Global Help desk Team .This call is regarding ticket raised by you related to your ESS page not loading properly.Are you still facing the same issue.Yes,I am not facing the issue now.Thanks for resolving it on time.You are welcome sir")
    print(Response)



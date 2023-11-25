#importing libraries
import joblib
import inputScript


#load the pickle file
classifier = joblib.load('rf1_final.pkl')

#input url
#print("enter url")
def fun(ur):
    url = ur
    
    #checking and predicting
    checkprediction = inputScript.main(url)
    prediction = classifier.predict(checkprediction)
    if(prediction==1):
        s="Phishing site"
    elif (prediction==-1):
        s="LEGITIMATE SITE"
    elif (prediction==0):
        s="Suspicious site"
        pass
        pass
    return s

# url=input()
# print(fun(url))
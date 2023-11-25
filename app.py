from flask import Flask,escape,request,render_template,url_for
from ip import fun


 
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def phy():
    input = request.form.get("inputbox")
    if input == None:
         input = 'https://www.google.com'
    print("Input: ",input)
    response = fun(input)
    print("Input: ",input,"Response: ",response)
    return render_template("index.html",input=input,response=response)

if __name__=='__main__':
    app.run(debug=True)
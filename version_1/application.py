from flask import Flask, render_template, request
import joblib
application = Flask(__name__)

vectorizer=joblib.load("vectorizer.pkl")
spam_ham_model=joblib.load("spam_ham_model.pkl")


@application.route('/', methods=['GET', 'POST'])
def spamorham():
    if request.method == "POST":
        #Get sent SMS
        message = request.form.get('message')
        
        #Predict result
        vect_message = vectorizer.transform([message])
        result = spam_ham_model.predict(vect_message)[0]

        print(result)
        return render_template("index.html", result= result)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    application.run()
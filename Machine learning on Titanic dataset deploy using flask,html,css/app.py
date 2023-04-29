from flask import Flask, request, render_template
import pickle
with open('model_titanic.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)
@app.route("/")

def index():
    return render_template('index.html')

@app.route("/Titanic", methods = ['POST', 'GET'])
def Survival():
    #PassengerId = int(request.form['PassengerId'])
    Pclass = int(request.form['Pclass'])
    Sex = int(request.form['Sex'])
    Age = int(request.form['Age'])
    SibSp = int(request.form['SibSp'])
    Parch = int(request.form['Parch'])
    Fare = int(request.form['Fare'])
    Cabin = int(request.form['Cabin'])
    Embarked = int(request.form['Embarked'])
    model_survival = model.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Cabin, Embarked]])
    
    return render_template('index.html', Survived=model_survival)



if __name__ == ('__main__'):
    app.run(debug=True)
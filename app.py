from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


df = pd.read_csv('jobs.csv')


@app.route('/')
def csv_tohtml():
    
    data = pd.read_csv('jobs.csv')
    
    return render_template('index.html', tables=[data.to_html()], titles=[''])    
    
if __name__=="__main__":
    app.run(host='localhost',port=int(5000))
    
    
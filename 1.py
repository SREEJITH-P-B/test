from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd


app = Flask(__name__)
df=pd.read_csv('static/data1.csv',index_col = 0)


@app.route('/', methods=("POST", "GET"))
def html_table():
    temp="static/"+"output.mp4"
    temp2="static/"+"output.ogg"
    temp3="static/"+"Musthafa.jpg"


    return render_template('check.html',  tables=[df.to_html(classes='data')], titles=df.columns.values,fname=temp,oname=temp2,iname=temp3)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
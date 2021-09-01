from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


ID = namedtuple('text','text2')
result_msc = []

@app.route('/')
def main_menu():
    return render_template('Main.html')

@app.route('/base')
def calculator():
    return render_template('base.html', Summ = "")

@app.route('/send', methods = ["POST"])
def send():
    summ = 0
    textbox = request.form['textbox']
    try:
      if not textbox.find("*") == -1:
        ID = textbox.split("*")
        len_max = len(ID)
        i = 0
        print("ID ",ID)
        while i < len_max - 1:
            summ = float(ID[i]) * float(ID[i+1])
            round(summ,1)
            i+=1
      if not textbox.find("+") == -1:
        ID = textbox.split("+")
        len_max = len(ID)
        i = 0
        print("ID ",ID)
        while i < len_max - 1:
            summ = float(ID[i]) + float(ID[i+1])
            round(summ,1)
            i+=1
      if not textbox.find("-") == -1:
        ID = textbox.split("-")
        len_max = len(ID)
        i = 0
        print("ID ",ID)
        while i < len_max - 1:
            summ = float(ID[i]) - float(ID[i+1])
            round(summ,1)
            i+=1
      if not textbox.find("/") == -1:
        ID = textbox.split("/")
        len_max = len(ID)
        i = 0
        print("ID ",ID)
        while i < len_max - 1:
            summ = float(ID[i]) / float(ID[i+1])
            round(summ,2)
            i+=1
      if not textbox.find("\\") == -1:
        ID = textbox.split("\\")
        len_max = len(ID)
        i = 0
        print("ID ",ID)
        while i < len_max - 1:
            summ = float(ID[i]) / float(ID[i+1])
            round(summ,1)
            i+=1
      print(summ) 
    except:
        summ = "ERROR"

    return render_template('base.html',Summ = summ)

@app.route('/<string:text>')
def calc(text): return str(text) + " Error, NONE PAGE" 

if __name__ == '__main__':
    app.run(debug=True)
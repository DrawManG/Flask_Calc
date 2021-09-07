from collections import namedtuple
import re

from flask import Flask, render_template, redirect, url_for, request
from flask.wrappers import Response


app = Flask(__name__)


ID = namedtuple('text','text2')
result_msc = []

@app.route('/')
def main_menu():
    return render_template('Main.html')

@app.route('/base')
def calculator():
    return render_template('base.html', Summ = "")


def clicked():

  clicked = str(request.values.dicts[1]).split("'")[3]
  print(clicked)
  return render_template('base.html',Summ ="::::"+ clicked )


@app.route('/base', methods = [ "POST"])
def send():
    summ = 0
    textbox = request.form['textbox']
    try:

      if str(request.values.dicts[1]['numb']):

        if str(request.values.dicts[1]['numb']) == "C":
          return render_template('base.html',Summ = "" )
        if str(request.values.dicts[1]['numb']) == "<-":
          return render_template('base.html',Summ = textbox[:-1] )
        return render_template('base.html',Summ = str(textbox) + str(request.values.dicts[1]).split("'")[7] )
    except: 
      pass

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
        while i < len_max:
            summ = float(summ) + float(ID[i])
            round(summ,1)
            i+=1
      if not textbox.find("-") == -1:
        ID = textbox.split("-")
        len_max = len(ID)
        if ID[0] == '':
          ID[1] = float(ID[1] * -1)
          del ID[0]
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
    except:
        summ = "ERROR"

    return render_template('base.html',Summ = summ )



@app.route('/<string:text>')
def calc(text): return str(text) + " Error, NONE PAGE" 

if __name__ == '__main__':
    app.run(debug=True)
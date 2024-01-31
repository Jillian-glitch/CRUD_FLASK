import pandas as pd
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

def db_conn():
   conn = psycopg2.connect(database="postgresql", host="localhost", user="postgres", password="6338", port="5432")
   return conn


@app.route('/')
def index():
     conn = db_conn()
     cur = conn.cursor()
     cur.execute("""SELECT *FROM courses""")
     data = cur.fetchall
     cur.close()
     conn.close()
     
     return render_template('index.html', data= data)
 
@app.route('/create', methods=['POST'])
def create():
        conn = db_conn()
        cur = conn.cursor()
        
        name = request.form['name']
        fees = request.form['fees']
        duration = request.form['duration']
        
        cur.execute = ("""INSERT INTO courses(name.fees, duration) VALUES(%S, %S, %S) """, (name, fees, duration, ))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    
@app.route('/update', methods=['POST'])
def uodate():
        conn = db_conn()
        cur = conn.cursor()
        
        
        name = request.form['name']
        fees = request.form['fees']
        duration = request.form['duration']
        id = request.form['id']
        
        cur.execute = ("""UPDATE courses SET name=%S,fees=%S, duration=%S WHERE id=%S""", (name, fees, duration, id, ))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    
    
@app.route('/delete', methods=['POST'])
def delete():
        conn = db_conn()
        cur = conn.cursor()
        
       
        id = request.form['id']
        
        cur.execute = ("""DELETE FROM courses  WHERE id=%S""", (id, ))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
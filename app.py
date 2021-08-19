from logging import error
from flask import Flask, render_template, url_for, redirect, request, flash
from flaskext.mysql import MySQL
import os
import pymysql.cursors
from datetime import datetime


app = Flask(__name__)

app.secret_key = "Fedora's little secret"
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'port'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''

mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    if request.method=='POST':
        form_data = request.form
        name = form_data['name']
        email = form_data['email']
        subject = form_data['subject']
        message = form_data['message']
        date = datetime.now()
        # some validation
        if len(name)<3:
            flash('Please enter a valid name','error')
        elif len(email)<3:
            flash('Please enter a valid email','error')
        elif subject=='':
            flash('Please enter a subject', 'error')
        elif message=='':
            flash('Please enter a message')
        else:
            # saving the info to the database
            conn= mysql.get_db()
            if conn:
                cursor=conn.cursor()
                cursor.execute('insert into contact (name,email,subject,message,date)\
                    VALUES (%s,%s,%s,%s,%s)',\
                    (name,email,subject,message,date))
                conn.commit()
                flash("Thanks for reaching out. I'll get back to you shortly",'success')
            else:
                flash('Unable to send your message. Please try again shortly' 'error')
        return redirect(url_for('index')+'#contact-section')
    else:
        return redirect(url_for('index')+'#contact-section')


if __name__ == '__main__':
    app.run(debug=True)
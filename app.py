from flask import Flask, render_template, url_for, redirect, request, flash
from flaskext.mysql import MySQL
import pymysql.cursors
from flask_mail import Mail, Message

import os
from datetime import datetime


app = Flask(__name__)

# # local
db_host='localhost'
db_name='port'
db_user='root'
db_pass=''

# prod
# db_host='us-cdbr-east-04.cleardb.com'
# db_name='heroku_2a27970d6c75913'
# db_user='b851d9c25fd34e'
# db_pass='b741ff2d'

app.secret_key = "Fedora's little secret"
app.config['MYSQL_DATABASE_HOST'] = db_host
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_USER'] = db_user
app.config['MYSQL_DATABASE_PASSWORD'] = db_pass

mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)

# app.config['MAIL_SERVER']='smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = '5ff3943b683f1b'
# app.config['MAIL_PASSWORD'] = 'ed6bbbbe849482'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'chenemiken15@gmail.com'
app.config['MAIL_PASSWORD'] = 'ojochenemi'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


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
                msg = Message('Hello from the other side!', sender='Chenemiken@mailtrap.io', recipients=['paul@mailtrap.io','akorneth16@gmail.com'])
                msg.body = 'Thanks for reaching out. your message was recieved'
                msg.html = render_template('index.html')
                mail.send(msg)
                flash("Thanks for reaching out. I'll get back to you shortly",'success')
            else:
                flash('Unable to send your message. Please try again shortly' 'error')
        return redirect(url_for('index')+'#contact-section')
    else:
        return redirect(url_for('index')+'#contact-section')


if __name__ == '__main__':
    app.run(debug=True)
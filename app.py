from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__, static_url_path='/static')
database = 'lost_pets.db'

def create_database():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS lost_pets
              (id INTEGER primary key,
              name TEXT NOT NULL,
              breed TEXT NOT NULL,
              color TEXT NOT NULL,
              sex TEXT NOT NULL,
              location TEXT NOT NULL,
              contact_info TEXT NOT NULL)''')
    conn.commit()
    conn.close()
    
# home page - report a lost pet
@app.route("/", methods=['GET', 'POST'])
def report_lost_pet():
    if request.method == 'POST':
        name = request.form['name']
        breed = request.form['breed']
        color = request.form['color']
        sex = request.form['sex']
        location = request.form['location']
        contact_info = request.form['contact_info']
        file = request.files['upload']
        file.save('static/uploads/' + file.filename)
        
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute('''INSERT INTO lost_pets (name, breed, color, sex, location, contact_info) 
                  VALUES (?,?,?,?,?,?)''', (name, breed, color, sex, location, contact_info))
        conn.commit()
        conn.close()
        
        return redirect('/success')
    return render_template('report_lost_pet.html')

# gallery page
@app.route("/gallery")
def lost_pets_gallery():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('SELECT * FROM lost_pets') # need to filter duplicate records 
    lost_pets = c.fetchall()
    conn.close()
    
    return render_template('gallery.html',lost_pets=lost_pets)

# success page 
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
        
        
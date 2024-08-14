from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Store the uploaded CVs (temporarily in memory for simplicity)
cv_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        pass
    return render_template('login.html')

@app.route('/editor', methods=['GET', 'POST'])
def editor():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        experience = request.form['experience']
        education = request.form['education']
        skills = request.form['skills']
        languages = request.form['languages']
        photo = request.files['photo']

        # Save the photo if uploaded
        if photo:
            photo_path = os.path.join('static', 'uploads', photo.filename)
            photo.save(photo_path)
        else:
            photo_path = None

        # Save the CV data
        cv = {
            'name': name,
            'email': email,
            'experience': experience,
            'education': education,
            'skills': skills,
            'languages': languages,
            'photo': photo_path
        }
        cv_data.append(cv)
        return redirect(url_for('cv_view', cv_id=len(cv_data) - 1))

    return render_template('editor.html')

@app.route('/cv/<int:cv_id>')
def cv_view(cv_id):
    # Retrieve the saved CV by ID
    cv = cv_data[cv_id]
    return render_template('cv_template.html', cv=cv)

if __name__ == '__main__':
    app.run(debug=True)


    

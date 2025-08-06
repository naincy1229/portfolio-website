from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/my_resume')
def my_resume():
    return render_template('my_resume.html')

@app.route('/projects')
def projects():
    return render_template('project.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')   # ✅ Added contact route
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

    



# print('flask project')

from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about',methods=['GET'])
def about():
    return render_template("about.html")
    
@app.route('/service',methods=['GET'])
def service():
    return render_template("services.html")


@app.route('/careers',methods=['GET'])
def careers():
    return render_template("careers.html")

@app.route('/contact',methods=['GET'])
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
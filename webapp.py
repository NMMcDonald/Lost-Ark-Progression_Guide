from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
   
def render_main():
    return render_template('home.html')

@app.route("/Tiers")
def render_page1():
    ilvl = request.args['ilvl']
    if ilvl == "T1":
        return render_template('page1.html')
    elif ilvl == "T2":
        return render_template('page2.html')
    else:
        return render_template('page3.html')

if __name__=="__main__":
    app.run(debug=True)

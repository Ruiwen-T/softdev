from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def disp_page():
    return render_template('static/index.html')

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run(port=3333) # changed port for MacOS
from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='public')

@app.route('/')
def index():
    print "static_folder: %s" % app.static_folder
    return app.send_static_file('index.html')

print app.url_map

if __name__ == '__main__':
    app.run(debug=True)
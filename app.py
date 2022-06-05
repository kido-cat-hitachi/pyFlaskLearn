from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World1111111'

if __name__ == '__main__':   
   #app.run(host, port, debug, options)
   app.run()
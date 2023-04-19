from flask import Flask
# importing the file flask from the flask folder 

app = Flask(__name__)
# telling the app Flask is being used
# import controller later
from controllers import controller

# controller - controls the request coming from the user 
if __name__ == '__main__':
    app.run(debug=True)
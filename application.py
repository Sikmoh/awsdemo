from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    intro = 'this is a test'
    return intro


if __name__ == '__main__':
    application.run()

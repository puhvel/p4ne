from flask import Flask
import * from glob

myweb = Flask(__name__)


@myweb.route('/')
def index():
    return "Help Page"

@myweb.route('/config')
def conf():
    f = open("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\substrings.txt")
    return print(f)


@myweb.route('/config','/hostname')
def page1():
    return "Если вы это читаете, \
              вы что-то знаете :)"


if __name__ == '__main__':
    myweb.run(debug=True)

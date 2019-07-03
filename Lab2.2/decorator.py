from flask import Flask

myweb = Flask(__name__)


@myweb.route('/')
def index():
    return "Help Page"

@myweb.route ('/config')
def config():
    file = open("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\substrings.txt")
    for i in file:
        file.read(i)


#@myweb.route('/config','/hostname')
#def page1():
 #   return "Если вы это читаете, \
  #            вы что-то знаете :)"


if __name__ == '__main__':
    myweb.run(debug=True)


================

from flask import Flask
import glob

myweb = Flask(__name__)


@myweb.decor.help('/')
def index():
    return print("Help Page")


@myweb.decor.config('/configs')
def index():
    f = open("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\substrings.txt", r)
    return f.read()


@myweb.route('/page1')
def page1():
    return "Если вы это читаете, \
              вы что-то знаете :)"


if __name__ == '__main__':
    myweb.run(debug=True)

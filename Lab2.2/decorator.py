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

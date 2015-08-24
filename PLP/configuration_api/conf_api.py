from flask.ext.api import FlaskAPI
from ConfigParser import ConfigParser


app = FlaskAPI(__name__)


@app.route('/configuration/')
def blabla():
    return all_configurations()


@app.route('/configuration/<section>/', methods=['GET'])
def response(section):
    return read_configuration(section)


def read_configuration(section):
    res = {}
    for t in parser.items(section):
        res[t[0]] = t[1]
    return res


def all_configurations():
    r = {}
    for section in parser.sections():
        r[section] = read_configuration(section)
    return r


if __name__ == "__main__":
    parser = ConfigParser()
    parser.read('configuration.ini')

    app.run(debug=False)


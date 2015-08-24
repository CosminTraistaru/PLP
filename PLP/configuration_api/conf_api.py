from flask import jsonify
from flask.ext.api import FlaskAPI
from ConfigParser import ConfigParser, NoSectionError, NoOptionError


app = FlaskAPI(__name__)


@app.route('/configuration/')
def all():
    return all_configurations()


@app.route('/configuration/<section>/', methods=['GET'])
def response_section(section):
    return read_configuration(section)


@app.route('/configuration/<section>/<key>/', methods=['GET'])
def response_key(section, key):
    return read_value(section, key)


@app.errorhandler(404)
def error_404(e):
    return {}


def read_value(section, key):
    res = {}
    try:
        res = {
            key: parser.get(section, key)
        }
    except NoOptionError:
        pass
    return res


def read_configuration(section):
    res = {}
    try:
        for t in parser.items(section):
            res[t[0]] = t[1]
    except NoSectionError:
        pass
    return res


def all_configurations():
    r = {}
    for section in parser.sections():
        r[section] = read_configuration(section)
    return r


if __name__ == "__main__":
    parser = ConfigParser()
    parser.read('configuration_api/configuration.ini')

    app.run(debug=True)

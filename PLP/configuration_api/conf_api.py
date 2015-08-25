from ConfReader import ConfReader
from flask.ext.api import FlaskAPI


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
    try:
        return parser.value(section, key)
    except KeyError:
        return {}


def read_configuration(section):
    try:
        return parser.options(section)
    except KeyError:
        return {}


def all_configurations():
    return parser.all()


if __name__ == "__main__":
    parser = ConfReader()
    parser.read('PLP/configuration_api/configuration.ini')
    app.run(debug=True)

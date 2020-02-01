import argparse
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--interface',
			type=str,
			default='0.0.0.0',
			help='Local interface to listen at')
	parser.add_argument('-p', '--port',
			type=int,
			default=5000,
			help='The port to bind the server to')
	return parser.parse_args()


if __name__ == '__main__':
	args = parse_args()
	app.run(host=args.interface, port=args.port, debug=True)


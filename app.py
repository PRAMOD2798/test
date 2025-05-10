from flask import Flask, request, render_template, jsonify
from graph_utils import Graph
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
graph = Graph()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file.filename.endswith('.csv'):
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        graph.load_from_csv(path)
        return jsonify({"message": "Graph uploaded"}), 200
    return jsonify({"error": "Only CSV allowed"}), 400

@app.route('/graph')
def get_graph():
    return jsonify(graph.to_vis_format())

@app.route('/bfs', methods=['POST'])
def bfs():
    start = request.json.get("start")
    return jsonify(graph.bfs(start))

@app.route('/dfs', methods=['POST'])
def dfs():
    start = request.json.get("start")
    return jsonify(graph.dfs(start))

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)

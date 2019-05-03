from flask import Flask,jsonify, render_template, request
from Main import SudokuSolver

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f2dc4afa20c6c6b4b7b0b63227fbf4d6'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_sudoku():
    ss = SudokuSolver(request.form['input_string'])
    if not ss.check():
        return 'Invalid'
    else:
        return ss.toString(ss.search(ss.grid_values()))
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=3000)

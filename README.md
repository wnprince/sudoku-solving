# Sudoku Solver

Ever solved a sudoku puzzle. It's tricky right? Don't worry! With this app you can get any valid sudoku puzzle solved within seconds. Just enter the sudoku config and hit submit.

**Live Preview** : https://sudoku-solving-application.herokuapp.com/

## Project Structure

```bash
├── static
│   ├── script.js
│   ├── styles.css
├── templates
│   ├── index.html
├── Main.py
├── server.py
├── .gitignore
├── README.md
```

## Technologies used

[<img align="left" alt="React" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />](#)
[<img align="left" alt="React" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/flask/flask.png" />](#)
[<img align="left" alt="React" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png" />](#)
[<img align="left" alt="React" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png" />](#)
[<img align="left" alt="React" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png" />](#) <br/>

## Running the app locally

You will require the following python modules if you wish to run this app

- click==7.1.2
- Flask==1.1.2
- gunicorn==20.1.0
- itsdangerous==1.1.0
- Jinja2==2.11.3
- MarkupSafe==1.1.1
- Werkzeug==1.0.1

To run the app, set uo a virtual environment, and install the modules mentioned in the requirements.txt using the following command:-

```
pip install -r requirements.txt
```

Once the modules are installed, simply run the command for windows :-

```
python server.py
```

For mac and linux run the following command :-

```
python3 server.py
```

Once the server is up-and-running, go to your browser, and visit http://localhost:3000 to use the app.
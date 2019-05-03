# Sudoku Solver

## About

This app can solve any valid sudoku puzzle. Just enter the sudoku config and hit submit. 

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

## Dependencies

You will require the following python modules if you wish to run this app

- astroid==2.2.5
- Click==7.0
- colorama==0.4.1
- Flask==1.0.2
- isort==4.3.17
- itsdangerous==1.1.0
- Jinja2==2.10.1
- lazy-object-proxy==1.3.1
- MarkupSafe==1.1.1
- mccabe==0.6.1
- pylint==2.3.1
- six==1.12.0
- typed-ast==1.3.5
- Werkzeug==0.15.2
- wrapt==1.11.1

## How to run

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
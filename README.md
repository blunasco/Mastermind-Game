# 🎮 Mastermind (Flask + SQLAlchemy)
---

## Quick Start
```bash
REQUIREMENTS:
Python 3.12
VSCode
```
## Please run the following commands on your terminal
```bash
git clone https://github.com/blunasco/Mastermind-Game.git
cd mastermind-game
python -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

App runs at: `http://127.0.0.1:5000`

---

## Endpoints

* `POST /start` → create a new game
* `POST /guess` → submit guesses
* `POST /end` → view results for a game

---

## Tech

* Backend: Python and Flask
* DB: SQLAlchemy
* Migrations: Alembic 
* Database Tools: DB Browser for SQLite (or SSMS / other DB clients)

## Troubleshooting
* if local host fails to load: 
    * stop the server
    * clear your browser cookies
    * run the app (python app.py)
* ModuleError or ImportError: 
    * make sure venv is active (source .venv/bin/activate) 
    * reinstall dependencies (pip install -r requirements.txt)
* Database errors(NoReferencedTableError) after adding to models.py:
    * ensure migrations are up to date (flask db migrate -m "") --> (flask db upgrade)



## Rules

* The secret code is 4 digits long
* Each digit is between 0–7
* You get 10 tries to guess the code
* After each guess, the game will return:
    * exact matches → correct digit in the correct position
    * number matches → correct digit but in the wrong position
---

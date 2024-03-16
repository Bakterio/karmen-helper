# Karmen helper
This repo contains 2 scripts.  

## 1. karmen-helper.py
The first one, `karmen-helper.py` is no longer under development and was meant to search in uploaded files on your karmen instance.

## 2. printer-notificationer.py
The second one, `printer-notificationer.py` is functioning.
### Dependencies
- [python 3](https://github.com/python/cpython) - for running the script 
- [espeak](https://github.com/espeak-ng/espeak-ng) - speach to text library for notifying user, when printer stops printing (optional, but you need to comment the line in the script if you don't want to use it)

### Instalation
Just clone this repo `git clone https://github.com/Bakterio/karmen-helper.git` wherever you want.

### Usage
Run script using run.sh. It opens python virtual environment and run the .py script.
- Give permitiones to run.sh using chmod `sudo chmod +x run.sh`
- Run script `./run.sh`

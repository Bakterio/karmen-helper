# Karmen helper
This repo contains 2 scripts.  

## 1. karmen-helper.py
The first one, `karmen-helper.py` is no longer under development and was meant to search in uploaded files on your karmen instance.

## 2. printer-notificationer.py
The second one, `printer-notificationer.py` is functioning. It will send you a notification when printer has finished printing, in order that you can clean it and print another thing you want. Optionally the script will read you the notification loud, so you won't miss it.
### Dependencies
- [python 3](https://github.com/python/cpython) - for running the script 
- [libnotify](https://gitlab.gnome.org/GNOME/libnotify) - for sending notifications using notify-send.
- [espeak](https://github.com/espeak-ng/espeak-ng) - speech to text library for notifying user, when printer finished printing (optional, but you need to comment the line in the script if you don't want to use it)

### Installation
Just clone this repo wherever you want.
```
git clone https://github.com/Bakterio/karmen-helper.git
```
Then put your **karmen token with read-all access** in token.txt
```
echo "your token here" >> token.txt
```
### Usage
Run script using run.sh. It opens python virtual environment and run the .py script.
- Give permissions to run.sh using chmod 
    ```
    sudo chmod +x run.sh
    ```
- Run script 
    ```
    ./run.sh
    ```

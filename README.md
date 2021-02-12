# ar-tel-machine
very simple Arabic numbers telling machine, made for fun

# Limits
This repo made for fun, not to be roubsut, reliable or any these production terms.
This telling machine supports playing number from 1 to 100 (both inclusive) only.

# Install
`pip install -r requirements.txt` <br>
if you have venv, activate it <br>
`python main.py`

# How to add my voice ?
Each speaker have separate folder in ./assets. Make new folder inside assets with your name. add your name inside speakers array in first lines of main.py file
``` python
speakers = ["ammar", "your-name-matched-with-folder-name"]
speakers = ["your-name-matched-with-folder-name", ] # if you want your voice only get played
```
generate your files named same as files inside assets/ammar folder 

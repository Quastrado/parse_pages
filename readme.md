# Nothing interesting

Just a few simple scripts for parsing some web pages

## We have:

### habr.py

Displays in the console 

- title 
- short description 
- publication dates
- name of the author 

of the given number of the most popular posts for the year from https://habr.com/ru/

Input data - desired number of posts

### smashingmagazine.py

Downloads wallpaper from https://www.smashingmagazine.com/category/wallpapers/ for the specified month and year in the desired resolution to the sm_images folder

Input data - month and year in format YYYY-MM and image resolution

### list-org.py

Print to the console

- name
- name of manager
- date of registration
- tax identification number
- reason code for registration
- main state registration number

one or another organization from https://www.list-org.com/

Input data - organization url. Like:
> https://www.list-org.com/company/3949708


## If you want to check them out:

Clone the repository using git
```bash
$ git clone https://github.com/Quastrado/
```
Create a virtual environment in the project folder using the venv tool
```bash
$ python3 -m venv env
```
Activate the virtual environment
```bash
$ . env/bin/activate
```
Install pip in a virtual environment
```bash
sudo apt install pip
```
Using file requirements.txt, install neсessary modules and packages
```bash
$ pip install -r requirements.txt
```

And run the desired script from the terminal. Like:
```bash
python habr.py
```





## Requirments 
* Python 3
* Flask
* Flask-Restful
* Requests
* Pycharm IDE(OPTIONAL)
## Installing the file
To install via Gitbash:
```bash
Git clone https://github.com/Astevenson180/test-python-api.git
cd test-python-api
```
To install via download:
* Download .Zip
* Extract .Zip

## Setting up and running via Pycharm IDE 
If you have a python environment already setup feel free to skip to the next section.

If you do not have python installed click [HERE](https://www.python.org/downloads/) to get the latest version

Install pycharm community edition [HERE](https://www.jetbrains.com/pycharm/download/#section=windows).

Once files are downloaded
* Open new_api_test.py in pycharm
* At the top right cornor select the button that says "Add python interpretor"
* select the file location where you downloaded python(not pycharm, but python from the first link)

### Installing the moduals:
* Once the files are open in pycharm select new_api_test.py tab.
* Select File - settings - Project: test_file_api.py - Project interpreter

![file_settings](https://user-images.githubusercontent.com/90855841/139473002-c70c2d61-70b8-4b5c-a71d-b5607e69d859.png)
&nbsp;
* press the plus button(+) and a search window that says "Available Packages" will open

![python_interpreter](https://user-images.githubusercontent.com/90855841/139473177-25c85d3f-61fb-48a8-818e-085a58c6f1da.png)

![installing_moduals](https://user-images.githubusercontent.com/90855841/139473087-1ef3811f-9784-4a29-b8da-e858fc0ec94e.png)

* you will need to add a total of three moduals to this
* flask
* flask-RESTful
* requests
* Select each one and press install package

### Running the program in pycharm
* select the new_api_test.py tab 

* right click and press run or press crtl+shift+F10
&nbsp;

![running_server_in_pycharm](https://user-images.githubusercontent.com/90855841/139477390-3b3fd5b6-e9b0-4c43-aca1-ee54e92a93f1.png)
&nbsp;
* Then select test_file_api.py and run same as before.


Navigate back to new_api_test.py tab and you should now see a response to the server:
![response_from_server_pycharm](https://user-images.githubusercontent.com/90855841/139478233-3c357b1f-37d3-4561-a1a6-f39fd053c730.PNG)
&nbsp;

## Running via Gitbash
* Install moduels via pip
```bash
pip install Flask flask-restful requests
```
* Open two windows of gitbash
* Run new_api_test.py to start the server
```bash
  python new_api_test.py
```
* Run test_file_api.py in other window to see a response
```bash
python test_file_api.py
```

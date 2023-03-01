# [Flask] Social Authentication with GitHub

This repository presents how to implement a web-based application which allows users to authenticate their credentials based on GitHub, and the application will create and store user accounts in its database.


## Prerequisites

You need to obtain GitHub OAuth information by visiting GitHub website and enter some configuration parameters, as follows:

 - Link: https://github.com/settings/applications/new
 - Application name: `Demo-Flask-Social-Auth`
 - Homepage URL: `http://127.0.0.1:5000`
 - Application description: *(leave it blank or enter your desired description)*
 - Authorization callback URL: `http://127.0.0.1:5000/login/github/authorized`

After obtaining the Client-ID and Client-Secret from GitHub, you can now insert them into the `env.sh`. If you are using Microsoft Windows OS, please read section **For Windows OS**.


## Implementation

First, we define two models in the `models.py`, i.e., `User`, `OAuth`. The `User` model will store the GitHub username of an authenticated user. The `OAuth` model is inherited from `OAuthConsumerMixin` of Flask-Dance to add the necessary fields to store OAuth information. You can find out more about the use of `OAuthConsumerMixin` at [here](https://flask-dance.readthedocs.io/en/v1.2.0/backends.html).

Second, we define the `github_blueprint` in `oauth.py` along with the `github_logged_in()` function which will automatically perform one of these actions:

 - If a given username does exist in the database, the function will log the user in.
 - Otherwise, the function will create a new user account in the database, and then log the user in.

And then, we implement the procedure to authenticate a user in the `login()` function in `app.py`.


## How to run this demo program

 1. You should create a new virtual environment. If you are using macOS 10.15 and later, I have a tutorial at [here](https://gist.github.com/duonghuuphuc/7939cfbf82d9664274d299fff3d4c205).
 2. You need to configure the Client-ID and Client-Secret in `env.sh`.
 3. You should install all Python packages as presented in `requirements.txt` by executing this command in the current environment: `$ pip install -r requirements.txt`.
 4. Create the database and its tables by executing the following commands:
```
$ export FLASK_APP=app.py
$ flask db init
$ flask shell
>>> from app import db
>>> db.create_all()
>>> db.session.commit()
>>> quit()
```
 5. Execute this command `source env.sh` to run the demo program. The server will be running locally on `http://127.0.0.1:5000`.

The following two screenshots are the results of the demo program if it is properly compiled and run.

![Login web page](https://www.dhpit.com/img/flask-social-auth-github-20220609-a.png)

![Result when a user is successfully authenticated](https://www.dhpit.com/img/flask-social-auth-github-20220609-b.png)


## For Windows OS

Although the demo program can be run on both MacOS/Linux-based OS and Windows OS, there are some notices when running it on Microsoft Windows OS, as follows:

- Using `set` instead of `export`
- You should install [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL) and the `.sh` files can be executed by running `bash env.sh` in CMD window
- Do not include any quotations when executing `set` commands in CMD (if the value doesn't have whitespaces), i.e., `set GITHUB_CLIENT_ID=12345abcde`

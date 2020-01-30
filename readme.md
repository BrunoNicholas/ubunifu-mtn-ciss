[![Build Status](https://travis-ci.org/BrunoNicholas/ubunifu-mtn-ciss.svg?branch=master)](https://travis-ci.org/BrunoNicholas/ubunifu-mtn-ciss)

[![Coverage Status](https://coveralls.io/repos/github/BrunoNicholas/ubunifu-mtn-ciss/badge.svg?branch=master)](https://coveralls.io/github/BrunoNicholas/ubunifu-mtn-ciss?branch=master)

# Welcome to this test API
The test api instance  for CIS purchases of packages, a brief start test shell.

## Table of content
  1. [Project Description](#project)
  2. [Installation](#installation)
  3. [The End-Points Strusture & Documentation](#structure)
  4. [Developer Insights](#developer)

## Project
This project is not meant to dive into the core specifics of operations but a brief of what the full API is meant to be, how to secure the HTTP requests, handle the responses from the different resources and finally enable one to enjoy the game played here.

Feel free to clone and give any hand of appreciation or support where necessary.

## Installation
This will take you through your installation journey for this project.
It is a simple and enjoyable one and it can be installed in different environmental platforms of your choice

### Linux
Clone this repository to any place on your system as below. This assums you have Git installed and you are comfortable with it.

```bash
git clone https://github.com/BrunoNicholas/test-cis.git
```

Upon a successful clone, ``` cd test-cis ```, and either stay in ```master``` branch or change to ```develop``` as below

```git
git checkout develop
```

Now it is time to set up a virtual environment, this project is built on Python 3.7.x but you could try it out with your other Python 3.x. But we will stick to going with Python 3.7.x

```bash
python3.7 -m venv env
```

If you are using Python 3.8.x, you can follow [this link](https://vsupalov.com/developing-with-python3-8-on-ubuntu-18-04/) to show you how this is done.

Now let us install the preferable package for all our modules. This can be done in two different ways

```bash
pip install --user pipenv
```

If the above does not work mostly in various virtual environments, just remove the ```--user``` flag and do as before

```bash
pip install pipenv
````

Now we can install all our project dependancies as below.

```bash
pipenv install -r requirements.txt
```

Once that is done, you can then go and start the server to follow along.

The endpoints are structured well so in any case you the browser does not return any JSON data, please help and raise a concern as an issue here. 

Otherwise, insert this code to start the serve

```bash
flask run
```

Remember to check out the documentation for the endpoints and make some good progress.


### Windows
Here, you need to install the Python 3.7 or any other 3.x just as above and follow along

Make sure that the right python has been added to the environmental PATH so that you can use it anywhere on the system.

You can follow along the Linux to see what is going on however the virtual environment here is different.

```bash
virtualenv venv
```

Once you browse to the cloned folder, the above shouyld work well.

## Structure
The structure of this project is a product of the documentation created by the swagger platform

You can check it out from the Swagger UI so as to know where you are.

In case you find errors, please post them as issues or for what is work, you can send in a pull request so that we can merge it together as we go ahead, thanks.

## License
As long as this project is public, it is under the MIT License, you can get some snippets to implement in your code.
Remember to give a hand of thanks to the dev.

## Developer
This project is an Ubunifu project

Led by

Official: [bserunkuma@ubunifu.systems](mailto:bserunkuma@ubunifu.systems)

Thanks, Nice coding and adventure!
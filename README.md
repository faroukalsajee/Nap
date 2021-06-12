# Nap

A basic (in progress) site built using Wagtail CMS, Python and Django framework. Wagtail is an open source CMS written in Python and built on the Django web framework.

## Install and run Wagtail
### Install dependencies
Wagtail supports Python 3.6, 3.7, 3.8 and 3.9.

To check whether you have an appropriate version of Python 3:

`$ python3 --version`

If this does not return a version number or returns a version lower than 3.6, you will need to install Python 3.

> .. important::
   Before installing Wagtail, it is necessary to install the **libjpeg** and **zlib** libraries, which provide support for working with JPEG, PNG and GIF images (via the Python **Pillow** library).
   The way to do this varies by platform—see Pillow's
   platform-specific installation instructions <https://pillow.readthedocs.org/en/latest/installation.html#external-libraries>_.

## Create and activate a virtual environment
We recommend using a virtual environment, which isolates installed dependencies from other projects. This tutorial uses venv, which is packaged with Python 3.

On Windows (cmd.exe):

`python3 -m venv mysite\env`

`mysite\env\Scripts\activate.bat`

On GNU/Linux or MacOS (bash):

`$ python3 -m venv mysite/env`

`$ source mysite/env/bin/activate`

For other shells see the venv documentation.

.. note::

   If you're using version control (e.g. git), ``mysite`` will be the directory for your project.
   The ``env`` directory inside of it should be excluded from any version control.
   
## Install Wagtail
Use pip, which is packaged with Python, to install Wagtail and its dependencies:

`$ pip install wagtail`

## Install project dependencies
`$ cd Nap`

`$ pip install -r requirements.txt`

## Create the database
If you haven't updated the project settings, this will be a SQLite database file in the project directory.

`$ python manage.py migrate`
This command ensures that the tables in your database are matched to the models in your project. Every time you alter your model (eg. you may add a field to a model) you will need to run this command in order to update the database.

## Create an admin user
`$ python manage.py createsuperuser`
When logged into the admin site, a superuser has full permissions and is able to view/create/manage the database.

## Start the server
`$ python manage.py runserver`

If everything worked, http://127.0.0.1:8000 will show you a welcome page. You can now access the administrative area at http://127.0.0.1:8000/admin


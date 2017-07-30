# DHL_UnitedByHCL_WebApp

A dhl python chatbot for Facebook Messenger.

This is a prototype app for UnitedByHcl Hackathon on the theme Artificial Inteligence Challenge 3 : Create an Assistive Chatbot – For DHL
Develop a chatbot to help simplify some of the DHL’s user centric problems.

You can visit [my deployment of the example online](https://dhlavenues.herokuapp.com/), deploy your own copy to Heroku or run an instance in your local computer.

## Deploying to Heroku

Follow the instructions provided in the [Facebook quickstart tutorial](https://developers.facebook.com/docs/messenger-platform/quickstart) for creating a page and an app.

Deploy your own copy to Heroku with this button (which requires a free Heroku account) and set the `VERIFY_TOKEN` and `FACEBOOK_TOKEN` environment variables to the values you get from following the tutorial.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/SamwelOpiyo/DHL_UnitedByHCL_WebApp)

## Running locally

### Requirements

- Python 2.7
- Make sure you have pip (pip --version)
- pip install virtualenv to install virtual environment
- Facebook messenger (you can also use the web version at https://www.messenger.com)
- Git 



Clone the repository into a directory of your own choice.

`git clone https://github.com/Avenues3/DHL_UnitedByHCL_WebApp.git`
`cd DHL_UnitedByHCL_WebApp`

Then, to run:

- Install requirements: `pip install -r requirements.txt` (you almost certainly want to do this in a virtualenv).
- Migrate: `python manage.py migrate`

### Setting up a Facebook app for Facebook messenger

* You're going to need a publicly routed https address. I used [ngrok](https://ngrok.com/) to create a tunnel to my local development machine.Download ngrok (https://ngrok.com/) , go to a new tab on your terminal and start it with `ngrok http 8000`

At this point, you will have to add the URLs to ALLOWED_HOSTS in `dhl/settings.py`.

* The server will need to be started for you to verify the webhook. See "Starting the server" below.
* Follow the instructions provided in the [Facebook quickstart tutorial](https://developers.facebook.com/docs/messenger-platform/quickstart) for creating a page and an app.
* Set the `VERIFY_TOKEN` and `FACEBOOK_TOKEN` environment variables to the values you get from following the tutorial.

### Starting the server

Is just a matter of

    $ python manage.py runworker
`


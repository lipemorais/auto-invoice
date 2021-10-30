# auto-invoice

The objective of this project is generate an invoice on [husky.io](https://husky.io) using 1 command

## Dependencies

You need to install `pipenv` since this project use it to handle Python dependencies 

## Installation

If you\'re using Debian Buster+:

    $ sudo apt install pipenv

Or, if you\'re using Fedora:

    $ sudo dnf install pipenv

Or, if you\'re using FreeBSD:

    # pkg install py36-pipenv

Or, if you\'re using Mac OS:

    $ brew install pipenv

Or, if you\'re using Windows:

    # pip install --user pipenv

## Setup
To set up the project you need to make a copy of `auto_invoice/.env.example`
```bash
cp auto_invoice/.env.example auto_invoice/.env
```

So you can fill the sensitive data in `auto_invoice/.env`

## Run

Once you are done with filling the data you can run

`make invoice`

You should look for 2 important logs:
1. `Login done successfully!!!` so you know that your login on husky was successful
2. `Invoice sent successfully!` so you know that your invoice was sent for your e-mail 

# EZAuth

### The easiest way to authenticate your users

Tired of searching for a good, free, open-source authentication API? Well, you're at the right place! Introducing EZAuth, the easiest way to set up your own authentication server!

## Requirements

There are literally ZERO requirements! You don't need any knowledge of programming or API's to set this up! Just a single click can get you your own EZAuth instance! To get started, click on the "Deploy to Heroku" button.\
If you do have programming knowledge and want to check the code out or edit it, you're free to do that! You can also host this instance on another host if you want, of course, but for people who don't want to pay for hosting Heroku is the perfect solution! There is more information on editing this code [here](#editing-the-code).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/mauritsf15/EZAuth)

## Why is EZAuth a great solution for you?

It's free, open-source, and is updated actively!

Suggestions are always welcome, if you want to suggest something please let me know by [sending me an email](mailto:ezauth@succ.pw)!

## Documentation

You can find the documentation at [ezauth.succ.pw](https://ezauth.succ.pw/)\
A tutorial on using this in App Inventor will be uploaded soon.

## Editing the code

If you don't want to host on Heroku I recommend editing the code, there is a chance the code will not work. EZAuth has access to the Heroke Postgres database integrated, but if you don't want to host the database on Heroku or want to host the whole application somewhere else, you should change line 7 from `app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']` to ``app.config['SQLALCHEMY_DATABASE_URI'] = 'ENTER_POSTGRES_DATABASE_URI_HERE'`. Your Postgres URI should start like the following: `postgres://`.\

#### If you need any help be sure to [send me an email](mailto:ezauth@succ.pw)!
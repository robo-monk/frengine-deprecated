<img src='https://i.imgur.com/55SWntb.png' width=420> </img>

###

`Python` API used to scrape web pages cleanly by [Fready](https://www.fready.herokuapp.com/)

###

# API Keys

For now the API is hosted on [Heroku](https://frengine.herokuapp.com/) and no keys are required. 
Probably in the future this will change.

# Basic Usage

You can preview the resulting clean `HTML` of a link by visiting:
`https://frengine.herokuapp.com/<link>`
- for example: https://frengine.herokuapp.com/https://en.wikipedia.org/wiki/Rick_and_Morty

# API Calls

You can get a `JSON` formated hash containing the `title` and the `summary` of the webpage by GET requesting:
`https://frengine.herokuapp.com/api/<link>`
- for example: https://frengine.herokuapp.com/api/https://en.wikipedia.org/wiki/Rick_and_Morty

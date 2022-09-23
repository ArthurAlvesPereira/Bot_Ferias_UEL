import os
from datetime import date, timedelta
from json import load

import tweepy

def tweet(tweettext):


  #API = tweepy.Client(
  #  consumer_key='rTXEsY6WFP0cfu8d7GCo141F9',
  #  consumer_secret='JN1clFJanZ7PFjQhB9nxjQdbTNRUaflngVNB3y8vrdDtXUQaXY',
  #  access_token='1572043759939993602-rudvqrYmJDRUZrAylkpBsGHjOQzvp3',
  #  access_token_secret='1XtFhdtZpGt3X6jYpbf2yp9eVn6y4c37BBMbEThPMOgWb'
  #)

  auth = tweepy.OAuthHandler('rTXEsY6WFP0cfu8d7GCo141F9', 'JN1clFJanZ7PFjQhB9nxjQdbTNRUaflngVNB3y8vrdDtXUQaXY')
  auth.set_access_token('1572043759939993602-p5FX0xRF47vhzWGjsMPmz3GsSVWE8l', 'AYbz7xtsJ7ecwXucUYsESYLYpHDlx6BSizEnvtQTSFmlk')

  api = tweepy.API(auth)

  api.update_status(tweettext)
  #api.update_with_media('https://c.tenor.com/W36UEwNPc0AAAAAC/shrek-sextafeira.gif', status=tweettext)


# Consumer keys and access tokens, used for OAuth

# OAuth process, using the keys and tokens

def format_tweet(current_date):

  current_year = date.today().year
  end_of_classes = date(current_year, 12, 10)
  exaltados = date(current_year, 10, 24)

  #date_test = date(current_year, 10, 24)

  days_left = (end_of_classes - current_date).days

  if current_date != end_of_classes:
    if current_date != exaltados:
      return f'Faltam {days_left} dias para o fim das aulas.'
    else:
      return f'Faltam {days_left} dias para o fim das aulas.\nHoje é dia de exaltados!'

  if current_date == end_of_classes:
    return "Hoje é o último dia de aula do ano letivo de 2022. Boas férias!"



  return None

#Gif = 'https://c.tenor.com/W36UEwNPc0AAAAAC/shrek-sextafeira.gif'
text = format_tweet(date.today())

#if Gif:
  #tweet(Gif)
#if text:
#    tweet(text)


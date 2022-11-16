### Bot V0.2

import datetime 
import tweepy

# Authenticate to Twitter

# Keys and secrets must be hidden

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)

# Determine the actual date and how many days are left

ferias = datetime.date(2022, 12, 10)
agora = datetime.date.today()

fdias =(ferias - agora).days

# Find wich day of the week is the date
agora.weekday()

# Ifs to determine the days

if fdias != 1:


  if agora.weekday() == 0:
    api.update_status_with_media("Faltam " + str(fdias) + " dias para as férias da UEL!\n", '/home/leninjitsu/Bot/eu odeio segunda.jpg')
  elif agora.weekday() == 4:
    api.update_status_with_media("Faltam " + str(fdias) + " dias para as férias da UEL\nE hoje é sexta-feira!", 'Bot_Ferias_UEL/shrek-sextafeira.gif')
  else:
    api.update_status("Faltam " + str(fdias) + " dias para as férias da UEL!")

elif fdias == 1:
  api.update_status("Ultimo dia de aula da UEL!")

else:
  api.update_status("Férias da UEL!")


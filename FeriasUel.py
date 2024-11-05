### Bot V0.3

import datetime 
import tweepy

# Autenticação do Bot

# Keys e Secrets devem estão "escondidas"

key = ''
secret = ''

bearer = ''

consumer_key = ''
consumer_secret = ''

api = tweepy.Client(bearer,key,secret,consumer_key,consumer_secret)

# Data das datas

ferias = datetime.date(2025, 2, 28)
agora = datetime.date.today()

fdias =(ferias - agora).days

# Acha o dia da semana
#agora.weekday()

# Ifs para determinar os qual a mensagem a ser mostrada

if fdias != 1:
  api.create_tweet(text="Faltam " + str(fdias) + " dias para as férias da UEL!")
elif fdias == 1:
  api.create_tweet(text="Ultimo dia de aula da UEL!")
else:
  api.create_tweet(text="Férias da UEL!!!")

# parte antiga do código

#   if agora.weekday() == 0:
#     api.update_status_with_media("Faltam " + str(fdias) + " dias para as férias da UEL!\n", '/home/leninjitsu/Bot/eu odeio segunda.jpg')
#   elif agora.weekday() == 4:
#     api.update_status_with_media("Faltam " + str(fdias) + " dias para as férias da UEL\nE hoje é sexta-feira!", 'Bot_Ferias_UEL/shrek-sextafeira.gif')
#   else:
#     api.update_status("Faltam " + str(fdias) + " dias para as férias da UEL!")
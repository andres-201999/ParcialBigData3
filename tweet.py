#Importaciones que se realizan
import socket
import tweepy

#Hashtags que se utilizarán
hashtags=['#nomnom','#homemade','#healthylifestyle','#fresh','#foodie','#madewithlove','#chefmode','#tasty','#fruitslove','#food']
#API y Token de twitter
apikey="s9r3qnh6DbLVClmE4bk4YhaIb"
apisecret="ey8Xn8MEsYVGD1uZvC0PPzKd39aINXyptVrcgb1kRwcwD5EJ1s"
access_token="1076967846801014784-rrDomRNVoujshbwqbZbf7KZTEFKarG"
access_token_secret="Gq0Ivi8OeJOlU1Fjrk3Cyf8whJpnhAT3OqT2LnTEMCZlM"

#Socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',9898))
s.listen()
conn,addr=s.accept()
print(f'conectado con {addr}')

#Funcion
class TwitterListener(tweepy.StreamListener):
    def on_status(self, status):
        diccionario=status.entities['hashtags']
        print(30*'-')
        for hashtag in diccionario:
          if '#'+str(hashtag['text']) in hashtags:
            conn.sendall(bytes(hashtag['text']+'\n',encoding='utf-8'))
            print(hashtag['text'])

#Codigo para accedes
auth=tweepy.OAuthHandler(apikey,apisecret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
streamListener = TwitterListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=hashtags)


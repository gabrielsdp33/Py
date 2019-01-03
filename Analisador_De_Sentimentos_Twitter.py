import tweepy
from textblob import TextBlob

#Autenticação
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Função que adiciona o rótulo ao tweet analisado
def get_label(analysis, limiar = 0):
	if analysis.sentiment[0]>limiar:
		return ' - POSITIVO\n'
	else:
		return ' - NEGATIVO\n'

#Faz a pesquisa desejada e salva no caminho especificado
caminho = ''
dataInicio = '2019-01-01'
dataFim = '2019-01-03'

pesquisa = input('Pesquisar...')

tweets = api.search(pesquisa, count = 100, since= dataInicio, until= dataFim)

with open(caminho, 'wb') as arquivoCSV:
    for tweet in tweets:
       analysis = TextBlob(tweet.text)
       linha = tweet.text + get_label(analysis)
       arquivoCSV.write(linha.encode('utf-8'))       


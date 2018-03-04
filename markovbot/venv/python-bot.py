import os 
import time
import re
import collections
from markovbot import MarkovBot

bot = MarkovBot()
bot2 = MarkovBot()

''' 
clean data for shakespeare
'''

'''
data = open("shakeComplete.txt", 'r').read()
fOne = ''.join(filter(lambda x: not x.isdigit(), data))
fTwo = (re.sub('[-,_[@?#*"%;()}]', " ", fOne))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
finalDataShake = fFour
'''
'''freud'''
dirname = os.path.dirname(os.path.abspath(__file__))
freudText = os.path.join(dirname, 'freudCompleteWorks.txt')
bot.read(freudText)
freudTweets =  bot.generate_text(25)
print(freudTweets)

'''cleaned Shakespeare'''
finalDataShake = os.path.join(dirname, 'shakeComplete.txt')
data = open(finalDataShake).read()
fOne = ''.join(filter(lambda x: not x.isdigit(), data))
fTwo = (re.sub('[-,_[@?#*"%;()}]', " ", fOne))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
finalSText = fFour
bot2.read(finalSText)
shakeTweets = bot2.generate_text(15)
print(shakeTweets)

'''
Keys/Tokens: 
'''
cons_key ='TRXh3CDSFBnPuZziANbqssl1l'
cons_secret ='sIfuEEp6T8qluDkU3S9PLcINoIIqcp0SUTrnwVfvdWhNRlIS6G'
access_token ='863265431691436032-PH9ASi1r3tfXJY90i4HuCVVpcLhUJ6D'
access_token_secret ='POslJ4RgWsgL7BzUV1WY7xZaI9YXGMmSIFPwA2vcZt1Uf'

'''
Login, tweet-period
'''
bot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix = "#Freud")
bot2.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot2.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix = "#ShakeSpeare") 
time.sleep(6400)

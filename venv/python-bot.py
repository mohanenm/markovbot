import os 
import time
from markovbot import MarkovBot


freud = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
book2 = os.path.join(dirname, 'freudCompleteWorks.txt')
bot.read(book2)





twitter =  bot.generate_text(15)
print(twitter)


cons_key ='TRXh3CDSFBnPuZziANbqssl1l'
cons_secret ='sIfuEEp6T8qluDkU3S9PLcINoIIqcp0SUTrnwVfvdWhNRlIS6G'

access_token ='863265431691436032-PH9ASi1r3tfXJY90i4HuCVVpcLhUJ6D'
access_token_secret ='POslJ4RgWsgL7BzUV1WY7xZaI9YXGMmSIFPwA2vcZt1Uf'
bot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix = "#freud") 
time.sleep(6400)

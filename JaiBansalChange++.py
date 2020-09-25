#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:18:56 2020

@author: jaibansal
"""

# used tweepy to help implement game
import tweepy
import random

#these were my twitter keys from twitter development when I created the game
#if you want to play the game, enter in your own twitter keys
#the game will not work unless you enter yours, as I have regenerated mine for 
#security purposes

twitter_keys = {
        'consumer_key':        'ZXJckXpHjBMzf23PueOItzcJQ',
        'consumer_secret':     'Xn4GrCXNv6SpejkOxkvJMQqyADz0kixpGMp8R466JdMkkMMvSo',
        'access_token_key':    '1198131685533134848-FocZJowvgmEloWa9aTYDGhHM6L7OiN',
        'access_token_secret': 'muCodPpPLF3ufKvsccBJXeVeUk2MWWjjaOtMW7N0cCqPV'
    }

#set up tweepy
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
api = tweepy.API(auth)

#find elon/kanye last 3200 tweets
#just change the first argument of the api call here to play with anyone you want
elon_tweets = api.user_timeline('@elonmusk', count = 3200)
kanye_tweets = api.user_timeline('@kanyewest', count = 3200)


#create arrays for kanye and elon's tweets that are cleaned per specs
elon_array= []
for tweet in elon_tweets:
    if not '@' in tweet.text:
        if not 'https' in tweet.text:
            elon_array.append(tweet.text)
        
kanye_array= []
for tweet in kanye_tweets:
    if not '@' in tweet.text:
        if not 'https' in tweet.text:
            kanye_array.append(tweet.text)


#length of both arrays (used for random tweet generation later)
elon_length = len(elon_array)
kanye_length = len(kanye_array)

#game starts
print('Welcome to the Kanye Elon Twitter Guessing Game!')
print('\n')

#change num_iterations to change how many times you want to play the game
num_iterations = 3
count = 0
num_correct_answers = 0

#game
while count < num_iterations:
    rand = random.randint(0,1) #decide which celeb tweet gets used
    if rand == 0:
        correct_answer = 'Elon Musk'
        rand2 = random.randint(0,elon_length -1)
        rand_tweet = elon_array[rand2]
    if rand == 1:
        correct_answer = 'Kanye West'
        rand2 = random.randint(0,kanye_length -1)
        rand_tweet = kanye_array[rand2]
    print(rand_tweet)
    print('\n')
    user_answer = input('Is this tweet from Elon Musk or Kanye West? ')
    print('\n')
    #program will not catch typos (could be fixed in later implementation)
    if user_answer.lower() == correct_answer.lower(): #case insensitive
        num_correct_answers = num_correct_answers + 1
    count = count +1


print('You got ', num_correct_answers, 'out of' , num_iterations ,' correct! Thanks for playing!')
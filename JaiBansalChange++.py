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
        'consumer_key':        'nuXn0yXPGggrmT0tKH7uPWiIi',
        'consumer_secret':     '4eT91FDJXZSQPrIa0UmTWNsd71kXg5It9yG0VCYwg4tZjiFQFF',
        'access_token_key':    '1198131685533134848-YNHqDsi22any1b29Z1uYyDBNM3hDp8',
        'access_token_secret': 'PZugPk20RGzeQjFLg9FcY1lSCd7EKVkKwUV4kXD4K1tel'
    }

#set up tweepy
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
api = tweepy.API(auth)



#change these variables to make the program work with whoever you want
celeb1_name = 'Elon Musk'
celeb2_name = 'Kanye West'

celeb1_twitter = '@elonmusk'
celeb2_twitter = '@kanyewest'

#find elon/kanye last 3200 tweets

celeb1_tweets = api.user_timeline(celeb1_twitter, count = 3200)
celeb2_tweets = api.user_timeline(celeb2_twitter, count = 3200)


#create arrays for kanye and elon's tweets that are cleaned per specs
celeb1_array= []
for tweet in celeb1_tweets:
    if not '@' in tweet.text:
        if not 'https' in tweet.text:
            celeb1_array.append(tweet.text)
        
celeb2_array= []
for tweet in celeb2_tweets:
    if not '@' in tweet.text:
        if not 'https' in tweet.text:
          celeb2_array.append(tweet.text)


#length of both arrays (used for random tweet generation later)
celeb1_length = len(celeb1_array)
celeb2_length = len(celeb2_array)

#game starts
print('Welcome to the',celeb1_name, 'and',celeb2_name,' Twitter Guessing Game!')
print('\n')


#change num_iterations to change how many times you want to play the game
num_iterations = 5
count = 0
num_correct_answers = 0

#game
while count < num_iterations:
    rand = random.randint(1,2) #decide which celeb tweet gets used
    if rand == 1:
        correct_answer = celeb1_name
        rand2 = random.randint(0,celeb1_length -1)
        rand_tweet = celeb1_array[rand2]
    if rand == 2:
        correct_answer = celeb2_name
        rand2 = random.randint(0,celeb2_length -1)
        rand_tweet = celeb2_array[rand2]
    print(rand_tweet)
    print('\n')
    user_answer = input('Is this tweet from ' + celeb1_name + ' or ' + celeb2_name + '? ')
    print('\n')
    #program will not catch typos (could be fixed in later implementation)
    if user_answer.lower() == correct_answer.lower(): #case insensitive
        num_correct_answers = num_correct_answers + 1
    count = count +1

#could add play again option in later implementation, didn't think necessary
print('You got ', num_correct_answers, 'out of' , num_iterations ,' correct! Thanks for playing!')
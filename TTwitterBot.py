import tweepy 
from tkinter import *

#Submit your Twitter API information below

apiKey = 'iph42pFcrgFIdgmhq9gaboM0B' #API/Consumer 
apiKeyScrt = 'z1YEz4Uraceiab1VvsyaIEtWwmUaVHXDbyAnY3nSXthZ7QiGwU' #API/Consumer Secret
accessTkn = '1112786517330722817-T1jAp2GwNsZ3JddAR7QUadNzcM54LO' #Access token
accessTknScrt = 'dsbDPfQL7iCUXCF2Z19tZ7GkE0PldqM7tOsI3Kut9mItl' #Access Token Secret


auth = tweepy.OAuthHandler(apiKey, apiKeyScrt)
auth.set_access_token(accessTkn, accessTknScrt)
api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.location)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

print("We are now following everyone that is following " + user.name)

root = Tk()

root.title("TBot Admin Tool") 
root.configure(background='#1b95e0')
root.geometry("470x470")

heading = Label(root, text="Twitter Bot Tool", bg='#1b95e0', fg='#fff',font=("Comic Sans MS", 32))


search = Label(root, text="Search", bg='#1b95e0', fg='#fff',font=("Arial bold", 12))
E1 = Entry(root, bd =5)

tweets = Label( root, text="Number of Tweets", bg='#1b95e0', fg='#fff',font=("Arial bold", 12))
E2 = Entry(root, bd =5)

response = Label(root, text="Response", bg='#1b95e0', fg='#fff',font=("Arial bold", 12))
E3 = Entry(root, bd=5)

reply = Label(root, text="Reply? (Y/N)", bg='#1b95e0', fg='#fff',font=("Arial bold", 12))
E4 = Entry(root, bd=5)

retweet = Label(root, text="Retweet? (Y/N)", bg='#1b95e0', fg='#fff',font=("Arial bold", 12))
E5 = Entry(root, bd=5)

favorite = Label(root, text="Favorite (Y/N)", bg='#1b95e0', fg='#fff',font=("Arial bold", 12))
E6 = Entry(root, bd=5)

follow = Label(root, text="Follow? (Y/N)", bg='#1b95e0', fg='#fff',font=("Arial bold", 12))
E7 = Entry(root, bd=5)



def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()


def getE4():
    return E4.get()

def getE5():
    return E5.get()

def getE6():
    return E6.get()

def getE7():
    return E7.get()


def mainFunction():
    getE1()
    search = getE1()
    
    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)
    
    getE3()
    phrase = getE3()
    
    getE4()
    reply = getE4()
    
    getE5()
    retweet = getE5()
    
    getE6()
    favorite = getE6()

    getE7()
    follow = getE7()

    if reply == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #reply
                print('\nTweet by: @' + tweet.user.screen_name)
                print('ID: @' + str(tweet.user.id))
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status('@'+ username +''+ phrase, in_reply_to_status_id=tweetId)
                print('Replied with' + phrase)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if retweet == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #retweet
                tweet.retweet()
                print('Retweeted the tweet')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if favorite == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Favorite
                tweet.favorite()
                print('Favorite the tweet')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if follow == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #follow
                tweet.user.follow()
                print('Follow the user')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break
                
    
submit = Button(root, text='Submit', command=mainFunction,  padx=16, fg='#fff', bg='#313233')

heading.pack()               
search.pack()
E1.pack()
tweets.pack()
E2.pack()
response.pack()
E3.pack()
reply.pack()
E4.pack()
retweet.pack()
E5.pack()
favorite.pack()
E6.pack()
follow.pack()
E7.pack()
submit.pack(side=BOTTOM)

root.mainloop()

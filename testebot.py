import tweepy


tweet_text = "Teste de tweet com imagem"
image_path = "home/arthur/Bot/Bot_Ferias_UEL/shrek-sextafeira.gif"

def sendTweet(tweet_text, image_path):
    """Post some text, and optionally an image to twitter.

    Args:
        tweet_text: String, text to post to twitter, must be less than 260 chars
        image_path: String, path to image on disk to be posted to twitter
    Returns:
        tweepy.status object, contains response from twitter request
    """
    #consumer_key='rTXEsY6WFP0cfu8d7GCo141F9',
    #consumer_secret='JN1clFJanZ7PFjQhB9nxjQdbTNRUaflngVNB3y8vrdDtXUQaXY',
    #access_token='1572043759939993602-rudvqrYmJDRUZrAylkpBsGHjOQzvp3',
    #access_token_secret='1XtFhdtZpGt3X6jYpbf2yp9eVn6y4c37BBMbEThPMOgWb'

    auth = tweepy.OAuthHandler('rTXEsY6WFP0cfu8d7GCo141F9', 'JN1clFJanZ7PFjQhB9nxjQdbTNRUaflngVNB3y8vrdDtXUQaXY')
    auth.set_access_token('1572043759939993602-rudvqrYmJDRUZrAylkpBsGHjOQzvp3', '1XtFhdtZpGt3X6jYpbf2yp9eVn6y4c37BBMbEThPMOgWb')

    api = tweepy.API(auth)


    if image_path:
        return api.update_with_media(filename=image_path, status=tweet_text)
    else:
        return api.update_status(tweet_text)

    return api.update_status(tweet_text)

sendTweet(tweet_text, image_path)
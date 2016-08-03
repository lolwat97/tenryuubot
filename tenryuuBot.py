import tweepy
from os import listdir
from os.path import isfile, join
import time

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print(api.me().name)

try:
    log = open('save.txt', 'r')
    for line in log:
        pass
    lastIndex = int(line)
    log.close()
except:
    lastIndex = -1

def generateFileList(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return files

def startPostingFrom(files, index, logfile):
    for i in range(index+1, len(files)):
        print('posting image ' + files[i])
        try:
            api.update_with_media('.\\images\\'+files[i])
        except:
            pass
        logfile.write(str(i) + '\n')
        logfile.flush()
        time.sleep(600)

with open('save.txt', 'w') as f:
    startPostingFrom(generateFileList('.\\images\\'), lastIndex+1, f)

#imagePath = input('filename please: ')
#api.update_with_media(imagePath)

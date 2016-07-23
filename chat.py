from cobe.brain import Brain
from tqdm import tqdm
import praw
import sys

old_stdout = sys.stdout

sys.stdout = tqdm

brain = Brain("cobe.brain")

# Removed to prevent impersonation
USER_AGENT = ''
USERNAME = ''
PASSWORD = ''
PINGNAME = '+/u/' + USERNAME
interface = praw.Reddit(USER_AGENT)
interface.login(username=USERNAME, password=PASSWORD, disable_warning=True)


def getreply(comment):
    body = comment.body
    
    return brain.reply(body.replace('+/u/RedditSimulatorBot', ''))

if __name__ == '__main__':
    for comment in tqdm(praw.helpers.comment_stream(interface, 'all'), unit=' comments'):
        brain.learn(comment.body)
        if PINGNAME in comment.body:
            tqdm.write("%")
            comment.reply(getreply(comment))

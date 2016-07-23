from cobe.brain import Brain
from tqdm import tqdm
import praw
import sys

old_stdout = sys.stdout

sys.stdout = tqdm

brain = Brain("cobe.brain")

# removed to prevent impersonation
USER_AGENT = ''
USERNAME = ''
PASSWORD = ''
interface = praw.Reddit(USER_AGENT)
interface.login(username=USERNAME, password=PASSWORD, disable_warning=True)

for comment in tqdm(praw.helpers.comment_stream(interface, 'all'), unit=' comments'):
    brain.learn(comment.body)

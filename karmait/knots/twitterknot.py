"""
Twiiter Official API: https://dev.twitter.com/rest/public

Reference:
    https://github.com/jbeluch/meetup-rsvper/blob/70ac6c291c48c1c52b13d850c9e93aad32301fc3/meetup-rsvper.py
"""
from .baseknot import BaseKnot


class TwitterKnot(BaseKnot):
    def get_tweets(self, since=None, until=None):
        pass

    def count_karma(self, since=None, until=None):
        pass

    def get_what_have_i_done(self, since=None, until=None):
        pass

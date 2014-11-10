from twitter import *
print "parody parrot"

t = Twitter(
    auth=OAuth(token, token_key, con_secret, con_secret_key)))

# Get your "home" timeline
t.statuses.home_timeline()
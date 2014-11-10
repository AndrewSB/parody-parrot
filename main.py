from twitter import *
print "parody parrot"

twitter_stream = TwitterStream(auth=OAuth("183299989-LE4WbYNKTLxibK5vx1meVMEdZpUjFQcfRoEdtkfX", "uhREnKogXj49HgqeX1uxvTC7WgEJHQkOVci2lKRrRGw7j", "zbsCXr4Bel5pxuHGi9KXcDFaR", "cgBUYOlgGKC1f4A57bn1iHnV3PlVq4B0nV13m98V2I3rpQonu7"))

iterator = twitter_stream.statuses.sample()

for tweet in iterator:
	print tweet
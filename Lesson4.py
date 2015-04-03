import twitter, datetime, urllib2, urllib, xively

user = 565929137 # My ID

file = open("res/twiterCredentials.txt")
cred = file.readline().strip().split(',')

api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],
					access_token_key=cred[2],access_token_secret=cred[3])

statuses = api.GetUserTimeline(user)

print(statuses[0].text)

response = urllib2.urlopen("http://www.ebay.co.uk/")

html = response.read()

print(html[:350])

raw_input("promt: ")
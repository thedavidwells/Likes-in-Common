#  DAVID WELLS & TANDRA FELLY

#  CS385- SOCIAL NETWORK ANALYSIS
#  FINAL PROJECT 
#  Description:  The following code uses the Facebook Graph API to gather data
#  The access token is a unique token acquired from David's facebook account.
#  It may expire after a time, however at the time of 

#  To get a Facebook Graph API Key go to http://developers.facebook.com/tools/explorer
#  This is where you will get your access token and paste it in below for the code to use.

#  Currently the code gathers all of the user's friend ID's, and then perfors a search on each
#  of those friends to determine all of their likes.

#  The goal of this tool is to be able to compare likes of you and your friends using different
#  methods of analysis.  One such example of analysis would be measuring the COSINE SIMILARITY 
#  of these likes.  

#  This code requires the use of simplejson - just use:  sudo easy_install simplejson  in the terminal. 
from urllib2 import urlopen
from simplejson import loads
import codecs
 

#  FACEBOOK GRAPH API INFORMATION
accessToken = 'CAAFOLzU4dccBAAsu4n8pBifvXi0fCqKhHZCaYhbhw5e7DLgTCVEEwZAECZAo3oSymnBKSjBv06xpRBZAQzQDusu8qRLf9oCxyTHXpx0VkvxvnewEKzXsJsXN2Swd15T5TnZAhZB2ZAe1nzgRkWmjmtZBx31epYbkta4ZD'  #INSERT YOUR ACCESS TOKEN
userId = '302800032'           #DAVID WELLS' FACEBOOK ID


# Read my FRIENDS as a json object
url='https://graph.facebook.com/' + userId + '/friends?access_token=' + accessToken
friends = loads(urlopen(url).read())
 
	#  Data comes in looking like this:
	# {
	#   "data": [
	#     {
	#       "name": "Toki Burke", 
	#       "id": "3205008"
	#     }, 
	#     {
	#       "name": "Josh Kim", 
	#       "id": "3206985"
	#     }, 
	#     {
	#       "name": "Melissa Dycus", 
	#       "id": "3219662"
	#     }, 
	#     {
	#       "name": "Jackie Klekman", 
	#       "id": "3616955"
	#     }, 
	#     {
	#       "name": "Emma Conley", 
	#       "id": "6014838"
	#     }, 
	#     ......



#  Iterate through the friends array and print out the friend ID, and friend's Name.
#  This is mostly to just to make sure the data looks right, but you can use it to
#  find a friend's userId if you need to.
for item in friends['data']:
    print item['id']
    print item['name']



#  Make a nested list of likes called database_of_likes
#  Level 1 is the friend, and Level 2 is a list of all of the things they like
database_of_likes = []

# Read LIKES as a json object
#url='https://graph.facebook.com/' + userId + '/likes?access_token=' + accessToken
#likes = loads(urlopen(url).read())

for item in friends['data']:
	userId = item['id']
	url='https://graph.facebook.com/' + userId + '/likes?access_token=' + accessToken
	likes = loads(urlopen(url).read())
	
	user_likes = []
	
	
	for i in likes['data']:
		current_like = i['name']

		# code to do test printing to the console
		# print i['id'].encode('ascii', 'ignore')
		# print i['name'].encode('ascii', 'ignore')

		user_likes.append( current_like )

	database_of_likes.append(user_likes)

print database_of_likes
		

d = {}

for likes in database_of_likes:
	d[like] = d.get[like,0] + 1

for i in d.keys():
	print i, d[i]














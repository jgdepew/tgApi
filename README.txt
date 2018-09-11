Documentation for tgApi 

the foundational url format is as follows:
	
	domain/<version>/api/
	version = ('v1', 'v2')

GET requests:
	domain/v2/api/venues/
		this will return a list of all venues
		NOTE: it is plural to indicate a list

	domain/v2/api/venues?field=field&anotherfield=anotherfield
		this will return a list of all venues based on your query parameters

	domain/v2/api/venue/<int:id>
		this will return a detail of a single venue
		NOTE: it is singular to indicate a single object

POST/PUT/DELETE requests:

	POST: domain/v2/api/venues/
		this will create a new venue object

	PUT: domain/v2/api/venue/<int:id>/update/
		this will do a partial_update on a venue with an unique id

	DELETE: domain/v2/api/venue/<int:id>/delete
		this will delete a venue with an unique id

The models are as follows:

	Entertainer:
		#v1
		name
		about
		created_at
		updated_at
		
		# v2
		# 'PA' = Performing Arts, 'SE' = Sporting Event
		type 

	Venue:
		#v1
		name
		address
		created_at
		updated_at
		
		# v2
		about 


	Event:
		#v1
		name
		entertainer - Foreign Key ID
		venue - Foreign Key ID
		date 
		created_at
		updated_at
	    
		#v2
		# 'PA' = Performing Arts, 'SE' = Sporting Event
		type 


What I would further implement if I had time:
	hyperlink for the foregin keys in the Event model
	pagination



Test Models for POST/PUT requests. Make them in order so that you can add Venue and Entertainer to the Event model

Entertainer
{
	"name": "Rufus",
	"about": "Aussie Band", 
	"type": "PA"
}

Venue
{
	"name": "Showbox",
	"address": "1234 1st St, Seattle WA",
	"about": "A venue"	
}

Event
{
	"name": "Rufus at the Showbox",
	"entertainer": 1,
	"venue": 1,
	"date": "2018-09-11T07:10:36.759961Z",
	"type": "PA"
}


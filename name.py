#!/usr/bin/env python

import web


urls = ('/','Index')
app = web.application(urls, globals())

class Index:
	def GET(self):
		return 'Hello World..'

if __name__ == "__main__":
	app.run()

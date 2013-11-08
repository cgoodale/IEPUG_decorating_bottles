# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# sigep311@gmail.com wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Cameron Goodale
# ----------------------------------------------------------------------------


















# from bottle import route, run, template, get, post, request
# from datetime import date

# @route('/')
# @route('/demo')
# def simple_function():
# 	return "Demo is working"

# @route('/hey/')
# @route('/hey/<name>')
# def h1_hey(name="Amigo"):
# 	message = template("<h1>Hey there {{temp_name}}! Template</h1>", temp_name=name)
# 	# message = "<h1>Hey there %s!</h1>" % name
# 	return message

# @get('/<year:int>/<month:int>/<day:int>')
# def iso_formatter(year, month, day):
# 	input_date = date(year, month, day)
# 	request
# 	return request


# run(host='localhost',
# 	port=8080,
# 	debug=True, reloader=True)
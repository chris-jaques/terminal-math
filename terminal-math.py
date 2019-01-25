"""
    Use this script to do simple comand line math
	*Use only square brackets
	*Use x for multiplication

	examples: 
	$ python3 terminal-math.py 40 / [3 x 20]
	$ python3 terminal-math.py sin[pi / 4] x log[25]
		
"""
import sys
import os
from math import *
import re
import json

CACHE_FILE=os.path.expanduser('~') + '/.varCache'
VARNAME_MATCH_RE = '\?([a-zA-Z_]+|_X_|\?)'

debug = False

def clearCache():
	os.remove(CACHE_FILE)

def saveCache(cache, file_handle):
	json.dump(cache,file_handle)
	

def getCacheVars():
	if not os.path.exists(CACHE_FILE):
		return {}

	with open(CACHE_FILE) as cache_file:
		try:
			cacheVars = json.load(cache_file)
		except ValueError:
			cacheVars = {}

	return cacheVars

def interpolate(expression, cache):
	vars = re.findall(VARNAME_MATCH_RE,expression)
	if debug:
		print(expression)
		print("VARS")
		print(vars)
	for v in vars:
		if v in cache:
			replace = cache[v]
		elif v == '_X_' and 'x' in cache:
			replace = cache['x']
		elif v == 'p1p2' and '?' in cache:
			replace = cache['?']
		else:
			replace = '0'
		expression = expression.replace('?'+v,str(replace))

	return expression

def calculate(args, cache):
	if len(args) > 0:
		expression = args.replace('[','(').replace(']',')').replace('??x','??*').replace('?x','?_X_').replace('x','*').replace('p1p2','??')
		expression = interpolate(expression, cache)
		if debug:
			print("EXPRESSION")
			print(expression)
		answer = eval(expression)
	else:
		answer = 0

	return answer


# Combine all args into a single string
args = ''
for i in range(1,len(sys.argv)):
	args += sys.argv[i]




cache = getCacheVars()

if args == 'v':
	print(cache)
elif args == 'c':
	clearCache()
	print("Cache Cleared")
elif re.match(VARNAME_MATCH_RE + '\=', args):
	with open(CACHE_FILE, 'w') as cache_file:
		var_name = re.search(VARNAME_MATCH_RE, args).group().partition('?')[2]
		var_value = args.split('=')[1]

		cache[var_name] = calculate(var_value, cache)
		json.dump(cache,cache_file)

		print(var_name + " = " + str(cache[var_name]))
else:	
	result = calculate(args, cache)
	with open(CACHE_FILE, 'w') as cache_file:
		cache['?'] = result
		json.dump(cache,cache_file)

	print(result,end='')


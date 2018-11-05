# The client of DDuplicated tool.
from os import path as opath, getcwd
from sys import argv

from dduplicated import commands

def get_paths(params):
	paths = []
	for param in params:
		path = opath.join(getcwd(), param)
		if opath.exists(path) and opath.isdir(path) and not opath.islink(path):
			paths.append(path)

	return paths


def main():
	params = argv
	processed_files = []
	# Remove the command name
	del params[0]

	if len(params) == 0 or "help" in params:
		commands.help()
	elif "detect" in params:
		processed_files = commands.detect(get_paths(params))

	elif "delete" in params:
		processed_files = commands.delete(commands.detect(get_paths(params)))
		
	elif "link" in params:
		processed_files = commands.link(commands.detect(get_paths(params)))
	
	else:
		commands.help()
	
	if len(processed_files) > 0:
		print(processed_files)
	else:
		print("No duplicates found")
		print("Great! Bye!")
		
	exit(0)

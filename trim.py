import sublime
import sublime_plugin
from  datetime import datetime

class TrimCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		insert_string = "- [{time}] ".format(time=datetime.now())
		print(insert_string)
		print(type(edit), type(self.view))
		for name in dir(self.view):
			if name[0] == '_':
				continue
			# if type(getattr(self.view,name) == 'function' ) :
			# 	continue
			print(name)
		print(self.view.word())


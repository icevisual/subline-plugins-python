import sublime
import sublime_plugin
from  datetime import datetime

class OutputCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		insert_string = "- [{time}] ".format(time=datetime.now())
		self.view.run_command('insert_snippet', {'contents': insert_string})
		# self.view.insert(edit, 0, "Hello, World!")

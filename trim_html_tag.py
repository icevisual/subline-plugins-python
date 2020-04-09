import sublime, sublime_plugin

class TrimHtmlTagCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    pattern = r'<(?:[^"\'>]|(["\'])[^"\']*\1)*>'
    # pattern = r'[\n\s]+'
    finds = self.view.find_all(pattern,0)
    startpoint = 0
    for i in range(len(finds)):
        start = self.view.find(pattern,startpoint)
        self.view.replace(edit,start,"")

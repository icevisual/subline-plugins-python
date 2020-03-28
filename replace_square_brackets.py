import sublime, sublime_plugin




class ReplaceSquareBracketsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("ReplaceSquareBracketsCommand")
        self.replace_(edit, r'\[',"{")
        self.replace_(edit, r'\]',"}")
        self.replace_(edit, r'\"',"\'")

    def replace_(self,edit,pattern0,replace0):
        pattern = pattern0
        # pattern = r'[\n\s]+'
        finds = self.view.find_all(pattern,0)
        startpoint = 0
        for i in range(len(finds)):
            start = self.view.find(pattern,startpoint)
            self.view.replace(edit,start,replace0)
import sublime, sublime_plugin

class AddCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents": "//"
            }
        )

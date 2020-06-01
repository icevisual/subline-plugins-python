import sublime, sublime_plugin

class TrimHtmlTagCommand(sublime_plugin.TextCommand):

  @staticmethod
  def number2chinese(num):
    names = '零一二三四五六七八九十百千万'
    result = ''
    if num <= 10:
      return names[num:num+1]
    if num < 100:
      shi = int(num / 10)
      ge = num % 10
      result = names[shi:shi+1] + names[10:11]
      if ge > 0:
        result += names[ge:ge+1]
      return result
    if num < 1000:
      bai = int(num / 100)
      shi = int((num - bai * 100)/ 10)
      ge = num % 10
      result = names[bai:bai+1] + names[11:12]
      if shi > 0:
        result += names[shi:shi+1]+ names[10:11]
      elif ge != 0:
        result += names[0:0+1]
      if ge > 0:
        result += names[ge:ge+1]
      return result
    return result

  def print_sql(self):
    print(TrimHtmlTagCommand.number2chinese(100))
    # ('N000000000020A', 'G20', '通用 二十', '2', '0', ':108:', '1492076318')
    for i in range(21,101):
      print("('N000000000%03dA', 'G%d', '通用 %s', '2', '0', ':108:', '1492076318')," % (i, i, TrimHtmlTagCommand.number2chinese(i)))
    a = 2
    if a is 2:
        return

  def run(self, edit):
    pattern = r'<(?:[^"\'>]|(["\'])[^"\']*\1)*>'
    # pattern = r'[\n\s]+'
    finds = self.view.find_all(pattern,0)
    startpoint = 0
    for i in range(len(finds)):
        start = self.view.find(pattern,startpoint)
        self.view.replace(edit,start,"")

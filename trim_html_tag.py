import sublime, sublime_plugin
import os

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
    print("INSERT INTO `sm_smell` (`smell_sn`, `en_name`, `cn_name`, `type`, `is_pc_show`, `tags`, `created_at`) VALUES")
    for i in range(101,1000):
      print("('N000000000%03dA', 'G%d', '通用 %s', '2', '0', ':108:', '1492076318')," % (i, i, TrimHtmlTagCommand.number2chinese(i)))

  def print_sql_f(self):
    print(TrimHtmlTagCommand.number2chinese(100))
    with open("a.txt","w") as f:
      # ('N000000000020A', 'G20', '通用 二十', '2', '0', ':108:', '1492076318')
      f.write("INSERT INTO `sm_smell` (`smell_sn`, `en_name`, `cn_name`, `type`, `is_pc_show`, `tags`, `created_at`) VALUES\n")
      for i in range(101,1000):
        f.write("('N000000000%03dA', 'G%d', '通用 %s', '2', '0', ':108:', '1492076318'),\n" % (i, i, TrimHtmlTagCommand.number2chinese(i)))

  def run(self, edit):
    return self.print_sql_f()
    pattern = r'<(?:[^"\'>]|(["\'])[^"\']*\1)*>'
    # pattern = r'[\n\s]+'
    finds = self.view.find_all(pattern,0)
    startpoint = 0
    for i in range(len(finds)):
        start = self.view.find(pattern,startpoint)
        self.view.replace(edit,start,"")

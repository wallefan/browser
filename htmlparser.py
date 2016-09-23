import html.parser

class Parser(html.parser.HTMLParser):
  def encounter_starttag(self, tag, attrs):
    try:
      self.current=tags.tagdict[tag](self.current, **dict(attrs))
    except:
      self.current=tags.BaseTag(self.current, **dict(attrs))
  def encounter_endtag(self, tag):
    self.current.finalize(tag)
  def encounter_data(self, data):
    self.current.add_data(data)
  def reset(self):
    self.current.finalize(None) # go all the way up the tree
    super().reset()

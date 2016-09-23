import html.parser

class Parser(html.parser.HTMLParser):
  def encounter_starttag(self, tag, attrs):
    try:
      self.current=tags.tagdict[tag](self.current, **dict(attrs))
    except:
      self.current=tags.BaseTag(self.current, **dict(attrs))
  def encounter_endtag(self, tag):
    self.current=self.current.finalize(tag)
  def encounter_data(self, data):
    self.current.add_data(data)
  def reset(self):
    self.encounter_endtag(None) # go all the way up the tree (implicit ending tag)
    super().reset()
  def encounter_comment(self, data):
    if data.startswith('if'):
      self.iffalse.append(...)
    elif data=='else':
      self.iffalse[-1]=not self.iffalse[-1]
    elif data=='endif':
      self.iffalse.pop()
  def encounter_startendtag(self, tag, attrs):
    # What am I supposed to do here?
    self.encounter_starttag(tag, attrs)
    self.encounter_endtag(tag)
    

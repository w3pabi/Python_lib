# Template extends

import string

template_text = '''
  Delimiter : %%
  Replated  : %width_underscore
  Ignored   : %notunderscored
'''

d = { 'width_underscore' : 'replaced',
      'notunderscored' : 'not replaced',
    }

class MyTemplate(string.Template):
    delimiter = '%'
    #idpattern is characters and  underbar and characters
    #so notunderscored is not _ if not_nuderscorecd is changed
    idpattern = '[a-z]+_[a-z]+'

t = MyTemplate(template_text)
print 'Modified ID pattern:'
print t.safe_substitute(d)

import re
import string

class MyTempleate(string.Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{) |          
    (?P<named>[_a-z][_a-z0-9]*)\}\} |
    (?P<braced>[_a-z][_a-z0-9]*)\}\} |
    (?P<invalid>)
    )
    '''


t = MyTempleate('''
{{{{
{{var}}
''')

print 'MATHCES:', t.pattern.findall(t.template)
print 'SUBSTITUTED:', t.safe_substitute(var='replatement')

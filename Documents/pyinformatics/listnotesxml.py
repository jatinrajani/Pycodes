import xml.etree.ElementTree as ET
input = '''
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>009</id>
<name>Brent</name>
</user>
</users>
</stuff>'''
tree=ET.fromstring(input)
lst=tree.findall('users/user')
for x in lst:
     print "name",x.find('name').text
     print "id",x.find('id').text
     print "attr",x.get('x')

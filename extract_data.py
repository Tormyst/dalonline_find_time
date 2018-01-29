# coding: utf-8
# %load my_session.py
import re
import sys

def clean(s):
    for l in s:
        if l == '&':
            return ' '
        if ord(l) >= ord('A') and ord(l) <= ord('Z'):
            return l
    return ' '
def decode_type(t):
    if t == 'b':
        return 'lab'
    if t == 'l':
        return 'lecture'
    if t == 't':
        return 'tutorial'

matcher = re.compile("""<b>([A-Z]{4} (\d*[^<]*))|(
<td CLASS="dett(.)"NOWRAP><p class="centeraligntext">(.*)</p></td>
<td CLASS="dett."NOWRAP><p class="centeraligntext">(.*)</p></td>
<td CLASS="dett."NOWRAP><p class="centeraligntext">(.*)</p></td>
<td CLASS="dett."NOWRAP><p class="centeraligntext">(.*)</p></td>
<td CLASS="dett."NOWRAP><p class="centeraligntext">(.*)</p></td>
<td CLASS="dett."NOWRAP>.*?(\d*)-(\d*)</td>)""", re.MULTILINE)

reader = open(sys.argv[1], 'r')
reader = reader.read()

output = open('results', 'w')
for match in matcher.finditer(reader):
    if match.group(1):
        string = 'CSCI {}'.format(match.group(2))
    else:
        string = ('{},{},{},{},{},{},{}-{}'.format(decode_type(match.group(4)),
                                            clean(match.group(5)),
                                            clean(match.group(6)),
                                            clean(match.group(7)),
                                            clean(match.group(8)),
                                            clean(match.group(9)),
                                            match.group(10),
                                            match.group(11)
                                                    ))
    print(string)
    print(string, file=output)
output.close()

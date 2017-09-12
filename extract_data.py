# coding: utf-8
# %load my_session.py
import re
import sys

def clean(s):
    if len(s) == 1:
        return s
    return ' '
def decode_type(t):
    if t == 'b':
        return 'lab'
    if t == 'l':
        return 'lecture'
    if t == 't':
        return 'tutorial'

matcher = re.compile("""(CSCI (\d*[^<]*))|(
<td CLASS="dett(.)"NOWRAP><p class="centeraligntext">(M|.*)</p></td>
<td CLASS="dett."NOWRAP><p class="centeraligntext">(T|.*)</p></td>
<td CLASS="dett."NOWRAP><p class="centeraligntext">(W|.*)</p></td>
<td CLASS="dett."NOWRAP><p class="centeraligntext">(R|.*)</p></td>
<td CLASS="dett."NOWRAP><p class="centeraligntext">(F|.*)</p></td>
<td CLASS="dett."NOWRAP>(\d*)-(\d*)</td>
<td CLASS="dett."NOWRAP>([^<]*)</td>)""", re.MULTILINE)

reader = open(sys.argv[1], 'r')
reader = reader.read()

output = open('results', 'w')
for match in matcher.finditer(reader):
    if match.group(1):
        string = 'CSCI {}'.format(match.group(2))
    else:
        string = ('{},{},{},{},{},{},{}-{},{}'.format(decode_type(match.group(4)),
                                            clean(match.group(5)),
                                            clean(match.group(6)),
                                            clean(match.group(7)),
                                            clean(match.group(8)),
                                            clean(match.group(9)),
                                            match.group(10),
                                            match.group(11),
                                            match.group(12)
                                                    ))
    print(string)
    print(string, file=output)
output.close()

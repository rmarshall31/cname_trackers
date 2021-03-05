#!/usr/bin/env python
from requests import get

cname_trackers_url = 'https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cname_trackers.txt'

output_filename = 'cname_trackers.txt'

request = get(cname_trackers_url)

with open(output_filename, 'w+') as output_file:
    for line in request.text.splitlines():
        if line.startswith('!#include'):
            foo = get(line.split(' ')[1])
            for bar in foo.text.splitlines():
                if bar.startswith('||'):
                    output_file.write(bar.lstrip('||').rstrip('^') + '\n')

import sys
import re

PATTERN = re.compile(
    r'(----(?:DOMAIN|SUBDOMAIN|VALUE|RECORDID|RECORDLINE): ).+?(?=----|$)'
)

for line in sys.stdin:
    print(PATTERN.sub(r'\1**REDACTED**', line), end='')
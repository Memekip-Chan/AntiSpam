#!/usr/bin/python3

print("Paste weird part of reddit title into this window, press Enter, then press Ctrl-C when done to generate an automod rule that blocks if it sees that text")

title = ""
while True:
    try:
        line = input()
    except:
        break
    title += line

regex = '"'

for char in title.strip():
    regex += ("\\U%08x" % ord(char)).upper()

regex += '"'

print(f'''\n\n
---
type: submission
crosspost_title+title (regex, includes): {regex}
moderators_exempt: false
action: remove
action_reason: "spambot"
modmail: the above post was removed for being spam''')

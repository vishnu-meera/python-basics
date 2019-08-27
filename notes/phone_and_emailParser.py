#! python3
import re , pyperclip
# create a regex for phone and
# create a regex for email
# get the texet off the clipboard
# extract


phoneRegEx = re.compile(r'''
	(((\d\d\d) | (\(\d\d\d\)))?
	(\s|-)
	\d\d\d
	-
	\d\d\d\d
	((ext(\.)?\s)|x
	(\d{2,5}))?)
''', re.VERBOSE)

emailRegEx = re.compile(r'''
	[a-zA-Z0-9_.+]+
	@
	[a-zA-Z0-9_.+]+
''',re.VERBOSE)
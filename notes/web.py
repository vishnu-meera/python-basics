import webbrowser, sys, pyperclip
#webbrowser.open('https://automatetheboringstuff.com')
sys.argv #['scriptname',values...]

if len(sys.argv)>1 :
	adres = ' '.join(sys.argv[1:])
else:
	adres = pyperclip.paste()

#webbrowser.open('https://www.google.com/maps/place/' + adres)

webbrowser.open('https://rei.splunkcloud.com/en-US/app/search/search?q=' + adres)

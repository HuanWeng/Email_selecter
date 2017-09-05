import csv

def get_page(url):
    try:
        import urllib
	return urllib.urlopen(url).read()
    except:
	return ''

if __name__ == '__main__':
        poo = get_page('http://www.mccormick.northwestern.edu/mechanical/people/faculty/')
	maildict = {}
	i = 0
	possispac = [' ', '\n', '\t', '\v', '\r']
	while True:
	    i = poo.find('href="mailto:', i) + 13
	    if i < 13:
		break
	    en = poo.find('"', i)
	    if poo[en: en + 7] == '">Email':
		spac = 0
		while poo[en + spac + 8] in possispac:
		    spac = spac + 1
	    	maildict[poo[en + spac + 8: poo.find('</a>', en)]] = poo[i: en]
	with open('email_selection.csv', 'w') as csvfile:
    	    writer = csv.writer(csvfile)
	    for ke, valu in maildict.items():
                writer.writerow([ke, valu])

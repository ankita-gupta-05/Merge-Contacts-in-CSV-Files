def merge_excel():
	with open('original_data.csv','rb') as f:
		reader=csv.reader(f,delimiter=',')
		dict1={row[1]:row[0::2] for row in reader}

	with open('final_data.csv','rb') as f:
		reader=csv.reader(f,delimiter=',')
		dict2={row[0]:row[1:] for row in reader}

	if 'Business Name' in dict1: del dict1['Business Name']
	if 'Business Name' in dict2: del dict2['Business Name']

	dict3={}
	for key in set().union(dict1,dict2):
		if key in dict1:
			dict3.setdefault(key,[]).extend(dict1[key])
			if key in dict2: dict3.setdefault(key,[]).extend(dict2[key])
			else:	dict3.setdefault(key,[]).extend([''])

		else:
			if key in dict2: dict3.setdefault(key,[]).extend(['','',dict2[key]])

	ofile=open('merged.csv','wb')
	writer = csv.DictWriter(ofile, fieldnames = ["Business NAme", "USER ID","Business Website","Video URL"])
	writer.writeheader()
	writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	for key in dict3.keys():
		writer.writerow([ key,dict3[key][0], dict3[key][1],dict3[key][2] ])

	ofile.close()

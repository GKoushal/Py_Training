prog_lang= ['Python', 'Java', 'Scala']

def lang_info(*lang,**lang_details):
	print(lang,lang_details)

lang_info('Python','Java','Scala', Py_index=0, Ja_index=1, Sc_index=1)

#for i in prog_lang:
	#print(i)
#Löffelsprache
import re


# def processString6(txt):
  
#   dictionary = {'a': 'alewa', 'e':'ellewe', 'i': 'ilewi', 'o': 'olewo', 'u': 'ulewu', 'ä': 'älewä', 'ö': 'ölewö', 'ü': 'ülewü', 'x': None, 'y': None, 'z': None}
#   transTable = txt.maketrans(dictionary)
#   txt = txt.translate(transTable)
#Text to Löffelsprache converter

inp = input()			#Text Input

rep_dict = {'a': 'alewa',		#dictionary a
            'e': 'elewe',		#dictionary e
            'i': 'ilewi',		#dictionary i
            'o': 'olewo',		#dictionary o
            'u': 'ulewu',		#dictionary u
            'ä': 'älewä',		#dictionary ä
            'ö': 'ölewö',		#dictionary ö
            'ü': 'ülewü',		#dictionary ü
            'ei': 'eilewei',	#dictionary ei
            'ie': 'ielewie',	#dictionary ie
            'au': 'aulewau'}	#dictionary au

def spoon_my_speech(string, rep_dict):
	pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)	#convertsion of letters by dict
	print(pattern.sub(lambda x: rep_dict[x.group(0)], string)) 														#Text Output

spoon_my_speech(inp,rep_dict) #calling function to convert text to "löffelsprache" | Usage: spoon_my_speech(TEXT,DICTIONARY)

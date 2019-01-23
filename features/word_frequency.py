import _global_
from collections import Counter
import glob
import errno

path_to_global = _global_.session_info['word_frequency']

characters_data = map(str.lower, _global_.key_words['characters'])
path = 'test_files/*.md'

files = glob.glob(path)

def catch():
	for file_name in files:
		try:
			with open(file_name, 'r') as f:
				new_key = file_name[len(path[-5::-1]):-3]

				path_to_global[new_key] = {"characters": {} }
				wordcount = Counter(f.read().lower().split())
				for key in characters_data:
					if key in wordcount:
						path_to_global[new_key]["characters"][key] = wordcount[key]
						
		except IOError as exc:
			if exc.errno != errno.EISDIR:
				raise

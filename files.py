
import os
x = os.listdir()
y = len(x)+1
ext={'python':['.py']},{'pictures':['.png','.jpg','.jpeg','.PNG']},{'Php':['.php']},{'javascript':['.js']},{'ht_cs':['.html','.css']},{'music':'.mp3'},{'video':'.mp4'}
files={}
for arrays in ext:
	for arrays_ext in arrays:
		#the extension array
		ext_array=arrays[arrays_ext]
		ext_array_n = len(ext_array)
		#the extension name
		#print(arrays_ext)
		for po in range(0,ext_array_n):	
			#the extension
			#print(ext_array[po])
			files.update({arrays_ext:[]})
			for fi in x:
				if ext_array[po] in fi:
					#print('We have one here is ', arrays_ext, fi)
					files[arrays_ext].append(fi)
					#print(fi)
		
		print(arrays_ext,' :',len(files[arrays_ext]))
#print(files)
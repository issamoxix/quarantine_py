import os
x = os.listdir()
y = len(x)+1
ext={'python':['.py']},{'pictures':['.png','.jpg','.jpeg']},{'Php':['.php']},{'javascript':['.js']},{'ht_cs':['.html','.css']}
files=[{}]
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
			files[0].update({arrays_ext:[]})
			for fi in x:
				if ext_array[po] in fi:
					#print('We have one here is ', arrays_ext, fi)
					files[0][arrays_ext].append(fi)
					print(fi)
		if len(files[0][arrays_ext]) >0:
			print(arrays_ext,' :',len(files[0][arrays_ext]))

#print(files)
		



		

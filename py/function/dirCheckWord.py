# -*- coding : utf-8 -*-
import os

def dirCheckWord(path,word,ispath=False):
	fileList = []
	root = os.path.abspath(path)
	for text in os.listdir(path):
		dirOrfile = os.path.join(root,text)
		if os.path.isdir(dirOrfile):
			fileListchild = dirCheckWord(dirOrfile,word,ispath)
			if fileListchild != [] :
				fileList.extend(fileListchild)
		else :
			if ispath : 
				resultCheck = dirOrfile 
			else : 
				resultCheck = text		
			if word in resultCheck:
				fileList.append(dirOrfile)	
	return fileList

def doCheck(path,word,ret='path',ispath=False):
	'''执行查找，ret参数如果是file并且返回结果就一个文件名包含指定字符串，
	就直接读取这个文件,ispath参数默认为False：只查找文件名中是否含有指定
	字符，如果为True：查找绝对路径下，包含目录名是否含有指定字符'''			
	fileList = dirCheckWord(path,word,ispath)
	if len(fileList) == 1 and ret == 'file':
		with open(fileList[0],'r',encoding='utf-8') as f:
			resultFlie = f.read()
			print(resultFlie)
	else :	
		for i in fileList:
			print(i)
	print('*** over ***')

if __name__ == '__main__':	
	#path =os.path.abspath('.')	
	#doCheck('C:/','Tencent Files','file')	
	doCheck('D:/','Tencent Files','path',True)	
	doCheck('E:/','Tencent Files','file')	
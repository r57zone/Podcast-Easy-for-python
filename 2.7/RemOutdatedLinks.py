#Podcast Easy 0.4 clear old links (27.08.2016) by r57zone
#http://r57zone.github.io
#Python 2.7

import urllib2, os

def GetUrl(url):
	try:
		responce=urllib2.urlopen(url)
		html=responce.read()
	except:
		html='-1'
	return html

def main():
	
	print ('')
	print (' Podcast Easy 0.4 clear old links')
	print ('')

	rss=open(os.getcwd()+'\\rss.txt', 'r') #if Linux os replace in path "\\" to "/"
	downloaded=open(os.getcwd()+'\\downloaded.txt', 'r').readlines() #if Linux os replace in path "\\" to "/"
	DownloadedUpdate=open(os.getcwd()+'\\downloaded.txt','w')

	source=''
	LinkCount=0
	
	#�������� ������ ������ / Creating a common list
	print(' ���� 1 - ���������� ������ ������')
	for i, address in enumerate(rss):
	
		#����� / Rss
		GetRss=GetUrl(address)
		if GetRss=='-1':
			break
			print('������, ����� "'+address+'" ����������. ���� ��� ��������� ������������, �� ������ ������� �� �� ����� "rss.txt" � ��������� �������.')

		source+=GetRss
	print(' ���� 2 - �������� ������ � ������')
	
	for line in downloaded:
		if source.find(line.replace("\n",''))==-1:
			LinkCount+=1
		else:
			DownloadedUpdate.write(line.replace("\n",'')+"\n")
	
	print(' ������� ������ : '+str(LinkCount))
 
	DownloadedUpdate.close()
	rss.close()
	#EN=Press ENTER to execute the command
	wait=raw_input('\n ������� Enter, ����� �����....')

if __name__=='__main__':
	main()

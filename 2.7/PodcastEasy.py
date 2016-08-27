# Podcast Easy 0.4 (27.08.2016) by r57zone
# http://r57zone.github.io
# Python 2.7

import urllib2, os

def GetUrl(url):
	try:
		responce=urllib2.urlopen(url)
		html=responce.read()
	except:
		html='-1'
	return html

def DownloadFile(url,path):
	filename=url.split('/')[-1]
	if os.path.exists(path+filename):
		FileExistsCounter=0
		while True:
			FileExistsCounter+=1
			if not os.path.exists(path+filename[0:filename.find('.mp3')]+'('+str(FileExistsCounter)+').mp3'):
				try:
					response=urllib2.urlopen(url)
					output=open(path+filename[0:filename.find('.mp3')]+'('+str(FileExistsCounter)+').mp3','wb')
					output.write(response.read())
					output.close()
					return True
				except:
					return False
				break
	else:
		try:
			response=urllib2.urlopen(url)
			output=open(path+filename,'wb')
			output.write(response.read())
			output.close()
			return True
		except:
			return False

def main():

	# ��������� / Settings
	# ������ / Example "C:\\Users\\User\\Desktop\\" - Windows, "/home/" - Linux
	PathDownloads=''
	# ��������� �������� / Download podcasts
	DownloadFiles=False
	# ------------------
	
	print ('')
	print (' Podcast Easy 0.4')
	print ('')

	rss=open(os.getcwd()+'\\rss.txt', 'r') # if Linux os replace in path "\\" to "/"
	downloaded=open(os.getcwd()+'\\downloaded.txt', 'r').read() # if Linux os replace in path "\\" to "/"

	# ������ ��� �������� ������ / List to download file
	download=[]

	for i, address in enumerate(rss):
	
		# ����� / Rss
		GetRss=GetUrl(address)
		if GetRss=='-1':
			continue

		# ������� ���� �� ����� ������ / Move tag to new line
		GetRss=GetRss.replace('<enclosure','\n<enclosure')
		GetRss=GetRss.replace('<pubDate>','\n<pubDate>')
  
		# ������� ��� ������ ����, ��������, ��� "http://pirates.radio-t.com/atom.xml" / �rutch for old feed, example - "http://pirates.radio-t.com/atom.xml"
		if GetRss.find('<audio src=')!=-1:
			GetRss=GetRss.replace('<audio src=','\n<audio url=')
		GetRss=GetRss.split('\n')
		
		print (' �������� ��������� ����: '+str(i+1)+' �� '+str(len(open(os.getcwd()+'\\rss.txt', 'r').readlines()))) # if Linux os replace in path "\\" to "/", EN=Checking news feeds: ... of
		
		for line in GetRss:
   
			# ���� ������ � ".MP3" / Look for line with ".MP3"
			if line.upper().find('.MP3')!=-1:
   
				# �������� ������ �� ������� ���� "<GUID" / Check line for the presence of tag "<GUID" 
				if line.upper().find('<GUID')==-1:
    
					# ������ �� mp3 ���� / Link to mp3 file
					MyLink=line[line.upper().find('URL="')+5:line.upper().find('.MP3')+4]
	 
					if MyLink.upper()[0:7]=='HTTP://' or MyLink.upper()[0:8]=='HTTPS://':
	 
						# ��������� ������ �� ������� � �� ������ ����������� ��������� / Check presence of link on list of downloaded podcasts
						if downloaded.find(MyLink)==-1:
							
							# ��������� �� ��������� �� ��� ��� � ������ �������� / Check if it is added in the download list
							if not MyLink in download:
      
								print (' ������ ����� ������� �� '+address.replace("\n",'')) # EN=Found a new podcast on
								# ���������� ������ � ������ ��� �������� / Add link to download list
								download.append(MyLink)
								
	
	if os.path.exists(os.getcwd()+'\\downloaded.txt'): # if Linux os replace in path "\\" to "/"
		DownloadedUpdate=open(os.getcwd()+'\\downloaded.txt', 'a') # if Linux os replace in path "\\" to "/"
	else:
		DownloadedUpdate=open(os.getcwd()+'\\downloaded.txt', 'w') # if Linux os replace in path "\\" to "/"
	
	# ������� ����������� ������ / Counter donwloaded files
	DownloadedCount=0
	# ������� ������ �������� / Counter error downloaded
	ErrorCount=0
	
	if len(download)>0:
		if DownloadFiles:
			# EN=Downloading podcasts : 0 of 
			print(' ��������� ��������� : 0 �� '+str(len(download)))
		else:
			# ��� �������� ������� ��������� / All podcasts downloaded
			DownloadedCount=1
	
	# �������� ������ / Download files
	for link in download:
		if DownloadFiles:
			if DownloadFile(link,PathDownloads)!='-1':
				# ���������� ������ �� ����������� ��������, ����� �� ��������� �� ����� / Save links to downloaded podcasts to not download them again
				DownloadedUpdate.write(link+"\n")
				DownloadedCount+=1
				# EN=Downloading podcasts : of
				print(' ��������� ��������� : '+str(DownloadedCount)+' �� '+str(len(download)))
			else:
				ErrorCount+=1
		else:
			DownloadedUpdate.write(link+"\n")

	if ErrorCount>0 or DownloadedCount>0:
		if ErrorCount==0:
			# EN=All podcasts downloaded
			print(' ��� �������� ���������')
		else:
			# EN=Failed download podcasts : 
			print(' �� ������� ��������� ��������� : '+str(ErrorCount))
	if ErrorCount==0 and DownloadedCount==0:
		# EN=Not found new podcasts
		print(' ����� ��������� �� �������')
 
	rss.close()
	DownloadedUpdate.close()
	# EN=Press ENTER to execute the command
	wait=raw_input('\n ������� Enter, ����� �����....')

if __name__=='__main__':
	main()

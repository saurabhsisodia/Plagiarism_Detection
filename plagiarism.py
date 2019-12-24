# Plagiarism Detection, Implementation using Rabin Karp Hash Technique.
' importing packages'
from nltk import word_tokenize,PorterStemmer
from nltk.corpus import stopwords
from collections import defaultdict

class Plagirism_Detection(object):
	
	def __init__(self,file1,file2):
		self.file1=file1
		self.file2=file2
		self.data1=''
		self.data2=''
		self.SH=0
		self.TH1=0
		self.TH2=0
		self.Files()

	# Basic File Handling
	def Files(self):
		
		self.data1=self.file1.read().lower()
		self.data2=self.file2.read().lower()
		self.file1.close()
		self.file2.close()
		self.Text_Preprocess()

	# Text Preprocessing
	# Removing stopwords and convert document into list of strings
	def Text_Preprocess(self):
		
		tokenize_data1=word_tokenize(self.data1)
		tokenize_data2=word_tokenize(self.data2)

		self.data1,self.data2=[],[]
		en_stops=set(stopwords.words('english'))
		for w in tokenize_data1:
			if w not in en_stops:
				self.data1.append(w)

		for w in tokenize_data2:
			if w not in en_stops:
				self.data2.append(w)
		self.All_Hash()

	# Calculating the Hash Value of a Particular word
	def Hash_Value(self,word):
		prime=101
		d=256
		h=1
		p=0
		m=len(word)

		for i in range(m-1):
			h=(h*d) % prime

		for i in range(m):
			p=(d*p+ord(word[i])) %prime

		return p

	# Find The similar hash values and total hash values in each document.
	def All_Hash(self):
		checked1,checked2=defaultdict(bool),defaultdict(bool)
		Hash_set1,Hash_set2=defaultdict(int),defaultdict(int)
		#TH1,TH2=0,0
		#SH=0

		# Total Hash of document first
		for word in self.data1:
			h=self.Hash_Value(word)
			self.TH1+=1
			Hash_set1[h]+=1

		# Total Hash of document second
		for word in self.data2:
			h=self.Hash_Value(word)
			self.TH2+=1
			Hash_set2[h]+=1

		# Find the Similar Hash values in documents
		for h in Hash_set1:
			if checked1[h]==False:
				self.SH+=min(Hash_set1[h],Hash_set2[h])
				checked1[h]=True
				checked2[h]=True

		for h in Hash_set2:
			if checked2[h]==False:
				self.SH+=min(Hash_set2[h],Hash_set1[h])
				checked2[h]=True
				checked1[h]=True

		#self.Find_Plagiarism_Rate(SH,TH1,TH2)

	# return Plagiarism rate 
	def Find_Plagiarism_Rate(self):
		p_rate=(2*self.SH/(self.TH1+self.TH2))*100
		return p_rate
		#print("Plagiarism Rate is %f percent" %(p_rate))
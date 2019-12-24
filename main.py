from tkinter import StringVar,filedialog
from tkinter import *
from functools import partial
import plagiarism

class frontend(object):
	def __init__(self):
		self.file1=''
		self.file2=''
	def Browse_Box1(self):
		self.file1=filedialog.askopenfilename(initialdir='/home/saurabh/NewFolder')
		#print(self.file)
		Label(text=self.file1).place(x=600,y=200)
	def Browse_Box2(self):
		self.file2=filedialog.askopenfilename(initialdir='/home/saurabh/NewFolder')
		Label(text=self.file2).place(x=600,y=300)
		print(self.file1)
		print(self.file2)

	def call_algo(self):
		obj2=plag.Plagirism_Detection(open(self.file1),open(self.file2))
		return obj2.Find_Plagiarism_Rate()
	def output(self):
		answer=self.call_algo()
		Label(text="plagiarism rate is "+ str(answer)).place(x=700,y=450)



obj=frontend()

' creating root window'
root=Tk()

' defining size of the root window'
root.geometry("1000x500")

' title of the root window'
root.title("PLAGIARISM DETECTION")

'heading of the window'
main_heading=Label(root,text="PLAGIARISM DETECTION",font=("arial",40,"bold")).place(x=300,y=0)


' botton for the output generated '
btn1=Button(root,text="Show_OUTPUT",command=obj.output).place(x=700,y=400)


label=Label(root,text="DOCUMENT-1").place(x=100,y=200)

button=Button(text="Browse",width=30,command=obj.Browse_Box1).place(x=250,y=195)
	
label=Label(root,text="DOCUMENT-2").place(x=100,y=300)
	
button=Button(text="Browse",width=30,command=obj.Browse_Box2).place(x=250,y=300)
root.mainloop()
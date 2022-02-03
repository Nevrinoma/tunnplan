from tkinter import *
from tkinter.font import Font

root=Tk()
root.geometry("1100x900")
root.title("Tunniplaan")
root.configure(bg="white")

p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
j=0

#for i in range (1,10,2):

ep = Label(root,text="Esmaspäev",font="Arial 15",fg="black",bg="white",height=6,width=10,relief="ridge").grid(row=1,column=0,rowspan=2,sticky=N+S+W+E)
tp = Label(root,text="Teisipäev",font="Arial 15",fg="black",bg="white",height=6,width=10,relief="ridge").grid(row=3,column=0,rowspan=2,sticky=N+S+W+E)
kp = Label(root,text="Kolmapäev",font="Arial 15",fg="black",bg="white",height=6,width=10,relief="ridge").grid(row=5,column=0,rowspan=2,sticky=N+S+W+E)
np = Label(root,text="Neljapäev",font="Arial 15",fg="black",bg="white",height=6,width=10,relief="ridge").grid(row=7,column=0,rowspan=2,sticky=N+S+W+E)
rp = Label(root,text="Reede",font="Arial 15",fg="black",bg="white",height=6,width=10,relief="ridge").grid(row=9,column=0,rowspan=2,sticky=N+S+W+E)

tund0= Label(root,text="0",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=1,sticky=N+S+W+E)
tund1= Label(root,text="1",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=2,sticky=N+S+W+E)
tund2= Label(root,text="2",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=3,sticky=N+S+W+E)
tund3= Label(root,text="3",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=4,sticky=N+S+W+E)
tund4= Label(root,text="4",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=5,sticky=N+S+W+E)
tund5= Label(root,text="5",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=6,sticky=N+S+W+E)
tund6= Label(root,text="6",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=7,sticky=N+S+W+E)
tund7= Label(root,text="7",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=8,sticky=N+S+W+E)
tund8= Label(root,text="8",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=9,sticky=N+S+W+E)
tund9= Label(root,text="9",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=10,sticky=N+S+W+E)
tund10= Label(root,text="10",font="Arial 19",fg="black",bg="white",height=2,width=5,relief="ridge").grid(row=0,column=11,sticky=N+S+W+E)

levverh= Label(root,text="",font="Arial 19",fg="black",bg="white",height=2,width=3,relief="ridge").grid(row=0,column=0,sticky=N+S+W+E)

ept0= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=1,column=1,columnspan=1,sticky=N+S+W+E)
ept6= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=1,column=7,columnspan=1,sticky=N+S+W+E)
tpt5= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=3,column=6,columnspan=1,sticky=N+S+W+E)
tpt0= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=3,column=1,columnspan=1,sticky=N+S+W+E)
kpt0= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=5,column=1,columnspan=1,sticky=N+S+W+E)
npt0= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=7,column=1,columnspan=1,sticky=N+S+W+E)
rpt0= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=9,column=1,columnspan=1,sticky=N+S+W+E)

ept10= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=1,column=11,columnspan=1,sticky=N+S+W+E)
tpt10= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=3,column=11,columnspan=1,sticky=N+S+W+E)
kpt10= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=5,column=11,columnspan=1,sticky=N+S+W+E)
npt10= Button(root,text="Rühmaju\nhataja\ntund",font="Arial 9",fg="black",bg="#ABE0FF",height=6,width=5,relief="ridge").grid(row=7,column=11,columnspan=1,sticky=N+S+W+E)
rpt10= Label(root,text="",font="Arial 19",fg="black",bg="white",height=6,width=5,relief="ridge").grid(row=9,column=11,columnspan=1,sticky=N+S+W+E)





#esmaspäev
ept1= Button(root,text="Programmeerimise alused",font="Arial 9",fg="black",bg="#ABE0FF",height=5,width=5,relief="ridge").grid(row=1,column=2,columnspan=3,sticky=SW+SE)
#ept11= Label(root,text="",font="Arial 9",fg="black",bg="white",height=5,width=5,relief="ridge").grid(row=1,column=2,columnspan=1,sticky=NW+NE)
ept2 = Button(root,text="Multimeedia",font="Arial 9",fg="black",bg="#ABC0FF",height=5,width=5,relief="ridge").grid(row=1,column=3,columnspan=2,sticky=NW+NE)
ept4 = Button(root,text="Inglise Keel",font="Arial 9",fg="black",bg="#FFFFF0",height=5,width=5,relief="ridge").grid(row=1,column=5,columnspan=2,sticky=NW+NE)
ept42 = Button(root,text="Multimeedia",font="Arial 9",fg="black",bg="#ABC0FF",height=5,width=5,relief="ridge").grid(row=1,column=5,columnspan=2,sticky=SW+SE)
ept7 = Button(root,text="Operatsioonisüstee\nmide alused",font="Arial 9",fg="black",bg="#E080FF",height=5,width=5,relief="ridge").grid(row=1,column=8,columnspan=2,sticky=S+W+E+N)
ept8 = Button(root,text="Tugiõpe\n(matema\natika)",font="Arial 9",fg="black",bg="#FCB9D1",height=5,width=5,relief="ridge").grid(row=1,column=10,columnspan=1,sticky=S+W+E+N)

#teisipäev
tpt1 = Button(root,text="Inglise keel\n(programmeerimise\nalused)",font="Arial 9",fg="black",bg="#CBCBCB",height=5,width=5,relief="ridge").grid(row=3,column=2,columnspan=2,sticky=NW+NE)
tpt1 = Button(root,text="Inglise Keel",font="Arial 9",fg="black",bg="#E0ABFF",height=5,width=5,relief="ridge").grid(row=3,column=2,columnspan=2,sticky=SW+SE)
tpt3 = Button(root,text="Füüsika",font="Arial 9",fg="black",bg="#FFFFD0",height=5,width=5,relief="ridge").grid(row=3,column=4,columnspan=2,sticky=S+W+E+N)
tpt6 = Button(root,text="Eesti keel",font="Arial 9",fg="black",bg="#CCB3FF",height=5,width=5,relief="ridge").grid(row=3,column=7,columnspan=1,sticky=NW+NE)
tpt7 = Button(root,text="Eesti keel",font="Arial 9",fg="black",bg="#CCB3FF",height=5,width=5,relief="ridge").grid(row=3,column=8,columnspan=1,sticky=NW+NE)
tpt6 = Button(root,text="Inglise keel\n(programmeerimise\nalused)",font="Arial 9",fg="black",bg="#CBCBCB",height=5,width=5,relief="ridge").grid(row=3,column=7,columnspan=2,sticky=SW+SE)
tpt8 = Button(root,text="Matemaatika",font="Arial 9",fg="black",bg="#FCB9D1",height=5,width=5,relief="ridge").grid(row=3,column=9,columnspan=1,sticky=S+W+E+N)
tpt9 = Button(root,text="Tugiõpe\n(Keemia)",font="Arial 9",fg="black",bg="#E080E0",height=5,width=5,relief="ridge").grid(row=3,column=10,columnspan=1,sticky=S+W+E+N)

#kolmapäev
kpt1= Button(root,text="Programmeerimise alused",font="Arial 9",fg="black",bg="#ABE0FF",height=5,width=5,relief="ridge").grid(row=5,column=2,columnspan=3,sticky=NW+NE)
kpt1 = Button(root,text="Eesti keel",font="Arial 9",fg="black",bg="#CAB4C7",height=5,width=5,relief="ridge").grid(row=5,column=2,columnspan=1,sticky=SW+SE)














root.mainloop()
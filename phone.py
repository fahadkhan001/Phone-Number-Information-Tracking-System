from tkinter import *
from tkinter import messagebox
import folium
import phonenumbers as pn 
from phonenumbers import geocoder, carrier, timezone




Root = Tk()

Root.geometry("6700x1500") 

Root.title("Phone Number Information-tracker")

Root.eval('tk::PlaceWindow . center')

Root.eval('tk::PlaceWindow . center')

Root.config(bg="#fff")

H = Root.winfo_screenheight()

W = Root.winfo_screenwidth()

w = W-50
h = H-82

Root.maxsize(w, h)

Root.minsize(w, h)



def get():
	# phon number 
	n = Inp.get()
	ln = len(n)
	#print(ln)


	if(ln<10 or ln>10):
		messagebox.showwarning("Phone Number information Tracker", "Invalid number")
		

	a = "+91"

	gnum = a+n

	r = pn.parse(gnum)



	F = Frame(Root, width=620, height=250, bg="#fff")
	F.place(x=20, y=430)
	


	rl = Label(F, text=r, font="Arial 10 bold", fg="#111542", bg="#fff")
	rl.place(x=20, y=20)
	


	# geocoder 

	G = geocoder.description_for_number(r, "en")

	gl = Label(F, text="Location : "+G, font="Arial 10 bold", fg="#111542", bg="#fff")
	gl.place(x=20, y=80)
	



	# Carrier

	C = carrier.name_for_number(r, "en")

	cl = Label(F, text="Network : "+C, font="Arial 10 bold", fg="#111542", bg="#fff")
	cl.place(x=20, y=120)
	


	# timezone 
	T = timeZone = timezone.time_zones_for_number(r)

	t = Label(F, text="Timezone : ", font="Arial 10 bold", fg="#111542", bg="#fff")
	t.place(x=20, y=160)


	tl = Label(F, text=T, font="Arial 10 bold", fg="#111542", bg="#fff")
	tl.place(x=80, y=160)



	#latitude and longitude
	
	from bck import lat, lng


	l= lat


	L= Label(F, text="latitude:",font="Arial 10 bold", fg="#111542", bg="#fff")
	L.place(x=20,y=180)



	L1= Label(F, text=l,font="Arial 10 bold", fg="#111542", bg="#fff")
	L1.place(x=80,y=180)




	A= lng


	a= Label(F, text="longitude:",font="Arial 10 bold", fg="#111542", bg="#fff")
	a.place(x=20,y=200)

	a1= Label(F, text=A,font="Arial 10 bold", fg="#111542", bg="#fff")
	a1.place(x=80,y=200)
	

	from bck import getloc


	b= getloc.address


	B= Label(F, text="location:",font="Arial 10 bold", fg="#111542", bg="#fff")
	B.place(x=20,y=220)


	B1= Label(F,text=b,font="Arial 10 bold", fg="#111542", bg="#fff")
	B1.place(x=80,y=220)
    


	Inp.delete(0, "end")

	



canvas = Canvas(Root, width = 670, height = 1150)
canvas.place(x=0, y=0)



N = Label(text="Phone Number Information Tracker", fg="#111542", font="Arial 25 bold", bg="#fff")
N.place(x=50, y=50)



number = Label(text="Mobile Number :",font="Arial 20 bold" ,bg="#fff")
number.grid(row=0, column=0, pady=200, padx=10)



Inp = Entry(width=70)
Inp.grid(row=0, column=1, pady=200)



btn = Button(text="TRACK", bg="blue", fg="#fff", font="Arial 15 bold", command=get)
btn.place(x=50, y=300)



	# Exit
exit = Button(text="EXIT", bg="red", fg="#fff", width=6, font="Arial 15 bold", command=quit)
exit.place(x=345, y=300)







#this is used when your application is ready to run, it is an ifnite loop used to run the application

Root.mainloop()
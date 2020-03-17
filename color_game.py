from tkinter import *
import requests
import mysql.connector
import random

class Color:
    def __init__(self):

        self.conn=mysql.connector.connect(host="remotemysql.com", user=" HCtIRqQfLj",password="Ybw3JBxfky",database=" HCtIRqQfLj")
        self.mycursor=self.conn.cursor()
        self.root=Tk()
        self.root.title("LOGIN SYSTEM")

        self.root.minsize(400,600)
        self.root.maxsize(400,600)
        self.root.configure(background="#FFFFFF")

        self.lable1=Label(self.root,text="LOGIN OR REGISTRATION",bg="#FFFFFF",fg="#7D9F4C")
        self.lable1.configure(font=("Cooper black",20))
        self.lable1.pack(pady=(30,10))

        self.click=Button(self.root,text="REGISTER",bg="#fff",fg="#992439",width=25,height=2,command=lambda:self.register())
        self.click.configure(font=("Constantia",10,"bold"))
        self.click.pack(pady=(10,20))

        self.click=Button(self.root,text="LOGIN",bg="#fff",fg="#992439",width=25,height=2,command=lambda:self.login())
        self.click.configure(font=("Constantia",10,"bold"))
        self.click.pack(pady=(10,20))


        self.result=Label(self.root,text="",bg="#FFFFFF",fg="#C61B6B")
        self.result.configure(font=("Constantia",14,"bold"))
        self.result.pack(pady=(5,10))
        
        self.root.mainloop()

    def register(self):
        
        self.root.destroy()
        self.root2=Tk()
        self.root2.title("REGISTRATION")

        self.root2.minsize(400,600)
        self.root2.maxsize(400,600)
        self.root2.configure(background="#AF708D")

        self.lable1=Label(self.root2,text="REGISTRATION FORM",bg="#AF708D",fg="#fff")
        self.lable1.configure(font=("Algerian",22,"bold"))
        self.lable1.pack(pady=(30,10))

        

        self.lable2=Label(self.root2,text="NAME",bg="#AF708D",fg="#fff")
        self.lable2.configure(font=("Constantia",22,"bold"))
        self.lable2.pack(pady=(30,10))

        self.user_name=Entry(self.root2)
        self.user_name.pack(ipadx=40,ipady=5)

        
        self.lable3=Label(self.root2,text="EMAIL",bg="#AF708D",fg="#fff")
        self.lable3.configure(font=("Constantia",22,"bold"))
        self.lable3.pack(pady=(30,10))

        self.user_email=Entry(self.root2)
        self.user_email.pack(ipadx=40,ipady=5)

        self.lable4=Label(self.root2,text="PASSWORD",bg="#AF708D",fg="#fff")
        self.lable4.configure(font=("Constantia",22,"bold"))
        self.lable4.pack(pady=(30,10))

        self.user_password=Entry(self.root2)
        self.user_password.pack(ipadx=40,ipady=5)


        self.click1=Button(self.root2,text="OK",bg="#FFFFFF",fg="#AF708D",width=25,height=2,command=lambda:self.registered())
        self.click1.configure(font=("Constantia",10,"bold"))
        self.click1.pack(pady=(10,20))

        self.root2.mainloop()


    def login(self):
        self.root.destroy()
                            
            
        self.root3=Tk()                                    
                              


           
        self.root3.title("LOGIN FORM")
        self.root3.minsize(600,600)
        self.root3.configure(background="#B6511A")



            
        self.Label1=Label(self.root3,text="LOGIN FORM",bg="#B6511A",fg="#FFF")
        self.Label1.configure(font=("Algerian",22,"bold"))
        self.Label1.pack(pady=(30,10))


            
            
        self.Label2=Label(self.root3,text="Enter your E-mail:",bg="#B6511A",fg="#FFF")
        self.Label2.configure(font=("Garamond",15,"bold"))
        self.Label2.pack(pady=(10,5))
        self.user_email=Entry(self.root3)
        self.user_email.pack(ipadx=6,ipady=6)

            
        self.Label2=Label(self.root3,text="Enter your password:",bg="#B6511A",fg="#FFF")
        self.Label2.configure(font=("Garamond",15,"bold"))
        self.Label2.pack(pady=(10,5))
        self.user_password=Entry(self.root3)
        self.user_password.pack(ipadx=6,ipady=6)

        self.click2=Button(self.root3,text="OK",bg="#FFFFFF",fg="#B6511A",width=5,height=1,command=lambda:self.logined())
        self.click2.configure(font=("Garamond",10,"bold"))
        self.click2.pack(pady=(5,5))

        self.root3.mainloop()




    def registered(self):
        
        name=self.user_name.get()
            
        x=len(name)
            
        if (x==0):
            self.root=Tk()

            self.root.title("ERROR Form")
            self.root.minsize(100,100)
                  
            self.root3.configure(background="#EA347C")
                              
            self.Label3=Label(self.root,text="INVALID NAME",bg="#EA347C",fg="#FFF")
            self.Label3.configure(font=("Garamond",15,"bold"))
            self.Label3.pack(pady=(10,5))
                  
            self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#EA347C",width=5,height=1,command=lambda:self.register1())
            self.click2.configure(font=("Garamond",10,"bold"))
            self.click2.pack(pady=(5,5))
            self.root.mainloop()
        
        
                  
        name1=name.upper()
          
        email=self.user_email.get()
        f=0
           
        for i in email:
             
            if(i=="@"  or i=="."):
                f+=1
            
        if f!=2 :
            self.root=Tk()
                   
            self.root.title("ERROR Form")
            self.root.minsize(100,100)
                  
            self.root.configure(background="#EA347C")
                              
            self.Label3=Label(self.root,text="INVALID EMAIL",bg="#EA347C",fg="#FFF")
            self.Label3.configure(font=("Garamond",15,"bold"))
            self.Label3.pack(pady=(10,5))
                   
            self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#EA347C",width=5,height=1,command=lambda:self.register1())
            self.click2.configure(font=("Garamond",10,"bold"))
            self.click2.pack(pady=(5,5))
            self.root.mainloop()
                   
        password=self.user_password.get()
            
        try:
            self.mycursor.execute("INSERT INTO users (user_id,name,email,password) VALUES (NULL,'{}','{}','{}')".format(name1,email,password))

            self.conn.commit()

        except Exception as e:
            self.root=Tk()
                   
            self.root.title("ERROR Form")
            self.root.minsize(100,100)
                  
            self.root.configure(background="#EA347C")
                              
            self.Label3=Label(self.root,text="INVALID EMAIL",bg="#EA347C",fg="#FFF")
            self.Label3.configure(font=("Garamond",15))
            self.Label3.pack(pady=(10,5))
                   
            self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#EA347C",width=5,height=1,command=lambda:self.register1())
            self.click2.configure(font=("Garamond",10,"bold"))
            self.click2.pack(pady=(5,5))
            self.root.mainloop()
                  



            
        self.root2.destroy()    

        self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' and password LIKE '{}'".format(email,password))
        self.a=self.mycursor.fetchall()
        self.b=self.a[0][0]

        
        self.mycursor.execute("INSERT INTO leader VALUES({},0)".format(self.b))
        self.conn.commit()
           
        self.root=Tk()                                 


          
        self.root.title("REGISTRATION")
        self.root.minsize(200,100)
        self.root.configure(background="#00a65a")



                  
        self.Label2=Label(self.root,text="Registered succesfully!!!!",bg="#00a65a",fg="#FFF")
        self.Label2.configure(font=("Garamond",20,"bold"))
        self.Label2.pack(pady=(10,5))

        self.click1=Button(self.root,text="OK",bg="#FFF",fg="#00a65a",width=5,height=1,command=lambda:self.destroy())
        self.click1.configure(font=("Garamond",10,"bold"))
        self.click1.pack(pady=(5,5))

        self.root.mainloop()


            
      #destroy  the GUI
    def destroy(self):
        self.root.destroy()


    def register1(self):
            #print("x")
            
        self.user_name.delete(first=0,last=100)
        self.user_email.delete(first=0,last=100)
        self.user_password.delete(first=0,last=100)
            
        self.root.destroy()




    def logined(self):
            
        email=self.user_email.get()
        password=self.user_password.get()
        self.email_save=email

        self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' and password LIKE '{}'".format(email,password))
  
        self.x=self.mycursor.fetchall()

        if(len(self.x)==0):
            
            self.root=Tk()

            self.root.title("ERROR Form")
            self.root.minsize(100,100)
                  #self.root.maxsize(600,600)
            self.root.configure(background="red")
                              
            self.Label3=Label(self.root,text="INVALID DATA",bg="red",fg="#FFF")
            self.Label3.configure(font=("Garamond",15))
            self.Label3.pack(pady=(10,5))
                   #print("x")
            self.click2=Button(self.root,text="RESET",bg="#FFF",fg="#FFFFFF",width=5,height=1,command=lambda:self.login2())
            self.click2.configure(font=("Garamond",20,"bold"))
            self.click2.pack(pady=(5,5))
            self.root.mainloop()

        self.root3.destroy()          

        self.root=Tk()                      

            
            #frame of GUI
        self.root.title("Login Form")
        self.root.minsize(200,100)
        self.root.configure(background="#00a65a")



                  
        self.Label2=Label(self.root,text="LOGIN Successfully!!!",bg="#00a65a",fg="#FFF")
        self.Label2.configure(font=("Garamond",20,"bold"))
        self.Label2.pack(pady=(10,5))

           
            
        self.Label2=Label(self.root,text="WELCOME",bg="#00a65a",fg="#FFF")
        self.Label2.configure(font=("Garamond",25))
        self.Label2.pack(pady=(10,5))
           
        y=self.x[0][1]

        self.Label2=Label(self.root,text=y,bg="#00a65a",fg="#FFF")
        self.Label2.configure(font=("Garamond",20,"bold"))
        self.Label2.pack(pady=(10,5))

        self.z=self.x[0][0]

        self.Label2=Label(self.root,text="Your ID NO.:",bg="#00a65a",fg="#FFF")
        self.Label2.configure(font=("Garamond",20,"bold"))
        self.Label2.pack(pady=(10,5))

            
        self.Label2=Label(self.root,text=self.z,bg="#00a65a",fg="#FFF")
        self.Label2.configure(font=("Garamond",20,"bold"))
        self.Label2.pack(pady=(10,5))


        self.click1=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.user())
        self.click1.configure(font=("Garamond",20,"bold"))
        self.click1.pack(pady=(5,5))



    def login2(self):
           
           
        self.user_email.delete(first=0,last=100)
        self.user_password.delete(first=0,last=100)
            
        self.root.destroy()



    def  user(self):
        self.destroy()



        self.root1=Tk()
        
        self.root1.title("PORTAL")

        self.root1.minsize(400,600)
        self.root1.maxsize(400,600)




        self.root1.configure(background="#FFFFFF")


        

        self.lable1=Label(self.root1,text="WELCOME TO BRAINGAME",bg="#FFFFFF",fg="#7D9F4C")
        self.lable1.configure(font=("Cooper black",20))
        self.lable1.pack(pady=(30,10))

        self.click=Button(self.root1,text="PLAY GAME",bg="#fff",fg="#992439",width=25,height=2,command=lambda:self.fetch())
        self.click.configure(font=("Constantia",10,"bold"))
        self.click.pack(pady=(10,20))

        self.click=Button(self.root1,text="VIEW LEADERBOARD",bg="#fff",fg="#992439",width=25,height=2,command=lambda:self.view())
        self.click.configure(font=("Constantia",10,"bold"))
        self.click.pack(pady=(10,20))


        self.click=Button(self.root1,text="EXIT",bg="#fff",fg="#992439",width=25,height=2,command=lambda:self.destroy1())
        self.click.configure(font=("Constantia",10,"bold"))
        self.click.pack(pady=(10,20))



        self.root.mainloop()


    def destroy1(self):
        self.root1.destroy()
        


    colours = ['Red','Blue','Green','Pink','Black', 
		'Yellow','Orange','White','Purple','Brown'] 
    score = 0

    timeleft = 30

    def startGame(self,event):
        if Color.timeleft == 30:
            self.countdown()
        self.nextColour()

    def nextColour(self):
        #Color.score
        #Color.timeleft

        if Color.timeleft>0:
            self.e.focus_set()
            if self.e.get().lower() == Color.colours[1].lower():
                Color.score += 1
            self.e.delete(first=0,last=100)
            random.shuffle(Color.colours)
            self.label.config(fg = str(Color.colours[1]), text = str(Color.colours[0]))
            self.scoreLabel.config(text = "Score: " + str(Color.score)) 


    def countdown(self):
        #Color.timeleft
        if Color.timeleft > 0:
            Color.timeleft -= 1
            self.timeLabel.config(text = "Time left: "+ str(Color.timeleft))
            self.timeLabel.after(1000, self.countdown) 

    def fetch(self):
        #self.mycursor.execute("""INSERT INTO leader VALUES({},0)""".format(self.z))
        
        self.root = Tk() 
        self.root.title("COLORGAME") 

        
        self.root.geometry("375x300") 

        
        self.instructions =Label(self.root, text = "Type in the colour"
                                                        "of the words, and not the word text!", 
                                                                                font = ('Helvetica', 12)) 
        self.instructions.pack() 

        # add a score label 
        self.scoreLabel = Label(self.root, text = "Press enter to start", 
                                                                                font = ('Helvetica', 12)) 
        self.scoreLabel.pack() 

        # add a time left label 
        self.timeLabel = Label(self.root, text = "Time left: " +
                                str(Color.timeleft), font = ('Helvetica', 12)) 
                                        
        self.timeLabel.pack() 

        # add a label for displaying the colours 
        self.label =Label(self.root, font = ('Helvetica', 60)) 
        self.label.pack() 

      
        #add entry box for typing in colours 
        self.e =Entry(self.root) 

       
        # run the game when the enter key is pressed 
        self.root.bind('<Return>', self.startGame) 
        self.e.pack() 

        # set focus on the entry box 
        self.e.focus_set()

        #self.root.destroy()

        self.Label3=Label(self.root,text="TYPE OK WHEN YOU ARE DONE",bg="red",fg="#FFF")
        self.Label3.configure(font=("Garamond",15))
        self.Label3.pack(pady=(10,5))
        

        self.click1=Button(self.root,text="OK",bg="#FFF",fg="#000",width=5,height=1,command=lambda:self.scores())
        self.click1.pack(pady=(5,5))

        # start the GUI 
        self.root.mainloop()


    def scores(self):
        #print(Color.score)
        new_score=Color.score
        print(Color.score)


        self.mycursor.execute("""UPDATE leader SET score={}
                                                            WHERE users_id={}
                                                                AND score<{}""".format(Color.score,self.z,Color.score))

        self.conn.commit()

        self.destroy()



    def view(self):
        self.destroy1()
        self.mycursor.execute("""SELECT name,score
                                                    FROM users
                                                    JOIN leader
                                                    ON leader.users_id=users.user_id
                                                    ORDER BY score DESC""")

        x=self.mycursor.fetchall()
        #print(self.x)

        temp=""
        for i in x:
            for j in i:
                j=str(j)
                temp=temp+j+"  "
            temp=temp+"\n"
            



        self.root=Tk()
        
        self.root.title("LEADER BOARD")

        self.root.minsize(400,600)
        self.root.maxsize(400,600)
        self.root.configure(background="#FFFFFF")
    

        self.lable1=Label(self.root,text="LAEDER BOARD",bg="#FFFFFF",fg="#C00A50")
        self.lable1.configure(font=("Garamond",20,"bold"))
        self.lable1.pack(pady=(30,10))

        self.lable1=Label(self.root,text="",bg="#FFFFFF",fg="#2A266B")
        self.lable1.configure(font=("Calibri",18))
        self.lable1.pack(pady=(30,10))
        self.lable1.configure(text=temp)

        self.click1=Button(self.root,text="OK",bg="#FFF",fg="#C00A50",width=5,height=1,command=lambda:self.destroy())
        self.click1.pack(pady=(5,5))



        self.root.mainloop()
            
     

obj=Color()



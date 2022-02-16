#import module 
from tkinter import * 
import tkinter.messagebox
import sqlite3
import qrcode 
from tkcalendar import Calendar
from datetime import datetime

import os 
import subprocess
import webbrowser 
# class for Front End UI( User interface)


class Bridge:
    def __init__(self,root):
        #create object referance instance of Database class as b
        b = Database()
        b.conn()

        self.root = root 
        self.root.title("UPV Calculation Software Version-1.0")
        #self.root.wm_state('zoomed')
        app_width =1366 
        app_height = 768

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)

        self.root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')    






        #self.root.geometry("1345x721")
        #self.root.maxsize(1345,721)
        self.root.config(bg="pink")
        '''Creating variables '''
        bId = StringVar()
        bName = StringVar()
        bDiscription=StringVar()
        bGlocation = StringVar()
        bLocations=StringVar()
        TLocations=StringVar()
        bTdate=StringVar()
        bsectionavg=StringVar()
        
        '''Result of calculations'''
        bResult = StringVar() 
        compressivestrength_fc= StringVar()   
        bReading = StringVar()
        bRpoint = StringVar()
        length = StringVar()
        caltime = StringVar()
        calculation = StringVar()

        def on_closing():
            print("Bridge : close method called")
            close = tkinter.messagebox.askyesno("UPV Calculation Software", "Really..... Do you want to close the system?")
            print(close)
            if close!=False:
                root.destroy()
                print("Bridge: Close method finished\n")
            else:
                root.lift()
            return 
            

        root.protocol("WM_DELETE_WINDOW", on_closing)

        ''' lets call the Database method to perform database operations'''
        def close():
            print("Bridge : close method called")
            close = tkinter.messagebox.askyesno("UPV Calculation Software", "Really..... Do you want to close the system?")
            print(close)
            if close!=False:
                root.destroy()
                print("Bridge: Close method finished\n")
            else:
                root.lift()
            return 








        def clear1():
            print("Bridge : clear reading  method called")
            #self.txtbId.delete(0,END)
            #self.txtbName.delete(0,END)
            #self.txtbdiscription.delete(0, END)
            #self.txtbGlocation.delete(0,END)
            #self.txtbLocations.delete(0,END)
            #self.txtbTdate.delete(0, END)
            #self.txtTLocations.delete(0,END)
            self.txtbReading.delete(0, END)
            
            #self.txtbResult.configure(state='normal')
            #self.txtbResult.delete(0, END)
            #self.txtbResult.configure(state='disabled')
            
            #self.txtbfc.configure(state='normal')
            #self.txtbfc.delete(0, END)
            #self.txtbfc.configure(state='disabled')

           # self.txtbResult.delete(0, END)
            self.txtbRpoint.delete(0, END)

            recordedBridgeList.delete(0, END)
            #recordedBridgeList1.delete(0, END)
            self.buttonSaveData.configure(state='normal')
            self.txtbId.focus()
            print("Bridge : clear  reading method finished")
            return






        def clear():
            print("Bridge : clear method called")
            self.txtbId.delete(0,END)
            self.txtbName.delete(0,END)
            self.txtbdiscription.delete(0, END)
            self.txtbGlocation.delete(0,END)
            self.txtbLocations.delete(0,END)
            self.txtbTdate.delete(0, END)
            self.txtTLocations.delete(0,END)
            self.txtbReading.delete(0, END)
            
            self.txtbResult.configure(state='normal')
            self.txtbResult.delete(0, END)
            self.txtbResult.configure(state='disabled')
            
            self.txtbfc.configure(state='normal')
            self.txtbfc.delete(0, END)
            self.txtbfc.configure(state='disabled')

            self.txtbResult.delete(0, END)
            self.txtbRpoint.delete(0, END)
            self.txtlength.delete(0,END)

            recordedBridgeList.delete(0, END)
            recordedBridgeList1.delete(0, END)
            self.buttoncalculateresult.configure(state='normal')
            self.buttonEditrecord.configure(state='normal')
            self.buttonSaverecord.configure(state='normal')
            self.buttonSaveData.configure(state='normal')
            self.txtbId.focus()
            print("Bridge : clear method finished")
            return
        #fuction to save the bridge details in database table 
        def getdate():
           from tkcalendar import Calendar
           from datetime import datetime
           top = Toplevel()
           top.title("Inserting date")
           top.iconbitmap("PPLICEO.ico")    
                       
           # Create Object
           
            
            # Set geometry
           top.geometry("400x400")
            
            # Add Calendar
           today = datetime.today()
           cal = Calendar(top, selectmode = 'day',
                        year = today.year, month = today.month,
                        day = today.day, date_pattern="dd/mm/yyyy")
            
           cal.pack(pady = 20)
            
           def grad_date():
                global txtdate
                date.config(text = "" + cal.get_date())
                txtdate=cal.get_date()
                demo=txtdate.split("/")
                
                
                new_txtdate = demo[0]+"/"+demo[1]+"/"+demo[2]
                #new format of date is (dd/mm/yyyy) test by printing it 
                print(new_txtdate)
                print(new_txtdate)
                self.txtbTdate.delete(0, END)
                self.txtbTdate.insert(END, new_txtdate)
                return cal.get_date()
            # Add Button and Label
           Button(top, text = "Get Date",
                command = grad_date).pack(pady = 20)
            
           date = Label(top, text = "")
           date.pack(pady = 20)
           bTdate = cal.get_date()
            #self.txtbTdate.insert(END, bTdate) 
            # Excecute Tkinter
           top.mainloop()    
           
           return  
        def insert():
            while True:
                try:
                    print("Bridge: insert method called")
                    
                    if (len(bId.get())!=0):
                        
                        b.insert(bId.get(), bName.get(), bDiscription.get(), bGlocation.get(), bLocations.get(),bTdate.get())
                        if (len(bResult.get())!=0):
                            b.insertresult(bId.get(), TLocations.get(), bsectionavg.get(), bResult.get(), compressivestrength_fc.get())
                        else:
                            tkinter.messagebox.askokcancel("UPV Calculation Software", "Looks like you did not calculate/insert the reading!")
                            
                        #recordedBridgeList.delete(0, END)
                        #recordedBridgeList.insert(END, bId.get(), bName.get(), bDiscription.get(), bGlocation.get(), bLocations.get(), TLocations.get(), bsectionavg.get(),bTdate.get(),bResult.get())
                        self.buttonSaveData.configure(state='disabled')
                        self.buttonResult.configure(bg='skyblue', fg='black')
                    else:
                        tkinter.messagebox.askyesno("UPV Calculation Software", "Please Enter Bridge ID..... Do you want to Enter it now?")
                        self.txtbId.focus()
                    print("Bridge: insert method Finished")
                    break
                except sqlite3.IntegrityError:
                    tkinter.messagebox.showerror("UPV Calculation Software!","Bridge Id should be Unique, Please check it again!")
                    break
        #fuction to save the bridge details in database table 
        def caltimef():
            global caltime1 
            a= float(length.get())
            b= float(bReading.get())
            
            caltime1 = a/b
            caltime1 = caltime1 * 1000000 
            self.buttonEditrecord.configure(state='normal')
            
             
        
        
        
        
        
        def insertreading():
           
            while True:
                try:
                    print("Bridge: insertreading method called")
                    print("caltime length", length)
                    print( "caltime reak", caltime)
                    #caltime = str(caltime1)                                
                    if (len(bId.get())!=0) and (len(TLocations.get())!=0):
                        b.insertreading(bId.get(),TLocations.get(),bRpoint.get(),bReading.get(),length.get(), caltime.get())
                        #recordedBridgeList.delete(0, END)
                        recordedBridgeList.pack_forget()
                        recordedBridgeList.insert(END, bId.get(),TLocations.get(),bRpoint.get(),bReading.get(),length.get())
                        recordedBridgeList.insert(END, "________________________________________\n")
                        self.buttoncalculateresult.configure(bg='skyblue', fg='black')
                    else:
                        tkinter.messagebox.askyesno("UPV Calculation Software", "Please Enter (Bridge ID..and Test Location)... Do you want to Enter it now?")
                        self.txtbId.focus()
                    self.txtbRpoint.delete(0, END)
                    self.txtbReading.delete(0,END)
                    self.txtlength.delete(0,END)
                    self.txtbRpoint.focus()
                    print("Bridge: insert method Finished")
                    break
                except sqlite3.IntegrityError:
                    tkinter.messagebox.showerror("UPV Calculation Software!","Please check your inserted data!")
                    break
        def calculate():
            print("Bridge : Calculate method called ")
            print("Database : connection method called\n")
            con = sqlite3.connect("bridgeval.db")
            cur = con.cursor()
            query2="SELECT * FROM readingdata WHERE (bid=? AND tlocation=?)"
            global ravg
            
            print(TLocations)
            print(bId)
            cur.execute(query2, (str(bId.get()),str(TLocations.get()),))
            items = cur.fetchall()
            i=0
            total = 0         
            print(items)
            for item in items:
                total= total + int(item[3])
                print(item)
                print(i)
                print(item[3])
                print(total)
                i= i+1
            #ravg=int(total/i)
            import math 
           
            ravg=total/i
            def round_half_up(n, decimals=0):
                multiplier = 10 ** decimals
                return math.floor(n*multiplier + 0.5) / multiplier

            rndravg=round_half_up(ravg,0)
            print("rndravg",rndravg)
            ravg=int(rndravg)
            ravg_km=ravg/1000
            sqravg_km= ravg_km ** 1.833 
            _sqravg_km= sqravg_km * 4.0284
            compressivestrength_fc_rnd= round_half_up(_sqravg_km,0)
            print("compressivestrength_fc_rnd:", compressivestrength_fc_rnd)
            compressivestrength_fc=int(compressivestrength_fc_rnd)

            if ((ravg >4500) and (ravg<=10000)):
                bResult="Excellent" 
                self.buttoncalculateresult.configure(bg='lightgray', fg='black')
            elif((ravg >=3501) and (ravg<=4500)):
                bResult="Good"
                self.buttoncalculateresult.configure(bg='lightgray', fg='black')

            elif((ravg >=3001) and (ravg<=3500)):
                bResult="Medium"
                self.buttoncalculateresult.configure(bg='lightgray', fg='black')

            elif((ravg >=2000) and (ravg<=3000)):
                bResult="Doubtful"
                self.buttoncalculateresult.configure(bg='lightgray', fg='black')
            elif((ravg >=0) and (ravg<=2000)):
                bResult="Poor"
                self.buttoncalculateresult.configure(bg='lightgray', fg='black')

            else:
                tkinter.messagebox.showerror("UPV Calculation Software!","Please check your inserted data or retake field record!")
                self.buttoncalculateresult.configure(bg='lightgray', fg='black')

            self.txtbResult.configure(state='normal')
            self.txtbResult.delete(0, END)
            self.txtbResult.insert(END, bResult)
            self.txtbResult.configure(state='disabled')


            self.txtbfc.configure(state='normal')
            self.txtbfc.delete(0, END)
            self.txtbfc.insert(END, compressivestrength_fc)
            self.txtbfc.configure(state='disabled')

            con.commit()
            con.close()
            showInBridgeList() # call Show reading list 
            self.buttonUpdate.configure(bg='skyblue', fg='black')
            print("Database : Calculate method finised ")

        # Fuction responsible to show Bridge reading information to the scrollbar
        def showInBridgeList():
            print("Bridge : showInBridgeList method called ") 
            #recordedBridgeList1.delete(0,END)
            #recordedBridgeList1.configure(state='disabled')
            recordedBridgeList.cofigure(state='normal')
            recordedBridgeList.delete(0,END)
            #recordedBridgeList1.pack_forget()
            
            for row in b.show(bId.get(),TLocations.get()):
                print(row)
                recordedBridgeList.insert(END, row, str(""))
            print("Bridge : showInBridgeList method finished\n")
        
        # Fuction responsible to show all  Bridge reading information to the scrollbar
        def showallInBridgeList():
            #global click 
            print("Bridge : showallInBridgeList method called ") 
            click=1 
            
            #recordedBridgeList.configure(state='disabled')
            #recordedBridgeList1.cofigure(state='normal')
            #recordedBridgeList1.delete(0,END)
            for row in b.showall():
                
                recordedBridgeList1.insert(END, row, str(""))
                
            print("Bridge : showallInBridgeList method finished\n")


        
        def bridgereadingRec(event): # This fuction to be called from scrollbar readingdata
            print("Bridge : bridgereadingRec method called ") 
            
            global bd 
            
            searchBd = recordedBridgeList.curselection()[0] 
            bd = recordedBridgeList.get(searchBd)
            print("bd ",bd)
            self.txtbId.delete(0,END)
            self.txtbId.insert(END, bd[0])

            self.txtTLocations.delete(0,END)
            self.txtTLocations.insert(END, bd[1])

            self.txtbRpoint.delete(0,END)
            self.txtbRpoint.insert(END, bd[2])

            self.txtbReading.delete(0, END)
            self.txtbReading.insert(END, bd[3])

            self.txtlength.delete(0,END)
            self.txtlength.insert(END, bd[4])
            self.buttoncalculateresult.configure(state='disabled')
            self.buttonEditrecord.configure(state='disabled')
            self.buttonSaverecord.configure(state='disabled')
           
            print("Bridge : bridgereadingRec method finished\n")

        
         # Fuction responsible to show Bridge reading information to the scrollbar
        def showInBridgeList():
            print("Bridge : showInBridgeList method called ") 
            #recordedBridgeList1.delete(0,END)
            #recordedBridgeList1.configure(state='disabled')
            recordedBridgeList.configure(state='normal')
            recordedBridgeList.delete(0,END)
                       
            for row in b.show(bId.get(),TLocations.get()):
                recordedBridgeList.insert(END, row, str(""))
            print("Bridge : showInBridgeList method finished\n")
        
        # Fuction responsible to show all  Bridge reading information to the scrollbar
        def showallInBridgeList():
            print("Bridge : showallInBridgeList method called ") 
            recordedBridgeList1.delete(0,END)
            for row in b.showall():
                recordedBridgeList1.insert(END, row, str(""))
            print("Bridge : showallInBridgeList method finished\n")


        
        def bridgeinfoshow(event): # This fuction to be called from scrollbar bridge data
            global binfo
            print("Bridge : bridgeinfoshow method called ") 
            #recordedBridgeList.configure(state='disabled')
            #recordedBridgeList1.cofigure(state='normal')
            searchBd1 = recordedBridgeList1.curselection()[0] 
            binfo = recordedBridgeList1.get(searchBd1)

            

            print("binfo ",binfo)
            self.txtbId.delete(0,END)
            self.txtbId.insert(END, binfo[0])

            self.txtbName.delete(0,END)
            self.txtbName.insert(END, binfo[1])

            self.txtbdiscription.delete(0,END)
            self.txtbdiscription.insert(END, binfo[2])

            self.txtbGlocation.delete(0, END)
            self.txtbGlocation.insert(END, binfo[3])

            self.txtbLocations.delete(0,END)
            self.txtbLocations.insert(END, binfo[4])

            self.txtbTdate.delete(0,END)
            self.txtbTdate.insert(END, binfo[5])

           
            
            self.txtbRpoint.delete(0, END)
            self.txtTLocations.delete(0,END)
            self.txtbReading.delete(0,END)
            self.txtlength.delete(0,END)

                       
            print("Bridge : bridginfoeshow all  method finished\n")
        
        # fuction to delete the data record from database table 
        def delete():
            print("Bridge : delete method called")
            dell = tkinter.messagebox.askyesno("UPV Calculation Software", "Really..... Do you want to delte the data?")
            if dell>0 :
                if (len(bId.get())!=0):
                    b.delete(binfo[0])
                    clear()
                    showallInBridgeList()
            print("Bridge : delete method finished\n")
        
        def deleterec():
            print("Bridge : delete method called")
            dell1 = tkinter.messagebox.askyesno("UPV Calculation Software", "Really..... Do you want to delte the reading?")
            if dell1>0 :
                if (len(bId.get())!=0 and len(TLocations.get())!=0 and len(bRpoint.get())!=0):
                    b.deletereading(bd[0], bd[1], bd[2])
                    clear1()
                    calculate()
                    showInBridgeList()
            print("Bridge : delete method finished\n")
        
        def updaterec():
            print("Bridge : update reading method called\n")
            dell2 = tkinter.messagebox.askyesno("UPV Calculation Software", "Really..... Do you want update the reading data?")
            if dell2>0 :
                if (len(bId.get())!=0 and len(TLocations.get())!=0 and len(bRpoint.get())!=0):
                    print("bd[0]", bd[0])
                    b.deletereading(bd[0],bd[1],bd[2])
                if (len(bId.get())!=0) and (len(TLocations.get())!=0):
                        b.insertreading(bId.get(),TLocations.get(),bRpoint.get(),bReading.get(),length.get(), caltime.get())   
                        recordedBridgeList.delete(0, END)
                recordedBridgeList.insert(END, (bId.get(),TLocations.get(),bRpoint.get(),bReading.get(),length.get()))
                recordedBridgeList.insert(END, "________________________________________\n")
                self.buttoncalculateresult.configure(state='normal')
                self.buttoncalculateresult.configure(bg='skyblue', fg='black')

            print("Bridge : update reading method finished\n")    
        def updatebinfo():
            print("Bridge : update bridge info method called\n")
            self.txtbResult.configure(state='normal')
            #self.txtbResult.delete(0, END)
            #self.txtbResult.configure(state='disabled')
            
            self.txtbfc.configure(state='normal')
            #self.txtbfc.delete(0, END)
            #self.txtbfc.configure(state='disabled')
            dell3 = tkinter.messagebox.askyesno("UPV Calculation Software", "Really..... Do you want update the bridge info data?")
            if dell3>0 :
                if (len(bId.get())!=0 and len(TLocations.get())!=0):
                    print("binfo[0], bd[0]", binfo[0],bd[1])
                    b.delete(binfo[0])
                    b.deleteres(binfo[0],bd[1])
                    b.insert(bId.get(), bName.get(), bDiscription.get(), bGlocation.get(), bLocations.get(),bTdate.get())
                    if (len(bResult.get())!=0):
                        b.insertresult(bId.get(), TLocations.get(), bsectionavg.get(), bResult.get(), compressivestrength_fc.get())
                    else:
                        tkinter.messagebox.askokcancel("UPV Calculation Software", "Looks like you did not calculate/insert the reading!")
                           
                recordedBridgeList.delete(0, END)
                recordedBridgeList.insert(END, (bId.get(),TLocations.get(),bRpoint.get(),bReading.get(),length.get()))
                recordedBridgeList.insert(END, "________________________________________\n")
                #self.buttoncalculateresult.configure(bg='skyblue', fg='black')
            self.buttonResult.configure(bg='skyblue', fg='black')    
            print("Bridge : update bridge information method finished\n")

        def search():
            print("Bridge : Search method finished\n")
            recordedBridgeList1.delete(0, END)
            for row in b.search(bId.get(),bName.get(),bDiscription.get(),bGlocation.get(),bLocations.get(),bTdate.get()):
                recordedBridgeList1.insert(END, row, str(""))
            print("Product : Search method finished\n")

        def result():
            #from create_table_fpdf2 import PDF
            '''

            data = [
                ["First name", "Last name", "Age", "City",], # 'testing','size'],
                ["Jules", "Smith", "34", "San Juan",], # 'testing','size'],
                ["Mary", "Ramos", "45", "Orlando",], # 'testing','size'],
                ["Carlson", "Banks", "19", "Los Angeles",], # 'testing','size'],
                ["Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire",], # 'testing','size'],
            ]

            data_as_dict = {"First name": ["Jules","Mary","Carlson","Lucas"],
                            "Last name": ["Smith","Ramos","Banks","Cimon"],
                            "Age": [34,'45','19','31']
                        }

            '''

           
            
            #pdf = PDF()
            #pdf.add_page()
            #pdf.set_font("Arial", size=12)
            from fpdf import FPDF
            
            con = sqlite3.connect("bridgeval.db")
            cur = con.cursor()
            #query1="SELECT * FROM readingdata WHERE (bid=? AND tlocation=?)"
            #cur.execute(query1, (str(bId.get()),str(TLocations.get()),))
            #data1 = cur.fetchall()
            #print(data1)
            #print(type(data1))
            #data=[]
            #for d in data1:
                #data.append(str(d))
              
            #pdf.create_table(table_data = data,title='I\'m the first title', cell_width='even')
            #pdf.ln()
            class PDF(FPDF):
                def footer(self):
                   # Position at 1.5 cm from bottom
                    self.set_y(-15)
                     # helvetica italic 8
                    self.set_font('helvetica', 'I', 8)
                    # Page number
                    #self.cell(0, 10, 'Signed by     Planplus Engineer       LGED             Third party')

                    self.cell(0, 10, 'This is a Auto generated report by Planplus Limited UPV software, Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
                    #def header(self):
                    # Logo
                    #self.image('logo_pb.png', 10, 8, 33)
                    # helvetica bold 15
                    #self.set_font('helvetica', 'B', 25)
                    # Move to the right
                    #self.cell(80)
                    # Title
                    #self.cell(30, 10, 'UPV SOFTWARE', 0, 0, 'C')
                    #self.set_font('helvetica', 'B', 15)
                    #import unicodedata
                    #txt= "μs"
                   # pdf.write(8,txt ) # where name is José

                    #self.cell(1, 25, 'A software product of Planplus Limited Bangladesh Time(μs)', 0, 0, 'C')
                    #self.cell(10, 25, txt="Hellow word", border=0, ln=0, align="", fill=False, link="", center=False, markdown=False
                    # Line break
                    
                    #self.cell(20,45, "Hellow word", 0, 0, "L")     
                    #self.ln(20)

                # Page footer
              

            TABLE_COL_NAMES_bridge0 = ("Measurement of UPV in accordance with ASTM C597")
            TABLE_DATA_bridge0=(" ")
            
            query1="SELECT bname FROM bridge WHERE (bid=?)"
            cur.execute(query1, (str(bId.get()),))
            data1 = cur.fetchall()
            TABLE_COL_NAMES_bridge1 = ("Name of the Project")
            TABLE_DATA_bridge1=(data1)
           
            query1="SELECT bid FROM bridge WHERE (bid=?)"
            cur.execute(query1, (str(bId.get()),))
            data1 = cur.fetchall()
            TABLE_COL_NAMES_bridge2 = ("Bridge ID")
            TABLE_DATA_bridge2=(data1)

            query1="SELECT bDiscription FROM bridge WHERE (bid=?)"
            cur.execute(query1, (str(bId.get()),))
            data1 = cur.fetchall()
            TABLE_COL_NAMES_bridge3 = ("Bridge Description")
            TABLE_DATA_bridge3=(data1)

            query1="SELECT bGlocation FROM bridge WHERE (bid=?)"
            cur.execute(query1, (str(bId.get()),))
            data1 = cur.fetchall()
            TABLE_COL_NAMES_bridge4 = ("Geo-Location")
            TABLE_DATA_bridge4=(data1)

            query1="SELECT blocations FROM bridge WHERE (bid=?)"
            cur.execute(query1, (str(bId.get()),))
            data1 = cur.fetchall()
            TABLE_COL_NAMES_bridge5 = ("Location")
            TABLE_DATA_bridge5=(data1)

            query1="SELECT tdate FROM bridge WHERE (bid=?)"
            cur.execute(query1, (str(bId.get()),))
            data1 = cur.fetchall()
            TABLE_COL_NAMES_bridge6 = ("Test Date")
            TABLE_DATA_bridge6=(data1)

            
            '''
            TABLE_COL_NAMES_bridge1 = ("Name of the project:", "Bridge ID:", "Bridge Description:","Bridge Geo-Location:", "Locations:", "Test Date")
            TABLE_DATA_bridge1=(data1)    
            '''
            
           

            query2="SELECT btlocation FROM calresult WHERE (bid=? AND btlocation=?)"
            cur.execute(query2, (str(bId.get()),str(TLocations.get()),))
            data = cur.fetchall()
            TABLE_COL_NAMES_tlocation = ("Test Point Location")
            TABLE_DATA_tlocaton = (data)

            query2="SELECT bsectionavg FROM calresult WHERE (bid=? AND btlocation=?)"
            cur.execute(query2, (str(bId.get()),str(TLocations.get()),))
            data = cur.fetchall()
            TABLE_COL_NAMES_resultavg = ("Average Velocity (m/s)")
            TABLE_DATA_resultavg = (data)

            query2="SELECT compressive_strength_fc FROM calresult WHERE (bid=? AND btlocation=?)"
            cur.execute(query2, (str(bId.get()),str(TLocations.get()),))
            datafc = cur.fetchall()
            TABLE_COL_NAMES_fc = ("Compressive Strength (MPa)")
            TABLE_DATAfc = (datafc)

            query2="SELECT btresult FROM calresult WHERE (bid=? AND btlocation=?)"
            cur.execute(query2, (str(bId.get()),str(TLocations.get()),))
            data = cur.fetchall()
            TABLE_COL_NAMES_result = ("Result")
            TABLE_DATA = (data)




            pdf = FPDF()
            #pdf.l_margin(2)
            #pdf.r_margin(2)
            pdf.add_page()
            pdf.set_font("Times", size=11)
            pdf.set_right_margin(22)
            pdf.set_left_margin(26)
            pdf.set_auto_page_break(22)
            line_height = pdf.font_size * 2
            col_width = pdf.epw / 1  # distribute content evenly
            

            def render_table_header(TABLE_COL_NAMES):
                pdf.set_font(style="B")  # enabling bold text
                pdf.cell(180, 4, TABLE_COL_NAMES, border=0)
                #pdf.ln(line_height)
                pdf.set_font(style="")  # disabling bold text

            def draw_table(TABLE_DATA):    
            #for _ in range(10):  # repeat data rows
                for row in TABLE_DATA:
                    if pdf.will_page_break(line_height):
                        render_table_header()
                    for datum in row:
                        if len(datum)>78:
                             pdf.multi_cell(0, 4, str(datum), border=0)
                        else:
                            pdf.cell(0, 4, str(datum), border=0)
                    #pdf.ln(line_height)
                    break
                pdf.ln(line_height)
                
            
            
            
            text =""
            pdf.cell(12, 12, text)
            pdf.ln(16)
            
            pdf.set_font("Times", size=16)
            line_height = pdf.font_size * 2.5
            col_width = pdf.epw / 1  # distribute content evenly


            pdf.set_font("Times",'B', size=16)
            line_height = pdf.font_size * 2.5
            text ="Measurement of UPV in accordance with ASTM C597"
            pdf.cell(12, 12, text)
            pdf.ln(6)

            #render_table_header(TABLE_COL_NAMES_bridge0)
            #draw_table(TABLE_DATA_bridge0)
            pdf.set_font("Times", size=9)
            line_height = pdf.font_size * 2
            text ="This report has been generated by automated software, developed by Plan Plus Limited, Bangladesh for"
            pdf.cell(12, 12, text)
            pdf.ln(4)
            text ="Ultrasonic  Pulse  Velocity (UPV) Test"
            pdf.cell(12, 12, text)
            pdf.ln(4)
            text ="Software version 1.0"
            pdf.cell(12, 12, text)
            pdf.ln(4)
            text = "©Copyright 2021. All Rights Reserved @Plan Plus Limited, Bangladesh"
            pdf.cell(12, 12, text)
            pdf.ln(7)
            text ="-------------------------------------------------------------------------------------------------------------------------"
            pdf.cell(12, 12, text)
            pdf.ln(12)
            #pdf.set_font("Times", size=10)
            #line_height = pdf.font_size * 2
            #render_table_header(TABLE_COL_NAMES_bridge_header1)
            
            pdf.set_font("Times", size=12)
            line_height = pdf.font_size * 2
            col_width = pdf.epw / 1 
            render_table_header(TABLE_COL_NAMES_bridge1)
            pdf.ln(4)
            draw_table(TABLE_DATA_bridge1)

            render_table_header(TABLE_COL_NAMES_bridge2)
            pdf.ln(4)
            draw_table(TABLE_DATA_bridge2)

            render_table_header(TABLE_COL_NAMES_bridge3)
            pdf.ln(4)
            draw_table(TABLE_DATA_bridge3)

            render_table_header(TABLE_COL_NAMES_bridge4)
            pdf.ln(4)
            draw_table(TABLE_DATA_bridge4)

            render_table_header(TABLE_COL_NAMES_bridge5)
            pdf.ln(4)
            draw_table(TABLE_DATA_bridge5)

            render_table_header(TABLE_COL_NAMES_bridge6)
            pdf.ln(4)
            draw_table(TABLE_DATA_bridge6)

            render_table_header(TABLE_COL_NAMES_tlocation)
            pdf.ln(4)
            draw_table(TABLE_DATA_tlocaton)
           
            #render_table_header(TABLE_COL_NAMES_result1)
            #draw_table(TABLE_DATA1)  
            '''
            pdf.set_font("Times", size=11)
               
            text ="       SL.                          Point                        Reading(m/s)              Distance B.T.(m)           Time(μs)"
            pdf.cell(12, 12, text)
            pdf.ln(10)
            '''
                        
            TABLE_COL_NAMES_reading = ("SL", "Point", "Reading (m/s)", "Distance (m)", "Time (micro.sec)" )
            query6="SELECT oid,point,reading,length, caltime FROM readingdata WHERE (bid=? AND tlocation=?)"
            cur.execute(query6, (str(bId.get()),str(TLocations.get()),))
            data6 = cur.fetchall()
            TABLE_DATA6 = (data6)

            
            pdf.set_font("Times", size=11)
            pdf.set_left_margin(28)
            line_height = pdf.font_size * 2
            col_width = pdf.epw / 5  # distribute content evenly
            
            def render_table_header1():
                pdf.set_font(style="B")  # enabling bold text
                for col_name in TABLE_COL_NAMES_reading:
                    pdf.cell(col_width, line_height, col_name, border=1, align = 'C')
                pdf.ln(line_height)
                pdf.set_font(style="")  # disabling bold text
            
            render_table_header1()
            
            #for _ in range(10):  # repeat data rows
            sl=1
            for row in TABLE_DATA6:
                if pdf.will_page_break(line_height):
                    render_table_header1()
               
                #for datum in row:
                    #pdf.cell(col_width, line_height, str(datum), border=1, align = 'C')
                pdf.cell(col_width, line_height, str(sl), border=1, align = 'C')
                pdf.cell(col_width, line_height, str(row[1]), border=1, align = 'C')
                pdf.cell(col_width, line_height, str(row[2]), border=1, align = 'C')
                pdf.cell(col_width, line_height, str(row[3]), border=1, align = 'C')
                pdf.cell(col_width, line_height, str(row[4]), border=1, align = 'C')
                sl=sl+1
                pdf.ln(line_height)



            
            pdf.ln(5)
            pdf.set_font("Times", size=12)
            pdf.set_left_margin(26)
            line_height = pdf.font_size * 2
            col_width = pdf.epw / 1
            
            
            render_table_header(TABLE_COL_NAMES_resultavg)
            pdf.ln(4)
            draw_table(TABLE_DATA_resultavg) 
            
            render_table_header(TABLE_COL_NAMES_fc)
            pdf.ln(4)
            draw_table(TABLE_DATAfc) 
            
            render_table_header(TABLE_COL_NAMES_result)
            pdf.ln(4)
            draw_table(TABLE_DATA)  

            #img = qrcode.make("UPV Calculation Software!This is a Software Product of Plan Plus Limited,Bangladesh. For more information please visit www.planpluslimited.com")
            
           
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=2,
                border=1,
            )
            qr.add_data('UPV Calculation Software. ©PlanPlus Limited, Bangladesh 2021. All right reserved.http://planpluslimited.com/')
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            
            pdf.image(img.get_image(), x=160, y=28)
            pdf.set_font("Times", size=11)
            pdf.ln(20)
            
            #text ="                                     PPL Representative                          LGED Representative "
            text =" "
            pdf.alias_nb_pages()
            pdf.cell(0, 5, text)
            pdf.ln(22)
                              
            string_in_string = "Upvcal_for_bridge_ID_{}Location_{}.pdf".format(TABLE_DATA_bridge2,TABLE_DATA_tlocaton)         
            pdf.output(string_in_string)
            self.buttonResult.configure(bg='lightgray', fg='black')
            tkinter.messagebox.showinfo("UPV Calculation Software!", "Your Report has been generated. Please check it in current directory!")          
            path = ('{}'.format(string_in_string))
            print(string_in_string)
            webbrowser.open_new(path)
            #subprocess.Popen([path], shell=True)
        '''Create the frame '''
        MainFrame=Frame(self.root,padx=20,bg ="pink")
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd=2, padx=60, pady=10,bg='white', relief=RIDGE)
        HeadFrame.pack(side=TOP)
     
        self.ITitle = Label(HeadFrame, font=('arial',30,'bold'), fg='black',
                    text='（UVP）橋梁用計算ソフト', bg='white')
        self.ITitle.grid()
        self.ITitle = Label(HeadFrame, font=('arial',18,'bold'), fg='gray',
                    text='A Software Product of Plan Plus Limited, Bangladesh', bg='white')
        self.ITitle.grid()
        self.ITitle = Label(HeadFrame, font=('arial',16,'bold'), fg='gray',
                    text='ISO 9001:2015 Certified Consulting Firm', bg='white')
        self.ITitle.grid()
        self.ITitle = Label(HeadFrame, font=('arial',14,'bold'), fg='gray',
                    text='www.planpluslimited.com', bg='white')
        self.ITitle.grid()
        self.ITitle = Label(HeadFrame, font=('arial',12,'bold'), fg='gray',
                    text='アジズ エムディ シャミム によって開発されました ', bg='white')
        self.ITitle.grid()

        OperationFrame = Frame(MainFrame, bd=2, width=1200, height=70, padx=40, pady=20,bg='white', relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)
        
                
        BodyFrame = Frame(MainFrame, bd=2, width=1200, height=768, padx=60, pady=20,bg='white', relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

      
        LeftbodyFrame = LabelFrame(BodyFrame, bd=2, width=280, height=380, padx=20, pady=10,bg='white', relief=RIDGE, font=('arial', 15, 'bold'),
                                                                                            fg='gray',text='Bridge information details')
        LeftbodyFrame.pack(side=LEFT)

        BottombodyFrame = LabelFrame(BodyFrame, bd=2, width=280, height=380, padx=20, pady=10,bg='white', relief=RIDGE, font=('arial', 15, 'bold'),
                                                                                            fg='gray',text='Enter reading data')
        BottombodyFrame.pack(side=LEFT)

        RightbodyFrame = LabelFrame(BodyFrame, bd=2, width=280, height=190, padx=20, pady=10,bg='white', relief=RIDGE, font=('arial', 15, 'bold'),
                                                                                            fg='gray',text='Reading List View')
        RightbodyFrame.pack()

        RightbodyFrame1 = LabelFrame(BodyFrame, bd=2, width=280, height=190, padx=20, pady=10,bg='white', relief=RIDGE, font=('arial', 15, 'bold'),
                                                                                            fg='gray',text='All Bridge info List ')
        RightbodyFrame1.pack()

        

        '''  Add the Widgets to LeftBodyFrame/ Bridge information details     '''
        self.labelbId = Label(LeftbodyFrame, font=('arial', 12, 'bold'), text="Bridge ID:", padx=2,bg='white')
        self.labelbId.grid(row=0, column=0,sticky=W)
        self.txtbId = Entry(LeftbodyFrame,font=('arial', 20, 'bold'),bd=3,bg='pink',textvariable=bId, width=20)
        self.txtbId.grid(row=0, column=1, sticky=W)

        self.labelbName = Label(LeftbodyFrame, font=('arial', 12, 'bold'), text="Name of the Project:", padx=2, bg='white')
        self.labelbName.grid(row=1, column=0, sticky=W)
        self.txtbName = Entry(LeftbodyFrame,font=('arial', 20, 'bold'),bd=3,bg='pink',textvariable=bName, width=20)
        self.txtbName.grid(row=1, column=1, sticky=W)

        self.labelbdiscription = Label(LeftbodyFrame, font=('arial', 12, 'bold'), text="Bridge Description:", padx=2, bg='white')
        self.labelbdiscription.grid(row=2, column=0, sticky=W)
        self.txtbdiscription = Entry(LeftbodyFrame,font=('arial', 20, 'bold'),bd=3,bg='pink',textvariable=bDiscription, width=20)
        self.txtbdiscription.grid(row=2, column=1, sticky=W)

        self.labelbGlocation = Label(LeftbodyFrame, font=('arial', 12, 'bold'), text="Geographic Location:", padx=2, bg='white')
        self.labelbGlocation.grid(row=3, column=0, sticky=W)
        self.txtbGlocation = Entry(LeftbodyFrame,font=('arial', 20, 'bold'),bd=3,bg='pink',textvariable=bGlocation, width=20)
        self.txtbGlocation.grid(row=3, column=1, sticky=W)
        
        self.labelbLocations = Label(LeftbodyFrame, font=('arial', 12, 'bold'), text="Local Location:", padx=2, bg='white')
        self.labelbLocations.grid(row=4, column=0, sticky=W)
        self.txtbLocations = Entry(LeftbodyFrame,font=('arial', 20, 'bold'),bd=3,bg='pink',textvariable=bLocations, width=20)
        self.txtbLocations.grid(row=4, column=1, sticky=W)

        

        self.labelbTdate = Label(LeftbodyFrame, font=('arial', 12, 'bold'), text="Test Date:", padx=2, bg='white')
        self.labelbTdate.grid(row=5, column=0, sticky=W)
        self.txtbTdate = Entry(LeftbodyFrame,font=('arial', 20, 'bold'),bd=3,bg='pink',textvariable=bTdate, width=12)
        self.txtbTdate.grid(row=5, column=1, sticky=W)

        self.buttongetdate = Button(LeftbodyFrame, text='Get date', font=('arial', 11, 'bold'), height='1', width='12',bd=4, command=getdate)
        self.buttongetdate.grid(row=5, column=1, sticky=E)



        self.labelbResult = Label(LeftbodyFrame, font=('arial', 12, 'bold'), text="Velocity Cal. Result:", padx=2, bg='white')
        self.labelbResult.grid(row=6, column=0, sticky=W)
        self.txtbResult = Entry(LeftbodyFrame,font=('arial', 20, 'bold'),bd=3,bg='pink',textvariable=bResult, width=20,  state=DISABLED)
        self.txtbResult.grid(row=6, column=1, sticky=W)

        self.labelbfc = Label(LeftbodyFrame, font=('arial', 12, 'bold'), text="Compressive strength", padx=2, bg='white')
        self.labelbfc.grid(row=7, column=0, sticky=W)
        self.txtbfc = Entry(LeftbodyFrame,font=('arial', 20, 'bold'),bd=3,bg='pink',textvariable=compressivestrength_fc, width=20,  state=DISABLED)
        self.txtbfc.grid(row=7, column=1, sticky=W)

        '''
        Add rocord for every reading         
        '''
        self.labelTLocations = Label(BottombodyFrame, font=('arial', 12, 'bold'), text="Test Location:", padx=2, bg='white')
        self.labelTLocations.grid(row=0, column=0, sticky=W)
        self.txtTLocations = Entry(BottombodyFrame,font=('arial', 20, 'bold'),bd=3,bg='pink',textvariable=TLocations, width=8)
        self.txtTLocations.grid(row=0, column=1, sticky=W)

        
        self.labelbRpoint = Label(BottombodyFrame, font=('arial', 12, 'bold'), text="Point", padx=2, bg='white')
        self.labelbRpoint.grid(row=1, column=0, sticky=W)
        self.txtbRpoint = Entry(BottombodyFrame,font=('arial', 20, 'bold'),bd=3,bg='skyblue',textvariable=bRpoint, width=8)
        self.txtbRpoint.grid(row=1, column=1, sticky=W)
        
        
        
        self.labelbReading = Label(BottombodyFrame, font=('arial', 12, 'bold'), text="Enter reading", padx=2, bg='white')
        self.labelbReading.grid(row=2, column=0, sticky=W)
        self.txtbReading = Entry(BottombodyFrame,font=('arial', 20, 'bold'),bd=3,bg='skyblue',textvariable=bReading, width=8)
        self.txtbReading.grid(row=2, column=1, sticky=W)

        self.labellength = Label(BottombodyFrame, font=('arial', 12, 'bold'), text="Length", padx=2, bg='white')
        self.labellength.grid(row=3, column=0, sticky=W)
        self.txtlength = Entry(BottombodyFrame,font=('arial', 20, 'bold'),bd=3,bg='skyblue',textvariable=length, width=8)
        self.txtlength.grid(row=3, column=1, sticky=W)
        
        self.labelbreding_more = Label(BottombodyFrame, font=('arial', 12, 'bold italic'), text="Select an operation", padx=2, bg='white')
        self.labelbreding_more.grid(row=4, column=0, sticky=W)
        

        '''Add Scroll bar '''
        scroll = Scrollbar(RightbodyFrame)
        scroll.grid(row=0, column=1, sticky='ns') 
        hbar = Scrollbar(RightbodyFrame1, orient=HORIZONTAL, name='hbar')
        hbar.grid(row=1, column=0, sticky='ew')
        vbar = Scrollbar(RightbodyFrame1, orient=VERTICAL, name='vbar')
        vbar.grid(row=0, column=1, sticky='ns')

        recordedBridgeList=Listbox(RightbodyFrame, width=30, height=6, font=('arial', 12,'bold'),
                            yscrollcommand = scroll.set)
                            
        recordedBridgeList1=Listbox(RightbodyFrame1, width=30, height=6, font=('arial', 12,'bold'),
                            yscrollcommand = vbar.set,xscrollcommand = hbar.set)
        
        #Called above created recordedBridgeList function from of init 
                    
        recordedBridgeList1.bind('<<ListboxSelect>>',bridgeinfoshow)
        recordedBridgeList1.grid(row=0, column=0, padx=8)
        scroll.config(command=recordedBridgeList1.yview)

        recordedBridgeList.bind('<<ListboxSelect>>', bridgereadingRec)
        recordedBridgeList.grid(row=0, column=0, padx=8)
        scroll.config(command=recordedBridgeList.yview)
        

        ''' Add the button to operation Frame '''
        self.buttonSaveData = Button(OperationFrame, text='Save', font=('arial', 14, 'bold'), height='1', width='8',bd=3, command=insert)
        self.buttonSaveData.grid(row=0, column=0)

        self.buttonResult = Button(OperationFrame, text='Report', font=('arial', 14, 'bold'), height='1', width='8',bd=3, command=result)
        self.buttonResult.grid(row=0, column=1)

        self.buttonClear = Button(OperationFrame, text='Reset', font=('arial', 14, 'bold'), height='1', width='8',bd=3, command=clear)
        self.buttonClear.grid(row=0, column=2)

        self.buttonShowall = Button(OperationFrame, text='Show All', font=('arial', 14, 'bold'), height='1', width='8',bd=3, command=showallInBridgeList)
        self.buttonShowall.grid(row=0, column=3)

        
        self.buttonSearch = Button(OperationFrame, text='Search', font=('arial', 14, 'bold'), height='1', width='8',bd=3, command=search)
        self.buttonSearch.grid(row=0, column=4)

        self.buttonUpdate = Button(OperationFrame, text='Update', font=('arial', 14, 'bold'), height='1', width='8',bd=3, command=updatebinfo)
        self.buttonUpdate.grid(row=0, column=5)

        self.buttonDelete = Button(OperationFrame, text='Delete', font=('arial', 14, 'bold'), height='1', width='8',bd=3, command=delete)
        self.buttonDelete.grid(row=0, column=6)



        self.buttonClose = Button(OperationFrame, text='Close', font=('arial', 14, 'bold'), height='1', width='8',bd=3, command=close)
        self.buttonClose.grid(row=0, column=7)


        self.buttoncaltimef = Button(BottombodyFrame, text='Get time', font=('arial', 12, 'bold'), height='1', width='10',bd=2, command=caltimef)
        self.buttoncaltimef.grid(row=5, column=1)

        self.buttonSaverecord = Button(BottombodyFrame, text='Insert', font=('arial', 12, 'bold'), height='1', width='10',bd=2, command=insertreading)
        self.buttonSaverecord.grid(row=6, column=1)

        self.buttoncalculateresult = Button(BottombodyFrame, text='Calculate', font=('arial', 12, 'bold'), height='1', width='10',bd=2, command=calculate)
        self.buttoncalculateresult.grid(row=7, column=1)

        self.buttonshow = Button(BottombodyFrame, text='Show', font=('arial', 12, 'bold'), height='1', width='10',bd=2, command=showInBridgeList)
        self.buttonshow.grid(row=5, column=0)

        self.buttonEditrecord = Button(BottombodyFrame, text='Update', font=('arial', 12, 'bold'), height='1', width='10',bd=2, command=updaterec)
        self.buttonEditrecord.grid(row=6, column=0)

        self.buttonDeletereading = Button(BottombodyFrame, text='Delete', font=('arial', 12, 'bold'), height='1', width='10',bd=2,command=deleterec)
        self.buttonDeletereading .grid(row=7, column=0)


# Back End Database operations
class Database:
    def conn(self):
        print("Database : connection method called\n")
        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        query= "create table if not exists bridge(bid text primary key,bname text, bDiscription text,bGlocation text, blocations text,tdate text)" 
        
        query1= "create table if not exists readingdata(bid text,tlocation text, point text, reading text,length text, caltime text)" 
        query2= "create table if not exists calresult(bid text,btlocation text,bsectionavg text,btresult text, compressive_strength_fc text)" 
        query3 = "create table if not exists user(first_name text,username text ,password text )"

        cur.execute(query)
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        con.commit()
        con.close()
        print("Database : connection method finished\n")

    def insert(self, bid, bName, bDiscription,bGlocation,bLocations,bTdate):
        
        print("Database : Insert method called\n")

        con = sqlite3.connect("bridgeval.db")
        
        cur = con.cursor()
        query = "insert into bridge values(?,?,?,?,?,?)"
        
        #bsectionavg=ravg
        cur.execute(query,(bid,bName, bDiscription,bGlocation,bLocations,bTdate))
        
        con.commit()
        con.close()
        print("Database : insert method finished\n")
    
    def insertresult(self,bid,btlocation,bsectionavg,btresult,compressivestrength_fc):
        print("Database : Insertresult method called\n")
        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        query1 = "insert into calresult values(?,?,?,?,?) "
        bsectionavg=ravg
        cur.execute(query1,(bid,btlocation,bsectionavg,btresult, compressivestrength_fc))
        con.commit()
        con.close()
        print("Database : insertresult method finished\n")
    
    def insertreading(self, bId, TLocation, bRpoint, bReading,length, caltime):
        print("Database : Insertreading method called\n")
        print("call time database", caltime1)
        
        caltime=round(caltime1, 2)

        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        print("call time live", caltime)
        query = "insert into readingdata values(?,?,?,?,?,?) "
        
        cur.execute(query,(bId,TLocation,bRpoint,bReading,length,caltime))
        '''
        query2="SELECT * FROM readingdata WHERE (bid=? AND tlocaton=?)"
        global ravg
        cur.execute(query2, bId,TLocation)
        items = cur.fetchall()
        i=0
        total = 0         
        for item in items:
            total= total + item[3]
            i= i+1
        ravg=total/i
        '''
        con.commit()
        con.close()
        print("Database : insert Reading entry method finished\n")
    


    def showall(self):

        print("Database : show all method called")
        global click 
        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        query="SELECT * FROM bridge"
        cur.execute(query)
        rows = cur.fetchall()
        #print (rows)
        con.close()
        print("Database: Show all  method finished")
        return rows 



    def show(self,bId, TLocation):
        print("Database : show method called")
        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        query="SELECT * FROM readingdata WHERE (bid=? AND tlocation=?)"
        cur.execute(query, (bId,TLocation))
        rows = cur.fetchall()
        con.close()
        print("Database: Show method finished")
        return rows 
    
    def deleteres(self, bid,tlocation):
        print("Database : Delete result method called")
        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        cur.execute("delete from calresult where bid=? and btlocation=?",(bid,tlocation,))
        con.commit()
        con.commit()
        print(" Database: delete result method finished\n")
    
    
    
    def delete(self, bid):
        print("Database : Delete method called")
        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        cur.execute("delete from bridge where bid=?",(bid,))
        con.commit()
        con.commit()
        print(" Database: delete method finished\n")
    
    def deletereading(self, bid, tlocation,point):
        print("Database : Delete method called for rading")
        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        cur.execute("delete from readingdata where bid=? and tlocation=? and point=?",(bid,tlocation,point,))
        con.commit()
        con.close()
        print(" Database: delete method finished\n")
        #bId.get(),bName.get(),bDiscription(),bGlocation.get(),bLocations.get(),bTdate.get()
    '''
    def updaterec(self, bid, tlocation,point,reading,length,caltime):
        print("Database : update method called for rading\n")
        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        cur.execute("delete from readingdata where bid=? and tlocation=? and point=?",(bid,tlocation,point,))
        cur.execute("update from readingdata where bid=? and tlocation=? and point=?",(bid,tlocation,point,))
        con.commit()
        con.close()
        print(" Database: update method finished\n")
        #bId.get(),bName.get(),bDiscription(),bGlocation.get(),bLocations.get(),bTdate.get()

    '''
    def search(self,bId="",bName="",bDiscription="",bGlocation="",bLocations="", bTdate=""):
        print("Database : Search method called \n", bId)
        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        cur.execute("select * from bridge where bid=? or bDiscription=? or bName=? or bGlocation=? or \
                            blocations=? or tdate=?",(bId,bName,bDiscription,bGlocation,bLocations,bTdate))
        row=cur.fetchall()
        con.close()
        print("Database : search method finished \n")
        return row 
    def update(self,bid="",bName="",bGlocation="",blocations=""):
        print("Database : Update method called ")
        con = sqlite3.connect("bridgeval.db")
        cur = con.cursor()
        cur.execute("update bridge set bid=? or bName=? or bDiscription=? or bGlocation=? or \
                            blocations=? or tlocation=?",(bid, bName,bDiscription,bGlocation,blocations,tlocation) )
        con.commit()
        con.close()
        print(pid, "Database : Update method finished\n")

    
if __name__ == '__main__':
    from PIL import ImageTk, Image 
    print("Please wait a moment!")
    print("UPV Software Loading..............")
    win =Tk()

    win.state('zoomed')
    win.iconbitmap('PPLICEO.ico')
    win.title("UPV Calculation Software Version-1.0")
    #win.attributes("-fullscreen", True)
    bg= ImageTk.PhotoImage(file="tista_bridge.png")
    my_canvas = Canvas(win)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0,0, image=bg, anchor="nw") 
    
    def resizer(e):
        global bg1, resized_bg, new_bg
        #open the image 
        bg1=Image.open("tista_bridge.png")
        resized_bg = bg1.resize((e.width, e.height),Image.ANTIALIAS)
        #define image again
        new_bg= ImageTk.PhotoImage(resized_bg)
        # Add it back to the canvus
        my_canvas.create_image(0,0, image=new_bg, anchor="nw") 
         

    def startapp():
        root=Toplevel()
        win.wm_state('iconic')
        win.iconify()
        root.iconbitmap('PPLICEO.ico')
        root.lift()
        application = Bridge(root)
        root.resizable(True,True)
        root.mainloop()
        return 
    
    def exit():
        win.destroy()
        root.destroy()
        return 
    
    def about():
        win2=Toplevel()
        win2.iconbitmap('PPLICEO.ico')
        win2.title("About us")
        win2.resizable(0,0)
        #win2.geometry("250x170")
        l1= Label(win2, font=('arial',30,'bold'), fg='black',
                    text='（UVP）橋梁用計算ソフト')
        l1.pack()
        l2= Label(win2, font=('arial',30,''), fg='black',
                    text='© Copyright 2021. All Rights Reserved @Plan Plus limited, Bangladesh')
        l2.pack()
        '''
        MainFrame=Frame(self.win2,bg ="gray")
        MainFrame.pack()
        MainFrame1=Frame(self.win2,bg ="gray")
        MainFrame1.pack()

        HeadFrame1 = Frame(MainFrame1, bd=2, padx=60, pady=10,bg='white', relief=RIDGE)
        HeadFrame1.pack(side=TOP)
     
        Label(HeadFrame1, font=('arial',36,'bold'), fg='black',
                    text='（UVP）橋梁用計算ソフト', bg='white')
        win2.ITitle.pack()
        '''
        win2.mainloop()


    def login():
        win3=Toplevel()
        win3.iconbitmap('PPLICEO.ico')
        win3.title("About us")
        win3.resizable(0,0)
        win3.geometry("350x350")
        l1= Label(win2, font=('arial',30,'bold'), fg='black',
                    text='（UVP）橋梁用計算ソフト')
        l1.pack()
        l2= Label(win2, font=('arial',30,''), fg='black',
                    text='Login ')
        l2.pack()
        '''
        MainFrame=Frame(self.win2,bg ="gray")
        MainFrame.pack()
        MainFrame1=Frame(self.win2,bg ="gray")
        MainFrame1.pack()

        HeadFrame1 = Frame(MainFrame1, bd=2, padx=60, pady=10,bg='white', relief=RIDGE)
        HeadFrame1.pack(side=TOP)
     
        Label(HeadFrame1, font=('arial',36,'bold'), fg='black',
                    text='（UVP）橋梁用計算ソフト', bg='white')
        win2.ITitle.pack()
        '''
        win3.mainloop()

    topMenu = Menu(win)
    win.config(menu=topMenu)

    submenu1 = Menu(topMenu)
    submenu2 = Menu(topMenu)
    topMenu.add_cascade(menu=submenu1, label="File")
    topMenu.add_cascade(menu=submenu2, label="Help")
    
    submenu1.add_command(label="Start Application", command=startapp)
    submenu1.add_command(label="Exit ", command= exit)
    submenu2.add_command(label="About ", command= about)
    win.bind('<Configure>', resizer)

    win.mainloop()

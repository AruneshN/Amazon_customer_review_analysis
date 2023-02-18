from bs4 import BeautifulSoup as bs
import requests
import tkinter as tk
import tkinter 
from requests.exceptions import MissingSchema
from tkinter import ttk 
from tkinter import*
from tkinter import messagebox
import pandas as pd 
from tkinter import filedialog
import csv


root=tk.Tk()
root.geometry("1366x768")
root.config(bg="skyblue")

url_entry = tk.Entry(root,width=80,fg="blue",font=("Courier",10, "underline"))
url_entry.pack()

var=StringVar()
var.set("AUTOMATED WEB SCRAPPING")
label=Label(root,textvariable=var,bd=8,bg='skyblue',fg="black",
      font=("HP Simplified Jpan",50,"underline")).place(x=250,y=10)
# w1=StringVar()

url_entry.place(x=290,y=180)

# w1=Entry(root,width=100,textvariable=url_entry)

def amazon():
    url = url_entry.get()
    # link="https://www.amazon.in/Samsung-Galaxy-Storage-Months-Replacement/product-reviews/B096VD213D/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&"
    link=url
    cust_name=[]
    review_title=[]
    rate=[]
    review_content=[]
    #how many pages i want i.e.,(1,10)

    for i in range(1,6):
        para={'pageNumber':str(i)}
        page=requests.get(link,params=para)
        page.content
        soup=bs(page.content,'html.parser')
        soup.prettify()
        names=soup.find_all('span',class_='a-profile-name')
        title=soup.find_all('a',class_='review-title')
        rating=soup.find_all('span',class_='a-icon-alt')
        review=soup.find_all("span",{"data-hook":"review-body"})
        
        for i in range(0,len(names)):
            cust_name.append(names[i].get_text())
        
        for i in range(0,len(title)):
            review_title.append(title[i].get_text())
        
        review_title[:]=[titles.strip('\n') for titles in review_title]
        review_title[:]=[titles.lstrip('\n') for titles in review_title]
        review_title[:]=[titles.rstrip('\n') for titles in review_title]
        for i in range(0,len(rating)):
            rate.append(rating[i].get_text())
        #rate.pop(9) 
        for i in range(0,len(review)):
            review_content.append(review[i].get_text())
        review_content[:]=[titles.lstrip('\n') for titles in review_content]
        review_content[:]=[titles.rstrip('\n') for titles in review_content]
            
        if len(cust_name)>len(review_content):
            #global length
            length=len(cust_name)-len(review_content)
            
            
        for i in range(length):
            cust_name.pop(length)
            
        if len(rate)>len(review_content):
            #global lenth
            lenth=len(rate)-len(review_content)
            
            
        for i in range(lenth):
            rate.pop(lenth)
            
            
    df=pd.DataFrame()
    df['Customer_Name']=cust_name
    df['Review_title']=review_title
    df['Reviews']=review_content
    df['Ratings']=rate
    df.to_csv(r'D:\Amazonmulti.csv',index=False)
    
   

def browsefiles():
    filename=filedialog.askopenfilename(initialdir="/D:",
                                        title="Select a File",
                            filetypes=(("csv files","*.csv*"),("all files"," *.* ")))
    
    
    
scrap_button = tk.Button(root, text='Scrap ', command=amazon,font=("times new roman",16,"bold")).place(x=970,y=166)


csv_button = tk.Button(root, text='Import CSV File ', command=browsefiles,font=("times new roman",16,"bold")).place(x=600,y=280)



def read_csvfile():
    #root1=tk.Tk()
    window =Toplevel(root)
    window.geometry("1366x768")
    window.config(bg="skyblue")
    #window = tk.Tk()
    window.title("Amazon Product Review")
    
    treeview = ttk.Treeview(window)
    treeview.pack(side='left', fill='both', expand=True)

    # Open the CSV file and read it
    with open(r'D:\Amazonmulti.csv', "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Add the header row to the Treeview
        header = next(reader)
        treeview["columns"] = header
        for col in header:
            treeview.heading(col, text=col)
        
        # Add the data rows to the Treeview
        for row in reader:
            treeview.insert("", "end", values=row)

    window.mainloop()
   
amazon_button = tk.Button(root, text='Amazon',command=read_csvfile, font=("times new roman",16,"bold")).place(x=640,y=375)

root.mainloop()

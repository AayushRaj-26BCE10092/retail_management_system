from timestamp import timestamp
from tabuler import tabular
from rich import print as pr
pr("[bold italic green]WELCOME TO RETAIL MANAGEMNT SYSTEM")
p=input("Enter 1 to access the inventory\nEnter 2 to access the biling srvice\nEnter 3 to access accounts log\nNow make your selection:")
if p.isnumeric():
    if int(p)==1:
        pr("[bold italic green]INVENTORY SYSTEM  INITATED")
        d={}
        f=open("invetory.txt","r+")
        b=f.read().split("\n")
        if b!=[""]:
            for items in b:
                if items!='':
                    a=items.split(",")
                    d.update({a[0]:a[1]})
        else:
            pr("[bold italic red]Empty inventory:","[bold italic green]Please add items")
        a=input("Enter 1 to access the whole inventory\nEnter 2 to serach for a specific item\nEnter 3 to see items less in stock\nEnter 4 to add an item to inventory\nNow make your selection:")
        if a.isnumeric():
            if int(a)==1:
                tabular(["Item","Quantity"],**d)
            elif int(a)==2:
                b=input("Enter the item:")
                if b in d:
                    pr(f"[bold italic cyan]{d[b]}")
                else:
                    pr("[bold italic red]Item not in inventory")
            elif int(a)==3:
                x={x:y for x,y in d.items() if int(y)<10}
                tabular(["Item","Quantity"],**x)
            elif int(a)==4:
                a=list(input("Make the entery in form of [item name],[quantity],[price]:").split(","))
                if a[0] in d:
                    b=int(a[1])
                    c=int(d[a[0]])
                    e=b+c
                    d[a[0]]=str(e)
                else :
                    d.update({a[0]:a[1]})
                f.seek(0)
                f.truncate()
                for items,values in d.items():
                    f.write(f"{items},{values}\n")
                with open("debits.txt","+a") as fi:
                    fi.write(f"{a[0]},{int(a[1])},Rs.{int(a[1])*int(a[2])},{timestamp()}\n")
            else:
                pr("[bold italic red]Invalid input")
        else:
            pr("[bold italic red]Invalid input")
    elif int(p)==2:
        pr("[bold italic green]BILLING SYSTEM INITIATED")
        name=input("enter the customers name:")
        mobile_no=input("enter the customers mobile no:")
        l=[]
        d={}
        file=open("invetory.txt","a+")
        file.seek(0)
        b=file.read().split("\n")
        if b!=[""]:
            for i in b:
                if i!='':
                    a=i.split(",")
                    d.update({a[0]:a[1]})
        while True:
            items=input("Enter the items as [itme_name],[quanitity],[price]\n or enter 1 to exit:").split(",")
            if items==["1"]:
                    break
            elif items[0] not in d:
                pr("[bold italic red]Item out of stock")
            else:
                x=int(d[items[0]])
                y=int(items[1])
                if x>y:
                    d[items[0]]=str(x-y)
                    l.append(items)
                else:
                    pr("[bold italic red]Less item in stock")
                file.seek(0)
                file.truncate()
                for item,values in d.items():
                    file.write(f"{item},{values}\n")
                total=int(items[1])*int(items[2])
                items.append(total)
        pr("[bold italic green]RECEIT")
        pr(f"[bold italic cyan]Name:{name}")
        pr(f"[bold italic cyan]mobile no:{mobile_no}")
        tabular(["item","quantity","price","total"],*l)
        sum=0
        for items in l:
            sum=sum+items[3]
        pr(f"[bold italic green]Total amount to pay:{sum}")
        with open("credits.txt","a+") as cred_file:
            cred_file.write(f"{name},Rs.{sum},{timestamp()}\n")
    elif int(p)==3:
        a=input("Enter 1 to access credit logs\nEnter 2 to access debits\nNow make your selection:")
        if a.isnumeric():
            if int(a)==1:
                with open("credits.txt","r") as file:
                    file.seek(0)
                    data=file.read().split("\n")
                    data.pop()
                    d=[]
                    for items in data:
                        a=list(items.split(","))
                        d.append(a)
                    if d!=[]:
                        pr("[bold italic green]CREDITS:")
                        tabular(["Name","Amount","Date"],*d)
                    else:
                        pr("[bold italic red]No credit logs available","[bold italic green]Please sell items to customers")
            elif int(a)==2:
                with open("debits.txt","r") as file:
                    file.seek(0)
                    data=file.read().split("\n")
                    data.pop()
                    d=[]
                    for items in data:
                        a=list(items.split(","))
                        d.append(a)
                    if d!=[]:
                        pr("[bold italic red]DEBITS")
                        tabular(["Name","Quantity","Amount","Date"],*d)
                    else:
                        pr("[bold italic red]No debit logs available","[bold italic green]Please stock up items in inventory")
            else:
                pr("[bold italic red]Invalid input")
        else:
            pr("[bold italic red]Invalid input")          
else:
    pr("[bold italic red]Invalid input")
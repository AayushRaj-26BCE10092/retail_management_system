from tabulate import tabulate
def tabular(h,*b,**a):
    data=[]
    for i,v in a.items():
        data.append([i,v])
    if a!={}:
        print(tabulate(tabular_data=data,headers=h,tablefmt="grid"))
    if b!=():
        print(tabulate(tabular_data=b,headers=h,tablefmt="grid"))
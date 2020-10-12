import pandas as pd

customers = {
    'CustomerId' : [1,2,3,4],
    'FirstName' : ["Furkan","Furkan","Furkan","Furkan"],
    'LastName' : ["Aygur","Aygur","Aygur","Aygur"]
}

orders = {
    'OrderId' : [10,11,12,13],
    'CustomerId' : [1,2,5,7],
    'OrderDate' : ['2020-12-10','2020-11-10','2020-10-10','2020-13-10']
}

df_customers = pd.DataFrame(customers , columns = ['CustomerId','FirstName','LastName'])
df_orders = pd.DataFrame(orders , columns = ['OrderId','CustomerId','OrderDate'])

print(df_customers)
print(df_orders)

result = pd.merge(df_customers, df_orders, how="inner")
print(result)

result = pd.merge(df_customers, df_orders, how="left")
print(result)

result = pd.merge(df_customers, df_orders, how="outer")
print(result)


# **************************************************************

customersA = {
    'CustomerId' : [1,2,3,4],
    'FirstName' : ["FurkanA1","FurkanA2","FurkanA3","FurkanA4"],
    'LastName' : ["AygurA1","AygurA2","AygurA3","AygurA4"]
}

customersB = {
    'CustomerId' : [1,2,3,4],
    'FirstName' : ["Furkan1","FurkanB2","FurkanB3","FurkanB4"],
    'LastName' : ["AygurB1","AygurB2","AygurB3","AygurB4"]
}

df_customersA = pd.DataFrame(customersA , columns = ['CustomerId','FirstName','LastName'])
df_custobersB = pd.DataFrame(customersB , columns = ['CustomerId','FirstName','LastName'])

result = pd.concat([df_customersA,df_custobersB], axis=0)
print(result)


result = pd.concat([df_customersA,df_custobersB], axis=1)
print(result)
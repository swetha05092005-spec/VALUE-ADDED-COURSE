import pandas as pd
from twilio.rest import Client
import time
acc_sid=""
acc_token=""
client=Client(acc_sid, acc_token)
df=pd.read_excel("data.xlsx")
for i in range(len(df)):
    name=df.loc[i,"NAME"]
    desig = df.loc[i, "DESIGNATION"]
    number = str(df.loc[i, "NUMBER"])
    number="+91"+number

    messages = {
    'staff': "Teach well",
    'student': "Concentrate only in Career",
    'corpenter': "Tight the Society",   
    'docter': "Thank you saver",        
    'engineer': "Hello National Builders",
    'manager': "Manage everything"
}

    msg = messages.get(desig.lower(), "hello")
    final_msg = f"{name},{msg}"
    client.messages.create(
    from_='whatsapp:+14155238886',
    body=final_msg,
    to=f'whatsapp:{number}')
print(f"sent to{name}->{number}")
time.sleep(1)
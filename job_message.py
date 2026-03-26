import requests
from twilio.rest import Client


acc_SID=""
auth_token=""

client=Client(acc_SID,auth_token)

students=['whatsapp:+91+....']


url="https://remoteok.com/api"
jobs=requests.get(url).json()


for job in jobs:
    if isinstance(job,dict):
        title=job.get("position","")
        if "java" in title.lower() or "python" in title.lower() or "engineer" in title.lower():
            message=f"""JOB ALERT!!!!
            Company:{job.get("company")}
            Role:{title}
            Link:{job.get("url")}
            """


            for number in students:
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=message,
                    to=number
                )  
            print("message sent to all")
            break
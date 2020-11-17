import smtplib


def mail(from_addr,to_addrs,mssg):
    
    server = smtplib.SMTP("smtp.sitemail.com", 587)
    server.starttls()
    print("Started.........................")
    server.login("youremail@site.com", 'password')
    print("Login  success.........")
    server.sendmail(from_addr, to_addrs, mssg)
    print("Mail Sent success.........")
    server.quit()



from_addr='anynamemail@canva.com'
to_addr='lerdirelmu@nedoz.com'
from_name='Canva'
subject="Discover India's Top 10 presentations templates"

message = f"""From: {from_name} <{from_addr}>
To: {to_addr}
Subject: {subject}
Team up and collaborate with our Top 10
Take your presentations to new heights with teamwork and keep your ideas flowing with our top 10 presentation templates. Real-time collaboration is now available, so you can invite anyone to co-create and work with you within moments.
Whether it’s a pitch deck, a sales report, or a business plan, staying on the same page has never been more effortless. Got an idea to share, a new insight, or feedback to add? Instantly have your say with live comments. So go on, create a winning presentation as a team today.
"""

mail(from_addr,to_addr,message.encode())

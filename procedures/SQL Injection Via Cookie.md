---
id: 608eb59b-f22f-4da4-af34-d680db42bf25
name: SQL Injection Via Cookie
type: procedure
verified: true
submitted: true
created_at: '2020-09-06T09:09:00.281666+00:00'
updated_at: '2023-05-26T18:51:04.842771+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[SQL]]'
- '[[Web Applications]]'
---

# SQL Injection Via Cookie

**Status**: ✓ Verified

## Summary

Cookie parameter is not usually controlled by the user of the application. But few application servers doesnot perform the validation checks on the cookie parameter which can be manipulated by an attacker to gain unauthorised access to the application's server and access sensitive information. 

## Description

# Description

Cookie parameter is not usually controlled by the user of the application. But few application servers doesnot perform the validation checks on the cookie parameter which can be manipulated by an attacker to gain unauthorised access to the application's server and access sensitive information.

# Instructions



1.Intecept the home page of the application and notice that cookie contains a TrackinID paramter .







![aea46c0e-9148-402a-9dbc-00b825d4140c.png](_assets/images/Mash/aea46c0e-9148-402a-9dbc-00b825d4140c.png)





2.Submit the above request and observe tha* welcome back *message in the response.







![14fd0780-733d-4e8c-8b2e-265b18ccfb0e.png](_assets/images/Mash/14fd0780-733d-4e8c-8b2e-265b18ccfb0e.png)







3.Modify the TrackingID paramter value to single quote and submit the request to the server.





![8bf6b1e0-621b-4072-8134-60501dcce62d.png](_assets/images/Mash/8bf6b1e0-621b-4072-8134-60501dcce62d.png)









4.Notice that response page does not contain the *welcome back* message







![70b576d7-cfca-466a-9110-56ca4a1bd992.png](_assets/images/Mash/70b576d7-cfca-466a-9110-56ca4a1bd992.png)





5.Now modify the TrackerID value to the following palyoad and submit the request to the server .Notice the welcome back message 



*‘+or+1=1- -*



![2dc4249c-c42a-4870-a27e-eb23a9629732.png](_assets/images/Mash/2dc4249c-c42a-4870-a27e-eb23a9629732.png)





6.Now change the payload and submit the request . NOtice that *welcome back* message isnt there in the response.

*‘+or=1=2- -*





![ecca089b-db78-439c-b820-d7fbd067d681.png](_assets/images/Mash/ecca089b-db78-439c-b820-d7fbd067d681.png)





7.Now send the request to the intruder tab. For this attack to work, user name should be known to the attacker by other attack techniques. USe the following payload to enumerate the db names of the database with the payload of dbnames. Add the payload position* table_name* . Also add the grep match pattern to identify the *welcome back *message in the response which indicates the successful response from the DB server.

*‘+UNION+SELECT+’a’+FROM+($table_name$)+WHERE+1=1- -*





![b15516a4-307d-44a6-9b25-ee390d4cb541.png](_assets/images/Mash/b15516a4-307d-44a6-9b25-ee390d4cb541.png)





8.When the attack finishes , notice that *users *dbname matches the grep pattern which indicates that db contains a db  with *users  *name 





![c4d3a98e-d373-42f2-8c2c-475619982f11.png](_assets/images/Mash/c4d3a98e-d373-42f2-8c2c-475619982f11.png)





9.Now enumerate the tables_columns .For this, attacker should already know atleast one username of the database. In this case the user of the db is administrator.Use the following payload to enumerate columns of the db.

*‘+UNION+SELECT+’a’+FROM+users+WHERE+($table_column$)='administrator'- -*





![e61f2c40-611c-4f23-ae3c-f4a541a9fab9.png](_assets/images/Mash/e61f2c40-611c-4f23-ae3c-f4a541a9fab9.png)





10. Add the payload to the payloads and start attack. Once the attack is fininshed , the resposne shows the valid column names for the db.





## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[SQL]]
- [[Web Applications]]



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

2.Submit the above request and observe tha* welcome back *message in the response.

3.Modify the TrackingID paramter value to single quote and submit the request to the server.

4.Notice that response page does not contain the *welcome back* message

5.Now modify the TrackerID value to the following palyoad and submit the request to the server .Notice the welcome back message 

*‘+or+1=1- -*

6.Now change the payload and submit the request . NOtice that *welcome back* message isnt there in the response.

*‘+or=1=2- -*

7.Now send the request to the intruder tab. For this attack to work, user name should be known to the attacker by other attack techniques. USe the following payload to enumerate the db names of the database with the payload of dbnames. Add the payload position* table_name* . Also add the grep match pattern to identify the *welcome back *message in the response which indicates the successful response from the DB server.

*‘+UNION+SELECT+’a’+FROM+($table_name$)+WHERE+1=1- -*

8.When the attack finishes , notice that *users *dbname matches the grep pattern which indicates that db contains a db  with *users  *name 

9.Now enumerate the tables_columns .For this, attacker should already know atleast one username of the database. In this case the user of the db is administrator.Use the following payload to enumerate columns of the db.

*‘+UNION+SELECT+’a’+FROM+users+WHERE+($table_column$)='administrator'- -*

10. Add the payload to the payloads and start attack. Once the attack is fininshed , the resposne shows the valid column names for the db.

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[SQL]]
- [[Web Applications]]

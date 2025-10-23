---
id: 4b847668-2e8b-4fd8-8c8c-ba744d4b64c7
name: Authentication Bypass via Information Disclosure
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T15:03:06.981760+00:00'
updated_at: '2023-05-26T15:56:58.782392+00:00'
platforms:
- Web
tags:
- '[[authentication]]'
- '[[broken authentication]]'
- '[[information disclosure]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Authentication Bypass via Information Disclosure

**Status**: ✓ Verified

## Summary

The application uses a custom header to validate if the user is an admin. The application can be accessed as a normal user and modify the header to gain admin access. 

## Description

# Description

The application uses a custom header to validate if the user is an admin. The application can be accessed as a normal user and modify the header to gain admin access.



# Procedure



1. Access the application and login as a normal user.







![0aa9f629-6eb2-4f40-98ea-20e24479b164.png]()







2. Refresh the page and intercept using Burp. Right-click and send it to repeater.





![1681059f-fb9d-4577-af8f-dcf5e065e5e4.png]()



3. In the repeater, modify the request and access */admin* using GET method. The response contains an information that the portal can only be accessed from localhost.





![25acf21b-4ded-42a0-b4d3-67ad15201f96.png]()



4. Modify the method to TRACE and access */admin.* Custom response header is observed in the response *X-Custom-IP-Authorization* which contains the IP address of user. 





![440c9251-27b5-41e6-8397-c1a201372163.png]()



5. In the Proxy -> Options -> Match and Replace -> Click on Add. In the Replace field, enter X-Custom-IP-Authorization: 127.0.0.1. Burp will keep adding the header for all the requests.



![ecaa74e9-96a8-40dd-981d-b8e75fa3689c.png]()



6. Access the website again and observe that X-Custom-IP-Authorization: 127.0.0.1 is added automatically to the requests.



![c28f8be4-3adb-49bd-9de5-2fe4f2d44eb3.png]()

7. Admin Panel option is observed and click on it.



![81a6ad1f-b1d8-4f23-b656-815d2cb10ce6.png]()



8. Admin panel is accessed





![e9fd7875-041a-437c-a24b-673171acaab4.png]()



## Platforms

- Web

## Tags

- [[authentication]]
- [[broken authentication]]
- [[information disclosure]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]



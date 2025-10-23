---
id: 601eb9ee-93d0-47ec-a76f-c3ae8d480c03
name: Path Traversal (Validation Of Start Of Path)
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T17:54:44.342511+00:00'
updated_at: '2023-05-26T18:24:52.530886+00:00'
platforms:
- Web
tags:
- '[[Path Traversal]]'
- '[[Web Applications]]'
---

# Path Traversal (Validation Of Start Of Path)

**Status**: ✓ Verified

## Summary

Some appluications validate the start of the file name as a filter. An attacker can bypass this by using the valid file paths at the start of the filename and then use the malicious file paths at the end 

## Description

# Description



Some appluications validate the start of the file name as a filter. An attacker can bypass this by using the valid file paths at the start of the filename and then use the malicious file paths at the end





# Instructions





1.Use the burp suite to intercept the request





![74eb6129-8cc2-4fe4-91f0-d68dbd221c91.png]()



2. Send the reques to the server 







![5a50f323-963a-43a2-9fb4-b03b2c6d54ee.png]()





3.Modify the filename paratemer to /var/www/images/37.jpg and send the request to the server and observe the response .





![07301f63-d446-4832-b859-b570be64bed1.png]()





4. Modify the filename value to the following and send the request to the server . It can be observed that the file contents of passwd are loaded in the response.

*`/var/www/images/../../../etc/passw*d`





![d45a1b54-8c90-429c-8ef1-824780f5ae69.png]()



## Platforms

- Web

## Tags

- [[Path Traversal]]
- [[Web Applications]]



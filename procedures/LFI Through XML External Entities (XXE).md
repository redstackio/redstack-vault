---
id: b142b1e2-12ac-41f3-8a54-864194b3affb
name: LFI Through XML External Entities (XXE)
type: procedure
verified: true
submitted: true
created_at: '2020-07-27T17:44:47.890047+00:00'
updated_at: '2023-05-26T18:40:32.154443+00:00'
platforms:
- Web
tags:
- '[[LFI]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xxe]]'
---

# LFI Through XML External Entities (XXE)

**Status**: ✓ Verified

## Summary

XXE can be performed by modifying the XML request and adding an external entity like SYSTEM to perform activities like Local File Inclusion (LFI). 

## Description

# Description

XXE can be performed by modifying the XML request and adding an external entity like SYSTEM to perform activities like Local File Inclusion (LFI).



# Instructions 



1. Enter username and password in the login page





![3930a48a-65c0-4100-a04b-a885ea7c7379.png](_assets/images/Mash/3930a48a-65c0-4100-a04b-a885ea7c7379.png)





2. Intercept the request in Burp Suite. The request is being sent in XML format.





![aee71b71-aa1a-4661-88c4-bdfadda4b83f.png](_assets/images/Mash/aee71b71-aa1a-4661-88c4-bdfadda4b83f.png)





3. Right-click on the request and send it to repeater.





![c58647c1-0894-4c83-aa1c-77339c06eadf.png](_assets/images/Mash/c58647c1-0894-4c83-aa1c-77339c06eadf.png)



4. Modify the XML request by adding the external entity (*SYSTEM*) including local file on the server i.e. */etc/passwd*. The application parses the XML request and responds with */etc/passwd* file.





![06ccb80b-8f32-4d68-9f52-13980a339b06.png](_assets/images/Mash/06ccb80b-8f32-4d68-9f52-13980a339b06.png)





## Platforms

- Web

## Tags

- [[LFI]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xxe]]



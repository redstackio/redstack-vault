---
id: 853f447f-7994-4b83-852b-b3c261803ef2
name: HTTP Request Smuggling CL TE Through Differential Response
type: procedure
verified: true
submitted: true
created_at: '2020-08-12T03:18:39.664961+00:00'
updated_at: '2023-05-26T18:38:51.939221+00:00'
platforms:
- Web
tags:
- '[[http request smuggling]]'
- '[[Web Applications]]'
---

# HTTP Request Smuggling CL TE Through Differential Response

**Status**: ✓ Verified

## Summary

In this type of Request Smuggling attack, an attacker will try to craft a CL TE request. If the request gets parsed by the application ,a differential response can be observed. 

## Description

# Description

In this type of Request Smuggling attack, an attacker will try to craft a CL TE request. If the request gets parsed by the application ,a differential response can be observed.



# Instructions





1. Intercept the request and send the request to the repeater tab.





![f5fd2a0d-4bf3-4e10-ab00-da1bfaf8eebb.jpg](_assets/images/Mash/f5fd2a0d-4bf3-4e10-ab00-da1bfaf8eebb.jpg)





2. Modify the request in the repeater tab to the following request . Observe the request was modified to 404 in the below.







**Code**: [[POST / HTTP/1.1
Host: your-lab-id.web-security-ac]]









3. Send the modified request to the server  and observe the response . It confirms the differential response from the server for the modified request.









![b7c8f4a7-efd1-4b71-9233-2dc0ddf44e16.jpg](_assets/images/Mash/b7c8f4a7-efd1-4b71-9233-2dc0ddf44e16.jpg)









## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[Web Applications]]



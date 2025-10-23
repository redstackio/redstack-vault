---
id: f3821842-e7cd-4945-a90b-27fb637ae3e6
name: ' Stored XSS to Perform CSRF'
type: procedure
verified: true
submitted: true
created_at: '2020-08-05T15:51:59.892318+00:00'
updated_at: '2023-05-26T18:36:32.403480+00:00'
platforms:
- Web
tags:
- '[[CSRF]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xss]]'
---

#  Stored XSS to Perform CSRF

**Status**: ✓ Verified

## Summary

Description A CSRF attack when done by itself can be patched easily by implementing CSRF tokens. By chaining XSS and CSRF together , an attacker can bypass the anti-CSRF token implementation. Instructions 1. Create a legitimate account on the application and login using the credentials. 

## Description

# Description 

A CSRF attack when done by itself can be patched easily by implementing CSRF tokens. By chaining XSS and CSRF together , an attacker can bypass the anti-CSRF token implementation.





# Instructions

# 

1. Create a legitimate account on the application and login using the credentials.







![4bf9fbb5-b729-45b0-9d1c-2e45a39343bc.PNG](_assets/images/Mash/4bf9fbb5-b729-45b0-9d1c-2e45a39343bc.PNG)





2. Click on *Change email *tab to access the page.







![3448374b-67eb-4f25-8f0a-68eff0284435.PNG](_assets/images/Mash/3448374b-67eb-4f25-8f0a-68eff0284435.PNG)









3. Right click on the *change email *page and click on *view page source. *It can be observed that  *post method *is used to submit the *update email* . It also can be observed that *anti CSRF tokens* are implemented in hidden field.









![17605b6e-d207-41ef-9654-4a1493124436.PNG](_assets/images/Mash/17605b6e-d207-41ef-9654-4a1493124436.PNG)







4. Frame a payload in such a way that* CSRF token*s from *hidden *filed will be taken and use a post method for *change email. *



*payload:*







**Code**: [[<script>
var req = new XMLHttpRequest();
req.onl]]









5. Submit the payload from step 4 in* comment* section of the blog.





![d4007996-0dc0-4da4-b8b5-922a4a6a89c1.PNG](_assets/images/Mash/d4007996-0dc0-4da4-b8b5-922a4a6a89c1.PNG)





6. Whoever visits the comment section of the page , the *payload *gets executed and the user's email will be changed to *test@test.com*







![362fc756-abb4-4390-bfb9-a093ef270207.PNG](_assets/images/Mash/362fc756-abb4-4390-bfb9-a093ef270207.PNG)











## Platforms

- Web

## Tags

- [[CSRF]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]



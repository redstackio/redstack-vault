---
id: 7ccbbbf5-d9e9-401b-b794-05d64fa545b0
name: UserID Controlled By Request Parameter With Password Disclosure
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T09:56:01.762495+00:00'
updated_at: '2023-05-26T18:48:57.606718+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# UserID Controlled By Request Parameter With Password Disclosure

**Status**: ✓ Verified

## Summary

Appliaction's detect the unwarranted access of resource without authentication and redirect the response to home page. While redirection , the response sometimes may leak the sensitive inforamtion due to logical flaw of the application 

## Description

# Description

Appliaction's detect the unwarranted access of resource without authentication and redirect the response to home page. While redirection , the response sometimes may leak the sensitive inforamtion due to logical flaw of the application





# Instructions





1.Login with the credentials provided and access *my account* .





![9f8e2f9a-7b72-4501-92d4-4c4cbe1902e7.png]()



2. Intercept the request using burp proxy tab.Observe that update password filed already contains the current password which is masked.





![7dbafac2-b65c-48c2-86d8-7e6b83f6256a.png]()





3.Change the *id *paramter value to *administrator and send the request. *





![8a57cdc1-8eb0-45fe-b5f4-588ec0d9908a.png]()



4. Observe the request is redirected  because the server didnot permit to access the resource and the response contains a password for the *administrator*.





![32ad51b0-3866-4a8d-9fa1-ec6b3a16edf9.png]()



5. Login with the password identified in the above step







![6e1bb0d9-e2bb-44d3-b4e2-129c7d8d19b6.png]()





6. Login was successful





![c869f67f-a0e9-42e2-9029-c3983c851dea.png]()



## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]



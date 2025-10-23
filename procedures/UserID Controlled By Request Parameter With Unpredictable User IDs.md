---
id: fa552cbf-10c2-49eb-b78f-85ec91fe49dc
name: UserID Controlled By Request Parameter With Unpredictable User IDs
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T08:26:35.801312+00:00'
updated_at: '2023-05-26T01:35:56.145773+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# UserID Controlled By Request Parameter With Unpredictable User IDs

**Status**: ✓ Verified

## Summary

Applications use unpredictable parameter values to tampering of the parameters. An attacker might replace the parameter id's with that of other users whch are disclosed somewhere in the application and gain unauthorised access. 

## Description

# Description

Applications use unpredictable parameter values to tampering of the parameters. An attacker might replace the parameter id's with that of other users whch are disclosed somewhere in the application and gain unauthorised access.



# Instructions







1. Navigate to the blog post by Carlos.





![d7dbd803-6128-425b-aed8-2fb4327d932e.png]()





2. Click on *Carlos *and Observe the url and identify *ID *parameter.





![e7affd65-38d3-4bce-8725-f24a2c97aba7.png]()





3.Login with the user *weiner *credentials and access *My Account* . 







![91615b09-d375-40d1-96d4-68357cbdb403.png]()



4. Intercept the request using burp proxy . Observe the ID parameter value.







![8e63488e-03f6-41d8-abec-d9d8289a633f.png]()



5. Change the id parameter value to the one from step 2 and submit the request to the server.







![40c7c2e9-dbeb-47d6-aee4-20b121a0dbce.png]()





6. Navigate to the browser window and observe that you are logged in without providing credentials.





![ed5e8bba-07a6-4d49-9d4c-fb4d525823d8.png]()



## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]



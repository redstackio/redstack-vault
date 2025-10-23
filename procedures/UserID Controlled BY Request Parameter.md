---
id: 0af1c9e6-8967-4840-abcd-5fb23eb6041b
name: UserID Controlled BY Request Parameter
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T04:28:09.969872+00:00'
updated_at: '2023-05-26T05:22:31.107584+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# UserID Controlled BY Request Parameter

**Status**: ✓ Verified

## Summary

Description Instructions 1.Log in to the account with credentials provided and acces account details 

## Description

Description





Instructions





1.Log in to the account with credentials provided and acces* account details*





![eeb41bd1-c150-4ee3-a8a5-a8209462fd5e.png]()



2. Observe that the url contains username in the *id *parameter.





![282735b3-549c-49f6-804d-bdf2f1a12969.png]()





3.Myaccount will have* APIkey of the user .*







![84d834cc-3bd7-4487-bdd1-7850f1c818a4.png]()



4. Relaod the page and capture the reuqest using burp intercept.





![16cadc3f-7c58-4e33-a1af-8aa366f8ab6b.png]()





5. Modify the *id *parameter value to *carlos *to access the account







![092aca14-95b4-45fd-9912-49ce4702c7d3.png]()





6.Observe that the apikey in the* my accoun*t details which belongs to carlos account





![e587508c-9267-4a23-beeb-db7538c3297b.png]()







## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]



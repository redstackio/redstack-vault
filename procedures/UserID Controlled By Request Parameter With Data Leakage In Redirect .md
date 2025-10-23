---
id: f6e00897-167f-491b-b25b-d4a60d76d664
name: 'UserID Controlled By Request Parameter With Data Leakage In Redirect '
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T09:30:24.864782+00:00'
updated_at: '2023-05-26T18:50:52.607662+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# UserID Controlled By Request Parameter With Data Leakage In Redirect 

**Status**: ✓ Verified

## Summary

Applications sometimes leak sensitive information through redirect response . In this case application is leaking apikey while redirecting the response. 

## Description

# Description

Applications sometimes leak sensitive information through redirect response . In this case application is leaking apikey while redirecting the response.



# Instructions





1. Login to the account with the given details(Weiner)  and access my account details . Intercept the reqeust using burp proxy tab.





![3138fd01-b904-48f9-9f65-836f2da67c40.png]()





2.Send the request to the repeater tab.





![08803f9d-391b-4c3a-aacd-5d9de407dacd.png]()



3. Change the ID parameter to *carlos and  *observe that the response redirects to the home page since the paramater value is not being accepted by the server





![95c4808e-6379-459c-9df9-a3738799e19e.png]()





4.While redirecting the request to the homepage , the response leaks sensitive data, in this case its an apikey. 







![995885f3-c813-4ddd-8e17-ea0cab01dd62.png]()



## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]



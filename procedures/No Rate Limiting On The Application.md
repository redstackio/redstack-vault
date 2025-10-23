---
id: cc26c9d0-cbf1-4c75-b5f0-f6cdf7a820dc
name: No Rate Limiting On The Application
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T16:05:02.699695+00:00'
updated_at: '2023-05-26T01:24:42.204031+00:00'
platforms:
- Web
tags:
- '[[Rate Limiting]]'
- '[[Web Applications]]'
---

# No Rate Limiting On The Application

**Status**: ✓ Verified

## Summary

Description Instructions 1. Go to the email verification feature of the application. 

## Description

Description





Instructions





1. Go to the email verification feature of the application.





![4029ca67-6e1f-4c94-afdb-ea950f66a979.png]()



2. click on* send confirmation link* with the burp intercept on and capture the request.







![f60506fc-4051-415a-be89-a615912f0e71.png]()





3.send the request to intruder and repeat it multiple times and set an arbitrary value in scope





![eb0a8ffa-335f-43ab-849e-657d3579f802.png]()







4.Set the payload options as required to start the attack and then click on *start attack. *Observe that a attack window is opened.





![6f23f117-9b8a-4f24-b059-efd6d4cad4dd.png]()





5. Observe the *200 *responses in the attacker's window. You will receive emails in vast amount as there is no rate limit.





![450dbc1b-0f97-4f70-b3fc-d3b4778f0c8b.png]()



## Platforms

- Web

## Tags

- [[Rate Limiting]]
- [[Web Applications]]



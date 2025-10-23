---
id: 4f3bea07-9f6f-4e14-8bd7-8d98c276be69
name: Insecure Deserialisation (Modify Serialised Objects)
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T17:54:49.504695+00:00'
updated_at: '2023-05-26T18:29:26.857567+00:00'
platforms:
- Web
tags:
- '[[Insecure Deserialisation]]'
- '[[Web Applications]]'
---

# Insecure Deserialisation (Modify Serialised Objects)

**Status**: ✓ Verified

## Summary

An attacker can modify the serailsed object as along as there is no validation check on the server during deserialisation which will lead to attacker having unauthorised acces to the application's resources.  Instructions 1.Log in using credentials. Browse the application while the intercept is off

## Description

# Description

An attacker can modify the serailsed object as along as there is no validation check on the server during deserialisation which will lead to attacker having unauthorised acces to the application's resources.

 

Instructions



1.Log in using credentials. Browse the application while the intercept is off. 

Notice that the post-login GET / request contains a session cookie that appears to be URL and Base64-encoded. Send this request to Burp Repeater





![ba31972c-fd67-4d2a-9164-a1c5439abff8.png](_assets/images/Mash/ba31972c-fd67-4d2a-9164-a1c5439abff8.png)







![a9ab9367-5886-41da-b639-1a1fc082526c.png]()











2. In Burp Decoder, select "Decode as" > "URL". On the cookie parameter value, select "Decode as" > "Base64" to reveal that the cookie is a serialized PHP object. 

Notice that the `admin` attribute contains `b:0`, indicating the boolean value `false`. Change this to `b:1. `

`Select *encode as base64* then select *encode as url* and copy the whole value to the clipbo`ard.







![e7552e6a-b7f7-44f0-9da1-59710b978655.png](_assets/images/Mash/e7552e6a-b7f7-44f0-9da1-59710b978655.png)





3. In the burp repeater , replace the session cookie with modified value from step 2 and send the request to the server.





![13401d38-d00d-47c0-a30d-89303f802826.png](_assets/images/Mash/13401d38-d00d-47c0-a30d-89303f802826.png)





4. Obseve that the response from step 3 contains the admin interface .





![f605e99c-4f2d-45d6-91e2-3fe68d641398.png](_assets/images/Mash/f605e99c-4f2d-45d6-91e2-3fe68d641398.png)







## Platforms

- Web

## Tags

- [[Insecure Deserialisation]]
- [[Web Applications]]



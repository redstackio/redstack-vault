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

2. In Burp Decoder, select "Decode as" > "URL". On the cookie parameter value, select "Decode as" > "Base64" to reveal that the cookie is a serialized PHP object. 

Notice that the `admin` attribute contains `b:0`, indicating the boolean value `false`. Change this to `b:1. `

`Select *encode as base64* then select *encode as url* and copy the whole value to the clipbo`ard.

3. In the burp repeater , replace the session cookie with modified value from step 2 and send the request to the server.

4. Obseve that the response from step 3 contains the admin interface .

## Platforms

- Web

## Tags

- [[Insecure Deserialisation]]
- [[Web Applications]]

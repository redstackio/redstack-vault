---
id: a1aafff6-3c98-499f-af2a-47624ca33779
name: OTP Bypass Through Response Manipulation
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T11:39:10.802616+00:00'
updated_at: '2023-05-26T01:34:52.133914+00:00'
platforms:
- Web
tags:
- '[[authentication bypass]]'
- '[[otp]]'
- '[[Web Applications]]'
---

# OTP Bypass Through Response Manipulation

**Status**: ✓ Verified

## Summary

OTP bypass can be achieved by manipulating the response of the server. 

## Description

# Description

OTP bypass can be achieved by manipulating the response of the server. 

# Instructions



1. Create an account using abc123@gmail.com, OTP Sent to abc123@gmail.com email id







![e5274f27-d284-489b-857e-ee48893187c2.png]()







2.Paste that correct OTP and Capture the Request into Burp. Now right click on the Request and click on **Do Intercept >Response To This Request and observe the response status code and body **





![34c863f7-5b00-4968-9706-53076e31c58b.png]()







3.Now again create another account victim123@gmail.com. Enter any wrong OTP and capture the request into Burp. Now right click on the Request and click on **Do Intercept >Response To This Request**.





![3e8ae009-2e7d-4fd8-8bd5-273878d7e633.png]()







4. Modify the intercepted response and replace the error message from step 3 with  empty  **{ } in the body . Replace the HTTP/1.1 400 Bad Request with *HTTP/1.1 200* Created. Observe that account has been successfully create**d.



## Platforms

- Web

## Tags

- [[authentication bypass]]
- [[otp]]
- [[Web Applications]]



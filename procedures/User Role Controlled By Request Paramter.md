---
id: cc4ca29f-dd1e-4ed1-8918-549b48d12d8b
name: User Role Controlled By Request Paramter
type: procedure
verified: false
submitted: false
created_at: '2020-08-31T18:23:18.939853+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# User Role Controlled By Request Paramter

## Summary

Few application's determine the user access rights at login with a hidden filed or parameter in a cookie . An aatacker can modify these parameter values to access unauthorised content. 

## Description

# Description

Few application's determine the user access rights at login with a hidden filed or parameter in a cookie . An aatacker can modify these parameter values to access unauthorised content.

# Instructions

1.Try to access the admin panel from the browser. Observe that the admin panel is not accessible with out credentials.

2.Navigate to the login page and intercept the request using burp . Change the cookie parameter *Admin=false* to A*dmin=true*  and submit the request.

3.Observe the response contains a 200 ok 

4. Click on admin panel and intercept the request. Modify the cookie parameter *Admin=false* to *Admin=true*

5. Observe the response with 200 ok

6. Go back to browser and observe that admin is looaded in the browser with out authentication.

## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]

---
id: 41323a3e-b961-4839-b1d2-b16e9f819c93
name: 'HTTP request smuggling CL.TE to bypass front-end security controls '
type: procedure
verified: true
submitted: true
created_at: '2020-08-12T03:34:57.581661+00:00'
updated_at: '2023-05-26T18:07:34.415693+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
---

# HTTP request smuggling CL.TE to bypass front-end security controls 

**Status**: ✓ Verified

## Summary

Descritpion In this kind of attack, front end server doesnt support Transfer-Encoding . In this case front end server doesnot grant access to admin panel.To have access to admin panel , attacker will bypass the front end security controls. Instructions 1.Intercept the request using Burp Suite and s

## Description

# Descritpion

In this kind of attack, front end server doesnt support Transfer-Encoding . In this case front end server doesnot grant access to admin panel.To have access to admin panel , attacker will bypass the front end security controls. 

# Instructions

# 

1.Intercept the request using Burp Suite and send the request to the repeater tab. Observe the response to the request .





![651ed472-85b8-4484-a8fd-2c436181b84a.jpg](_assets/images/Mash/651ed472-85b8-4484-a8fd-2c436181b84a.jpg)







2.Change the url from step1 in the repeater tab to admin to access admin panel. A 403 response can be seen denying the access to the admin panel.







![890cfa00-6aac-40b7-9a61-8ca38864a851.jpg](_assets/images/Mash/890cfa00-6aac-40b7-9a61-8ca38864a851.jpg)







3.Modify the request from step2 to the following and send the request to the server. A 401 resposne can be observed which is different to the resposne from step 2. And also in the response, observe the message *Admin interface only available if logged in as Administrator  or if requested as localhost.*





*Modified Request:*



*0*

*GET /admin HTTP/1.1*

*x-Ignore: X*





![08790a11-a011-41de-b7a1-a37573c709e5.jpg](_assets/images/Mash/08790a11-a011-41de-b7a1-a37573c709e5.jpg)







4. Modify the request from step 3 to the following to access the admin panel.



*Modified Request:*



*0*



*GET /admin HTTP/1.1*

*Host : localhost*

*x-ignore : x*





![8619ec3e-a52e-4e07-9128-7b85c418420c.jpg](_assets/images/Mash/8619ec3e-a52e-4e07-9128-7b85c418420c.jpg)







5.Send the modified request from step 4 to the server and 201 resposne can be seen . We were able to access the admin panel.





![c791a103-4dad-4e30-aa2c-c9ffd3765157.jpg](_assets/images/Mash/c791a103-4dad-4e30-aa2c-c9ffd3765157.jpg)













## Platforms

- Web

## Tags

- [[Web Applications]]



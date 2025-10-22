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

2.Change the url from step1 in the repeater tab to admin to access admin panel. A 403 response can be seen denying the access to the admin panel.

3.Modify the request from step2 to the following and send the request to the server. A 401 resposne can be observed which is different to the resposne from step 2. And also in the response, observe the message *Admin interface only available if logged in as Administrator  or if requested as localhost.*

*Modified Request:*

*0*

*GET /admin HTTP/1.1*

*x-Ignore: X*

4. Modify the request from step 3 to the following to access the admin panel.

*Modified Request:*

*0*

*GET /admin HTTP/1.1*

*Host : localhost*

*x-ignore : x*

5.Send the modified request from step 4 to the server and 201 resposne can be seen . We were able to access the admin panel.

## Platforms

- Web

## Tags

- [[Web Applications]]

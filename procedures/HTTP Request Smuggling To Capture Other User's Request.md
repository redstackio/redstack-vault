---
id: ded9ad93-25e8-434f-9fc1-d37e1b05d83f
name: HTTP Request Smuggling To Capture Other User's Request
type: procedure
verified: false
submitted: false
created_at: '2020-08-12T04:05:10.296857+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Web
tags:
- '[[http request smuggling]]'
- '[[Web Applications]]'
---

# HTTP Request Smuggling To Capture Other User's Request

## Summary

In this kind of attack, an attacker will smuggle a request to the back-end server that causes the next user's request to be stored in the application. Then attacker will retreive the next user's request and staels the victim's cookie 

## Description

# Description

In this kind of attack, an attacker will smuggle a request to the back-end server that causes the next user's request to be stored in the application. Then attacker will retreive the next user's request and staels the victim's cookie 

# Instructions

# 

1. Intercept the comment post request of the application and send it to the repeater .

2.Increase the comment-post request's Content-Lengthto 400, then smuggle it to the backend server

3.1. If the stored request is incomplete and doesn't include the Cookie header, you will need to slowly increase the value of the Content-Length header in the smuggled request, until the whole cookie is captured. 

Copy the user's cookie from the response and use it to access the victim's account.

## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[Web Applications]]

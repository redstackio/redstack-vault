---
id: 0411d32d-05b7-4a23-a3ec-4c9cd57433bf
name: HTTP Request Smuggling To Reveal Front End Request Rewriting
type: procedure
verified: true
submitted: true
created_at: '2020-08-12T03:59:14.781954+00:00'
updated_at: '2023-05-26T01:05:50.739997+00:00'
platforms:
- Web
tags:
- '[[http request smuggling]]'
- '[[Web Applications]]'
---

# HTTP Request Smuggling To Reveal Front End Request Rewriting

**Status**: ✓ Verified

## Summary

In this kind of HTTP request smuggling , an attacker will observe the response of the front end server and will make a note of the specific response headers . The specific response header from the front end server will be used to craft a request to access the backend server resources(in this case a

## Description

# Description

In this kind of HTTP request smuggling , an attacker will observe the response of the front end server and will make a note of the specific response headers . The specific response header from the front end server will be used to craft a request to access the backend server resources(in this case admin panel).



# Instructions

# 

1. Intercept the search request of the application and send it to the repeater tab.





![11e63908-db6d-4096-a9fa-8d1da2cab9a9.jpg](_assets/images/Mash/11e63908-db6d-4096-a9fa-8d1da2cab9a9.jpg)







2. Add the following request to the request in step 1 and send the request to the server (step 3).









**Code**: [[0
POST /  HTTP/1.1
Content-Type: application/x-w]]







3. Observe the response with* x-bkdpqI-Ip* parameter .



![4ad83972-a107-4e66-a1d7-63b53430ed17.png](_assets/images/Mash/4ad83972-a107-4e66-a1d7-63b53430ed17.png)





3.Observe the response parameter in step 2 to rewrite the request to access the admin panel. 







**Code**: [[0
GET /admin /  HTTP/1.1
x-BkdpqI_Ip: 127.0.0.1]]









4.send the modified request with the rewritten request to the server to get the admin panel.







![d928704a-7014-4988-a92b-488c4a3a7f61.jpg](_assets/images/Mash/d928704a-7014-4988-a92b-488c4a3a7f61.jpg)















## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[Web Applications]]



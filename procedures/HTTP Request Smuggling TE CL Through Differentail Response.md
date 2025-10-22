---
id: 4dafeb20-e9cf-40b3-99bf-71fe47b59892
name: HTTP Request Smuggling TE CL Through Differentail Response
type: procedure
verified: true
submitted: true
created_at: '2020-08-12T03:25:11.780980+00:00'
updated_at: '2023-05-26T18:18:54.413257+00:00'
platforms:
- Web
tags:
- '[[http request smuggling]]'
- '[[Web Applications]]'
---

# HTTP Request Smuggling TE CL Through Differentail Response

**Status**: ✓ Verified

## Summary

In this type of Request Smuggling attack, an attacker will try to craft a  TE CL request. If the request gets parsed by the application ,a differential response can be observed. 

## Description

# Description

In this type of Request Smuggling attack, an attacker will try to craft a  TE CL request. If the request gets parsed by the application ,a differential response can be observed.

# Instructions

# 

# 

1. Intercept the request and send it to the repeater tab.

2. Modify the request in the repeater tab to the following. Observe the POST 404 request .

**Code**: [[POST / HTTP/1.1
Host: your-lab-id.web-security-ac]]

3. Send the modified request to the application server and observe the response.

## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[Web Applications]]

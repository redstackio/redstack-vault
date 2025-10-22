---
id: d2ffa842-1be8-456e-a996-e6d6188c9e44
name: Web Cache Posioning Via Unkeyed Query String
type: procedure
verified: true
submitted: true
created_at: '2020-09-04T16:27:27.468017+00:00'
updated_at: '2023-05-26T18:17:49.324459+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
- '[[web cache posioning]]'
---

# Web Cache Posioning Via Unkeyed Query String

**Status**: ✓ Verified

## Summary

Descritpion In this kind of attack, an attacker will craft a malicious url and induce the victim to click on the url. Once clicked , malicious JS code gets executed on the victim's machine.This kind of attack will have more impact more users of the application with out attacker having to interact. 

## Description

# Descritpion

In this kind of attack, an attacker will craft a malicious url and induce the victim to click on the url. Once clicked , malicious JS code gets executed on the victim's machine.This kind of attack will have more impact more users of the application with out attacker having to interact.

# Instructions

1.With burp running and proxying requests, browse through the application. Identify home page request from the HTTP history tab under proxy and send the reqeust to the the repeater tab.

2.Add parameters to the request url and send the request to the server. Notice the *X*-*cache hit *in the response headers which indicate that the parameters are not included in the cache key

3.Add the origin header to the request and observe the response. Origin header acts as a cache buster.

4.Modify the parameters in the url from step 2 to add the payload as below. Keep sending the request to the server until the payload is relfected in the response. Once the cache is poisoned , remove the query parameters from the request and send the request to the server . Notice that cached response containing payload can be seen in the response tab.

*`/?evil='/><script>alert(1)</script*>`

5.

## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web cache posioning]]

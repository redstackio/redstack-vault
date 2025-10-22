---
id: 8aed1e11-39cf-4843-a85a-d8d380b7b46f
name: Parameter Cloaking
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T19:29:20.393805+00:00'
updated_at: '2023-05-26T18:26:37.062338+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
---

# Parameter Cloaking

**Status**: ✓ Verified

## Summary

Cloaking allows an attacker to use paramters arbitarily in the application's logic. There might be the differences on how cache and the application parses the parameters. This will allow attacker to trick the cache to execute arbitary code through excluded parameters by an application. 

## Description

# Description

Cloaking allows an attacker to use paramters arbitarily in the application's logic. There might be the differences on how cache and the application parses the parameters. This will allow attacker to trick the cache to execute arbitary code through excluded parameters by an application.

# Instructions

1.  From HTTP History identify the below request and send it to the repeater tab.

2.If we append another parameter *test=1234* with a semicolon to already existing parameter utm_content , the cache is treating it as single parameter as it can be observed in the response.

3.identify the *`/js/geolocate.js?callback=setCountryCooki*e from the HTTP history tab and send the request to the repeater tab`

4. *callback* parameter can be controlled by an attacker. Observe the parameter value gets reflected in the response.

5.Modify the url in the following way. Observe two *callback *parameters. But only the last *callback* parameter value is reflected in the response.

*`GET /js/geolocate.js?callback=setCountryCookie&utm_content=1234;callback=myFunctio*n`

6. Now, modify the second callback parameter to trigger alert . Observe the response contains alert(1) which when loaded in the browser gets executed. Replay the request to keep the cache poisoned for the subsequent victim.If the victim access the resource url , it will trigger the alert().

*`GET /js/geolocate.js?callback=setCountryCookie&utm_content=foo;callback=alert(1*)`

## Platforms

- Web

## Tags

- [[Web Applications]]

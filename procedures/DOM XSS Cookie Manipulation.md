---
id: da094ea0-4025-41f8-862b-c373316efec1
name: DOM XSS Cookie Manipulation
type: procedure
verified: true
submitted: true
created_at: '2020-08-07T15:03:08.156147+00:00'
updated_at: '2023-05-26T01:26:00.287899+00:00'
platforms:
- Web
tags:
- '[[cookie manipulation]]'
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# DOM XSS Cookie Manipulation

**Status**: ✓ Verified

## Summary

An attacker exploits the cookie when the javascript of the application writes data from a source into document.cookie without sanitizing the input. An attacker may be able to craft a url and deliver it to victim when clicked by the victim will set an attacker controlled data in the victim's cookie.

## Description

# Description

An attacker exploits the cookie when the javascript of the application writes data from a source into *document.cookie* without sanitizing the input. An attacker may be able to craft a url and deliver it to victim when clicked by the victim will set an attacker controlled data in the victim's cookie.



# Instructions

# 

1. Navigate to any of the products on the following e-commerce application.  Use chrome extension* cookie editor* to observe the cookies in the application.Under cookie editor , a *lastviewproduct *cookie with value being url of the last view product can be observed.







![93a8b615-07bc-496f-9995-1f592bed51ff.PNG]()





2. Craft a url as shown below and send it to the victim through social engineering means.



*payload :*







**Code**: [[
<iframe src="https://aca71fbe1fd30d7180c004e800d]]







3. When the victim clicks on the url , the browser opens the malious url and then saves the url in the* lastviewedproduct* cookie. The *onload  *event present in the payload from step 2 will then immediately redirect the victim to the homepage of the application. 









![fd7f5c63-61f2-40e0-9462-7fd954e045c5.PNG]()



## Platforms

- Web

## Tags

- [[cookie manipulation]]
- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]



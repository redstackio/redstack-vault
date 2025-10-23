---
id: b104bb3a-2855-4894-99d3-e557dc6abe12
name: Third party Information Disclosure Through Error Message
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T15:48:31.313898+00:00'
updated_at: '2023-05-26T18:18:05.854995+00:00'
platforms:
- Web
tags:
- '[[information disclosure]]'
- '[[injection]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Third party Information Disclosure Through Error Message

**Status**: ✓ Verified

## Summary

Sensitive Information of an application that is disclosed will let an attacker to further his attacks on the application . In this case , a thirdparty framework information is disclosed . 

## Description

# Description

Sensitive Information of an application that is disclosed will let an attacker to further his attacks on the application . In this case , a thirdparty framework information is disclosed .

# Instructions

# 

1. Observe different items present in the page . Try to access any of the items in the page . 









![46f5487a-1498-4ace-bada-4b4fff0bddd7.PNG]()



2.A *productid  *parameter can be observed with* numeric *value. Change the numeric value to string.









![2bce3e43-ac8e-43af-912c-db1f541ef9c7.PNG]()







3..Change the *id *parameter value to string . An error can observed in the response which shows* apache struts* being used along with its version displayed.







![d355e28b-384f-4255-b0a7-9221e0c909b6.PNG]()











## Platforms

- Web

## Tags

- [[information disclosure]]
- [[injection]]
- [[owasp top 10]]
- [[Web Applications]]



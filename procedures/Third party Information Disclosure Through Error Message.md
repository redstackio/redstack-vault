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

2.A *productid  *parameter can be observed with* numeric *value. Change the numeric value to string.

3..Change the *id *parameter value to string . An error can observed in the response which shows* apache struts* being used along with its version displayed.

## Platforms

- Web

## Tags

- [[information disclosure]]
- [[injection]]
- [[owasp top 10]]
- [[Web Applications]]

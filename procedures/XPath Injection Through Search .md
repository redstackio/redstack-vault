---
id: f2d65daa-f252-42c5-abe2-34ad50700ab0
name: 'XPath Injection Through Search '
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T16:17:37.677420+00:00'
updated_at: '2023-05-26T01:26:27.854062+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xml]]'
---

# XPath Injection Through Search 

**Status**: ✓ Verified

## Summary

An attacker will craft an XML query through XPath to maliciously exfilitrate the sensitive information from application's server . 

## Description

# Description

 An attacker will craft an XML query through XPath to maliciously exfilitrate the sensitive information from application's server .

# 

# Instructions

# 

1.Observe the url with two parameters with user controlled data. 

2.Try to generate an error message to enumerate the application's server information through injecting *single quote *after the* action *in url.

3.An error message can be observed in the response page which reveals Xpath being in use for querying data.

4. Construct a XML query through XPath to reveal password information from backend files and insert in the url aas shown below .

*Payload  :  ')]/password | a[contains(a,'*

5. Submitting the request with* payload w*ill reveal sensitive information.* *

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xml]]

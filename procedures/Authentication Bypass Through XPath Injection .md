---
id: 4dc86340-342b-4018-b8a5-3e48cf93cbe4
name: 'Authentication Bypass Through XPath Injection '
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T15:48:34.879652+00:00'
updated_at: '2023-05-26T15:59:03.892256+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[XPath Injection]]'
---

# Authentication Bypass Through XPath Injection 

**Status**: ✓ Verified

## Summary

XML querying is done through Xpath, that allows the XML query to locate the information. An attacker can craft the Xpath query to  bypass the authenticaion mechanism if the underlying authentication is through XML. 

## Description

# Description

XML querying is done through Xpath, that allows the XML query to locate the information. An attacker can craft the Xpath query to  bypass the authenticaion mechanism if the underlying authentication is through XML.

# Instructions

1.Insert a *single quote * to test the login form for error message

2. Upon submitting the request with *single quote, a*n error message can be observed  which will validate the usage of XPath .

3. After confirming that XPath being used for authentication on server side , try the following *payloads* in the login form.

*payloads*

*' or '1'='1*

*' or ''='*

*x' or 1=1 or 'x'='y*

4. As it can be observed , an attacker was able to bypass the authentication mechanism implemented through XML.

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[XPath Injection]]

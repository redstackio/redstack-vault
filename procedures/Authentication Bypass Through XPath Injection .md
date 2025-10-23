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







![a4dfc1a9-d58e-4ff7-a647-a81960838c66.PNG](_assets/images/Mash/a4dfc1a9-d58e-4ff7-a647-a81960838c66.PNG)





2. Upon submitting the request with *single quote, a*n error message can be observed  which will validate the usage of XPath .







![bc95b3cb-8f71-4a00-95cf-5c9e089c790a.PNG](_assets/images/Mash/bc95b3cb-8f71-4a00-95cf-5c9e089c790a.PNG)





3. After confirming that XPath being used for authentication on server side , try the following *payloads* in the login form.



*payloads*

*' or '1'='1*

*' or ''='*

*x' or 1=1 or 'x'='y*





![3cbe4daf-8535-4561-b133-b95f304e91ef.PNG](_assets/images/Mash/3cbe4daf-8535-4561-b133-b95f304e91ef.PNG)



4. As it can be observed , an attacker was able to bypass the authentication mechanism implemented through XML.





![de27748a-a0e3-4006-80fc-224f706a2e49.PNG](_assets/images/Mash/de27748a-a0e3-4006-80fc-224f706a2e49.PNG)





## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[XPath Injection]]



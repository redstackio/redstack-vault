---
id: e269fadf-0e12-40ab-b0bd-ec4a904bf7b5
name: DOMXSS Using Web messages & JavaScript URL
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T14:51:46.620302+00:00'
updated_at: '2023-05-26T01:22:32.207771+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# DOMXSS Using Web messages & JavaScript URL

**Status**: ✓ Verified

## Summary

DOM based XSS vulnerabilty can be triggered through web messages and csn be exploited via JavaScript url. 

## Description

# Description

DOM based XSS vulnerabilty can be triggered through web messages and csn be exploited via JavaScript url.

# Instructions

1. Access the application and right click on the below page . Select *view page source *

2.Observe that the source code contains a event listener which listens web messages. Observe that it also contains* location.href.*

3.Craft a malicious payload in the similar way as below

**Code**: [[
<iframe src="https://acb11f271e33403880064a21005]]

4.Observe that the response contains a alert popup triggered by the above payload.

## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]

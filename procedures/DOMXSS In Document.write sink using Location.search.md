---
id: b77a13c7-6d53-44c6-9078-e3a2ac00c9a3
name: DOMXSS In Document.write sink using Location.search
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T07:04:48.559617+00:00'
updated_at: '2023-05-26T18:30:17.805758+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[Web Applications]]'
---

# DOMXSS In Document.write sink using Location.search

**Status**: ✓ Verified

## Summary

document.write function writes data out to the page. Location.search under document.write can be exploited by an attacker to execute the malicious javascript code. 

## Description

# Description

*document.write* function writes data out to the page. *Location.search* under *document.write* can be exploited by an attacker to execute the malicious javascript code.

# Instructions

1.Enter some random alpha numeric string in the search box as shown.

2. Right click on the page and select *view page source* and observe that the random string has been placed inside the* img src* attribute

3. Append "> to the alpha numeric string 

4. Observe the response displays "> which indicates break out of the* img src* attribute.

5.Use the following payload in the search box

* "><svgonload=alert(1)>*

6. The payload from above step gets executed and a alert can be seen in the response

## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[Web Applications]]

---
id: b4f8654b-a660-4080-8afa-dabf0b4b67c3
name: Reflected XSS With Some SVG Markup Allowed
type: procedure
verified: true
submitted: true
created_at: '2020-08-26T18:35:39.262667+00:00'
updated_at: '2023-05-26T18:21:16.145856+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS With Some SVG Markup Allowed

**Status**: ✓ Verified

## Summary

Some applications may block common tags . An attacker can bypass this blockage by use SVG tags and events to execute malicious javascript code. 

## Description

# Description

Some applications may block common tags . An attacker can bypass this blockage by use SVG tags and events to execute malicious javascript code.

# Instructions

1.Enter the following XSS payload and click on search.

* `<img src=1 onerror=alert(1)*>`

2.Observe that the payload gets blocked by the server. 

3.With burp running and proxying requests through the browser , intercept the search functionality of the application. Send the request to the intruder tab.

4.Under *intruder *tab, *positions *tab select the *search *term and click on add to add the search value to the parameter position

5.  Use the XSS cheatsheet from the below link and click on *copytags to clipboard t*o copy all the payloads* . F*

[*https://portswigger.net/web-security/cross-site-scripting/cheat-shee](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)t*

6.From the burp *intruder *tab, in the *payloads *tab click *paste *to paste list of tags into the payload list and then click on *start attack* 

7.Once the attack is done, observe the responses for all the payloads. Observe that for except *discard *payload response status code is 400. *Discard* payload response has 200 status code indicating that the tag is allowed.

8.Now go back to intruder tab and replace the search term value with *<svg><discard%20=1>* and click on add to add the payload position.

9. Using XSS cheatsheet from step 5 , click on *copy attributes to clipboard* to copy the attributes and paste it in the payloads tab. Click on s*tart attack .*

10. Observe that all responses have 400 status code except for  *onbegin *attribute payload 

11. Craft the Javascript payload with attribute tags discard and attribute onbegin in the following way and url encode the payload .

*%22%3E%3Csvg%3E%3Cdiscard%20onbegin=alert(1)%3E*

*Load the following url in the browser and observe that a alert is poped out in the response page of the application.*

[*https://your-lab-id.web-security-academy.net/?search=%22%3E%3Csvg%3E%3Cdiscard%20onbegin=alert(1)%3](https://your-lab-id.web-security-academy.net/?search=%22%3E%3Csvg%3E%3Cdiscard%20onbegin=alert(1)%3E)E*

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]

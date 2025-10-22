---
id: e199c13c-0b29-43fa-8547-fe95f7b8a224
name: Reflected XSS in Canonical Link Tag
type: procedure
verified: true
submitted: true
created_at: '2020-08-26T16:44:02.778198+00:00'
updated_at: '2023-05-26T15:56:28.075425+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS in Canonical Link Tag

**Status**: ✓ Verified

## Summary

Canonical tags are included in the HTML code to indicate the original source of content. 

## Description

# Description

Canonical tags are included in the HTML code to indicate the original source of content.

# Instructions

1. Navigate to the comment section of the application.

2. Right click on the page and select view page source . Observe that the string from the comment section is reflected inside an anchor *href *attribute.

3. Now craft a payload to trigger an alert using keyboard. Encode the payload in URL format . This sets the X key as an access key for the whole page. When a user presses the access key, the alert function is called.

*Payload : 'accesskey='x'onclick='alert(1)*

4.Load the following url in the browser.

[*https://your-lab-id.web-security-academy.net/?%27accesskey=%27x%27onclick=%27alert(1](https://your-lab-id.web-security-academy.net/?%27accesskey=%27x%27onclick=%27alert(1)))*

5.1. To trigger the exploit on yourself, press one of the following key combinations:

*On Windows: ALT+SHIFT+X*

*On MacOS: CTRL+ALT+X*

*On Linux: Alt+X*

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]

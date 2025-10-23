---
id: 5564aa0f-ec14-465c-8fc1-b3b7b7022b5f
name: Reflected XSS With Custom Tags(All Other tags Blocked)
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T09:45:04.773041+00:00'
updated_at: '2023-05-26T01:28:22.475157+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS With Custom Tags(All Other tags Blocked)

**Status**: ✓ Verified

## Summary

Some of the web applications blocks all the tags to prevent the malicious execution of JavaScript code. Custom tags can be used to bypass this restriction on the applications to execute JS code. 

## Description

# Description

Some of the web applications blocks all the tags to prevent the malicious execution of JavaScript code. Custom tags can be used to bypass this restriction on the applications to execute JS code.

# Instructions



1. Post a comment with a random alphanumeric string in the "Website" input and click on *search.*







![5e87bc80-fb00-4e59-ad9a-1d86ee7820c0.png]()





2. Right click on the page and select* view page source* and search for the string entered in above step.





![d8f1c5a3-4fd2-4842-b193-dde4d22a2dbd.png]()





3.Craft a standard XSS payload and enter it in the search box. 

*<script>alert(1)</script>*



![63f921e7-d6a4-47ce-bc37-0b1bad6a7baf.png]()





4.Observe that the tag is blocked and the execution of payload is prevented.







![be520524-0734-46eb-92c4-58eb3d2b715c.png]()





5.The folowing code triggers an *onfocus* event handler which in turn triggers the *alert *function.







**Code**: [[<script>
location = 'https://your-lab-id.web-secu]]





6. Craft a exploit using the JS code from the above step and access the exploit in the payload in the browser to observe the alert popup.

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]



---
id: 63b427ee-c687-4853-9c92-c1251790ad45
name: Stored DOM XSS
type: procedure
verified: true
submitted: true
created_at: '2020-08-05T14:55:04.907320+00:00'
updated_at: '2023-05-26T01:06:02.982736+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Stored DOM XSS

**Status**: ✓ Verified

## Summary

In stored DOM XSS , response is served in a different page rather than the same page as payload.The server stores the payload and  serves the payload to all the users of application who visits the page. 

## Description

# Description

In stored DOM XSS , response is served in a different page rather than the same page as *payload.*The server stores the* payload and  *serves the *payload *to all the users of application who visits the page.

# Instructions

1.  Insert the *payload* into comment section as shown below.

*Payload : *<img src=1 onerror=alert(1)>

2. As it can be observed in the response , the* payload *doesnt get executed by the application.  The angle brackets gets encoded by the application.

3. Change the *Payload *by adding open and close brackets before the *payload.*

*Modified Payload:<>*<img src=1 onerror=alert(1)>

4.The comment gets submitted successfully.

5. Go back to blog to access the comment section of the blog.

6. The *Payload* gets stored in the comment section of the blog. Whoever visits the page the *Payload* gets executed.

## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]

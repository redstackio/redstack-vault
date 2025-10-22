---
id: 4859e3fe-9930-4779-b9e0-63f554ea261b
name: 'Stored XSS To Capture Passwords Using Burp Collaborator '
type: procedure
verified: true
submitted: true
created_at: '2020-08-05T18:13:46.432602+00:00'
updated_at: '2023-05-26T01:30:22.636048+00:00'
platforms:
- Web
tags:
- '[[Burp]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Stored XSS]]'
- '[[Web Applications]]'
---

# Stored XSS To Capture Passwords Using Burp Collaborator 

**Status**: ✓ Verified

## Summary

This kind of attack technique will give access to every other account on the application to the attacker. A victim's password/sensitive info will be sent to attacker's domain that was created using burp collaborator which is available for users having Burp Suite Professional edition. 

## Description

# Description

This kind of attack technique will give access to every other account on the application to the attacker. A victim's password/sensitive info will be sent to attacker's domain that was created using burp collaborator which is available for users having Burp Suite Professional edition.

# 

# Instructions

# 

# 

1. Open the Burp Suite  Professional version. Under burp menu, click on *burp collaborator client .*

2.Insert the *payload *into comment section of the blog.

*Payload*:

**Code**: [[<input name=username id=username>
<input type=pas]]

3. Any user who visits the comment section of the blog get their credentials sent to attacker through the *burp collaborator* client . Comment that is submitted in step 2 can be seen in comment section.

4.In burp collaborator window, check for *http type requests . I*f you dont see any  requests* click on poll now* and wait for few seconds to observe the *HTTP request*

5. In Burp collaborator window Under *request to collaborator,* observe the username and password.

6. Login into the application with credentials from step 5.

7. With credentials obtained through burp collaborator, you can successfully login as *administrator*

## Platforms

- Web

## Tags

- [[Burp]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Stored XSS]]
- [[Web Applications]]

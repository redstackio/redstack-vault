---
id: fecdd907-c237-465a-81a7-490308997bc6
name: Stored XSS Onclick Where <> & " HTML Encoded And ' and \ Escaped
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T11:31:07.939575+00:00'
updated_at: '2023-05-26T01:31:16.552313+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Stored XSS]]'
- '[[Web Applications]]'
---

# Stored XSS Onclick Where <> & " HTML Encoded And ' and \ Escaped

**Status**: ✓ Verified

## Summary

Descritpion Applications encode few strings and escape few strings to prevent the execution of JavaScript by an attacker. Instructions 1. Navigate to comment section of the application and enter the details as shown below. 

## Description

Descritpion

Applications encode few strings and escape few strings to prevent the execution of JavaScript by an attacker.

Instructions

1. Navigate to comment section of the application and enter the details as shown below.

2.Observe that the random string has been reflected inside an `onclick` event handler attribute by going to view source code.

3. Modify the comment to inect a malicious JavaScript url to trigger a alert popup.

[*http://foo?&apos;-alert(1)-&apo](http://foo/?&apos;-alert(1)-&apos)s`*;`

4. Navigate to the comment section and click on* Hi admin* comment.Observe that a alert popup has been triggered by the payload.

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Stored XSS]]
- [[Web Applications]]

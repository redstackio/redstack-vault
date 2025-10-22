---
id: af6da4b0-deb1-4158-b59c-18b60e6d7e70
name: Stored XSS href Attribute & Double quotes HTML Encoded
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T10:48:07.947143+00:00'
updated_at: '2023-05-26T18:18:24.650583+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Stored XSS]]'
- '[[Web Applications]]'
---

# Stored XSS href Attribute & Double quotes HTML Encoded

**Status**: ✓ Verified

## Summary

Description Some applications will HTML encode the href attribute and double quotes to prevent the execution of JavaScript code. Instructions 1. Navigate to the comment section of the blog and enter details as below. 

## Description

Description

Some applications will HTML encode the href attribute and double quotes to prevent the execution of JavaScript code. 

Instructions

1. Navigate to the comment section of the blog and enter details as below.

2.Observe that the search term has been reflected inside an anchor href attribute.

3. Enter the following payload in the comment box and post the comment.

*`javascript:alert(1*)`

4.Naviage to the comment section and observe the comment with *hello hackers. *Click on* hello hackers *to view the comment. Observe that the alert popup is triggered 

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Stored XSS]]
- [[Web Applications]]

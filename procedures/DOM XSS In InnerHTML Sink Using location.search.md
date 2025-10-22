---
id: a2656929-20d1-45a0-9985-7cae6491f22e
name: DOM XSS In InnerHTML Sink Using location.search
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T07:39:15.560499+00:00'
updated_at: '2023-05-26T18:11:44.221162+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# DOM XSS In InnerHTML Sink Using location.search

**Status**: ✓ Verified

## Summary

innerHTML is part of DOM that allows javascript code to manipulate the application's page. 

## Description

# Description

innerHTML is part of DOM that allows javascript code to manipulate the application's page.

# Instructions

1. Enter random  string in the search box

2.Search the random string in the *page source *using search option. Observe that the search does not show the *string *entered in the search box from step1

3. Observe that the JS uses* innerHTML* script in the page source

4. Enter the payload *<img src=1 onerror=alert(1)> . *The payload changes the* HTML *contents of a div element  using data from* location.search.*

5. Observe that the a alert popup can be seen in the applciation

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]

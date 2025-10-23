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





![bdb1422d-eed1-4eae-a5a0-f566e6f6efa0.png]()







2.Search the random string in the *page source *using search option. Observe that the search does not show the *string *entered in the search box from step1







![e9c7c271-c326-44c1-ba71-c0da17a853c1.png]()





3. Observe that the JS uses* innerHTML* script in the page source







![461f73e6-3a09-4946-8d7b-9d519048db1e.png]()





4. Enter the payload *<img src=1 onerror=alert(1)> . *The payload changes the* HTML *contents of a div element  using data from* location.search.*







![ff464d7f-56c3-4ce9-8fb3-2a3a8b742a30.png]()





5. Observe that the a alert popup can be seen in the applciation





![5e5b7ea2-24ad-4a7d-8410-1347da7cfe42.png]()



## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]



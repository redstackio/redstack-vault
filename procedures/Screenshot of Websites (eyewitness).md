---
id: c88f4634-8840-49d1-8a5e-33f034018e75
name: Screenshot of Websites (eyewitness)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:37.872816+00:00'
updated_at: '2023-05-26T18:30:44.248609+00:00'
commands:
- '[[eyewiness screenshot a list of URL''s]]'
- '[[eyewitness screenshot a single url]]'
---

# Screenshot of Websites (eyewitness)

**Status**: ✓ Verified

## Summary

Eyewitness is capable of parsing a large list of http servers and taking screenshots using a headless selenium browser. Use this tool to capture screenshots from a list of URL's. 

## Description

# Description

Eyewitness is capable of parsing a large list of http servers and taking screenshots using a headless selenium browser.

Use this tool to capture screenshots from a list of URL's.

##  Instructions

1. Use eye witness to capture a screenshot of a single URL



**Command** ([[eyewitness screenshot a single url]]):

```bash
eyewitness --web --single https://redstack.io

```





2. (Optional) If you have a text file of URL's from a tool like httprobe try this.



**Command** ([[eyewiness screenshot a list of URL's]]):

```bash
eyewitness --web -f http.txt

```





## Commands Used

- [[eyewiness screenshot a list of URL's]]
- [[eyewitness screenshot a single url]]



---
id: 76f1cd51-8b65-4328-8ee3-882ad61e94f1
name: Session Fixation
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T14:09:37.643261+00:00'
updated_at: '2023-05-26T18:37:59.803174+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Session Fixation]]'
- '[[Session Management]]'
- '[[Web Applications]]'
---

# Session Fixation

**Status**: ✓ Verified

## Summary

Session fixation can be performed by setting the session identifier in the browser by using a crafted URL. Application continues to use the fixed session identifier even after authentication. 

## Description

# Description

Session fixation can be performed by setting the session identifier in the browser by using a crafted URL. Application continues to use the fixed session identifier even after authentication.

# 

# Instructions

# 

1. Access the application and observe in cookie editor that there are not cookies set





![229e16bb-1eea-4dfb-8432-ea1115a0b0f9.png](_assets/images/Mash/229e16bb-1eea-4dfb-8432-ea1115a0b0f9.png)







2. Craft a URL to fix the session identifier in the browser as shown in the below screenshot







![d2eb4c73-9087-443a-bb42-3586405ad20d.png](_assets/images/Mash/d2eb4c73-9087-443a-bb42-3586405ad20d.png)





3. Login into the application and observe that the session identifier is not modified





![92909fde-f72a-40ed-8bbd-1a780d3a6e93.png](_assets/images/Mash/92909fde-f72a-40ed-8bbd-1a780d3a6e93.png)















## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Session Fixation]]
- [[Session Management]]
- [[Web Applications]]



---
id: aba1bc36-5e59-4edb-96a5-2bc95f7acff8
name: Sensitive Information Disclosure - Browser Back Button
type: procedure
verified: true
submitted: true
created_at: '2020-08-16T19:28:10.366683+00:00'
updated_at: '2023-05-26T18:30:29.466582+00:00'
platforms:
- Web
tags:
- '[[information disclosure]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Sensitive Information Disclosure - Browser Back Button

**Status**: ✓ Verified

## Summary

If the application is caching the pages and logout mechanism is not implemented properly, last visited page with all the details can be viewed by clicking on the back button in the browser. 

## Description

# Description



If the application is caching the pages and logout mechanism is not implemented properly, last visited page with all the details can be viewed by clicking on the back button in the browser.



# Procedure



1. Login into the application and access any page with sensitive information





![acab807a-936a-4d41-8343-323e3b09abd1.png](_assets/images/Mash/acab807a-936a-4d41-8343-323e3b09abd1.png)





2. Click on Logout and observe that no session information is present in the browser. Session information can be observed by using cookie editor as shown in the below screenshot.





![c63f24c1-997c-4a2a-8345-ffc6f5f6ca5b.png](_assets/images/Mash/c63f24c1-997c-4a2a-8345-ffc6f5f6ca5b.png)





3. Click on the back button and observe that the last visited page is loaded with details in it.





![6a61250e-c34f-40e4-84ce-fe5893f56657.png]()







## Platforms

- Web

## Tags

- [[information disclosure]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]



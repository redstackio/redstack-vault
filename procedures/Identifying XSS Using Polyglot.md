---
id: fee2febf-967e-4f5d-a47b-81a5b8080c51
name: Identifying XSS Using Polyglot
type: procedure
verified: true
submitted: true
created_at: '2020-09-07T06:38:29.093745+00:00'
updated_at: '2023-05-26T01:11:04.704917+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Polyglot]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# Identifying XSS Using Polyglot

**Status**: ✓ Verified

## Summary

XSS (cross-site scripting) can be performed by inserting javascript payloads through user input fields. Identifying XSS would consume lot of time as it needs a number of payloads to be inserted in the input fields. Polyglot payload will help in identifying XSS quickly as it has got various injectio

## Description

# Description

XSS (cross-site scripting) can be performed by inserting javascript payloads through user input fields. Identifying XSS would consume lot of time as it needs a number of payloads to be inserted in the input fields. Polyglot payload will help in identifying XSS quickly as it has got various injection contexts.



# Procedure



1. Identify any user input field in the application. 





![a2f73f28-151b-4ede-9786-3ef31819d9c5.png](_assets/images/Mash/a2f73f28-151b-4ede-9786-3ef31819d9c5.png)





2. Insert the below polyglot in the search field and click on search.



```
*jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e*
```



![3c968465-8f6b-4c53-b506-621fa1933953.png](_assets/images/Mash/3c968465-8f6b-4c53-b506-621fa1933953.png)



3. After clicking on search, observe that the payload gets executed and an alert box is shown in the browser.





![0a0912e5-3d49-49f6-9ad8-972e43a6d4d1.png](_assets/images/Mash/0a0912e5-3d49-49f6-9ad8-972e43a6d4d1.png)







## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Polyglot]]
- [[Web Applications]]
- [[xss]]



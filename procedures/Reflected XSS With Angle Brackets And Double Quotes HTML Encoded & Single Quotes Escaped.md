---
id: 50160d32-16f6-4c36-980e-9c84344e0d7c
name: Reflected XSS With Angle Brackets And Double Quotes HTML Encoded & Single Quotes
  Escaped
type: procedure
verified: true
submitted: true
created_at: '2020-08-26T17:40:53.986734+00:00'
updated_at: '2023-05-26T15:54:46.452082+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS With Angle Brackets And Double Quotes HTML Encoded & Single Quotes Escaped

**Status**: ✓ Verified

## Summary

Descritpion Application functionality or application's WAF will try to prevent user input from breaking out of JS string by encoding single quote. An attacker can bypass this by using backslah instead of single quote to craft a JavaScript load. Instructions 1. Submit a random alpha numeric string i

## Description

# Descritpion

Application functionality or application's WAF will try to prevent user input from breaking out of JS string by encoding single quote. An attacker can bypass this by using backslah instead of single quote to craft a JavaScript load.



# Instructions



1. Submit a random alpha numeric string in the searh box







![13a6be3c-84ea-4ac6-9e7a-983890d06742.png](_assets/images/Mash/13a6be3c-84ea-4ac6-9e7a-983890d06742.png)



2.Observe that the random string has been reflected inside a JavaScript string





![09da050b-75b9-488d-bc28-de5dff8cca47.png](_assets/images/Mash/09da050b-75b9-488d-bc28-de5dff8cca47.png)





3. Insert the* test'payload *in the search box . Use chrome developer tools to identify the payload in the JS response . 



![01f69e51-e34d-413b-a090-f8bedd52b7ee.png](_assets/images/Mash/01f69e51-e34d-413b-a090-f8bedd52b7ee.png)





4.Observe that single quote gets backslash-escaped, preventing from breaking out of the string







![25015e36-3ced-4716-ad8d-bae96dbb7271.png](_assets/images/Mash/25015e36-3ced-4716-ad8d-bae96dbb7271.png)





5. Replace the payload from above step to *`\'-alert(1)/*/ and click on *search`*.





![5970e908-bf75-4ef7-9390-9c399a3510b4.png](_assets/images/Mash/5970e908-bf75-4ef7-9390-9c399a3510b4.png)





6. A alert popup can be seen in the response of the page.







![490ed02b-6199-4ea8-a72c-6fe4bcbf8a6b.png](_assets/images/Mash/490ed02b-6199-4ea8-a72c-6fe4bcbf8a6b.png)



## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]



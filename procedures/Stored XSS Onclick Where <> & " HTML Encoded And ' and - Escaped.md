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





![425c8d0f-844c-428d-9fea-8cf14580e6d9.png](_assets/images/Mash/425c8d0f-844c-428d-9fea-8cf14580e6d9.png)





2.Observe that the random string has been reflected inside an `onclick` event handler attribute by going to view source code.





![a503e34b-bff6-4baa-b19a-c8cef0797a48.png](_assets/images/Mash/a503e34b-bff6-4baa-b19a-c8cef0797a48.png)





3. Modify the comment to inect a malicious JavaScript url to trigger a alert popup.



[*http://foo?&apos;-alert(1)-&apo](http://foo/?&apos;-alert(1)-&apos)s`*;`



![199d414f-33ec-42ab-91a1-e87eefe3bb6b.png](_assets/images/Mash/199d414f-33ec-42ab-91a1-e87eefe3bb6b.png)





4. Navigate to the comment section and click on* Hi admin* comment.Observe that a alert popup has been triggered by the payload.





![69cf940a-83e6-4d67-bd2c-f87bf057db2a.png](_assets/images/Mash/69cf940a-83e6-4d67-bd2c-f87bf057db2a.png)



## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Stored XSS]]
- [[Web Applications]]



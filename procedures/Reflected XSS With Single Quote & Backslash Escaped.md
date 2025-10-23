---
id: 5c3e62b1-d76c-4d50-bc5e-0c1e61a7f4c2
name: Reflected XSS With Single Quote & Backslash Escaped
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T11:44:22.456050+00:00'
updated_at: '2023-05-26T18:25:43.673947+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS With Single Quote & Backslash Escaped

**Status**: ✓ Verified

## Summary

Descritpion Instructions 1. Navigate to the search functionality of the application and enter some random alpha numeric string. 

## Description

Descritpion



Instructions





1. Navigate to the search functionality of the application and enter some random alpha numeric string.







![227623a7-cd98-4178-8459-928f77d4fcd4.png]()





2.Right click on the page and select* view page source* after clickin on search in the aboce step.Observe that the random string has been reflected inside a JavaScript string.





![8e567dcd-b69b-45b3-a9ff-daa58d0de257.png]()

3.Use the following payload in the search box. Observe the extra closed script tag at the begining of the payload . It is required to first close the existing tag in the application.

*`</script><script>alert(document.cookie)</script*>`





![cba258e5-fc37-423f-8b5d-df8e03a4d254.png]()



4. Observe the alert popup triggered by the payload.





![280c9811-744e-4dab-980d-923a2925d834.png]()



## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]



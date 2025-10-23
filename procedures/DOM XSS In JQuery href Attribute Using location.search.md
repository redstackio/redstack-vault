---
id: 1ff5bbcd-8cbd-4d90-99d7-d3ca22367222
name: DOM XSS In JQuery href Attribute Using location.search
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T08:03:29.774174+00:00'
updated_at: '2023-05-26T18:30:06.186140+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# DOM XSS In JQuery href Attribute Using location.search

**Status**: ✓ Verified

## Summary

The search function in the application uses the JQuery library function to find an anchor element and change its href attribute using location.search 

## Description

# Description

The search function in the application uses the JQuery library function to find an anchor element and change its href attribute using location.search



# Instructions





1.Navigate to *submit feedback* from the home page







![f03d5607-38bc-47a0-a3f9-1b232b1f6a4d.png]()





2. On the Submit feedback page, change the query parameter returnPath to / followed by a random alphanumeric string.







![a1285f71-e143-4cd7-a232-001e5c309dde.png]()







3. Right-click and inspect the element, and observe that random string has been placed inside an ahref attribute.





![85b08643-3435-4003-9972-ac80bbc048c0.png]()





4.Change returnPath to javascript:*alert(document.cookie*), then load the modified url in the browser.







![c084b80f-bb4f-4fea-bacf-0c2135daa38c.png]()





5. Click on back button and observe that* document.cookie* getting loaded at the bottom of the page.





![801f4406-a020-479b-9b5c-f784fcd6a446.png]()



6. Observe the alert popup in the response to the payload in the application's page.







![48b77833-461d-4c7b-b0b8-9fd9dd4de6fd.png]()



## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]



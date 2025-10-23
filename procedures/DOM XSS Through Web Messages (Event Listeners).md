---
id: 5437202f-310d-4102-a1ce-bb336c31ad06
name: DOM XSS Through Web Messages (Event Listeners)
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T16:25:31.633250+00:00'
updated_at: '2023-05-26T18:10:15.102392+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# DOM XSS Through Web Messages (Event Listeners)

**Status**: ✓ Verified

## Summary

An attacker will exploit the application through web messages where there is no validation on origin of incoming web messages in the event listeners. 

## Description

# Description

An attacker will exploit the application through web messages where there is no validation on origin of incoming web messages in the event listeners. 

# 

# Instructions

# 

1. In chrome browser tab, Right click on the page and select *inspect*  . Observe the  Event listeners tab in chrome developer tools.







![e87fd760-ff0a-421d-b352-c8e13481f4f3.PNG]()









2. Craft a malicious url with *onload  *event along with the url of the application .  This malicious link will be sent to victim through social engineering ways. 







**Code**: [[<iframe src="https://acd21f091e0ad0d180d025af00600]]







3. Once the victim clicks on malicious link , *onload*  event gets triggered since there was no validation check on the origin of the event listener. 



In this current scenario , the application doesn't have any cookies implemented so it doesn't alert the cookie  







![e81afb55-a576-404a-a1fb-07c4a0861256.PNG]()









## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]



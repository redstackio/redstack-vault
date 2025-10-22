---
id: a9e1ded8-dc84-47a1-8b6c-1f8acc7098fb
name: HTML GET CSRF Payload with User Interaction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:55.368757+00:00'
updated_at: '2023-04-06T03:55:55.381924+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Golden Ticket|T1558.001 - Golden Ticket]]'
- '[[Silver Ticket|T1558.002 - Silver Ticket]]'
tags:
- '[[Cross-Site Request Forgery]]'
- '[[HTML GET - Requiring User Interaction]]'
- '[[Payloads]]'
---

# HTML GET CSRF Payload with User Interaction

## Summary

HTML GET CSRF Payload with User Interaction is a type of attack that tricks a user into performing an action on a website that they did not intend to do. The attacker crafts a malicious link that, when clicked, sends a request to the target website with the user's credentials. This can result in th

## Description

# Description

HTML GET CSRF Payload with User Interaction is a type of attack that tricks a user into performing an action on a website that they did not intend to do. The attacker crafts a malicious link that, when clicked, sends a request to the target website with the user's credentials. This can result in the attacker gaining access to sensitive information or performing unauthorized actions on behalf of the user. This attack can be executed by embedding a link in an email or on a website. The business value of this attack is that it can be used to gain unauthorized access to a system or steal sensitive information.

## Requirements

1. Access to the target website

1. Ability to craft a malicious link

1. Trick the user into clicking on the link

## Defense

1. Implement CSRF tokens to validate requests

1. Use HTTP POST instead of GET requests

1. Implement multi-factor authentication to prevent unauthorized access

## Objectives

1. To trick the user into clicking on a malicious link

1. To execute unauthorized actions on behalf of the user

1. To steal sensitive information

# Instructions

1. Craft a malicious link with the desired action and embed it in an email or on a website. When the user clicks on the link, the action will be executed on the target website.

**Code**: [[<a href="http://www.example.com/api/setusername?us]]

> The 'data' field contains the HTML code for the malicious link. The 'text' field contains a visual aid for crafting the link. The 'instruction' field provides high-level steps for executing the attack.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Golden Ticket|T1558.001 - Golden Ticket]]
- [[Silver Ticket|T1558.002 - Silver Ticket]]

## Tags

- [[Cross-Site Request Forgery]]
- [[HTML GET - Requiring User Interaction]]
- [[Payloads]]

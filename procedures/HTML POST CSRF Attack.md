---
id: bd49c407-69e4-4c06-8401-2b250a796a10
name: HTML POST CSRF Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:56.146635+00:00'
updated_at: '2023-04-10T20:21:25.075758+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Spearphishing Attachment|T1193 - Spearphishing Attachment]]'
tags:
- '[[Cross-Site Request Forgery]]'
- '[[HTML POST - Requiring User Interaction]]'
- '[[Payloads]]'
commands:
- '[[Form Submission]]'
---

# HTML POST CSRF Attack

## Summary

The HTML POST CSRF attack is a social engineering attack that involves tricking a user into clicking on a link or visiting a website that contains a malicious HTML form. This form submits a request to a target website on behalf of the user, using the user's existing session with the website. By doi

## Description

# Description

The HTML POST CSRF attack is a social engineering attack that involves tricking a user into clicking on a link or visiting a website that contains a malicious HTML form. This form submits a request to a target website on behalf of the user, using the user's existing session with the website. By doing so, the attacker can perform actions on the user's behalf without their knowledge or consent.

The HTML POST CSRF attack requires the user to interact with the malicious form, which can be disguised as a legitimate form on a trusted website. By submitting the form, the user unknowingly triggers the attack and allows the attacker to perform actions on their behalf.

 

## Requirements

1. The attacker must be able to create a malicious HTML form

1. The victim user must have an active session with the target website

 

## Defense

1. Implement CSRF tokens in forms to prevent unauthorized requests

1. Use SameSite cookies to prevent cross-site requests

1. Implement multi-factor authentication to prevent unauthorized access to user accounts

 

## Objectives

1. To perform unauthorized actions on a target website using a victim user's existing session

1. To gain access to sensitive information or perform unauthorized transactions

 

# Instructions

1. The attacker creates a malicious HTML form and hosts it on a website or sends it to the victim user. The form is designed to look like a legitimate form on a trusted website. When the victim user submits the form, the attack is triggered and the request is sent to the target website's API endpoint.

 



**Code**: [[<form action="http://www.example.com/api/setuserna]]



> The 'username' field in the form contains the value that the attacker wants to set as the victim user's username on the target website. By submitting the form, the victim user unknowingly performs this action on their behalf.



**Command** ([[Form Submission]]):

```bash
Submit a form with a hidden input named 'username' and a value of 'CSRFd'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Spearphishing Attachment|T1193 - Spearphishing Attachment]]

## Commands Used

- [[Form Submission]]

## Tags

- [[Cross-Site Request Forgery]]
- [[HTML POST - Requiring User Interaction]]
- [[Payloads]]



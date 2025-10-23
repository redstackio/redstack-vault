---
id: 040f8df3-7015-46ad-a17f-b8d197842a84
name: CSRF Attack via HTML GET Payload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:55.391762+00:00'
updated_at: '2023-04-06T03:55:55.401352+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Cross-Site Request Forgery]]'
- '[[HTML GET - No User Interaction]]'
- '[[Payloads]]'
---

# CSRF Attack via HTML GET Payload

## Summary

A Cross-Site Request Forgery (CSRF) attack occurs when an attacker tricks a victim into performing an action on a website without their knowledge or consent. In this scenario, the attacker sends a malicious HTML GET payload to the victim's browser, which will automatically execute the payload when 

## Description

# Description

A Cross-Site Request Forgery (CSRF) attack occurs when an attacker tricks a victim into performing an action on a website without their knowledge or consent. In this scenario, the attacker sends a malicious HTML GET payload to the victim's browser, which will automatically execute the payload when the victim visits a specific website. The payload contains a URL that will change the victim's username on a targeted website to a value specified by the attacker. This attack requires no user interaction and can be executed without the victim's knowledge. This type of attack is commonly used to perform unauthorized actions, such as changing a victim's password or making purchases.

 

## Requirements

1. Access to the targeted website.

1. Ability to send a malicious HTML GET payload to the victim's browser.

 

## Defense

1. Implement CSRF tokens to validate requests.

1. Use SameSite cookies to prevent CSRF attacks.

1. Educate users on the dangers of clicking on links or visiting websites from untrusted sources.

 

## Objectives

1. Change the victim's username on a targeted website.

1. Perform unauthorized actions on the targeted website.

 

# Instructions

1. The following HTML GET payload should be sent to the victim's browser:

 



**Code**: [[<img src="http://www.example.com/api/setusername?u]]



> This payload contains an image tag with a source URL that will change the victim's username on a targeted website to a value specified by the attacker. When the victim visits a specific website that contains this payload, it will automatically execute and change their username without their knowledge or consent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Cross-Site Request Forgery]]
- [[HTML GET - No User Interaction]]
- [[Payloads]]



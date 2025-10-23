---
id: 3d58787d-a4b6-424a-8a30-cf274b5188d6
name: Account Takeover Through Password Reset Poisoning
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.789366+00:00'
updated_at: '2023-04-06T03:55:53.799003+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Phishing|T1566 - Phishing]]'
sub_techniques:
- '[[Spearphishing Attachment|T1566.001 - Spearphishing Attachment]]'
- '[[Spearphishing Link|T1566.002 - Spearphishing Link]]'
- '[[Spearphishing via Service|T1566.003 - Spearphishing via Service]]'
tags:
- '[[Account Takeover]]'
- '[[Account Takeover Through Password Reset Poisoning]]'
- '[[Password Reset Feature]]'
---

# Account Takeover Through Password Reset Poisoning

## Summary

Account takeover through password reset poisoning is a technique used by attackers to gain access to a victim's account by manipulating the password reset feature. The attacker sends a phishing email to the victim with a link to a fake password reset page. When the victim enters their email address

## Description

# Description

Account takeover through password reset poisoning is a technique used by attackers to gain access to a victim's account by manipulating the password reset feature. The attacker sends a phishing email to the victim with a link to a fake password reset page. When the victim enters their email address, the attacker intercepts the request and modifies the header to redirect the request to a page controlled by the attacker. The victim then enters their new password, which is captured by the attacker. This technique can be used to gain access to sensitive information or to spread malware.

From a technical standpoint, this attack involves manipulating the HTTP request header to redirect the password reset request to a page controlled by the attacker. This can be done using a tool like Burp Suite or by modifying the request manually using a proxy like Charles Proxy. The attacker can then capture the victim's new password and use it to gain access to their account.

From a business perspective, this attack can result in the compromise of sensitive information, such as financial data or personal information. It can also damage the reputation of the company if the attack is made public.

 

## Requirements

1. Ability to intercept and modify HTTP requests

1. Phishing email to victim

 

## Defense

1. Educate users on how to identify and avoid phishing emails

1. Implement multi-factor authentication to prevent unauthorized access

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Gain access to a victim's account

1. Compromise sensitive information

1. Spread malware

 

# Instructions

1. Intercept the password reset request using a tool like Burp Suite or by manually modifying the request using a proxy like Charles Proxy. Modify the header to redirect the request to a page controlled by the attacker. Forward the modified request to the server.

 



**Code**: [[POST https://example.com/reset.php HTTP/1.1
Accept]]



> The attacker intercepts the password reset request and modifies the header to redirect the request to a page controlled by the attacker. This can be done using a tool like Burp Suite or by manually modifying the request using a proxy like Charles Proxy. The modified request is then forwarded to the server, which responds with a new password for the victim's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Phishing|T1566 - Phishing]]

### Sub-Techniques

- [[Spearphishing Attachment|T1566.001 - Spearphishing Attachment]]
- [[Spearphishing Link|T1566.002 - Spearphishing Link]]
- [[Spearphishing via Service|T1566.003 - Spearphishing via Service]]

## Tags

- [[Account Takeover]]
- [[Account Takeover Through Password Reset Poisoning]]
- [[Password Reset Feature]]



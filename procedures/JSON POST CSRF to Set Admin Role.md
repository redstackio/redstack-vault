---
id: 1f360473-0dbd-4b55-b663-3496e5fdf9b0
name: JSON POST CSRF to Set Admin Role
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:56.255375+00:00'
updated_at: '2023-04-10T20:21:26.911826+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Image File Execution Options Injection|T1183 - Image File Execution Options Injection]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Cross-Site Request Forgery]]'
- '[[JSON POST - Complex Request]]'
- '[[Payloads]]'
---

# JSON POST CSRF to Set Admin Role

## Summary

This procedure describes a Cross-Site Request Forgery (CSRF) attack that uses a JSON POST request to set the admin role. The attack relies on tricking the victim into visiting a malicious website that contains a hidden or disguised form that submits the request. When the victim submits the form, th

## Description

# Description

This procedure describes a Cross-Site Request Forgery (CSRF) attack that uses a JSON POST request to set the admin role. The attack relies on tricking the victim into visiting a malicious website that contains a hidden or disguised form that submits the request. When the victim submits the form, the request is sent to the target website with the victim's credentials, allowing the attacker to set the admin role without the victim's knowledge.

Technically, the attack uses an XMLHttpRequest object to send a POST request to the target website's API endpoint. The request includes a JSON payload that sets the role to admin. The withCredentials property is set to true to ensure that the victim's credentials are sent with the request. The Content-Type header is set to application/json;charset=UTF-8 to specify the format of the payload.

The business value of this attack is that it allows the attacker to gain unauthorized access to the target website as an admin, which could lead to data theft, data manipulation, or other malicious activities.

 

## Requirements

1. The victim must be authenticated to the target website.

1. The victim must visit a malicious website that contains the attack payload.

 

## Defense

1. Implement CSRF protection mechanisms such as anti-CSRF tokens or SameSite cookies to prevent attackers from executing CSRF attacks.

1. Educate users on the risks of clicking on links from untrusted sources and the importance of verifying the authenticity of websites before entering sensitive information.

1. Monitor network traffic for suspicious activity, such as unexpected POST requests or requests to unfamiliar endpoints.

 

## Objectives

1. Set the admin role on the target website without the victim's knowledge or consent.

 

# Instructions

1. To execute this attack, the attacker must first create a malicious website that includes the payload code. The payload code should be hidden or disguised so that the victim is not aware of the attack. When the victim visits the malicious website, the payload code is executed in the victim's browser, sending the POST request to the target website's API endpoint. If the victim is authenticated to the target website, the request will be sent with the victim's credentials, allowing the attacker to set the admin role without the victim's knowledge.

 



**Code**: [[<script>
var xhr = new XMLHttpRequest();
xhr.open(]]



> The payload code creates an XMLHttpRequest object and sets its open() method to send a POST request to the target website's API endpoint. The withCredentials property is set to true to ensure that the victim's credentials are sent with the request. The setRequestHeader() method is used to set the Content-Type header to application/json;charset=UTF-8 to specify the format of the payload. The send() method is used to send the JSON payload that sets the role to admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Image File Execution Options Injection|T1183 - Image File Execution Options Injection]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Cross-Site Request Forgery]]
- [[JSON POST - Complex Request]]
- [[Payloads]]



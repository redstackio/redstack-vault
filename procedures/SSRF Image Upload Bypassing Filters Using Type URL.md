---
id: 8c6a455a-e342-4dc2-abc2-c79de163bfa0
name: SSRF Image Upload Bypassing Filters Using Type URL
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.692217+00:00'
updated_at: '2023-04-10T20:24:06.114790+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypassing using type=url]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[Change input type to URL]]'
- '[[Upload image from URL]]'
---

# SSRF Image Upload Bypassing Filters Using Type URL

## Summary

This procedure involves bypassing filters by utilizing the 'type=url' parameter in an image upload function to perform a Server-Side Request Forgery attack. The attacker can craft a specially crafted URL that will be sent to the server and cause it to make a request to a specified endpoint. This ca

## Description

# Description

This procedure involves bypassing filters by utilizing the 'type=url' parameter in an image upload function to perform a Server-Side Request Forgery attack. The attacker can craft a specially crafted URL that will be sent to the server and cause it to make a request to a specified endpoint. This can allow the attacker to access internal systems and data, or perform actions on behalf of the server. This technique can be used by attackers to perform reconnaissance, lateral movement, or achieve persistence.

To perform this attack, the attacker needs to have access to the image upload function and craft a specially crafted URL that contains the endpoint they wish to access. The server will then make a request to the specified endpoint, allowing the attacker to access the data or perform actions on behalf of the server.

The business value of this attack is that it can allow attackers to gain access to sensitive data or perform actions on behalf of the server, potentially leading to financial loss, reputational damage, or regulatory fines.

 

## Requirements

1. Access to the image upload function

1. Ability to craft a specially crafted URL

 

## Defense

1. Implement input validation and sanitization to prevent attackers from crafting specially crafted URLs

1. Implement access controls to prevent unauthorized access to sensitive data or systems

1. Monitor network traffic for suspicious requests and behavior

 

## Objectives

1. Gain access to internal systems and data

1. Perform actions on behalf of the server

 

# Instructions

1. To trigger this vulnerability, follow the steps below:
1. Change the "type" attribute of the file input field from "file" to "url".
2. Paste the URL of the image you want to upload into the text field.
3. Hit enter to upload the image.


 



**Code**: [[Change "type=file" to "type=url"
Paste URL in text]]



> This command exploits a vulnerability that allows users to upload images from any image URL. By changing the "type" attribute of the file input field to "url", the user can bypass server-side checks and upload an image from any URL, including URLs that are not allowed by the server. This can lead to a Server-Side Request Forgery (SSRF) attack, where the attacker can make the server send requests to arbitrary destinations, potentially leading to data leakage or remote code execution.



**Command** ([[Change input type to URL]]):

```bash
document.querySelector('input[type=file]').type = 'url';
```





**Command** ([[Upload image from URL]]):

```bash
document.querySelector('input[type=url]').value = 'https://example.com/image.jpg';
document.querySelector('input[type=url]').dispatchEvent(new Event('change'));
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Change input type to URL]]
- [[Upload image from URL]]

## Tags

- [[Bypassing filters]]
- [[Bypassing using type=url]]
- [[Server-Side Request Forgery]]



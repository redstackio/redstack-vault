---
id: e52f47ab-2574-4e8d-a7ae-115f818ebd5d
name: SSRF Bypass using Decimal IP Location
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.371859+00:00'
updated_at: '2023-04-10T20:24:01.615437+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using a decimal IP location]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[IP Address Conversion]]'
---

# SSRF Bypass using Decimal IP Location

## Summary

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send requests from a server to another server on behalf of the victim user. This technique is often used to bypass network security measures and access sensitive information. In this procedure, we will discuss how to b

## Description

# Description

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send requests from a server to another server on behalf of the victim user. This technique is often used to bypass network security measures and access sensitive information. In this procedure, we will discuss how to bypass filters using a decimal IP location. This technique is used when the server-side application filters requests based on IP addresses, but allows decimal IP locations.

Technical Explanation: In this procedure, we will use the 'IP Address Translation' command to convert the decimal IP location to a valid IP address that the server-side application can understand. By doing this, we can bypass the filters and send the request to the desired server. 

Business Value: This technique can be used to gain unauthorized access to sensitive information and systems, which can result in data breaches and financial losses.

 

## Requirements

1. Access to a server-side application that filters requests based on IP addresses

 

## Defense

1. Implement input validation to ensure that only valid IP addresses are accepted

1. Use a web application firewall to detect and block SSRF attempts

1. Monitor network traffic for unusual activity and investigate any suspicious requests

 

## Objectives

1. Bypass server-side filters to access sensitive information

 

# Instructions

1. To translate IP addresses, use the following commands:

 



**Code**: [[http://2130706433/ = http://127.0.0.1
http://32322]]



> The 'http://2130706433/' is equivalent to 'http://127.0.0.1' IP address, while 'http://3232235521/' is equivalent to 'http://192.168.0.1' IP address, 'http://3232235777/' is equivalent to 'http://192.168.1.1' IP address, and 'http://2852039166/' is equivalent to 'http://169.254.169.254' IP address. Use these translations as needed in your scripts or applications.



**Command** ([[IP Address Conversion]]):

```bash
http://2130706433/ = http://127.0.0.1
http://3232235521/ = http://192.168.0.1
http://3232235777/ = http://192.168.1.1
http://2852039166/  = http://169.254.169.254
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[IP Address Conversion]]

## Tags

- [[Bypassing filters]]
- [[Bypass using a decimal IP location]]
- [[Server-Side Request Forgery]]



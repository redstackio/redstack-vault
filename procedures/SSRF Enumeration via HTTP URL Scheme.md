---
id: d388b46a-d5b9-4138-bf38-d7a60aec7920
name: SSRF Enumeration via HTTP URL Scheme
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.803511+00:00'
updated_at: '2023-04-10T20:24:03.948733+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
tags:
- '[[HTTP]]'
- '[[Server-Side Request Forgery]]'
- '[[SSRF exploitation via URL Scheme]]'
---

# SSRF Enumeration via HTTP URL Scheme

## Summary

SSRF Enumeration via HTTP URL Scheme is a technique used by attackers to identify internal systems and services that are not exposed to the public internet. This technique is often used in reconnaissance operations to gather information about a target's internal network. Attackers can use this tech

## Description

# Description

SSRF Enumeration via HTTP URL Scheme is a technique used by attackers to identify internal systems and services that are not exposed to the public internet. This technique is often used in reconnaissance operations to gather information about a target's internal network. Attackers can use this technique by crafting a malicious URL that includes the IP address or hostname of the internal system they wish to target. When the URL is accessed by the vulnerable application, it will make a request to the internal system, revealing information about its existence and potentially sensitive data. This technique can be used to discover vulnerable systems and services that can be targeted in a later stage of the attack.

 

## Requirements

1. Access to a vulnerable application that allows SSRF exploitation via HTTP URL Scheme

 

## Defense

1. Implement input validation and filtering to prevent malicious inputs from being processed by the application

1. Implement network segmentation to prevent access to internal systems from external sources

1. Monitor network traffic for suspicious activity, such as requests to internal IP addresses or hostnames

 

## Objectives

1. Identify internal systems and services that are not exposed to the public internet

1. Gather information about a target's internal network

1. Discover vulnerable systems and services that can be targeted in a later stage of the attack

 

# Instructions

1. The attacker can use this command to scan ports of the target system by replacing the IP address in the URL with the target system's IP address. The attacker can also fetch any content from the web by replacing the URL in the command with the desired URL.

 



**Code**: [[ssrf.php?url=http://127.0.0.1:22
ssrf.php?url=http]]



> The 'ssrf.php' script is being used to perform Server Side Request Forgery (SSRF) attacks. The 'url' parameter in the command specifies the URL to be fetched or the IP address and port number to be scanned. This command can be used to bypass firewalls and access internal systems. It is important to note that this command can be very dangerous if used maliciously and can result in serious security breaches.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

## Tags

- [[HTTP]]
- [[Server-Side Request Forgery]]
- [[SSRF exploitation via URL Scheme]]



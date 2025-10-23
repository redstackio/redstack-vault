---
id: ae5767ce-f097-4f9f-ba3f-79649cd184c0
name: XXE Denial of Service via YAML Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.292212+00:00'
updated_at: '2023-04-10T20:24:44.217935+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
tags:
- '[[Exploiting XXE to perform a deny of service]]'
- '[[XML External Entity]]'
- '[[Yaml attack]]'
---

# XXE Denial of Service via YAML Attack

## Summary

The XXE Denial of Service via YAML Attack is a technique that leverages the XML External Entity vulnerability to cause a denial of service on a target system. This attack is performed by sending a specially crafted YAML file that contains an external entity reference. When the target system process

## Description

# Description

The XXE Denial of Service via YAML Attack is a technique that leverages the XML External Entity vulnerability to cause a denial of service on a target system. This attack is performed by sending a specially crafted YAML file that contains an external entity reference. When the target system processes the YAML file, it will attempt to resolve the external entity reference, which can cause the system to become unresponsive or crash.

From an offensive perspective, this attack can be used to disrupt the availability of a target system, causing a loss of service for legitimate users. From a technical standpoint, this attack exploits the XXE vulnerability by injecting malicious code that causes the system to consume resources until it can no longer function. From a business perspective, this attack can result in lost revenue and reputation damage due to the unavailability of critical services.


 

## Requirements

1. Access to a target system that is vulnerable to XXE

1. Ability to send a specially crafted YAML file to the target system

 

## Defense

1. Implement input validation and sanitization techniques to prevent XXE attacks

1. Use a web application firewall to detect and block malicious requests

1. Regularly update and patch all software components to address known vulnerabilities

 

## Objectives

1. Deny access to a target system

1. Disrupt the availability of critical services

 

# Instructions

1. This command creates a list with the same element repeated multiple times. The number of repetitions is determined by the number of '*' symbols before the reference to the original list.

 



**Code**: [[a: &a ["lol","lol","lol","lol","lol","lol","lol","]]



> The command uses YAML syntax to create a list with repeated elements. The original list is defined in line 'a: &a ["lol","lol","lol","lol","lol","lol","lol","lol","lol"]'. This list is then used to create new lists, where each element is repeated multiple times. For example, the list 'b' is defined as '&b [*a,*a,*a,*a,*a,*a,*a,*a,*a]', which means that each element of list 'a' is repeated 9 times to create the list 'b'. Similarly, the list 'c' is created by repeating each element of list 'b' 9 times, and so on, until the list 'i' is created by repeating each element of list 'h' 9 times.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]

## Tags

- [[Exploiting XXE to perform a deny of service]]
- [[XML External Entity]]
- [[Yaml attack]]



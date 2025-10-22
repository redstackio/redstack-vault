---
id: c3f8c38d-b7af-4fa2-ba0b-93589561a61c
name: SSRF URL for Oracle Cloud Instances via AWS Instance Metadata and User Data
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.680180+00:00'
updated_at: '2023-04-10T20:23:54.110170+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Cloud Instances]]'
- '[[SSRF URL for Oracle Cloud]]'
commands:
- '[[Retrieve EC2 metadata]]'
---

# SSRF URL for Oracle Cloud Instances via AWS Instance Metadata and User Data

## Summary

This procedure involves exploiting a Server-Side Request Forgery (SSRF) vulnerability to extract sensitive information from an Oracle cloud instance. The attacker uses the AWS Instance Metadata and User Data service to obtain the instance's metadata and extract sensitive information such as access 

## Description

# Description

This procedure involves exploiting a Server-Side Request Forgery (SSRF) vulnerability to extract sensitive information from an Oracle cloud instance. The attacker uses the AWS Instance Metadata and User Data service to obtain the instance's metadata and extract sensitive information such as access keys, instance ID, and security group. This information can then be used to launch further attacks against the cloud infrastructure or steal sensitive data.

To exploit this vulnerability, the attacker sends a specially crafted request to the vulnerable application, which then sends a request to the AWS metadata service. The response from this service contains sensitive information that is then extracted by the attacker.

This procedure can be used by attackers to gain unauthorized access to cloud infrastructure and data, leading to data breaches and financial loss for the targeted organization.

## Requirements

1. Access to a vulnerable application with SSRF vulnerability

1. Knowledge of AWS Instance Metadata and User Data service

## Defense

1. Implement input validation and sanitization to prevent SSRF attacks

1. Limit access to AWS Instance Metadata and User Data service

1. Implement network segmentation to limit access to cloud infrastructure

## Objectives

1. Extract sensitive information from Oracle cloud instances

1. Gain unauthorized access to cloud infrastructure and data

# Instructions

1. To access AWS Instance Metadata and User Data, use the given URLs:

**Code**: [[http://192.0.0.192/latest/
http://192.0.0.192/late]]

> AWS Instance Metadata and User Data are used to provide information about an instance running on Amazon Web Services (AWS). The given URLs provide access to the metadata and user data of the instance. The metadata includes information about the instance, such as the instance ID, availability zone, and security groups. The user data is information that can be passed to the instance during launch and is often used to configure the instance.

To access the metadata and user data, simply make an HTTP request to the appropriate URL. For example, to get the instance ID, you would make an HTTP request to http://192.0.0.192/latest/meta-data/instance-id. Similarly, to get the user data, you would make an HTTP request to http://192.0.0.192/latest/user-data/.

**Command** ([[Retrieve EC2 metadata]]):

```bash
http://192.0.0.192/latest/
http://192.0.0.192/latest/user-data/
http://192.0.0.192/latest/meta-data/
http://192.0.0.192/latest/attributes/
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]

## Commands Used

- [[Retrieve EC2 metadata]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Cloud Instances]]
- [[SSRF URL for Oracle Cloud]]

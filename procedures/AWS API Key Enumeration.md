---
id: f6144f1b-160c-41be-9b4e-4cad22af5b9b
name: AWS API Key Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.488492+00:00'
updated_at: '2023-04-10T20:20:51.623258+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing API KEYS]]'
commands:
- '[[Retrieve API keys including values]]'
---

# AWS API Key Enumeration

## Summary

AWS API Key Enumeration is a technique used to discover and list the API keys associated with an AWS account. This technique is often used as a precursor to other attacks, as it provides the attacker with the necessary credentials to perform further actions. To perform this technique, an attacker c

## Description

# Description

AWS API Key Enumeration is a technique used to discover and list the API keys associated with an AWS account. This technique is often used as a precursor to other attacks, as it provides the attacker with the necessary credentials to perform further actions. To perform this technique, an attacker can use various AWS services such as CloudTrail or Access Analyzer to discover the keys. Business value of this technique is to identify and secure any exposed API keys to prevent unauthorized access to AWS resources.

## Requirements

1. Valid AWS credentials with IAM permissions to list API keys

1. Access to AWS services such as CloudTrail or Access Analyzer

## Defense

1. Implement least privilege access by granting IAM users and roles only the permissions they need

1. Enable AWS CloudTrail and monitor activity logs for suspicious activity

1. Regularly rotate API keys and use AWS Secrets Manager to securely store and manage them

## Objectives

1. Discover and list API keys associated with an AWS account

1. Use the discovered API keys to perform further attacks

# Instructions

1. To retrieve API keys, run the following command:

This command retrieves all API keys associated with your Amazon API Gateway account. The --include-values option will also return the API key values, which can be useful for troubleshooting or auditing purposes.

**Command** ([[Retrieve API keys including values]]):

```bash
aws apigateway get-api-keys --include-values
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]

## Commands Used

- [[Retrieve API keys including values]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing API KEYS]]

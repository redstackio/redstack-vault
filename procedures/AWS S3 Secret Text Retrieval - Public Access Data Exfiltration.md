---
id: 9c99d79e-01e6-4ba7-9371-61c5254df2ab
name: AWS S3 Secret Text Retrieval - Public Access Data Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.117026+00:00'
updated_at: '2023-04-10T20:20:27.139499+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
tags:
- '[[Cloud - AWS]]'
- '[[Data Exfiltration]]'
- '[[Public Access]]'
---

# AWS S3 Secret Text Retrieval - Public Access Data Exfiltration

## Summary

AWS S3 Secret Text Retrieval is a technique used to exfiltrate data from an AWS S3 bucket that has been made public. An attacker can use this technique to retrieve sensitive information such as passwords, API keys, and other secrets stored in the bucket. The attacker can then use these secrets to e

## Description

# Description

AWS S3 Secret Text Retrieval is a technique used to exfiltrate data from an AWS S3 bucket that has been made public. An attacker can use this technique to retrieve sensitive information such as passwords, API keys, and other secrets stored in the bucket. The attacker can then use these secrets to escalate privileges or perform further attacks against the target organization.

To execute this technique, the attacker must first identify a public S3 bucket that contains the desired data. The attacker can then use the AWS S3 Secret Text Retrieval command to download the data from the bucket. This technique can be difficult to detect as it uses a legitimate AWS command and can blend in with normal network traffic.

Business value: An attacker can use this technique to steal sensitive data from an organization, which can result in financial loss, reputational damage, and legal consequences.

## Requirements

1. Access to a public AWS S3 bucket containing desired data

1. Valid AWS credentials with permissions to execute the AWS S3 Secret Text Retrieval command

## Defense

1. Ensure that AWS S3 buckets are not made public unless necessary

1. Implement access controls to restrict access to AWS S3 buckets

1. Monitor AWS S3 bucket activity for suspicious behavior

## Objectives

1. Retrieve sensitive data from a public AWS S3 bucket

1. Use the retrieved data to escalate privileges or perform further attacks

# Instructions

1. To retrieve a secret text file from an AWS S3 bucket, use the following Python code:

**Code**: [[https://bucket-name.region.amazonaws.com/secret.tx]]

> The 'data' field should contain the URL of the secret text file in the AWS S3 bucket. The 'lang' field should be set to 'python'. Use the 'boto3' library to access the AWS S3 bucket. First, create a client object for the AWS S3 service. Then, use the 'get_object' method to retrieve the secret text file from the bucket. Finally, access the text data from the response object using the 'read' method. Be sure to handle any exceptions that may occur during the process.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Tags

- [[Cloud - AWS]]
- [[Data Exfiltration]]
- [[Public Access]]

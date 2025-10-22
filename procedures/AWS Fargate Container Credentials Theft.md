---
id: 0d0d8328-0c05-4857-9e0e-1d1decedd1b4
name: AWS Fargate Container Credentials Theft
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.293993+00:00'
updated_at: '2023-04-10T20:20:23.226302+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[AWS - Metadata SSRF]]'
- '[[Cloud - AWS]]'
- '[[Method for Container Service (Fargate)]]'
---

# AWS Fargate Container Credentials Theft

## Summary

The AWS Fargate Container Credentials Theft procedure involves exploiting a Server Side Request Forgery (SSRF) vulnerability in AWS metadata service to obtain the credentials of the container running in Fargate. This can be used to access other AWS services and resources that the container has perm

## Description

# Description

The AWS Fargate Container Credentials Theft procedure involves exploiting a Server Side Request Forgery (SSRF) vulnerability in AWS metadata service to obtain the credentials of the container running in Fargate. This can be used to access other AWS services and resources that the container has permission to access. The attacker can use this technique to escalate their privileges and move laterally within the target environment.

To carry out this attack, the attacker sends a crafted request to the AWS metadata service from the container to obtain the credentials. This attack can be carried out remotely, as long as the attacker can send requests to the metadata service from the container.

This procedure provides an attacker with a way to obtain AWS credentials from a Fargate container, which can be used to further compromise the target environment.

## Requirements

1. Access to the target environment

1. Ability to send requests to the metadata service from the container

## Defense

1. Ensure that the AWS metadata service is not publicly accessible

1. Implement network segmentation to limit access to the metadata service

1. Monitor network traffic for requests to the metadata service

## Objectives

1. Obtain AWS credentials from a Fargate container

1. Access other AWS services and resources that the container has permission to access

1. Escalate privileges and move laterally within the target environment

# Instructions

1. To fetch the AWS_CONTAINER_CREDENTIALS_RELATIVE_URI variable, navigate to https://awesomeapp.com/download?file=/proc/self/environ and search for the variable in the output.

**Code**: [[JAVA_ALPINE_VERSION=8.212.04-r0
HOSTNAME=bbb3c57a0]]

> The AWS_CONTAINER_CREDENTIALS_RELATIVE_URI variable is used to obtain credentials for an AWS Fargate task. It contains a URI that can be used to retrieve the task's IAM role credentials. The IAM role credentials can be used to access AWS resources from within the task.

2. Run the command to retrieve the AWS credentials and use the URL provided to dump the AccessKey and SecretKey.

> The AWS credentials are provided in the JSON object. The AccessKey and SecretKey can be dumped using the credential URL provided in the 'text' field of the JSON object. The 'lang' field specifies the language in which the command is to be run.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Data from Information Repositories|T1213 - Data from Information Repositories]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[AWS - Metadata SSRF]]
- [[Cloud - AWS]]
- [[Method for Container Service (Fargate)]]

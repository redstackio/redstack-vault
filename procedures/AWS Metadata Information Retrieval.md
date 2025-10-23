---
id: e2715a4a-5e83-4242-847c-6b3ce607da41
name: AWS Metadata Information Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.321652+00:00'
updated_at: '2023-04-10T20:19:49.862753+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Execution through API|T1106 - Execution through API]]'
tags:
- '[[AWS Metadata]]'
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Remote code execution]]'
commands:
- '[[curl http://169.254.169.254/latest/meta-data]]'
---

# AWS Metadata Information Retrieval

## Summary

AWS Metadata Information Retrieval is a technique that allows an attacker to retrieve sensitive information about the AWS instance, such as access keys, security groups, and IAM roles. This technique can be used to escalate privileges and gain access to other AWS services. The attacker can use the 

## Description

# Description

AWS Metadata Information Retrieval is a technique that allows an attacker to retrieve sensitive information about the AWS instance, such as access keys, security groups, and IAM roles. This technique can be used to escalate privileges and gain access to other AWS services. The attacker can use the 'Metadata Information Retrieval' command to retrieve the metadata from the instance.

 

## Requirements

1. Access to the AWS instance

1. The 'Metadata Information Retrieval' command

 

## Defense

1. Restrict access to the AWS instance to authorized personnel only

1. Use IAM roles with appropriate permissions to limit access to sensitive information

1. Implement network segmentation to limit lateral movement within the AWS environment

 

## Objectives

1. Retrieve sensitive information about the AWS instance

1. Escalate privileges

1. Gain access to other AWS services

 

# Instructions

1. Execute the above command to retrieve metadata information from the target system.

 

The above command is used to retrieve metadata information from the target system. This information can be useful for further exploitation of the system. The command uses the 'curl' utility to make an HTTP request to the URL 'http://169.254.169.254/latest/meta-data'. This URL is a well-known endpoint for retrieving metadata information in EC2 instances. If the command is successful, it will return the metadata information in plain text format.



**Command** ([[curl http://169.254.169.254/latest/meta-data]]):

```bash
curl http://169.254.169.254/latest/meta-data
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Execution through API|T1106 - Execution through API]]

## Commands Used

- [[curl http://169.254.169.254/latest/meta-data]]

## Tags

- [[AWS Metadata]]
- [[Cloud - AWS]]
- [[Exploitation]]
- [[Remote code execution]]



---
id: 94c9f495-f3be-4a34-bdd2-74918c82ec5f
name: AWS API Gateway Version Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.442138+00:00'
updated_at: '2023-04-10T20:20:45.313831+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Service Discovery|T1007 - System Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing all versions of a rest api]]'
commands:
- '[[Get API Gateway stages]]'
---

# AWS API Gateway Version Enumeration

## Summary

AWS API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. This procedure aims to list all versions of a REST API hosted on AWS API Gateway. By doing so, an attacker can identify the versions of the API that are 

## Description

# Description

AWS API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. This procedure aims to list all versions of a REST API hosted on AWS API Gateway. By doing so, an attacker can identify the versions of the API that are vulnerable to specific attacks, such as injection or privilege escalation. 

To list all versions of a REST API, the attacker can use the 'Get API Gateway Stages' command. This command will return a list of all stages associated with the specified API Gateway REST API, including the stages' deployment IDs and the URLs that link to each stage. 

The business value of this procedure is that it allows an attacker to identify vulnerable API versions and exploit them to gain unauthorized access to sensitive data or perform other malicious activities.

 

## Requirements

1. Access to the targeted AWS account

1. Authenticated access to the AWS API Gateway service

1. Permission to execute the 'Get API Gateway Stages' command

 

## Defense

1. Regularly review and monitor API Gateway usage and configurations

1. Implement proper authentication and authorization mechanisms to prevent unauthorized access to the API Gateway service

1. Implement proper input validation and sanitization to prevent injection attacks on API versions

 

## Objectives

1. Identify all versions of a REST API hosted on AWS API Gateway

1. Identify vulnerable API versions

 

# Instructions

1. Use this command to get a list of all the stages in an API Gateway REST API.

 

The 'aws apigateway get-stages' command is used to retrieve a list of all the stages in an API Gateway REST API. The '--rest-api-id' option is used to specify the ID of the REST API for which you want to retrieve the stages. This command returns a JSON object that contains information about each stage, including its name, deployment ID, and description. This information can be useful for managing and monitoring your API Gateway deployment.



**Command** ([[Get API Gateway stages]]):

```bash
aws apigateway get-stages --rest-api-id ID
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Service Discovery|T1007 - System Service Discovery]]

## Commands Used

- [[Get API Gateway stages]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing all versions of a rest api]]



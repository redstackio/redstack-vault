---
id: 7460b8eb-0e39-4c17-9b92-742127ba9ffe
name: AWS API Gateway Method Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.417383+00:00'
updated_at: '2023-04-10T20:19:54.335935+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Deployment Software|T1017 - Application Deployment Software]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing method information for the endpoint]]'
commands:
- '[[Get API Gateway Method]]'
---

# AWS API Gateway Method Enumeration

## Summary

AWS API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. The AWS API Gateway Method Enumeration procedure involves listing method information for the endpoint. This can be useful for identifying potential vulne

## Description

# Description

AWS API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. The AWS API Gateway Method Enumeration procedure involves listing method information for the endpoint. This can be useful for identifying potential vulnerabilities and weaknesses in the API Gateway configuration. By enumerating the API Gateway methods, an attacker can identify the available endpoints and potentially discover sensitive information that can be used to launch further attacks. 

Technical: The AWS API Gateway Method Enumeration procedure involves using the 'Get API Gateway Method' command to retrieve information about the methods available for a specific endpoint. This command returns a list of HTTP methods that are supported by the specified API Gateway endpoint. 

Business Value: This procedure can be used by security professionals to identify potential vulnerabilities in their AWS environment and take steps to remediate them. By identifying weaknesses in the API Gateway configuration, organizations can ensure that their APIs are secure and not exposing sensitive information.

## Requirements

1. Valid AWS credentials with permissions to access the API Gateway service

1. Access to the API Gateway endpoint to be enumerated

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Implement network segmentation to limit access to the API Gateway endpoint

1. Regularly monitor and audit the API Gateway configuration for potential vulnerabilities

## Objectives

1. Identify the available endpoints in the API Gateway configuration

1. Discover potential vulnerabilities and weaknesses in the API Gateway configuration

1. Remediate identified vulnerabilities to ensure the security of the AWS environment

# Instructions

1. To get a specific method in the API Gateway, use the following AWS CLI command:

**Code**: [[aws apigateway get-method --rest-api-id ApiID --re]]

> This command retrieves the details of a specific method in the API Gateway. Replace 'ApiID' with the ID of the API Gateway and 'ID' with the ID of the resource containing the method. Replace 'method' with the HTTP method (e.g. GET, POST, PUT) of the method you want to retrieve. This command can be useful for troubleshooting and debugging API Gateway issues.

**Command** ([[Get API Gateway Method]]):

```bash
aws apigateway get-method --rest-api-id ApiID --resource-id ID --http-method method
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Deployment Software|T1017 - Application Deployment Software]]

## Commands Used

- [[Get API Gateway Method]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing method information for the endpoint]]

---
id: 0692ca07-bad5-4009-ae81-863dc3026bb9
name: AWS API Gateway Resource Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.370832+00:00'
updated_at: '2023-04-10T20:20:38.262625+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing information about endpoints]]'
commands:
- '[[Get API Gateway Resources]]'
---

# AWS API Gateway Resource Enumeration

## Summary

The AWS API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. The AWS API Gateway Resource Enumeration procedure involves listing information about endpoints in order to gain a better understanding of the target

## Description

# Description

The AWS API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. The AWS API Gateway Resource Enumeration procedure involves listing information about endpoints in order to gain a better understanding of the target's API Gateway resources. This information can then be used to identify potential attack vectors and vulnerabilities.

Technical Description: The procedure involves using the 'Get API Gateway Resources' command to list all resources in the specified REST API. This will return a list of resources with their associated ID, path, and methods. The information gathered can be used to identify potential vulnerabilities such as missing authentication or authorization controls.

Business Value: By identifying potential vulnerabilities in the API Gateway resources, organizations can proactively secure their APIs and prevent unauthorized access.

 

## Requirements

1. Valid AWS credentials with permissions to access the target's API Gateway

1. Network access to the target's API Gateway

 

## Defense

1. Ensure that AWS credentials are properly secured and not shared

1. Implement proper authentication and authorization controls for API Gateway resources

1. Regularly monitor API Gateway logs for suspicious activity

 

## Objectives

1. Identify potential attack vectors and vulnerabilities in the target's API Gateway resources

1. Proactively secure APIs and prevent unauthorized access

 

# Instructions

1. To get a list of resources in an Amazon API Gateway REST API, use the 'aws apigateway get-resources' command with the --rest-api-id parameter followed by the ID of the REST API.

 

The 'aws apigateway get-resources' command returns a list of resources in an Amazon API Gateway REST API. The --rest-api-id parameter is required and should be followed by the ID of the REST API for which you want to retrieve the resources. This command can be useful for discovering the resources available in an API and for understanding the structure of the API. The output of the command includes information about each resource, such as its ID, parent ID, path, and resource methods. 



**Command** ([[Get API Gateway Resources]]):

```bash
aws apigateway get-resources --rest-api-id ID
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get API Gateway Resources]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing information about endpoints]]



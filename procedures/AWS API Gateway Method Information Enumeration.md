---
id: 1740301f-710a-4fd3-afd5-7b8f43020e09
name: AWS API Gateway Method Information Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.862780+00:00'
updated_at: '2023-04-10T20:20:28.529447+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Listing method information for the endpoint]]'
- '[[Persistence]]'
commands:
- '[[Get API Gateway Method]]'
---

# AWS API Gateway Method Information Enumeration

## Summary

The AWS API Gateway Method Information Enumeration procedure involves using the 'Get API Gateway Method' command to list details about the methods associated with a specific endpoint in an AWS API Gateway. This information can be used to gain a better understanding of the API and its functionality.

## Description

# Description

The AWS API Gateway Method Information Enumeration procedure involves using the 'Get API Gateway Method' command to list details about the methods associated with a specific endpoint in an AWS API Gateway. This information can be used to gain a better understanding of the API and its functionality. From an offensive standpoint, this procedure can be used to identify potential vulnerabilities and misconfigurations in the API Gateway that could be exploited to gain unauthorized access to sensitive data or functionality.

Technically, this procedure involves making an authenticated request to the AWS API Gateway using the appropriate credentials and specifying the endpoint and method for which information is being requested. The resulting response will include details such as the HTTP method, integration type, and request/response models.

From a business perspective, this procedure can help organizations better understand the APIs they have deployed in AWS and identify potential security risks. By regularly performing this procedure, organizations can ensure that their APIs are properly configured and secured.

 

## Requirements

1. Valid AWS credentials with permissions to access the API Gateway

1. Access to the AWS API Gateway endpoint being queried

 

## Defense

1. Ensure that AWS credentials are properly secured and not shared unnecessarily

1. Implement proper access controls for the API Gateway to prevent unauthorized access

1. Regularly review API Gateway configurations and logs for signs of malicious activity

 

## Objectives

1. List information about the methods associated with a specific endpoint in an AWS API Gateway

1. Identify potential vulnerabilities and misconfigurations in the API Gateway

1. Better understand the APIs deployed in AWS

 

# Instructions

1. Use this command to retrieve the details of a specific method in an API Gateway REST API.

 



**Code**: [[aws apigateway get-method --rest-api-id ApiID --re]]



> The `--rest-api-id` parameter specifies the ID of the API Gateway REST API to which the method belongs. The `--resource-id` parameter specifies the ID of the resource that contains the method. The `--http-method` parameter specifies the HTTP method of the method to retrieve. This command returns the details of the specified method, including the method's integration, request, and response configuration.



**Command** ([[Get API Gateway Method]]):

```bash
aws apigateway get-method --rest-api-id ApiID --resource-id ID --http-method method
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get API Gateway Method]]

## Tags

- [[Cloud - AWS]]
- [[Listing method information for the endpoint]]
- [[Persistence]]



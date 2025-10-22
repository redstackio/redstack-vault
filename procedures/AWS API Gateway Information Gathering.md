---
id: 7dc6be59-6013-4a49-9ac4-89c069761fe8
name: AWS API Gateway Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.789208+00:00'
updated_at: '2023-04-10T20:20:15.102544+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Listing information about a specific API]]'
- '[[Persistence]]'
commands:
- '[[Get API Gateway REST API]]'
---

# AWS API Gateway Information Gathering

## Summary

The AWS API Gateway Information Gathering procedure involves using the 'Get API Gateway' command to list information about a specific API. This procedure can be used by an attacker to gather intelligence about the API's structure, resources, and methods in order to identify potential vulnerabilitie

## Description

# Description

The AWS API Gateway Information Gathering procedure involves using the 'Get API Gateway' command to list information about a specific API. This procedure can be used by an attacker to gather intelligence about the API's structure, resources, and methods in order to identify potential vulnerabilities or weaknesses. From a technical perspective, this procedure is relatively simple and only requires access to the AWS API Gateway service. However, the business value of this procedure is significant as it can help attackers identify sensitive data or functionality that can be abused for malicious purposes.

## Requirements

1. Valid AWS API Gateway credentials

## Defense

1. Ensure that AWS API Gateway credentials are properly secured and not shared with unauthorized individuals

1. Implement network segmentation and access controls to limit access to the API Gateway service

1. Regularly monitor API Gateway logs and traffic to identify suspicious activity

## Objectives

1. Identify potential vulnerabilities or weaknesses in the API's structure

1. Identify sensitive data or functionality that can be abused for malicious purposes

# Instructions

1. To get information about an existing API Gateway, run the following command:

This command retrieves information about a specific API Gateway by providing the ID of the REST API. The ID can be found in the API Gateway console or by running 'aws apigateway get-rest-apis' command. This command returns a JSON object that contains the details of the API Gateway, including its name, description, endpoint URL, and more.

**Command** ([[Get API Gateway REST API]]):

```bash
aws apigateway get-rest-api --rest-api-id ID
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Get API Gateway REST API]]

## Tags

- [[Cloud - AWS]]
- [[Listing information about a specific API]]
- [[Persistence]]

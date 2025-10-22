---
id: 5c4deba9-6179-4a73-87de-b37f580269cb
name: AWS API Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.348603+00:00'
updated_at: '2023-04-10T20:20:51.266590+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Deployment Software|T1017 - Application Deployment Software]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing information about a specific API]]'
commands:
- '[[Get API Gateway REST API ID]]'
---

# AWS API Enumeration

## Summary

The AWS API Enumeration procedure involves listing information about a specific API to gain a better understanding of the target environment. This procedure can be used to identify potential vulnerabilities or misconfigurations that could be exploited by an attacker. From a technical perspective, t

## Description

# Description

The AWS API Enumeration procedure involves listing information about a specific API to gain a better understanding of the target environment. This procedure can be used to identify potential vulnerabilities or misconfigurations that could be exploited by an attacker. From a technical perspective, this procedure involves using the 'Get REST API Details' command to retrieve information about the target API, such as its name, description, stages, and resources. From a business perspective, this procedure can help organizations identify and remediate potential security risks in their AWS environment.

## Requirements

1. Valid AWS credentials

1. Access to the target API

## Defense

1. Ensure that AWS credentials are properly secured and not shared

1. Implement strong access controls to limit access to the target API

1. Monitor AWS CloudTrail logs for any suspicious activity related to the target API

## Objectives

1. Identify potential vulnerabilities or misconfigurations in the target environment

1. Gain a better understanding of the target environment

1. Remediate potential security risks in the AWS environment

# Instructions

1. To get the details of a specific REST API in Amazon API Gateway, use the following command:

The `aws apigateway get-rest-api` command is used to retrieve details about a specific REST API in Amazon API Gateway. To use this command, replace the `ID` parameter with the ID of the REST API you want to retrieve details for. The command will return a JSON object that contains information about the REST API, including its ID, name, description, endpoint configuration, and more.

**Command** ([[Get API Gateway REST API ID]]):

```bash
aws apigateway get-rest-api --rest-api-id ID
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Deployment Software|T1017 - Application Deployment Software]]

## Commands Used

- [[Get API Gateway REST API ID]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing information about a specific API]]

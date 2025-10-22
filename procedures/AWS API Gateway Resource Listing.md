---
id: 33424625-7a38-4703-8103-b4a286ec68c9
name: AWS API Gateway Resource Listing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.834650+00:00'
updated_at: '2023-04-10T20:20:01.976002+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Listing information about a specific endpoint]]'
- '[[Persistence]]'
commands:
- '[[Get API Gateway Resource]]'
---

# AWS API Gateway Resource Listing

## Summary

The AWS API Gateway Resource Listing procedure involves using the 'Get API Gateway Resource' command to retrieve information about a specific endpoint within an API Gateway. This can be useful for discovering potential entry points into an AWS environment, as well as identifying misconfigured or vu

## Description

# Description

The AWS API Gateway Resource Listing procedure involves using the 'Get API Gateway Resource' command to retrieve information about a specific endpoint within an API Gateway. This can be useful for discovering potential entry points into an AWS environment, as well as identifying misconfigured or vulnerable endpoints.

At a technical level, this procedure involves making an API call to the AWS API Gateway service and providing the appropriate parameters to retrieve information about a specific resource. This procedure can be used by both offensive and defensive security professionals to identify potential vulnerabilities in an AWS environment.

From a business perspective, this procedure can help organizations identify potential security risks and take proactive measures to secure their AWS environment.

## Requirements

1. Valid AWS credentials with appropriate permissions to access the API Gateway service

1. Network access to the API Gateway service

1. AWS CLI or SDK installed

## Defense

1. Ensure that AWS credentials are properly secured and not shared unnecessarily

1. Regularly review and audit API Gateway configurations for misconfigured or vulnerable endpoints

1. Implement network security measures such as firewalls and access controls to limit access to the API Gateway service

## Objectives

1. Retrieve information about a specific endpoint within an AWS API Gateway

1. Identify potential entry points into an AWS environment

1. Identify misconfigured or vulnerable endpoints

# Instructions

1. To get a specific resource in an Amazon API Gateway REST API, use the following command:

**Code**: [[aws apigateway get-resource --rest-api-id ID --res]]

> This command retrieves information about a resource in an API Gateway REST API. The `--rest-api-id` option specifies the ID of the REST API containing the resource, and the `--resource-id` option specifies the ID of the resource to retrieve. This command can be useful for debugging and troubleshooting API Gateway resources.

**Command** ([[Get API Gateway Resource]]):

```bash
aws apigateway get-resource --rest-api-id ID --resource-id ID
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get API Gateway Resource]]

## Tags

- [[Cloud - AWS]]
- [[Listing information about a specific endpoint]]
- [[Persistence]]

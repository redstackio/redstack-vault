---
id: ac24dbd6-aefd-4aa9-b3b3-d8f2bd1db0fc
name: AWS Listing Rest APIs
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.768423+00:00'
updated_at: '2023-04-10T20:20:12.946347+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Listing Rest API''S]]'
- '[[Persistence]]'
commands:
- '[[List all REST APIs]]'
---

# AWS Listing Rest APIs

## Summary

The AWS Listing Rest APIs procedure involves searching for and obtaining a list of all available Rest APIs in an AWS environment. This can be useful for an attacker to identify potential targets for further exploitation or to gain a better understanding of the target's infrastructure. To execute th

## Description

# Description

The AWS Listing Rest APIs procedure involves searching for and obtaining a list of all available Rest APIs in an AWS environment. This can be useful for an attacker to identify potential targets for further exploitation or to gain a better understanding of the target's infrastructure. To execute this procedure, the attacker would first need to gain access to the AWS environment and then use the List Rest APIs command to obtain a list of all available Rest APIs.

From a technical standpoint, this procedure involves making an API call to the AWS environment to retrieve a list of available Rest APIs. The business value of this procedure is that it allows an attacker to gain insights into the target's infrastructure, which can be used to plan further attacks.

## Requirements

1. Access to the target AWS environment

1. Permissions to execute the List Rest APIs command

## Defense

1. Ensure that access to the AWS environment is properly secured with strong authentication mechanisms

1. Implement network segmentation to limit access to sensitive resources

1. Monitor for unauthorized access to the AWS environment and suspicious API calls

## Objectives

1. Identify all available Rest APIs in the target AWS environment

1. Gain insights into the target's infrastructure

# Instructions

1. Use the above command to list all the REST APIs created in your AWS account.

**Code**: [[aws apigateway get-rest-apis]]

> This command retrieves a list of all the REST APIs created in your AWS account. It returns a JSON object containing information such as the API ID, name, description, and endpoint URLs. This command does not require any arguments.

**Command** ([[List all REST APIs]]):

```bash
aws apigateway get-rest-apis
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List all REST APIs]]

## Tags

- [[Cloud - AWS]]
- [[Listing Rest API'S]]
- [[Persistence]]

---
id: 16176625-0362-47b6-a68f-da9036342a44
name: AWS REST API Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.325163+00:00'
updated_at: '2023-04-10T20:20:41.013534+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Service Discovery|T1007 - System Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing Rest API''S]]'
commands:
- '[[Get all REST APIs]]'
---

# AWS REST API Enumeration

## Summary

AWS REST API Enumeration is a technique used to discover and list the available REST APIs in an AWS environment. This technique can be used by an attacker to identify potential entry points into the environment or to gather information for further attacks. By listing the available APIs, an attacker

## Description

# Description

AWS REST API Enumeration is a technique used to discover and list the available REST APIs in an AWS environment. This technique can be used by an attacker to identify potential entry points into the environment or to gather information for further attacks. By listing the available APIs, an attacker can identify the services that are exposed to the internet and potentially vulnerable to attacks. This technique is commonly used in reconnaissance and information gathering phases of an attack. 

To perform this technique, the attacker can use various tools or scripts to query the AWS environment for the available REST APIs. The attacker can then analyze the results to identify any sensitive or critical APIs that can be targeted for further attacks. 

The business value of this technique is to identify potential security gaps in the AWS environment and take appropriate measures to secure the environment.

## Requirements

1. Access to the AWS environment

1. API keys or credentials with appropriate permissions

1. Tools or scripts for querying the AWS environment

## Defense

1. Ensure that unnecessary APIs are not exposed to the internet

1. Implement proper authentication and authorization mechanisms for accessing the APIs

1. Monitor and analyze the logs for any suspicious activity related to API access

## Objectives

1. Discover and list the available REST APIs in an AWS environment

1. Identify potential entry points into the environment

1. Gather information for further attacks

# Instructions

1. To list all the REST APIs in your AWS account, run the following command:

**Code**: [[aws apigateway get-rest-apis]]

> This command retrieves a list of all the REST APIs in your AWS account. You can use this command to get information about the APIs, such as their IDs, names, and descriptions. This command does not require any arguments.

**Command** ([[Get all REST APIs]]):

```bash
aws apigateway get-rest-apis
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Service Discovery|T1007 - System Service Discovery]]

## Commands Used

- [[Get all REST APIs]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing Rest API'S]]

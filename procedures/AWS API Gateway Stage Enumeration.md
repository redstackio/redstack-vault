---
id: 8c99e625-9683-4352-8fe3-c715fa8e2f82
name: AWS API Gateway Stage Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.885072+00:00'
updated_at: '2023-04-10T20:20:33.329009+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials In Files|T1552.001 - Credentials In Files]]'
- '[[DLL Side-Loading|T1574.002 - DLL Side-Loading]]'
tags:
- '[[Cloud - AWS]]'
- '[[Listing all versions of a rest api]]'
- '[[Persistence]]'
commands:
- '[[Get API Gateway Stages]]'
---

# AWS API Gateway Stage Enumeration

## Summary

The AWS API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. An attacker can use the API Gateway Stages command to list all versions of a REST API. This can be useful when trying to identify outdated or vulnera

## Description

# Description

The AWS API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. An attacker can use the API Gateway Stages command to list all versions of a REST API. This can be useful when trying to identify outdated or vulnerable versions of an API. An attacker can use this information to target specific versions of an API to exploit known vulnerabilities or to perform reconnaissance on the target environment.

To use this technique, an attacker would need to have valid AWS credentials and access to the API Gateway service. This technique can be used as part of a larger attack chain to gain access to sensitive data or systems within the target environment.

## Requirements

1. Valid AWS credentials

1. Access to the API Gateway service

## Defense

1. Ensure that AWS credentials are properly secured and rotated on a regular basis

1. Monitor API Gateway activity for suspicious behavior, such as listing all versions of an API

1. Implement access controls to limit who has access to the API Gateway service

## Objectives

1. Identify outdated or vulnerable versions of an API

1. Perform reconnaissance on the target environment

# Instructions

1. Use this command to retrieve a list of stages for a specific API Gateway REST API.

The 'aws apigateway get-stages' command is used to retrieve a list of stages for a specific API Gateway REST API. The '--rest-api-id' argument is used to specify the ID of the REST API for which you want to retrieve the stages. This command can be useful for viewing the stages that are available for an API and for verifying that a new stage has been created successfully. The output of this command will include information about each stage, such as its name, deployment ID, and description.

**Command** ([[Get API Gateway Stages]]):

```bash
aws apigateway get-stages --rest-api-id ID
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Hijack Execution Flow|T1574 - Hijack Execution Flow]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files|T1552.001 - Credentials In Files]]
- [[DLL Side-Loading|T1574.002 - DLL Side-Loading]]

## Commands Used

- [[Get API Gateway Stages]]

## Tags

- [[Cloud - AWS]]
- [[Listing all versions of a rest api]]
- [[Persistence]]

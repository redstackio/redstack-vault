---
id: 24dc5d9d-0bab-46ea-b90b-83f05ebfd840
name: AWS RCE for Credential Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.536371+00:00'
updated_at: '2023-04-10T20:20:14.751160+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[CMSTP|T1191 - CMSTP]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Access]]'
- '[[Getting credentials using RCE]]'
commands:
- '[[Get Environment Variables]]'
---

# AWS RCE for Credential Access

## Summary

AWS RCE for Credential Access is a technique used to gain access to AWS credentials by exploiting a vulnerability in a public-facing application or web-based service. This technique involves using Remote Code Execution (RCE) to execute malicious code on the target system, which can be used to steal

## Description

# Description

AWS RCE for Credential Access is a technique used to gain access to AWS credentials by exploiting a vulnerability in a public-facing application or web-based service. This technique involves using Remote Code Execution (RCE) to execute malicious code on the target system, which can be used to steal sensitive information such as AWS Access Keys or Secret Access Keys. Once these credentials are obtained, the attacker can use them to access and control resources within the AWS environment.

From an offensive perspective, AWS RCE for Credential Access can be used to gain access to sensitive data and resources within an AWS environment. This technique can be particularly effective when combined with other techniques such as lateral movement or privilege escalation.

From a defensive perspective, it is important to ensure that all public-facing applications and web-based services are properly secured and regularly audited for vulnerabilities.

## Requirements

1. Access to a vulnerable public-facing application or web-based service

1. Ability to execute Remote Code on the target system

## Defense

1. Regularly audit public-facing applications and web-based services for vulnerabilities

1. Implement strong authentication and access control measures within the AWS environment

1. Monitor for anomalous activity within the AWS environment, such as unusual resource access or changes to security settings

## Objectives

1. Gain access to AWS credentials

1. Access and control resources within the AWS environment

# Instructions

1. To retrieve system environment variables, make a GET request to the provided URL. The response will contain a list of all the environment variables that are currently set in the system.

This command retrieves the system environment variables that are currently set. These variables can be used by the Lambda function to customize its behavior, such as setting up connection strings, API keys, or other configuration options. The retrieved variables can be used in the Lambda function code to access external resources or perform some specific tasks based on the values of the variables. The retrieved variables can also be used in the API Gateway configuration to control the behavior of the API endpoints.

**Command** ([[Get Environment Variables]]):

```bash
https://apigateway/prod/system?cmd=env
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[CMSTP|T1191 - CMSTP]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[Get Environment Variables]]

## Tags

- [[Cloud - AWS]]
- [[Credential Access]]
- [[Getting credentials using RCE]]

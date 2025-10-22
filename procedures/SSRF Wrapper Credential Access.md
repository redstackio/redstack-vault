---
id: c8e895ae-4136-4b60-8e39-6e9f53f58e54
name: SSRF Wrapper Credential Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.582646+00:00'
updated_at: '2023-04-10T20:20:45.663613+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials in Registry|T1552.002 - Credentials in Registry]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Access]]'
- '[[Getting credentials using SSRF and wrappers]]'
commands:
- '[[Execute System Command]]'
---

# SSRF Wrapper Credential Access

## Summary

SSRF Wrapper Credential Access is a technique that involves exploiting a Server-Side Request Forgery (SSRF) vulnerability to access instance metadata from within a cloud environment. This technique can be used to obtain AWS credentials that are stored within the instance metadata, which can then be

## Description

# Description

SSRF Wrapper Credential Access is a technique that involves exploiting a Server-Side Request Forgery (SSRF) vulnerability to access instance metadata from within a cloud environment. This technique can be used to obtain AWS credentials that are stored within the instance metadata, which can then be used to gain access to other cloud resources. To execute this technique, an attacker sends a crafted request to the targeted application, which is then forwarded by the application to the instance metadata endpoint. The attacker can then extract the AWS credentials from the response and use them to access other resources within the cloud environment.

This technique requires a vulnerable application that accepts user input and makes requests to external resources. A successful attack requires the attacker to have network access to the targeted application and knowledge of the instance metadata endpoint.

## Requirements

1. Access to a vulnerable application that accepts user input and makes requests to external resources

1. Knowledge of the instance metadata endpoint

## Defense

1. Implement input validation and sanitization to prevent SSRF vulnerabilities

1. Restrict network access to instance metadata endpoint

1. Rotate AWS credentials regularly to limit the impact of credential theft

## Objectives

1. Obtain AWS credentials stored within instance metadata

1. Gain access to other cloud resources using obtained credentials

# Instructions

1. To retrieve the environment variables of the system, use the following command:

curl https://apigateway/prod/system?cmd=file:///proc/self/environ

This will return a list of all the environment variables currently set on the system.

The 'cmd' parameter in the URL specifies the command to be executed on the system. In this case, we are executing the 'file' command with the argument '/proc/self/environ', which returns a list of environment variables. The 'curl' command is used to make the HTTP request to the specified URL and retrieve the output of the command.

**Command** ([[Execute System Command]]):

```bash
https://apigateway/prod/system?cmd=file:///proc/self/environ
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials in Registry|T1552.002 - Credentials in Registry]]

## Commands Used

- [[Execute System Command]]

## Tags

- [[Cloud - AWS]]
- [[Credential Access]]
- [[Getting credentials using SSRF and wrappers]]

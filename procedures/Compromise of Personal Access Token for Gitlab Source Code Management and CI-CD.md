---
id: 2ae76e00-18bf-4ae6-9fb3-e3e161c19c47
name: Compromise of Personal Access Token for Gitlab Source Code Management and CI/CD
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.273867+00:00'
updated_at: '2023-04-10T20:34:09.402134+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Personal Access Token]]'
- '[[Source Code Management & CI/CD Compromise]]'
commands:
- '[[Create Personal Access Token for GitLab API]]'
---

# Compromise of Personal Access Token for Gitlab Source Code Management and CI/CD

## Summary

Compromising a Personal Access Token (PAT) for Gitlab Source Code Management and CI/CD allows an attacker to perform actions on behalf of the user who generated the token. This can include cloning or modifying source code repositories, running arbitrary code in CI/CD pipelines, or accessing sensiti

## Description

# Description

Compromising a Personal Access Token (PAT) for Gitlab Source Code Management and CI/CD allows an attacker to perform actions on behalf of the user who generated the token. This can include cloning or modifying source code repositories, running arbitrary code in CI/CD pipelines, or accessing sensitive data such as credentials or API keys. From a technical perspective, this attack can be accomplished through phishing, social engineering, or exploiting vulnerabilities in the Gitlab application. The business value of this attack is significant, as it can result in the theft of intellectual property, disruption of software development processes, and reputational damage for the affected organization.

 

## Requirements

1. Valid credentials for the Gitlab application

1. Access to the network or device where the Gitlab application is hosted

1. Knowledge of the Gitlab Personal Access Token generation process

 

## Defense

1. Implement multi-factor authentication for Gitlab accounts

1. Monitor Gitlab access logs for suspicious activity

1. Enforce least privilege access controls for Gitlab repositories and pipelines

 

## Objectives

1. Obtain a valid Gitlab Personal Access Token

1. Use the token to gain access to Gitlab source code repositories and CI/CD pipelines

1. Execute arbitrary code or access sensitive data within the Gitlab environment

 

# Instructions

1. To create a Personal Access Token in Gitlab, use the following command:

 



**Code**: [[curl -k --request POST --header "PRIVATE-TOKEN: ap]]



> This command creates a Personal Access Token (PAT) in Gitlab, which can be used to authenticate API requests. The `curl` command is used to make a POST request to the Gitlab API endpoint for creating a PAT. The `--header` option is used to specify the `PRIVATE-TOKEN` header, which is the API token used for authentication. The `--data` options are used to specify the name of the token, the expiration date (which is left blank to create a token that never expires), and the scopes that the token should have access to. In this case, the token is given access to the `api`, `read_repository`, and `write_repository` scopes. Finally, the URL for the API endpoint is specified, which includes the user ID of the user for whom the token is being created.



**Command** ([[Create Personal Access Token for GitLab API]]):

```bash
curl -k --request POST --header "PRIVATE-TOKEN: apiToken" --data "name=user-persistence-token" --data "expires_at=" --data "scopes[]=api" --data "scopes[]=read_repository" --data "scopes[]=write_repository" "https://gitlabHost/api/v4/users/UserIDNumber/personal_access_tokens"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Steal Application Access Token|T1528 - Steal Application Access Token]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Create Personal Access Token for GitLab API]]

## Tags

- [[Personal Access Token]]
- [[Source Code Management & CI/CD Compromise]]



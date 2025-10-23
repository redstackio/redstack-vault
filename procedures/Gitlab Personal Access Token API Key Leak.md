---
id: bbe2f6b4-1da4-4ede-8d71-56a2168493f8
name: Gitlab Personal Access Token API Key Leak
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.287122+00:00'
updated_at: '2023-04-06T03:55:53.304117+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[API Key Leaks]]'
- '[[Exploit]]'
- '[[Gitlab Personal Access Token]]'
commands:
- '[[Retrieve Projects]]'
---

# Gitlab Personal Access Token API Key Leak

## Summary

GitLab is a web-based Git repository manager that provides source code management, continuous integration and deployment, and more. GitLab Personal Access Tokens (PATs) allow users to authenticate with GitLab via API. If an attacker gains access to a PAT, they can use it to perform various actions 

## Description

# Description

GitLab is a web-based Git repository manager that provides source code management, continuous integration and deployment, and more. GitLab Personal Access Tokens (PATs) allow users to authenticate with GitLab via API. If an attacker gains access to a PAT, they can use it to perform various actions on behalf of the user. This procedure details how to exploit a Gitlab Personal Access Token leak. An attacker can use this procedure to gain access to sensitive information or perform unauthorized actions on behalf of the user. The technical explanation of this procedure includes sending a curl request to the GitLab API endpoint with the PAT as a parameter. The business value of this procedure is that it can allow attackers to steal sensitive data or perform unauthorized actions, which can lead to reputational damage, financial loss, or legal issues.

 

## Requirements

1. Valid GitLab Personal Access Token

 

## Defense

1. Implement access controls and restrictions on GitLab Personal Access Tokens

1. Monitor GitLab logs for suspicious activity related to API key usage

1. Regularly rotate GitLab Personal Access Tokens to reduce the risk of unauthorized access

 

## Objectives

1. To gain unauthorized access to sensitive information

1. To perform unauthorized actions on behalf of the user

 

# Instructions

1. To exploit a GitLab Personal Access Token leak, run the following command:

 



**Code**: [[curl "https://gitlab.example.com/api/v4/projects?p]]



> The command sends a GET request to the GitLab API endpoint to retrieve a list of projects. The private_token parameter is the GitLab Personal Access Token that is being used to authenticate the request. Replace <your_access_token> with the actual token value.



**Command** ([[Retrieve Projects]]):

```bash
curl "https://gitlab.example.com/api/v4/projects?private_token=<your_access_token>"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[Retrieve Projects]]

## Tags

- [[API Key Leaks]]
- [[Exploit]]
- [[Gitlab Personal Access Token]]



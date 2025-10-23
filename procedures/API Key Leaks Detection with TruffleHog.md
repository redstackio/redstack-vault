---
id: 84c93e3f-df47-43c1-a871-dfc513ce77a8
name: API Key Leaks Detection with TruffleHog
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:51.047962+00:00'
updated_at: '2023-05-26T18:54:15.275796+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[API Key Leaks]]'
- '[[Tools]]'
commands:
- '[[Scan GitHub API endpoint for secrets using TruffleHog]]'
- '[[Scan GitHub organization for secrets using TruffleHog]]'
- '[[Scan GitHub repository for secrets using TruffleHog]]'
- '[[Scan local Git repository for secrets using TruffleHog]]'
---

# API Key Leaks Detection with TruffleHog

## Summary

TruffleHog is an open-source tool designed to search for secrets like API keys, passwords, and other sensitive information in code repositories. It searches the entire commit history of a repository and flags any matches it finds. The tool is highly customizable and can be used to scan a variety of

## Description

# Description

TruffleHog is an open-source tool designed to search for secrets like API keys, passwords, and other sensitive information in code repositories. It searches the entire commit history of a repository and flags any matches it finds. The tool is highly customizable and can be used to scan a variety of code repositories, including Git, GitHub, and Bitbucket. The tool is useful for both offensive and defensive purposes. For attackers, it can help identify sensitive information that can be used to gain unauthorized access to systems or data. For defenders, it can help identify vulnerabilities and prevent attacks before they occur.

 

## Requirements

1. Access to the code repository

1. TruffleHog tool installed

 

## Defense

1. Keep sensitive information like API keys and passwords out of code repositories

1. Use strong authentication mechanisms to prevent unauthorized access to code repositories

1. Regularly scan code repositories for sensitive information using tools like TruffleHog

 

## Objectives

1. Identify sensitive information like API keys and passwords in code repositories

1. Prevent unauthorized access to systems and data

 

# Instructions

1. To scan a GitHub repository for API key leaks, run the following command:

docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/OWNER/REPO

Replace `OWNER` and `REPO` with the appropriate values for the repository you want to scan.

To scan an entire GitHub organization, run:

docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --org=ORG_NAME

Replace `ORG_NAME` with the name of the organization you want to scan.

 



**Code**: [[docker run -it -v "$PWD:/pwd" trufflesecurity/truf]]



> The `--repo` option specifies the repository to scan. The `--org` option specifies the organization to scan. The `--endpoint` option specifies the GitHub API endpoint to use. The `--token` option specifies a GitHub personal access token to use for authentication. The `--concurrency` option specifies the number of concurrent requests to make to the GitHub API.



**Command** ([[Scan GitHub repository for secrets using TruffleHog]]):

```bash
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```





**Command** ([[Scan GitHub organization for secrets using TruffleHog]]):

```bash
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --org=trufflesecurity
```





**Command** ([[Scan local Git repository for secrets using TruffleHog]]):

```bash
trufflehog git https://github.com/trufflesecurity/trufflehog.git
```





**Command** ([[Scan GitHub API endpoint for secrets using TruffleHog]]):

```bash
trufflehog github --endpoint https://api.github.com --org trufflesecurity --token GITHUB_TOKEN --debug --concurrency 2
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[Scan GitHub API endpoint for secrets using TruffleHog]]
- [[Scan GitHub organization for secrets using TruffleHog]]
- [[Scan GitHub repository for secrets using TruffleHog]]
- [[Scan local Git repository for secrets using TruffleHog]]

## Tags

- [[API Key Leaks]]
- [[Tools]]



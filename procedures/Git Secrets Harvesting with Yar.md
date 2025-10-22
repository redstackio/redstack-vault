---
id: 6fcd1c1c-61f6-45b5-abf6-977e0bb6b0fc
name: Git Secrets Harvesting with Yar
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.149950+00:00'
updated_at: '2023-04-10T20:33:56.935154+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
tags:
- '[[Git]]'
- '[[Harvesting secrets]]'
- '[[Insecure Source Code Management]]'
- '[[Tools]]'
- '[[Yar]]'
commands:
- '[[Install yar]]'
- '[[Run yar]]'
---

# Git Secrets Harvesting with Yar

## Summary

Git is a widely used source code management tool that contains sensitive information such as passwords, API keys, and other secrets. Attackers can harvest these secrets by using tools such as Yar. Yar is a command-line tool that scans Git repositories for secrets and other sensitive information. It

## Description

# Description

Git is a widely used source code management tool that contains sensitive information such as passwords, API keys, and other secrets. Attackers can harvest these secrets by using tools such as Yar. Yar is a command-line tool that scans Git repositories for secrets and other sensitive information. It can be used to search for secrets in an organization's Git repositories and can help identify potential vulnerabilities that can be exploited by attackers. The tool is simple to use and can be integrated into an organization's security testing process to identify potential security risks.

## Requirements

1. Access to the Git repository

1. Installation of Yar tool

## Defense

1. Ensure that sensitive information such as passwords and API keys are not stored in Git repositories

1. Implement access controls to limit who can access Git repositories

1. Regularly scan Git repositories for sensitive information using tools such as Yar

## Objectives

1. Identify secrets and sensitive information in Git repositories

1. Assess the security of an organization's Git repositories

1. Improve the security of an organization's Git repositories

# Instructions

1. To use Yar to harvest secrets from a Git repository, follow these steps:

**Code**: [[go get github.com/nielsing/yar # https://github.co]]

> 1. Install Yar by running the command 'go get github.com/nielsing/yar'
2. Navigate to the Git repository you want to scan
3. Run the command 'yar -o orgname --both'
4. Yar will scan the repository and output any secrets or sensitive information it finds.

**Command** ([[Install yar]]):

```bash
go get github.com/nielsing/yar
```

**Command** ([[Run yar]]):

```bash
yar -o orgname --both
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Information Repositories|T1213 - Data from Information Repositories]]

## Commands Used

- [[Install yar]]
- [[Run yar]]

## Tags

- [[Git]]
- [[Harvesting secrets]]
- [[Insecure Source Code Management]]
- [[Tools]]
- [[Yar]]

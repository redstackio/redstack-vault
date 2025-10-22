---
id: 50659863-ad69-487c-965b-c39067111b6e
name: Git Repository Secrets Harvesting with Trufflehog
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.117184+00:00'
updated_at: '2023-04-10T20:33:53.515540+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tags:
- '[[Git]]'
- '[[Harvesting secrets]]'
- '[[Insecure Source Code Management]]'
- '[[Tools]]'
- '[[trufflehog]]'
commands:
- '[[Install truffleHog]]'
- '[[Run truffleHog]]'
---

# Git Repository Secrets Harvesting with Trufflehog

## Summary

Git repositories often contain sensitive information such as passwords, API keys, and other secrets. Trufflehog is a tool that can be used to search Git repositories for secrets by performing a regex search on the contents of each file in a repository's commit history. This tool can be used by atta

## Description

# Description

Git repositories often contain sensitive information such as passwords, API keys, and other secrets. Trufflehog is a tool that can be used to search Git repositories for secrets by performing a regex search on the contents of each file in a repository's commit history. This tool can be used by attackers to harvest credentials and other sensitive information that may be stored in a repository. By using trufflehog, an attacker can quickly and easily identify secrets that have been accidentally committed to a repository, or that have been added to a repository by a developer who is not following best practices for secure coding. This tool can also be used by defenders to identify sensitive information that may have been accidentally committed to a repository and to remediate the issue before an attacker can exploit it.

## Requirements

1. Access to a Git repository

1. Installation of trufflehog tool

## Defense

1. Ensure that sensitive information is not stored in Git repositories.

1. Implement secure coding practices to prevent secrets from being added to repositories.

1. Implement access controls to prevent unauthorized access to Git repositories.

## Objectives

1. Identify sensitive information that has been accidentally committed to a Git repository.

1. Identify credentials and other secrets that may have been added to a repository by a developer who is not following best practices for secure coding.

1. Remediate any issues identified by trufflehog to prevent attackers from exploiting sensitive information.

# Instructions

1. 1. Install trufflehog by running the command 'pip install truffleHog' in a terminal window.
2. Run the trufflehog command, specifying the repository URL as an argument. For example, 'truffleHog --regex --entropy=False https://github.com/dxa4481/truffleHog.git'.
3. Review the output of the trufflehog command to identify any sensitive information that has been committed to the repository.

**Code**: [[pip install truffleHog # https://github.com/dxa448]]

> The trufflehog tool searches the contents of each file in a Git repository's commit history for strings that match a regular expression. The --regex option specifies that a regex search should be performed, and the --entropy=False option specifies that entropy analysis should not be performed. The repository URL is provided as an argument to the trufflehog command.

**Command** ([[Install truffleHog]]):

```bash
pip install truffleHog # https://github.com/dxa4481/truffleHog
```

**Command** ([[Run truffleHog]]):

```bash
truffleHog --regex --entropy=False https://github.com/dxa4481/truffleHog.git
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]
- [[Modify Authentication Process|T1556 - Modify Authentication Process]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Commands Used

- [[Install truffleHog]]
- [[Run truffleHog]]

## Tags

- [[Git]]
- [[Harvesting secrets]]
- [[Insecure Source Code Management]]
- [[Tools]]
- [[trufflehog]]

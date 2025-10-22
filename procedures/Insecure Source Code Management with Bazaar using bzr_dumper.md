---
id: 5f3c899e-554f-4acb-bc4b-066c4a2f9bfb
name: Insecure Source Code Management with Bazaar using bzr_dumper
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.362248+00:00'
updated_at: '2023-04-10T20:33:52.054962+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
sub_techniques:
- '[[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]'
tags:
- '[[Bazaar]]'
- '[[bzr_dumper]]'
- '[[Insecure Source Code Management]]'
- '[[Tools]]'
commands:
- '[[Clone git repository]]'
- '[[Create standalone tree]]'
- '[[Revert changes]]'
---

# Insecure Source Code Management with Bazaar using bzr_dumper

## Summary

Insecure Source Code Management with Bazaar using bzr_dumper is a technique that can be used to extract source code from a Bazaar repository. This technique is used when the target has an insecurely configured Bazaar repository. The bzr_dumper tool can be used to extract the source code from the ta

## Description

# Description

Insecure Source Code Management with Bazaar using bzr_dumper is a technique that can be used to extract source code from a Bazaar repository. This technique is used when the target has an insecurely configured Bazaar repository. The bzr_dumper tool can be used to extract the source code from the target's repository. The tool works by cloning the repository and then extracting the source code using various GET requests. This technique can be used to gain access to sensitive source code, including credentials and other sensitive information. The business value of this technique is that it allows an attacker to gain access to sensitive information that can be used to further compromise the target's systems.

## Requirements

1. Access to an insecurely configured Bazaar repository

1. Python 3

## Defense

1. Securely configure Bazaar repositories by using authentication and access controls.

1. Regularly monitor Bazaar repositories for unauthorized access or changes.

1. Use secure coding practices to minimize the impact of source code leaks.

## Objectives

1. Gain access to sensitive source code

1. Extract credentials and other sensitive information

# Instructions

1. To use this technique, first clone the Bazaar repository using the `git clone` command. Then, use the `dumper.py` script from the `bzr_dumper` tool to extract the source code. The `-u` option specifies the URL of the target repository, and the `-o` option specifies the output directory for the extracted source code.

**Code**: [[git clone https://github.com/SeahunOh/bzr_dumper
p]]

> The `dumper.py` script works by making various GET requests to the target repository. The script extracts the source code and saves it to the output directory. The `bzr revert` command is used to remove the cloned repository.

**Command** ([[Clone git repository]]):

```bash
git clone https://github.com/SeahunOh/bzr_dumper
```

**Command** ([[Create standalone tree]]):

```bash
python3 dumper.py -u "http://127.0.0.1:5000/" -o source
```

**Command** ([[Revert changes]]):

```bash
bzr revert
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]

### Sub-Techniques

- [[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]

## Commands Used

- [[Clone git repository]]
- [[Create standalone tree]]
- [[Revert changes]]

## Tags

- [[Bazaar]]
- [[bzr_dumper]]
- [[Insecure Source Code Management]]
- [[Tools]]

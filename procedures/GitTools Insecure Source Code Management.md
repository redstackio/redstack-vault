---
id: fca71fe6-8638-40f3-bbe6-215b608b89e0
name: GitTools Insecure Source Code Management
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.083950+00:00'
updated_at: '2023-04-10T20:33:55.232299+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Automated Exfiltration|T1020 - Automated Exfiltration]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
tags:
- '[[Automatic recovery]]'
- '[[Git]]'
- '[[GitTools]]'
- '[[Insecure Source Code Management]]'
- '[[Tools]]'
commands:
- '[[Checkout Git repository]]'
- '[[Clone GitTools repository]]'
- '[[Dump Git repository]]'
---

# GitTools Insecure Source Code Management

## Summary

GitTools is a collection of tools for interacting with and exploiting Git repositories. The gitdumper.sh script can be used to clone a target's .git repository and then checkout the entire repository. If the target's .git repository is not properly secured, this tool can be used to exfiltrate sensi

## Description

# Description

GitTools is a collection of tools for interacting with and exploiting Git repositories. The gitdumper.sh script can be used to clone a target's .git repository and then checkout the entire repository. If the target's .git repository is not properly secured, this tool can be used to exfiltrate sensitive information such as passwords, source code, and other sensitive information. This tool can be used by an attacker to gain access to sensitive information and pivot to other systems within the network.

 

## Requirements

1. Access to the target's .git repository

1. GitTools installed on the attacker's system

 

## Defense

1. Secure the .git repository by restricting access to authorized users only

1. Monitor for any unauthorized access to the .git repository

1. Regularly review and audit the access control policies for the .git repository

 

## Objectives

1. Clone a target's .git repository

1. Exfiltrate sensitive information from the repository

1. Checkout the entire repository

 

# Instructions

1. Run the following commands:

 



**Code**: [[git clone https://github.com/internetwache/GitTool]]



> The first command clones GitTools from the official repository. The second command uses gitdumper.sh to clone the target's .git repository to the specified destination directory. The third command checks out all the files in the repository to the current directory.



**Command** ([[Clone GitTools repository]]):

```bash
git clone https://github.com/internetwache/GitTools
```





**Command** ([[Dump Git repository]]):

```bash
./gitdumper.sh http://target.tld/.git/ /tmp/destdir
```





**Command** ([[Checkout Git repository]]):

```bash
git checkout -- .
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Automated Exfiltration|T1020 - Automated Exfiltration]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

## Commands Used

- [[Checkout Git repository]]
- [[Clone GitTools repository]]
- [[Dump Git repository]]

## Tags

- [[Automatic recovery]]
- [[Git]]
- [[GitTools]]
- [[Insecure Source Code Management]]
- [[Tools]]



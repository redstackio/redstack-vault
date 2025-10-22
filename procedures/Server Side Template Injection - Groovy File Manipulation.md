---
id: 7594c426-8111-4de7-bd71-5afe6e88e7d2
name: Server Side Template Injection - Groovy File Manipulation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.138911+00:00'
updated_at: '2023-04-10T20:23:42.025337+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[File Permissions Modification|T1222 - File Permissions Modification]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Groovy]]'
- '[[Groovy - Read and create File]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Create new file]]'
- '[[Read text from file]]'
---

# Server Side Template Injection - Groovy File Manipulation

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server-side. In this specific case, the attacker is exploiting a vulnerability in Groovy, a popular scripting language used in Java applications. By using the 'File Manipulation' comman

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server-side. In this specific case, the attacker is exploiting a vulnerability in Groovy, a popular scripting language used in Java applications. By using the 'File Manipulation' command, the attacker can read and create files on the server, potentially allowing them to access sensitive information or upload malicious files. This technique can be used to achieve lateral movement or persistence on the target network.

From a technical perspective, the attacker is injecting malicious code into the Groovy template engine, which is then executed on the server-side. This allows the attacker to bypass any client-side security controls and execute arbitrary code on the server. From a business perspective, this attack can result in data theft, data destruction, or ransomware attacks, which can have a significant impact on the victim organization's reputation, financial stability, and legal liabilities.

## Requirements

1. Access to the target network

1. Knowledge of the target application's use of Groovy templates

1. Ability to inject malicious code into Groovy templates

## Defense

1. Implement input validation and output encoding to prevent SSTI vulnerabilities

1. Restrict access to sensitive files and directories on the server

1. Monitor for suspicious file creation or modification activities on the server

## Objectives

1. Read sensitive files on the server

1. Create new files on the server

1. Achieve lateral movement on the target network

1. Maintain persistence on the target network

# Instructions

1. This command is used for file manipulation. It can be used to read, write, or create files. The first line of code reads the contents of the notepad.exe file located in the C:/Windows directory and stores it in a variable named x. The second line of code reads the contents of a file located at the specified path and stores it in a variable named x. The third line of code creates a new file with the specified name and location.

**Code**: [[${String x = new File('c:/windows/notepad.exe').te]]

> The first argument of the File constructor specifies the path of the file to be manipulated. The getText method is used to read the contents of the file in the specified encoding. The createNewFile method is used to create a new file with the specified name and location.

**Command** ([[Read text from file]]):

```bash
${String x = new File('/path/to/file').getText('UTF-8')}
```

**Command** ([[Create new file]]):

```bash
${new File("C:\Temp\FileName.txt").createNewFile();}
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[File Permissions Modification|T1222 - File Permissions Modification]]
- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Create new file]]
- [[Read text from file]]

## Tags

- [[Groovy]]
- [[Groovy - Read and create File]]
- [[Server Side Template Injection]]

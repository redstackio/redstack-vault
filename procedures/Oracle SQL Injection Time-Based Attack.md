---
id: 11908b7e-0e9c-4402-9035-861c6028a6ac
name: Oracle SQL Injection Time-Based Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.281634+00:00'
updated_at: '2023-04-10T20:23:10.333500+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Non-Standard Port|T1571 - Non-Standard Port]]'
tags:
- '[[Oracle SQL Injection]]'
- '[[Oracle SQL Time based]]'
---

# Oracle SQL Injection Time-Based Attack

## Summary

The Oracle SQL Injection Time-Based Attack is a technique used by attackers to inject malicious SQL queries into an Oracle database. This technique is used to extract sensitive information from the database or to perform unauthorized actions. The attacker can use the Receive Message from DBMS_PIPE 

## Description

# Description

The Oracle SQL Injection Time-Based Attack is a technique used by attackers to inject malicious SQL queries into an Oracle database. This technique is used to extract sensitive information from the database or to perform unauthorized actions. The attacker can use the Receive Message from DBMS_PIPE command to send SQL queries to the database and retrieve the results. By using time-based techniques, the attacker can delay the response of the database to extract information without being detected.

From a technical perspective, the attacker can use the time delay function in the SQL query to perform the attack. The attacker can inject a time delay into the query and use the Receive Message from DBMS_PIPE command to retrieve the results. This technique can be used to extract sensitive information, such as usernames and passwords, from the database.

The business value of this attack is that it can be used to gain unauthorized access to sensitive information stored in the database. This can lead to financial loss, reputational damage, and legal consequences for the organization.

## Requirements

1. Access to the Oracle database

1. Knowledge of SQL injection techniques

1. The Receive Message from DBMS_PIPE command

## Defense

1. Implement input validation and parameterized queries to prevent SQL injection attacks

1. Use database monitoring tools to detect and alert on suspicious activity

1. Limit access to the database to only authorized users and implement strong authentication mechanisms

## Objectives

1. Extract sensitive information from the Oracle database

1. Perform unauthorized actions on the database

# Instructions

1. This command receives a message from the named pipe using the DBMS_PIPE package. The message is received into the buffer variable specified in the command. The name of the named pipe is specified in the '[RANDSTR]' parameter, and the amount of time to wait for the message is specified in the [SLEEPTIME] parameter.

**Code**: [[AND [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]]]

> The DBMS_PIPE package is used to send messages between sessions in Oracle. The RECEIVE_MESSAGE function is used to receive a message from a named pipe. The '[RANDSTR]' parameter specifies the name of the named pipe to receive from. The [SLEEPTIME] parameter specifies the amount of time to wait for a message to arrive. If a message arrives within the specified time, it is stored in the buffer variable specified in the command. If no message arrives within the specified time, the function returns 0.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Non-Standard Port|T1571 - Non-Standard Port]]

## Tags

- [[Oracle SQL Injection]]
- [[Oracle SQL Time based]]

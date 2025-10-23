---
id: cbc9a144-243d-4a29-8761-2c557cda1c30
name: RDS Password-based Authentication Data Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.017071+00:00'
updated_at: '2023-04-10T20:20:30.249176+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
sub_techniques:
- '[[Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 - Exfiltration Over Unencrypted
  Non-C2 Protocol]]'
tags:
- '[[Data exfiltration]]'
- '[[Password based authentication]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[Connect to MySQL server]]'
---

# RDS Password-based Authentication Data Exfiltration

## Summary

RDS is a managed database service provided by AWS. In this procedure, an attacker with valid credentials and password-based authentication can exfiltrate data from an RDS instance. The attacker can connect to the MySQL server using the provided command and then use various SQL queries to extract se

## Description

# Description

RDS is a managed database service provided by AWS. In this procedure, an attacker with valid credentials and password-based authentication can exfiltrate data from an RDS instance. The attacker can connect to the MySQL server using the provided command and then use various SQL queries to extract sensitive data. This attack can be performed remotely and may go unnoticed for extended periods.

Technical Explanation: An attacker can use the provided command to connect to the MySQL server of the RDS instance. Once connected, the attacker can use SQL queries to read and exfiltrate sensitive data. The attacker can also use SQL injection techniques to modify data, which can lead to data corruption or further compromise.

Business Value: An attacker can use this procedure to steal sensitive data and use it for financial gain or competitive advantage. This attack can also lead to reputational damage and loss of customer trust.

 

## Requirements

1. Valid credentials with password-based authentication

1. Network access to the RDS instance

1. Knowledge of SQL queries and injection techniques

 

## Defense

1. Use multi-factor authentication (MFA) to prevent unauthorized access to RDS instances

1. Encrypt sensitive data stored in RDS instances to prevent data exfiltration

1. Monitor network traffic for suspicious activity and SQL injection attempts

 

## Objectives

1. Exfiltrate sensitive data from an RDS instance

1. Avoid detection and maintain access to the data

 

# Instructions

1. To connect to a MySQL server, use the 'mysql' command followed by the necessary arguments. 

The arguments are as follows:

-h or --host: Specifies the host name or IP address of the MySQL server. 
-u or --user: Specifies the MySQL user name to use when connecting to the server. 
-P or --port: Specifies the TCP/IP port number to use for the connection. 
-p or --password: Specifies the password to use when connecting to the server. 

Example: mysql -h localhost -u root -P 3306 -p

 

This command is used to connect to a MySQL server using the command line. The user must have the necessary permissions to access the server. Once connected, the user can execute SQL commands on the server.



**Command** ([[Connect to MySQL server]]):

```bash
mysql -h hostname -u name -P port -p password
```



## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

### Sub-Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 - Exfiltration Over Unencrypted Non-C2 Protocol]]

## Commands Used

- [[Connect to MySQL server]]

## Tags

- [[Data exfiltration]]
- [[Password based authentication]]
- [[RDS - Relational Database Service]]



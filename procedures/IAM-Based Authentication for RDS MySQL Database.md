---
id: 85beb649-4de9-422c-aa7b-409b1b78746d
name: IAM-Based Authentication for RDS MySQL Database
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.079586+00:00'
updated_at: '2023-04-10T20:20:55.149059+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Data exfiltration]]'
- '[[IAM Based authentication]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[Connect to MySQL server]]'
- '[[Generate RDS DB Auth Token]]'
---

# IAM-Based Authentication for RDS MySQL Database

## Summary

IAM-Based Authentication for RDS MySQL Database is a technique that leverages AWS Identity and Access Management (IAM) to authenticate and authorize access to RDS MySQL databases. This technique allows users to generate an authentication token using the Generate RDS DB Auth Token command, and then 

## Description

# Description

IAM-Based Authentication for RDS MySQL Database is a technique that leverages AWS Identity and Access Management (IAM) to authenticate and authorize access to RDS MySQL databases. This technique allows users to generate an authentication token using the Generate RDS DB Auth Token command, and then use the token to connect to the MySQL database using the Connect to MySQL Database using Token command. This technique is useful for preventing unauthorized access to RDS MySQL databases and for securing sensitive data stored within the database.

## Requirements

1. AWS Identity and Access Management (IAM) user or role with appropriate permissions

1. Access to RDS MySQL database

1. AWS CLI or other tool that supports IAM-based authentication

## Defense

1. Ensure that IAM users and roles have appropriate permissions to access RDS MySQL databases

1. Use network security controls, such as firewalls, to restrict access to RDS MySQL databases

1. Monitor database activity for unusual or suspicious behavior

## Objectives

1. Authenticate and authorize access to RDS MySQL databases

1. Prevent unauthorized access to RDS MySQL databases

1. Secure sensitive data stored within RDS MySQL databases

# Instructions

1. To generate a database authentication token for an Amazon RDS DB instance, use the `aws rds generate-db-auth-token` command. The command requires the following arguments:

- `hostname`: The hostname of the DB instance.
- `port`: The port number on which the DB instance accepts connections.
- `username`: The name of the user to authenticate.
- `region`: The AWS region in which the DB instance is located.

The command returns a token that can be used to authenticate to the DB instance.

This command generates a database authentication token that can be used to authenticate to an Amazon RDS DB instance. The token is generated using the hostname, port, username, and region of the DB instance. Once the token is generated, it can be used to authenticate to the DB instance using any tool that supports AWS Signature Version 4. For example, you can use the token with the `mysql` command-line tool by setting the `MYSQL_PWD` environment variable to the token and using the `--ssl-ca` option to specify the SSL certificate authority file. This allows you to connect to the DB instance securely without having to store the DB password in plain text.

**Command** ([[Generate RDS DB Auth Token]]):

```bash
TOKEN=$(aws rds generate-db-auth-token --hostname hostname --port port --username username --region region)
```

2. To connect to a MySQL database using a token, use the following command:

**Code**: [[mysql -h hostname -u name -P port --enable-clearte]]

> The `mysql` command is used to connect to a MySQL database. The `-h` flag specifies the hostname of the server where the database is located. The `-u` flag specifies the username to use when connecting. The `-P` flag specifies the port number to use for the connection. The `--enable-cleartext-plugin` flag is used to enable cleartext authentication. The `--user` flag specifies the user to authenticate as. The `--password` flag is used to specify the token to use for authentication.

**Command** ([[Connect to MySQL server]]):

```bash
mysql -h hostname -u name -P port --enable-cleartext-plugin --user=user --password=$TOKEN
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Exfiltration|TA0010 - Exfiltration]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Connect to MySQL server]]
- [[Generate RDS DB Auth Token]]

## Tags

- [[Data exfiltration]]
- [[IAM Based authentication]]
- [[RDS - Relational Database Service]]

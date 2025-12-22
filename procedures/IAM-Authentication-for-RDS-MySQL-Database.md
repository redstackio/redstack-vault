---
id: 85beb649-4de9-422c-aa7b-409b1b78746d
name: IAM-Authentication-for-RDS-MySQL-Database
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.079586+00:00'
updated_at: '2023-04-10T20:20:55.149059+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/Data exfiltration]]'
  - '[[tags/IAM Based authentication]]'
  - '[[tags/RDS - Relational Database Service]]'
commands:
  - '[[commands/Generate-RDS-DB-Auth-Token]]'
  - '[[commands/Connect-to-RDS-MySQL-with-IAM-Token]]'
platforms:
  - AWS
  - Linux
tools: []
validated: true
---

# IAM-Authentication-for-RDS-MySQL-Database

## Summary

This procedure demonstrates how to use AWS Identity and Access Management (IAM) for authenticating to an Amazon RDS MySQL database instance without relying on traditional database passwords. By generating a temporary authentication token via the AWS CLI and using it with the MySQL client, attackers or testers can gain access to the database using valid IAM credentials, enabling data exfiltration, persistence, or privilege escalation in cloud environments.

## Description

IAM database authentication allows IAM users or roles to connect to RDS MySQL instances by generating a short-lived authentication token that acts as a password. This method leverages AWS Signature Version 4 for secure, token-based access, avoiding the need to store static database credentials. In offensive security scenarios, this technique is useful for maintaining access to cloud databases using compromised IAM roles, exfiltrating sensitive data over alternative protocols, or evading detection by using legitimate AWS mechanisms. The process involves generating the token with AWS CLI and then connecting via the MySQL client with cleartext plugin enabled to handle the token format. Prerequisites include IAM permissions like rds-db:connect on the database resource.

## Requirements

1. AWS CLI installed and configured with IAM credentials that have rds-db:connect permission on the target RDS instance.
2. Access to the RDS MySQL database endpoint, including hostname, port (default 3306), and username (mapped to IAM user).
3. MySQL client installed on the attacking machine (e.g., via apt install mysql-client on Linux).
4. Network connectivity to the RDS instance, potentially requiring VPC peering or security group adjustments.

## Defense

- Restrict IAM policies to least privilege, ensuring only necessary roles have rds-db:connect permissions on specific RDS resources.
- Use network security controls like VPC security groups, NACLs, and firewalls to limit access to RDS endpoints from unauthorized sources.
- Monitor AWS CloudTrail for generate-db-auth-token API calls and RDS connection logs for unusual authentication patterns or high-frequency token generations.
- Enable RDS logging and integrate with tools like Amazon GuardDuty or third-party SIEM for anomaly detection in database access.

## Objectives

1. Generate a temporary authentication token using IAM credentials to access the RDS MySQL database.
2. Establish a secure connection to the database without exposing static passwords, enabling data querying or modification.
3. Facilitate exfiltration of sensitive data or maintain persistence in AWS environments using valid accounts.

## Instructions

### Step 1: Generate Authentication Token

**Context**: Use the AWS CLI to create a temporary token based on the RDS instance details and IAM credentials. This token expires after 15 minutes, providing time-limited access.

**Command** ([[commands/Generate-RDS-DB-Auth-Token]]):
```bash
TOKEN=$(aws rds generate-db-auth-token --hostname $_RDS_HOSTNAME --port $_RDS_PORT --username $_DB_USERNAME --region $_AWS_REGION)
```

> This command calls the AWS RDS API to generate a token signed with the IAM credentials. The token is base64-encoded and includes a timestamp for expiration. Verify the token generation by checking for a long string output without errors like "AccessDenied". If successful, the $TOKEN variable holds the auth string ready for use in the MySQL client.

### Step 2: Connect to RDS MySQL Database

**Context**: Use the generated token as the password in the MySQL client connection, enabling cleartext authentication to bypass traditional password handling. This step establishes an interactive session for querying the database.

**Command** ([[commands/Connect-to-RDS-MySQL-with-IAM-Token]]):
```bash
mysql -h $_RDS_HOSTNAME -u $_DB_USERNAME -P $_RDS_PORT --enable-cleartext-plugin --password=$TOKEN
```

> The MySQL client connects to the RDS instance using the token for authentication. The --enable-cleartext-plugin flag allows the client to send the token in cleartext, as required for IAM auth. Upon success, you enter the MySQL prompt (mysql>), where you can run queries like SHOW DATABASES; to verify access. If the token expires mid-session, regenerate and reconnect. Common errors include handshake failures if the plugin is not enabled or if IAM permissions are insufficient.

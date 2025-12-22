---
id: 677cc791-aa32-4c2f-8322-0ae64be83575
name: Generate-RDS-DB-Auth-Token
type: command
executor: bash
data: >-
  TOKEN=$(aws rds generate-db-auth-token --hostname $_RDS_HOSTNAME --port
  $_RDS_PORT --username $_DB_USERNAME --region $_AWS_REGION)
output: null
created_at: '2023-04-06T03:56:14.073780+00:00'
updated_at: '2023-04-10T20:20:55.168825+00:00'
platforms:
  - AWS
  - Linux
tags:
  - iam
  - rds
  - authentication
verified: true
validated: true
---

# Generate-RDS-DB-Auth-Token

## Command

```bash
TOKEN=$(aws rds generate-db-auth-token --hostname $_RDS_HOSTNAME --port $_RDS_PORT --username $_DB_USERNAME --region $_AWS_REGION)
```

## Description

This command generates a temporary authentication token for connecting to an Amazon RDS MySQL database using IAM credentials. The token serves as a password and is valid for 15 minutes, enabling secure, passwordless access to the database.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RDS_HOSTNAME | The DB instance endpoint (e.g., mydb.cluster-abc123.us-east-1.rds.amazonaws.com) | Yes |
| $_RDS_PORT | The port number for the DB instance (default 3306) | Yes |
| $_DB_USERNAME | The database username mapped to the IAM role/user | Yes |
| $_AWS_REGION | The AWS region of the RDS instance (e.g., us-east-1) | Yes |
| --hostname | Specifies the DB endpoint | Built-in |
| --port | Specifies the connection port | Built-in |
| --username | Specifies the DB user for authentication | Built-in |
| --region | Specifies the AWS region | Built-in |

## Examples

### Basic Usage

```bash
TOKEN=$(aws rds generate-db-auth-token --hostname mydb.abc123.us-east-1.rds.amazonaws.com --port 3306 --username dbuser --region us-east-1)
```

### Advanced Usage

For scripting, export the token:
```bash
export TOKEN=$(aws rds generate-db-auth-token --hostname $_RDS_HOSTNAME --port $_RDS_PORT --username $_DB_USERNAME --region $_AWS_REGION)
echo $TOKEN
```

## Expected Output

A long base64-encoded string representing the authentication token, e.g.,
```
myrdsdbinstance.us-east-1.rds.amazonaws.com:3306/?Action=connect&CurrentTime=...&Signature=...
```
No output if assigned to a variable; errors like "An error occurred (AccessDenied) when calling the GenerateDBAuthToken operation" indicate permission issues.

## Related

- [[procedures/IAM-Authentication-for-RDS-MySQL-Database]]
- [[commands/Connect-to-RDS-MySQL-with-IAM-Token]]

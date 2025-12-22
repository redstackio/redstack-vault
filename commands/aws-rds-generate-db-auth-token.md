---
id: 677cc791-aa32-4c2f-8322-0ae64be83575
name: aws-rds-generate-db-auth-token
type: command
executor: bash
data: >-
  TOKEN=$(aws rds generate-db-auth-token --hostname $_RDS_HOSTNAME --port $_PORT
  --username $_DB_USERNAME --region $_REGION)
output: null
created_at: '2023-04-06T03:56:14.073780+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - rds
  - auth
  - exfiltration
verified: true
validated: true
---

# aws-rds-generate-db-auth-token

## Command

```bash
TOKEN=$(aws rds generate-db-auth-token --hostname $_RDS_HOSTNAME --port $_PORT --username $_DB_USERNAME --region $_REGION)
```

## Description

This command generates a temporary authentication token for IAM-based access to an RDS database instance. The token acts as a password for database clients and expires in 15 minutes, enabling exfiltration without static credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --hostname $_RDS_HOSTNAME | RDS endpoint hostname (e.g., mydb.abcdef.us-east-1.rds.amazonaws.com) | Yes |
| --port $_PORT | Database port (e.g., 3306 for MySQL) | Yes |
| --username $_DB_USERNAME | Database username (e.g., admin) | Yes |
| --region $_REGION | AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
TOKEN=$(aws rds generate-db-auth-token --hostname mydb.abcdef.us-east-1.rds.amazonaws.com --port 3306 --username admin --region us-east-1)
echo $TOKEN
```

### Integration with Client

```bash
TOKEN=$(aws rds generate-db-auth-token --hostname $_RDS_HOSTNAME --port $_PORT --username $_DB_USERNAME --region $_REGION)
mysql -h $_RDS_HOSTNAME -P $_PORT -u $_DB_USERNAME -p$TOKEN mydb
```

## Expected Output

A base64-encoded token string, e.g., "BOOTSTRAP...==". Use it immediately in a database client; success allows query execution, failure indicates insufficient permissions.

## Related

- [[procedures/IAM-Based-Authentication-Data-Exfiltration-via-RDS]]

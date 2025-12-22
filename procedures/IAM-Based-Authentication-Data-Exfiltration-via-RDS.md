---
id: 3bf18aca-8f10-4e1f-a2ac-9a42ee41957b
name: IAM-Based-Authentication-Data-Exfiltration-via-RDS
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.046450+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques:
  - >-
    [[sub-techniques/Exfiltration Over Asymmetric Encrypted Non-C2
    Protocol|T1048.002 - Exfiltration Over Asymmetric Encrypted Non-C2
    Protocol]]
  - >-
    [[sub-techniques/Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 -
    Exfiltration Over Unencrypted Non-C2 Protocol]]
tags:
  - '[[tags/Data exfiltration]]'
  - '[[tags/IAM Based authentication]]'
  - '[[tags/RDS - Relational Database Service]]'
commands:
  - '[[commands/aws-sts-get-caller-identity]]'
  - '[[commands/aws-iam-list-attached-role-policies]]'
  - '[[commands/aws-iam-get-policy-version]]'
  - '[[commands/aws-rds-generate-db-auth-token]]'
platforms:
  - AWS
tools: []
validated: true
---

# IAM-Based-Authentication-Data-Exfiltration-via-RDS

## Summary

This procedure outlines how attackers with compromised IAM credentials can leverage IAM-based authentication to generate temporary tokens for accessing AWS RDS instances, enabling data exfiltration without traditional database passwords. It covers identifying the current IAM context, enumerating role policies, retrieving policy details, and generating auth tokens to connect to the database and extract sensitive information.

## Description

IAM-based authentication for RDS allows users to authenticate to MySQL or PostgreSQL databases using AWS IAM credentials instead of passwords. Attackers who have obtained IAM access keys or assumed roles with RDS permissions can generate short-lived authentication tokens via the AWS CLI or SDK. These tokens can then be used with database clients like mysql or psql to query and exfiltrate data over alternative protocols. This technique is particularly dangerous in environments with over-privileged IAM roles, as it bypasses password-based controls and can lead to the theft of customer records, financial data, or other sensitive information stored in RDS. The procedure assumes the attacker has initial IAM access and focuses on the authentication and exfiltration steps, mapping to MITRE ATT&CK for exfiltration over alternative protocols.

## Requirements

1. AWS CLI v2 installed and configured with IAM credentials that have permissions for STS, IAM, and RDS services (e.g., rds-db:connect).
2. Knowledge of the target RDS instance details: hostname, port (default 3306 for MySQL, 5432 for PostgreSQL), database username, and AWS region.
3. Network access to the RDS endpoint (e.g., via VPC peering, bastion host, or direct internet if publicly accessible).
4. A database client tool like mysql or psql installed to use the generated token for connections.

## Defense

- Enforce least privilege IAM policies, explicitly denying rds-db:connect where unnecessary and using resource-based policies on RDS clusters.
- Enable AWS CloudTrail logging for API calls to STS, IAM, and RDS; monitor for anomalous generate-db-auth-token invocations or policy enumerations.
- Implement RDS encryption at rest and in transit, combined with database-level row/column access controls (e.g., MySQL roles).
- Use AWS Config rules to detect over-privileged roles and enable MFA for IAM users.

## Objectives

1. Verify the current IAM identity and permissions to ensure viable access for exfiltration.
2. Enumerate attached role policies to identify exploitable permissions for RDS access.
3. Retrieve detailed policy versions to understand exact permissions granted.
4. Generate a temporary authentication token to connect to the RDS instance and exfiltrate data.

## Instructions

### Step 1: Verify Current IAM Identity

**Context**: Begin by confirming the IAM user or role whose credentials are in use, including the account ID and ARN. This step helps attackers understand their current permissions and troubleshoot access issues before proceeding to RDS authentication.

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity
```

This command queries the Security Token Service (STS) to return the account, user ARN, and role ARN if assumed. It requires sts:GetCallerIdentity permission and provides foundational context for subsequent steps.

### Step 2: List Attached Role Policies

**Context**: Enumerate all managed policies attached to the current IAM role to identify permissions related to RDS access, such as rds-db:connect or iam:PassRole. This reveals potential avenues for generating auth tokens without needing to assume additional roles.

**Command** ([[commands/aws-iam-list-attached-role-policies]]):
```bash
aws iam list-attached-role-policies --role-name $_ROLE_NAME
```

Replace $_ROLE_NAME with the role name from Step 1 (e.g., "MyRDSRole"). The output lists policy ARNs; review for RDS-related policies. Requires iam:ListAttachedRolePolicies permission.

### Step 3: Retrieve IAM Policy Version Details

**Context**: For a specific policy identified in Step 2, fetch the full details of its current version to inspect statements granting RDS permissions. This allows attackers to confirm token generation capabilities before attempting database access.

**Command** ([[commands/aws-iam-get-policy-version]]):
```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
```

Use the policy ARN from Step 2 and the default version ID (v1 or latest). The response includes the policy document in JSON; search for "Action": "rds-db:connect". Requires iam:GetPolicyVersion permission.

### Step 4: Generate RDS Authentication Token

**Context**: Use the confirmed IAM permissions to create a temporary auth token for the RDS instance. This token (valid for 15 minutes) replaces a password in database client connections, enabling queries to exfiltrate data (e.g., SELECT * FROM sensitive_table).

**Command** ([[commands/aws-rds-generate-db-auth-token]]):
```bash
TOKEN=$(aws rds generate-db-auth-token --hostname $_RDS_HOSTNAME --port $_PORT --username $_DB_USERNAME --region $_REGION)
```

Substitute $_RDS_HOSTNAME (e.g., mydb.cluster-abc123.us-east-1.rds.amazonaws.com), $_PORT (3306), $_DB_USERNAME (e.g., admin), and $_REGION (e.g., us-east-1). Then connect via: mysql -h $_RDS_HOSTNAME -P $_PORT -u $_DB_USERNAME -p$TOKEN mydb. Requires rds-db:connect permission; use the connection to run exfiltration queries.

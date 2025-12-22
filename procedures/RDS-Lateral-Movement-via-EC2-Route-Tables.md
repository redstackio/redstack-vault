---
id: 2f0a7a4b-d05f-4c12-ad18-7aa7795c224c
name: RDS-Lateral-Movement-via-EC2-Route-Tables
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.485334+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Valid Accounts|T1078 - Valid Accounts]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - '[[techniques/Cloud Services|T1021.006 - Cloud Services]]'
sub_techniques: []
tags:
  - '[[tags/Lateral Movement and Pivoting]]'
  - '[[tags/Listing routing tables]]'
  - '[[tags/RDS - Relational Database Service]]'
  - '[[tags/AWS]]'
  - '[[tags/EC2]]'
commands:
  - '[[commands/aws-ec2-describe-route-tables-by-vpc-id]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# RDS-Lateral-Movement-via-EC2-Route-Tables

## Summary

RDS Lateral Movement via EC2 Route Tables is a technique used by attackers to pivot from an EC2 instance to an RDS instance within the same VPC. By querying the EC2 route tables using AWS CLI, an attacker can identify the private IP addresses or endpoints of RDS instances and establish a connection to them. This requires valid AWS credentials with permissions to query EC2 resources and can enable privilege escalation or data exfiltration from the database.

## Description

In AWS environments, EC2 instances and RDS databases in the same Virtual Private Cloud (VPC) communicate via private IP addresses. Route tables define the network routing, including destinations for RDS endpoints. An attacker with compromised EC2 access and appropriate IAM permissions can enumerate these routes to discover RDS instances without direct API calls to RDS services, evading some detection. This technique leverages valid cloud credentials for lateral movement, mapping to MITRE ATT&CK for cloud scenarios where attackers exploit infrastructure configurations to expand access.

## Requirements

1. Valid AWS credentials with EC2 read permissions (e.g., ec2:DescribeRouteTables).
2. Access to an EC2 instance or environment within the target VPC.
3. AWS CLI installed and configured with the credentials.
4. Network connectivity within the VPC to reach RDS endpoints (e.g., security groups allowing traffic).

## Defense

- Implement least privilege IAM policies to restrict DescribeRouteTables actions to necessary roles only.
- Monitor CloudTrail logs for unusual EC2 API calls, especially from compromised instances.
- Use VPC flow logs to detect anomalous intra-VPC traffic to RDS ports (e.g., 3306 for MySQL).
- Regularly audit route tables and RDS security groups to ensure no unintended exposures.
- Enable RDS encryption and multi-factor authentication for database access.

## Objectives

1. Identify RDS instances and their private IP addresses or endpoints within the VPC.
2. Establish a database connection to the RDS instance using discovered network details.
3. Escalate privileges within the RDS instance or exfiltrate sensitive data.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure AWS CLI is installed and authenticated with credentials that have EC2 read access. This step confirms the environment is set up before querying resources.

**Command** ([[commands/aws-ec2-describe-route-tables-by-vpc-id]] variant for verification):
```bash
aws sts get-caller-identity
```

> This command retrieves the current AWS identity. If it returns your role or user ARN without errors, credentials are valid. If not, configure with `aws configure` using access key, secret key, and region.

### Step 2: Retrieve VPC ID if Unknown

**Context**: If the VPC ID is not known, enumerate VPCs associated with the current EC2 instance or account to target the correct one. This uses EC2 metadata or API calls.

**Command** ([[tools/AWS-CLI]] with EC2 describe-vpcs):
```bash
aws ec2 describe-vpcs --filters "Name=is-default,Values=true" --query "Vpcs[0].VpcId" --output text
```

> This fetches the default VPC ID. For specific VPCs, adjust filters (e.g., by tags). Expected output: A VPC ID like "vpc-12345678". Use this ID in the next step.

### Step 3: Describe Route Tables for the VPC

**Context**: Query the EC2 route tables to list routes, including those pointing to RDS endpoints or private IPs. Look for routes to database subnets or NAT gateways that reveal RDS locations.

**Command** ([[commands/aws-ec2-describe-route-tables-by-vpc-id]]):
```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$_VPC_ID"
```

> Replace $_VPC_ID with the actual VPC ID (e.g., vpc-12345678). This returns JSON with route table details, including DestinationCidrBlocks, InstanceId (for ENIs), and VpcId. Parse for RDS indicators like routes to 10.x.x.0/24 subnets or specific RDS ENI IDs.

### Step 4: Parse Output for RDS Indicators

**Context**: Analyze the JSON output to identify RDS-related routes. RDS instances often use specific CIDR blocks or are associated with database subnets.

Use jq for parsing if available:
```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$_VPC_ID" | jq '.RouteTables[].Routes[] | select(.DestinationCidrBlock? | startswith("10.")) | .DestinationCidrBlock'
```

> Expected output: List of private CIDRs (e.g., "10.0.1.0/24"). Cross-reference with known RDS subnets via AWS console or additional describe-subnets call. If RDS endpoint IPs are exposed, note them for connection.

### Step 5: Establish Connection to RDS

**Context**: Use the discovered IP or endpoint to connect to the RDS database. This assumes database credentials are available or obtainable via other means.

Example for MySQL RDS:
```bash
mysql -h $_RDS_ENDPOINT -u $_DB_USER -p
```

> Replace $_RDS_ENDPOINT with the IP from routes (e.g., 10.0.1.100), $_DB_USER with a valid user. Expected: Successful login prompt. If connected, query databases to confirm access and proceed to exfiltration or escalation.

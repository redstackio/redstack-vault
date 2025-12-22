---
id: 379b36c5-484a-441e-9d13-a7e2bf96af7d
name: rds-lateral-movement-via-ec2-instances-in-vpc
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.511741+00:00'
updated_at: '2023-04-10T20:20:17.683928+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Lateral Movement and Pivoting]]'
  - '[[tags/Listing instances on the specified VPC ID]]'
  - '[[tags/RDS - Relational Database Service]]'
  - '[[tags/Scenario]]'
commands:
  - '[[commands/aws-ec2-describe-instances-by-vpc-id]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# RDS Lateral Movement via EC2 Instances in VPC

## Summary

This procedure enables attackers with AWS credentials to discover EC2 instances within a specific VPC, facilitating lateral movement to access an RDS database instance. By enumerating running EC2 instances, an attacker can identify potential pivot points to connect to the RDS service, assuming network connectivity and appropriate IAM permissions.

## Description

In cloud environments like AWS, lateral movement often involves leveraging compute resources (EC2 instances) to reach isolated services like RDS databases. This procedure focuses on discovering EC2 instances in a target VPC using the AWS CLI. Once instances are identified, attackers can SSH, use AWS Systems Manager (SSM), or exploit instance configurations to pivot traffic toward the RDS endpoint. This technique is common in multi-account or segmented VPC setups where direct RDS access is restricted. Prerequisites include valid AWS credentials with ec2:DescribeInstances permissions and knowledge of the target VPC ID, which can be obtained via prior reconnaissance (e.g., querying VPC configurations). The outcome allows attackers to map the environment and plan further access to sensitive database data.

## Requirements

1. Valid AWS credentials with at least ec2:DescribeInstances permission.
2. AWS CLI installed and configured with access to the target account/region.
3. Knowledge of the target VPC ID (discoverable via aws ec2 describe-vpcs).
4. Network access to execute CLI commands (e.g., from a compromised workstation or EC2 instance).

## Defense

- Implement least-privilege IAM policies to restrict DescribeInstances actions to necessary roles.
- Use VPC network ACLs and security groups to segment EC2 and RDS access, preventing unauthorized pivoting.
- Enable AWS CloudTrail logging for API calls and monitor for anomalous DescribeInstances queries.
- Regularly audit VPC configurations and instance metadata to detect exposed credentials.

## Objectives

1. Enumerate all EC2 instances running in the specified VPC to identify potential pivot hosts.
2. Gather instance details (ID, type, state, launch time) for targeting.
3. Enable lateral movement by selecting an EC2 instance as a jump host to reach the RDS database.
4. Access sensitive data in RDS via the pivoted connection.

## Instructions

### Step 1: Configure AWS CLI and Verify Access

**Context**: Ensure the AWS CLI is set up with credentials that have the necessary permissions. This step verifies connectivity to the target AWS region and account before querying instances.

Run the AWS CLI configure command if not already set, or test with a simple query.

**Command** ([[commands/aws-ec2-describe-instances-by-vpc-id]] variant for testing):
```bash
aws configure list
```

> This displays current configuration. If credentials are invalid, reconfigure using `aws configure` with access key, secret key, region (e.g., us-east-1), and output format (json).

### Step 2: Identify the Target VPC ID

**Context**: If the VPC ID is unknown, query available VPCs to discover it. This is a prerequisite for filtering EC2 instances.

Use the AWS CLI to list VPCs.

**Command**:
```bash
aws ec2 describe-vpcs --query 'Vpcs[].{VPCId:VpcId,CidrBlock:CidrBlock}' --output table
```

> Expected output is a table of VPC IDs and CIDR blocks. Select the relevant VPC ID based on network segmentation or tags (e.g., for the RDS-associated subnet).

### Step 3: Describe EC2 Instances in the VPC

**Context**: Query EC2 instances filtered by the VPC ID to list potential pivot points. This reveals running instances that could be used to route traffic to RDS.

**Command** ([[commands/aws-ec2-describe-instances-by-vpc-id]]):
```bash
aws ec2 describe-instances --filters "Name=vpc-id,Values=vpc-0123456789abcdef0"
```

> Replace `vpc-0123456789abcdef0` with the actual VPC ID. This returns JSON details including InstanceId, InstanceType, State (e.g., running), LaunchTime, and PrivateIpAddress. Focus on running instances in subnets connected to RDS.

### Step 4: Analyze Output and Plan Pivot

**Context**: Parse the JSON output to identify suitable EC2 instances (e.g., those with SSM agent or SSH access). This step involves manual review or jq for filtering.

Use jq to filter running instances.

**Command**:
```bash
aws ec2 describe-instances --filters "Name=vpc-id,Values=vpc-0123456789abcdef0" --query 'Reservations[].Instances[?State.Name==`running`].{InstanceId:InstanceId,PrivateIp:PrivateIpAddress,Type:InstanceType}' --output table
```

> Expected output is a table of running instances. Select one (e.g., by InstanceId) and connect via SSH/SSM: `aws ssm start-session --target i-0123456789abcdef0`. From the instance, query RDS endpoints or use database clients to connect.

### Step 5: Verify Pivot to RDS

**Context**: Once connected to the EC2 instance, confirm RDS accessibility. This validates the lateral movement path.

From the EC2 instance shell, test RDS connectivity (assuming RDS endpoint known).

**Command** (example mysql client):
```bash
mysql -h rds-endpoint.region.rds.amazonaws.com -u dbuser -p
```

> Success if connection established without errors, allowing SQL queries to exfiltrate data.

---
id: 5cf79d88-84d4-41c9-80eb-d3bf716b3823
name: Enumerate-EC2-Route-Tables-by-VPC-ID
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.386168+00:00'
updated_at: '2023-04-10T20:20:11.833313+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Remote System Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - Enumeration
  - AWS-EC2
  - Route-Tables
  - VPC-Discovery
commands:
  - '[[commands/aws-ec2-describe-route-tables-filter-vpc-id]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-EC2-Route-Tables-by-VPC-ID

## Summary

This procedure uses the AWS CLI to query and list all route tables associated with a specific VPC ID in an Amazon EC2 environment. It enables discovery of network routing configurations, helping to map the target's VPC topology for further enumeration or identifying misconfigurations that could lead to lateral movement in cloud infrastructure.

## Description

In cloud penetration testing or red team engagements targeting AWS, enumerating route tables provides insight into how traffic is directed within a VPC, including internet gateways, NAT gateways, and peering connections. This technique falls under remote system discovery as it reveals infrastructure details without direct host access. The procedure assumes the attacker has obtained AWS credentials with read permissions on EC2 resources (e.g., via IAM role compromise or misconfigured access keys). By filtering on a known VPC ID—potentially discovered through prior enumeration like describing VPCs—this reveals route table IDs, associations, and routes, which can inform attacks like pivoting to private subnets or exfiltrating data via unexpected routes. Expected outcomes include a JSON structure detailing route propagations and destinations, allowing attackers to visualize network boundaries.

## Requirements

1. AWS CLI installed and configured with credentials that have `ec2:DescribeRouteTables` permissions (e.g., ReadOnlyAccess policy or equivalent).
2. Knowledge of the target VPC ID (e.g., obtained from prior VPC enumeration).
3. Network access to AWS API endpoints (no direct VPC access required, but credentials must be valid for the target account/region).

## Defense

- Restrict IAM policies to deny `ec2:DescribeRouteTables` for non-admin users and monitor usage via CloudTrail logs.
- Enable AWS Config rules to alert on unauthorized API calls and implement least-privilege access for EC2 actions.
- Regularly audit CloudTrail for anomalous describe operations, especially from unexpected IPs or roles, and use GuardDuty for behavioral anomaly detection in cloud APIs.

## Objectives

1. List all route tables linked to the specified VPC to identify network paths and associations.
2. Discover routing configurations that reveal VPC topology, such as internet-facing routes or subnet associations.
3. Gather data for mapping the overall AWS network structure to support targeted exploitation.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Before executing the enumeration, confirm that the AWS CLI is properly set up with credentials for the target account and region. This ensures the command authenticates correctly and targets the right environment, preventing errors from misconfigured sessions.

Use the [[tools/AWS-CLI]] to check configuration:

```bash
aws configure list
```

> This command displays current profile settings, including access key, secret key (masked), region, and output format. If needed, run `aws configure` to set the default region (e.g., us-east-1) and credentials. Expected output includes valid region and profile details without authentication errors.

### Step 2: Execute Route Tables Enumeration

**Context**: Run the AWS CLI command to filter and describe route tables for the specific VPC ID. This step retrieves detailed routing information, including table IDs, subnet associations, and route destinations, which can expose potential pivot points like public internet routes.

**Command** ([[commands/aws-ec2-describe-route-tables-filter-vpc-id]]):

```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$_VPC_ID" --region $_REGION
```

> Replace $_VPC_ID with the target VPC identifier (e.g., vpc-12345678) and $_REGION with the AWS region (e.g., us-east-1). The --filters option limits results to the specified VPC, reducing noise. If no region is set, it defaults to the configured one. Expected output is a JSON array under "RouteTables", listing each table's ID, VPC ID, associations (e.g., subnet IDs), and routes (e.g., destination CIDRs and gateways). Success is indicated by non-empty RouteTables array; empty results suggest no tables or permission issues.

### Step 3: Parse and Analyze Output

**Context**: Review the JSON output to extract key details like route destinations and associations. This step involves manual inspection or piping to jq for filtering, helping identify exploitable configurations such as routes to internal resources.

Use jq (if available) or manual parsing:

```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$_VPC_ID" --region $_REGION | jq '.RouteTables[] | {RouteTableId, VpcId, Routes: .Routes[] | {DestinationCidrBlock, GatewayId}}'
```

> This filters the output to show route table IDs, VPC ID, and route details like CIDR blocks and gateways. Expected output includes structured data revealing traffic flows (e.g., 0.0.0.0/0 to igw-xxx for internet access). If jq is not installed, save raw JSON to a file and inspect with a text editor. Success indicators include identifiable routes that map to known subnets or external gateways.

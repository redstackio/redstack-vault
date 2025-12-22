---
id: c2842a10-bd38-4def-a681-d57df0cd2e64
name: rds-subnet-group-enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.901936+00:00'
updated_at: '2023-04-10T20:20:39.624272+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
  - '[[techniques/Remote System Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Listing information about subnet groups in RDS]]'
  - '[[tags/RDS - Relational Database Service]]'
commands:
  - '[[commands/aws-rds-describe-db-subnet-groups]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# RDS Subnet Group Enumeration

## Summary

RDS Subnet Group Enumeration is a discovery technique used to gather information about the DB subnet groups associated with Amazon RDS instances in an AWS environment. By querying the AWS RDS API, an attacker with compromised credentials can identify subnet group details, including VPC IDs, subnet IDs, and descriptions, which may reveal network architecture and potential pivot points for lateral movement or further exploitation within the cloud infrastructure.

## Description

This procedure leverages the AWS CLI to describe DB subnet groups, providing visibility into the networking configuration of RDS databases. In an attack scenario, this information helps map the target's VPC structure, identify associated subnets, and assess exposure risks, such as publicly accessible subnets or misconfigurations. The technique is particularly useful during cloud reconnaissance phases after initial credential compromise, enabling attackers to plan targeted attacks on database resources. Expected outcomes include a list of subnet groups with their constituent subnets, VPC associations, and status, which can inform subsequent actions like attempting direct access to RDS endpoints or exploiting subnet-level permissions.

## Requirements

1. Valid AWS credentials with at least read access to RDS (e.g., rds:DescribeDBSubnetGroups permission).
2. AWS CLI installed and configured with the target account's access key and secret key.
3. Network access to AWS APIs (typically over HTTPS to regional endpoints).
4. Optional: Specifying a region if not using the default.

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies to restrict DescribeDBSubnetGroups actions to necessary roles only.
- Enable AWS CloudTrail logging for RDS API calls to monitor and alert on enumeration attempts.
- Use VPC security groups and NACLs to limit RDS exposure, and avoid public subnet placements for databases.
- Regularly audit IAM credentials and rotate them to mitigate risks from compromised accounts.

## Objectives

1. Enumerate DB subnet groups to map RDS networking configuration.
2. Identify VPC and subnet details for potential lateral movement targets.
3. Assess RDS instance exposure and misconfigurations for further exploitation.

## Instructions

### Step 1: Configure AWS CLI and Query DB Subnet Groups

**Context**: Ensure AWS CLI is set up with the compromised credentials, then execute the describe command to retrieve subnet group information. This step lists all DB subnet groups in the current region, revealing network details without requiring specific subnet group names upfront.

**Command** ([[commands/aws-rds-describe-db-subnet-groups]]):
```bash
aws rds describe-db-subnet-groups --region $_AWS_REGION
```

> This command queries the RDS service for all DB subnet groups. Replace $_AWS_REGION with the target AWS region (e.g., us-east-1). If no region is specified, it uses the default from your AWS configuration. The output is a JSON structure containing subnet group details. Review the response for VPCId, SubnetGroupDescription, and Subnets array to identify key network components. If the command succeeds, you'll see a list of groups; if access is denied, it indicates insufficient permissions—escalation may be needed.

### Step 2: Parse and Analyze Output for Insights

**Context**: After retrieving the JSON output, parse it to extract actionable intelligence, such as subnet IDs and availability zones, which can guide further discovery of RDS instances or VPC resources.

**Command** ([[commands/aws-rds-describe-db-subnet-groups]] with jq for parsing):
```bash
aws rds describe-db-subnet-groups --region $_AWS_REGION | jq '.DBSubnetGroups[] | {DBSubnetGroupName: .DBSubnetGroupName, VpcId: .VpcId, Subnets: [.Subnets[] | {SubnetIdentifier: .SubnetIdentifier, SubnetAvailabilityZone: .SubnetAvailabilityZone.Name}]}'
```

> Use jq (a JSON processor) to filter the output for readability. Install jq if not present (e.g., apt install jq on Linux). This step provides a concise view of subnet groups and their subnets. Look for patterns like default VPC usage or overlapping subnets that might indicate broader infrastructure details. Success is confirmed by structured output showing group names and subnet identifiers without errors.

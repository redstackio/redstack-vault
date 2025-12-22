---
id: 09b9d9d8-da69-48aa-9ba8-b98ca30da806
name: aws-region-information-gathering
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.231968+00:00'
updated_at: '2023-04-10T20:20:35.846435+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing information about a specific region]]'
commands:
  - '[[commands/aws-ec2-describe-instances-by-region]]'
tools:
  - '[[tools/aws-cli]]'
platforms:
  - AWS
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# aws-region-information-gathering

## Summary

This procedure uses the AWS CLI to gather detailed information about EC2 instances in a specific AWS region, including instance IDs, types, security groups, and states. It is useful for reconnaissance in cloud environments to map infrastructure, identify running services, and spot potential entry points or misconfigurations during red team engagements or security audits.

## Description

In AWS environments, attackers or security testers often need to enumerate resources in specific regions to understand the target's cloud footprint. The 'aws ec2 describe-instances' command queries the EC2 API for instance metadata, providing visibility into virtual machines without direct access. This technique aligns with discovery tactics by revealing system details like instance configurations and network associations. It requires valid AWS credentials with read permissions on EC2 (e.g., ec2:DescribeInstances). Use this in scenarios where initial access to AWS credentials has been obtained, such as via compromised IAM roles or stolen keys, to pivot and explore regional deployments. Expected outcomes include a JSON output listing instances, which can be parsed for further analysis, such as identifying public-facing instances or unusual security groups.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least 'ec2:DescribeInstances' permission.
2. AWS CLI installed and configured on the local machine (version 2 recommended for full feature support).
3. Network access to AWS endpoints (no VPC endpoints required for public regions).
4. Specification of the target region (e.g., us-east-1) to avoid default region assumptions.

## Defense

- Implement least-privilege IAM policies to restrict DescribeInstances actions to necessary roles only.
- Enable AWS CloudTrail logging for API calls and monitor for anomalous DescribeInstances queries from unexpected IPs or users.
- Use AWS Organizations SCPs to deny cross-region enumeration in multi-account setups.
- Rotate credentials regularly and alert on unusual API activity via Amazon GuardDuty.

## Objectives

1. Retrieve comprehensive metadata on EC2 instances in a targeted AWS region.
2. Identify active instances, their configurations, and associated resources for potential exploitation.
3. Support broader reconnaissance by feeding instance data into tools for vulnerability scanning or lateral movement planning.

## Instructions

### Step 1: Configure AWS CLI and Specify Region

**Context**: Ensure the AWS CLI is set up with credentials and the target region is specified to focus the query. This step verifies access and scopes the enumeration to avoid broad queries that could trigger alerts.

If not already configured, set up credentials using environment variables or the AWS config file. Then, execute the command to describe instances in the specified region.

**Command** ([[commands/aws-ec2-describe-instances-by-region]]):
```bash
aws ec2 describe-instances --region $_AWS_REGION
```

> This command calls the EC2 API to list all instances in the given region. Replace $_AWS_REGION with the target (e.g., us-west-2). If filters are needed (e.g., by state), add --filters options, but start without for full discovery. Success is indicated by a JSON response without permission errors.

### Step 2: Parse and Analyze Output

**Context**: Review the JSON output to extract key details like instance IDs, types, and security groups. This manual or scripted step helps identify high-value targets, such as database instances or those in default VPCs.

Use jq or similar tools to filter the output:
```bash
aws ec2 describe-instances --region $_AWS_REGION | jq '.Reservations[].Instances[] | {InstanceId, InstanceType, State, SecurityGroups}'
```

> Expected output includes structured data on instances. If no instances exist, an empty array is returned. Verify by checking for InstanceId fields and cross-reference with AWS console if possible for validation.

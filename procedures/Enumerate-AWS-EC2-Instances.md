---
id: c4876117-e31a-46e3-9911-4be0d77f6a98
name: Enumerate-AWS-EC2-Instances
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.255067+00:00'
updated_at: '2023-04-10T20:20:56.911751+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - aws
  - cloud
  - enumeration
  - ec2
commands:
  - '[[commands/aws-ec2-describe-instances]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - AWS
validated: true
---

# Enumerate-AWS-EC2-Instances

## Summary

This procedure uses the AWS CLI to retrieve detailed information about specific EC2 instances in an AWS environment, including instance IDs, types, states, IP addresses, launch times, and associated security groups. It enables attackers with valid credentials to map out the target's cloud infrastructure, identify running instances, and spot potential vulnerabilities such as overly permissive security groups or outdated instance types for further exploitation.

## Description

In cloud environments like AWS, enumerating EC2 instances is a key discovery technique to understand the target's virtual machine footprint. With compromised credentials (e.g., IAM user keys or assumed roles), an attacker can query the EC2 API via the AWS CLI's describe-instances command. This reveals critical details that inform subsequent attacks, such as targeting instances with public IPs for exploitation or analyzing security groups for lateral movement opportunities. The procedure assumes the attacker has at least read access to EC2 resources and focuses on specifying instance IDs obtained from prior broader enumerations (e.g., listing all instances). Output is returned in JSON format, which can be piped to tools like jq for parsing. This aligns with reconnaissance in cloud-native attacks, where understanding resource inventory is foundational.

## Requirements

1. Valid AWS credentials with ec2:DescribeInstances permission (e.g., IAM policy allowing EC2 read access).
2. AWS CLI version 2.x installed and configured with the target's account credentials via `aws configure`.
3. Network access to AWS APIs (typically over HTTPS port 443); specify the correct region with --region if not default.
4. Instance IDs to query, obtained from previous discovery (e.g., via aws ec2 describe-instances without --instance-ids for a full list).

## Defense

- Enable and monitor AWS CloudTrail logs for unauthorized describe-instances API calls, alerting on unusual IP sources or high-volume queries.
- Apply principle of least privilege by scoping IAM policies to deny DescribeInstances unless explicitly needed, using conditions like aws:RequestedRegion.
- Use AWS Organizations SCPs to restrict EC2 actions across accounts and integrate with SIEM for anomaly detection on credential usage patterns.
- Regularly audit EC2 configurations with AWS Config rules to identify and remediate exposed instances or weak security groups.

## Objectives

1. Retrieve comprehensive details on targeted EC2 instances to map infrastructure.
2. Identify running instances, networking configurations, and potential entry points for escalation.
3. Gather data for planning targeted attacks, such as exploiting misconfigurations in security groups.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Ensure the AWS CLI is set up with credentials that have the necessary permissions and test basic connectivity to avoid errors during enumeration. This step confirms access to the target region and account.

**Command** ([[commands/aws-ec2-describe-instances]]):
```bash
aws ec2 describe-instances --instance-ids $_INSTANCE_IDS --region $_REGION --dry-run
```

> The --dry-run flag simulates the API call without executing it, helping verify permissions without retrieving data. If successful, no error is returned; otherwise, it indicates insufficient permissions or invalid credentials. Replace $_INSTANCE_IDS with a known ID (or omit for a full list test) and $_REGION with the target (e.g., us-east-1). Expected output: No error message, confirming access.

### Step 2: Enumerate Details for Specific Instances

**Context**: Execute the core enumeration to fetch detailed metadata on the specified EC2 instances. This provides actionable intelligence on instance state, networking, and configurations, which can be used to pivot to other attacks like instance metadata service exploitation if applicable.

**Command** ([[commands/aws-ec2-describe-instances]]):
```bash
aws ec2 describe-instances --instance-ids $_INSTANCE_IDS --region $_REGION --output json
```

> Run this against one or more instance IDs separated by spaces (e.g., i-1234567890abcdef0 i-0987654321fedcba0). The --output json ensures structured data for easy parsing. If no instances match, an empty Reservations array is returned. Use filters like --filters "Name=instance-state-name,Values=running" to narrow results if needed. Expected output: A JSON structure with Reservations containing Instances arrays, detailing InstanceId, InstanceType, State (e.g., running/stopped), PrivateIpAddress, VpcId, SecurityGroups, LaunchTime, and more. Pipe to jq for extraction, e.g., | jq '.Reservations[].Instances[].InstanceId' to list IDs only.

### Step 3: Parse and Analyze Output for Insights

**Context**: Process the JSON output to extract key details and identify attack opportunities, such as public IPs or default security groups. This step adds value by turning raw data into targeted intelligence.

**Instructions**: Save the output to a file for analysis:
```bash
aws ec2 describe-instances --instance-ids $_INSTANCE_IDS --region $_REGION > ec2-details.json
```
Then use jq to query specific fields:
```bash
jq '.Reservations[].Instances[] | {InstanceId, State: .State.Name, PublicIp: .PublicIpAddress, SecurityGroups}' ec2-details.json
```

> This isolates critical fields like public IPs (potential direct access points) and security groups (for port exposure analysis). If public IPs are present and security groups allow inbound traffic on common ports (e.g., 22/3389), prioritize those for scanning. Expected output: Filtered JSON objects highlighting exploitable attributes. If no public IPs, focus on private ones for lateral movement planning.

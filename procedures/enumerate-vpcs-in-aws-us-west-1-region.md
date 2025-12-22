---
id: edb80866-fd03-41e1-8319-ac813597dee2
name: enumerate-vpcs-in-aws-us-west-1-region
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.256582+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Cloud-Infrastructure-Discovery|T1589 - Cloud Infrastructure
    Discovery]]
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/AWS]]'
  - '[[tags/VPC]]'
  - '[[tags/RDS]]'
  - '[[tags/Cloud-Discovery]]'
commands:
  - '[[commands/aws-ec2-describe-vpcs-us-west-1]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate VPCs in AWS us-west-1 Region

## Summary

This procedure uses the AWS CLI to list all Virtual Private Clouds (VPCs) in the us-west-1 region, providing visibility into the target's cloud infrastructure. This discovery technique helps identify network boundaries, potential RDS instances, and other resources for further enumeration or targeting in a red team engagement.

## Description

In cloud environments like AWS, attackers with compromised credentials can enumerate infrastructure components to map the attack surface. Listing VPCs reveals isolated network segments where services like RDS databases may reside, enabling targeted follow-on actions such as subnet discovery or service enumeration. This procedure assumes valid AWS credentials with read access to EC2 resources and focuses on the us-west-1 region (Oregon). The output includes VPC IDs, CIDR blocks, and states, which can be correlated with RDS DB instances via additional queries. Use this in scenarios where initial access to AWS APIs is gained through stolen keys or IAM roles.

## Requirements

1. AWS CLI installed and configured with credentials (e.g., access key ID and secret access key) that have at least `ec2:DescribeVpcs` permissions.
2. Network access to AWS endpoints (no VPC endpoint restrictions).
3. Target AWS account with VPCs in us-west-1 region.
4. Basic familiarity with JSON output parsing for review.

## Defense

- Implement least-privilege IAM policies to restrict `ec2:DescribeVpcs` to necessary roles only.
- Enable AWS CloudTrail logging for API calls and monitor for anomalous `DescribeVpcs` requests from unexpected IPs or users.
- Use AWS Organizations SCPs to deny discovery actions in sensitive regions.
- Alert on high-volume API queries in us-west-1 to detect reconnaissance.

## Objectives

1. Retrieve a complete list of VPCs in the us-west-1 region to map cloud network architecture.
2. Identify VPCs potentially hosting RDS instances for prioritized targeting.
3. Gather attributes like CIDR blocks and tags to inform lateral movement planning.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure your AWS credentials are set up correctly to avoid authentication errors during enumeration. This step confirms access to the target region without executing the full query.

**Command** ([[commands/aws-ec2-describe-vpcs-us-west-1]] variant for verification):
```bash
aws sts get-caller-identity --region us-west-1
```

> This command returns your AWS account details, user ARN, and confirms the region is reachable. If it fails with AccessDenied, update your credentials or IAM policy.

### Step 2: Execute VPC Enumeration Command

**Context**: Run the core command to fetch all VPC details. This retrieves a JSON array of VPC objects, including IDs, states (available/pending), CIDR blocks, and DHCP options, which can reveal network segmentation relevant to RDS deployments.

**Command** ([[commands/aws-ec2-describe-vpcs-us-west-1]]):
```bash
aws ec2 describe-vpcs --region us-west-1
```

> The command queries the EC2 API for VPCs in us-west-1. Pipe to `jq` for filtering if needed (e.g., `| jq '.Vpcs[] | {VpcId, CidrBlock}'`). Expect a JSON response; if no VPCs exist, it returns an empty array.

### Step 3: Review and Filter Output for RDS Relevance

**Context**: Parse the results to identify VPCs associated with RDS by cross-referencing VPC IDs with RDS instance details (optional follow-on). This step validates success and extracts actionable intel like tags indicating database usage.

**Command** (Manual review or pipe):
```bash
aws ec2 describe-vpcs --region us-west-1 | jq '.Vpcs[] | select(.Tags[]?.Key == "Name" and .Tags[]?.Value | contains("rds"))'
```

> Manually inspect the JSON for VPCs with tags like "rds" or correlate with `aws rds describe-db-instances --region us-west-1` (requires RDS permissions). Success is confirmed by non-empty VPC listings; note any default VPCs for common misconfigurations.

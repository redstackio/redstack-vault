---
id: 9ba693da-af0d-4937-8d83-3e67dcb3a59e
name: Create-AWS-VPC-in-Alternate-Region-for-Resource-Hiding
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:22.995321+00:00'
updated_at: '2023-05-25T20:05:50.127974+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Indicator Removal on Host]]'
sub_techniques: []
tags:
  - aws
  - cloud
  - evasion
  - vpc
commands:
  - '[[commands/aws-ec2-create-vpc]]'
  - '[[commands/aws-ec2-modify-vpc-dns-hostnames]]'
platforms:
  - Cloud
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Create-AWS-VPC-in-Alternate-Region-for-Resource-Hiding

## Summary

This procedure demonstrates how to create a Virtual Private Cloud (VPC) in an alternate AWS region to isolate and hide EC2 instances, subnets, and gateways from detection in the primary region. This technique can be used in red team operations to establish persistent, low-visibility infrastructure for command and control or lateral movement while minimizing exposure to monitoring in the target's main operational region.

## Description

In cloud environments, attackers with valid AWS credentials can provision resources in secondary regions to evade detection. By creating a VPC in a less-monitored region (e.g., eu-west-1 instead of us-east-1), resources like EC2 instances become harder to discover through standard reconnaissance or logging in the primary region. This procedure covers creating the VPC with a specified CIDR block and optionally enabling DNS hostnames for easier internal resolution. It assumes access to AWS CLI with EC2 permissions and is applicable in scenarios where the attacker aims to build out hidden infrastructure without triggering alerts in the main environment.

## Requirements

1. AWS CLI installed and configured with credentials that have EC2 full access (e.g., AmazonEC2FullAccess policy).
2. Valid AWS account access, preferably with permissions to create VPCs in multiple regions.
3. Network connectivity to AWS endpoints.
4. Basic knowledge of CIDR notation for VPC addressing.

## Defense

- Enable AWS CloudTrail across all regions to log VPC creation events (EventName: CreateVpc).
- Implement IAM policies restricting VPC creation to specific regions or requiring approval workflows.
- Use AWS Config rules to monitor for VPCs in non-standard regions and alert on unusual provisioning patterns.
- Regularly audit resource inventories with AWS Resource Explorer or third-party tools like Prisma Cloud.

## Objectives

1. Provision a new VPC in an alternate region to host hidden resources.
2. Configure optional DNS settings for internal name resolution within the VPC.
3. Verify the VPC creation without exposing it in the primary region's monitoring.

## Instructions

### Step 1: Create the VPC in Alternate Region

**Context**: This step provisions a new VPC using the AWS CLI, specifying a CIDR block for the network range and targeting an alternate region to isolate resources from the primary environment. Choose a region different from the target's main operations to reduce visibility.

**Command** ([[commands/aws-ec2-create-vpc]]):
```bash
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --region eu-west-1
```

> This command creates a VPC with the IP range 10.0.0.0/16 in the eu-west-1 region. Replace the CIDR block and region as needed. The output includes the VPC ID, which should be noted for further configuration.

### Step 2: (Optional) Enable DNS Hostnames in the VPC

**Context**: Enabling DNS hostnames allows EC2 instances within the VPC to receive DNS entries that resolve to their private IP addresses, facilitating internal communication without public exposure. This is useful for setting up hidden services but increases resolvability if queried.

**Command** ([[commands/aws-ec2-modify-vpc-dns-hostnames]]):
```bash
aws ec2 modify-vpc-attribute --vpc-id vpc-12345678 --enable-dns-hostnames "{\"Value\":true}" --region eu-west-1
```

> Use the VPC ID from Step 1. This modifies the VPC attribute to enable DNS hostnames. The JSON value must be properly escaped. Success is indicated by a return code of 0 with no errors.

---
id: caaf1337-b75d-4abd-a836-2f31c4b83246
name: Enumerate-AWS-EC2-AMIs
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:19.368656+00:00'
updated_at: '2023-05-25T20:04:43.584266+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - '[[tags/AWS]]'
  - '[[tags/Cloud]]'
  - discovery
  - enumeration
commands:
  - '[[commands/aws-ec2-describe-all-images]]'
  - '[[commands/aws-ec2-describe-image-by-id]]'
  - '[[commands/aws-ec2-describe-images-with-filters]]'
platforms:
  - Cloud
tools:
  - '[[tools/aws-cli]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Enumerate-AWS-EC2-AMIs

## Summary

This procedure enumerates Amazon Machine Images (AMIs) in an AWS account using the AWS CLI. It allows discovery of all available AMIs, detailed information for specific AMIs by ID, and filtered results based on attributes like OS type or volume type. This is useful for reconnaissance in cloud environments to identify available images for potential instance launches, analysis of custom images, or understanding the account's image inventory.

## Description

In offensive security operations, enumerating EC2 AMIs provides visibility into the cloud infrastructure's available templates for virtual machines. AMIs contain the software configuration (OS, applications, and data) required to launch an EC2 instance. By listing AMIs, an attacker with compromised AWS credentials can assess the environment for custom or sensitive images that might reveal additional information or enable further exploitation, such as launching instances with pre-configured backdoors. This procedure assumes access to an AWS account with EC2 read permissions (e.g., ec2:DescribeImages). It uses the AWS CLI tool and supports specifying profiles and regions for multi-account or multi-region environments. Potential outcomes include identifying public, private, or marketplace AMIs owned by the account or shared with it.

## Requirements

1. AWS CLI installed and configured with credentials that have EC2 read permissions (e.g., AmazonEC2ReadOnlyAccess policy).
2. Valid AWS profile name if using named profiles (default is 'default').
3. Target AWS region (e.g., us-east-1); if not specified, defaults to the profile's default region.
4. Knowledge of specific AMI IDs for detailed queries, or filter criteria like OS type (e.g., 'windows', 'linux') and volume type (e.g., 'ebs').

## Defense

Defensive measures and detection strategies:

- Monitor AWS CloudTrail logs for DescribeImages API calls, which indicate enumeration activity. Set up alerts for unusual patterns from unexpected IPs or high-volume queries.
- Implement least-privilege IAM policies to restrict DescribeImages access to necessary roles only.
- Use AWS Config to track AMI changes and ownership, and enable GuardDuty for cloud API activity monitoring.
- Rotate credentials regularly and monitor for anomalous access patterns via AWS IAM Access Analyzer.

## Objectives

1. Discover all AMIs in the account to map the image inventory.
2. Retrieve detailed metadata for specific AMIs to analyze configurations.
3. Filter AMIs by attributes like OS or storage type for targeted reconnaissance.
4. Expected outcome: Comprehensive list of AMIs with details like creation date, architecture, and block device mappings, aiding in further cloud discovery.

## Instructions

### Step 1: List All AMIs

**Context**: This step retrieves a complete list of all AMIs accessible to the account, including owned, shared, and marketplace images. It provides an overview of the image landscape without filters, useful for initial reconnaissance.

**Command** ([[commands/aws-ec2-describe-all-images]]):
```bash
aws ec2 describe-images
```

> This command queries the EC2 API for all images and outputs JSON with details like ImageId, Name, Description, CreationDate, and Architecture. Run it in the target region; pipe to jq for parsing if needed (e.g., | jq '.Images[].ImageId'). Expect a potentially large JSON response listing dozens or hundreds of AMIs.

### Step 2: Describe Specific AMI by Image ID

**Context**: Once an AMI ID is identified (e.g., from Step 1), this step fetches detailed information about that specific image, including block device mappings, product codes, and state. This is essential for analyzing a particular AMI's configuration.

**Command** ([[commands/aws-ec2-describe-image-by-id]]):
```bash
aws ec2 describe-images --image-ids $_AMI_ID --profile $_PROFILE --region $_REGION
```

> Replace $_AMI_ID with the target ImageId (e.g., ami-0abcdef1234567890), $_PROFILE with your AWS profile (e.g., default), and $_REGION with the AWS region (e.g., us-east-1). The output is JSON detailing the AMI's properties, such as RootDeviceName, VirtualizationType, and Hypervisor. Success is indicated by a non-empty Images array in the response.

### Step 3: Describe AMIs with Filters

**Context**: Apply filters to narrow down AMIs based on criteria like platform (OS type) or root device type (e.g., EBS-backed). This is optional but refines results for specific scenarios, such as finding Windows AMIs with EBS volumes.

**Command** ([[commands/aws-ec2-describe-images-with-filters]]):
```bash
aws ec2 describe-images --filters "Name=$_FILTER_NAME1,Values=$_FILTER_VALUE1" "Name=$_FILTER_NAME2,Values=$_FILTER_VALUE2"
```

> Common filters include Name=platform,Values=windows for OS type or Name=root-device-type,Values=ebs for volume type. The command returns filtered JSON output. For example, filtering for Windows EBS AMIs helps identify compatible images quickly. Verify success by checking for relevant Images in the response.

---
id: 6a49a245-e63c-4aad-9cfa-7ea80f73dffe
name: AWS-Instance-Profile-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.510160+00:00'
updated_at: '2023-04-10T20:20:24.671628+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Cloud Instance Metadata API|T1522 - Cloud Instance Metadata
    API]]
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - cloud-aws
  - exploitation
  - listing-instance-profiles
  - privilege-escalation
commands:
  - '[[commands/aws-iam-list-instance-profiles]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS-Instance-Profile-Enumeration

## Summary

This procedure enumerates AWS instance profiles associated with EC2 instances to identify available IAM roles and their permissions, enabling potential privilege escalation by assuming those roles. It uses the AWS CLI to query IAM and can be combined with instance metadata access for deeper reconnaissance in cloud environments.

## Description

AWS Instance Profiles serve as containers for IAM roles that grant permissions to EC2 instances without embedding long-term credentials. Attackers with initial AWS access can list these profiles to map the environment's permission structure, revealing opportunities for lateral movement or escalation. This technique leverages the IAM API for listing and may integrate with the Instance Metadata Service (IMDS) to retrieve profile details from within an instance. In a red team scenario, this helps identify over-privileged roles that could lead to broader resource access, such as S3 buckets or other services. Prerequisites include valid AWS credentials with iam:ListInstanceProfiles permission; outcomes include a list of profiles with associated ARNs for further analysis.

## Requirements

1. Valid AWS credentials configured in the environment (e.g., via AWS CLI profile) with at least iam:ListInstanceProfiles permission.
2. AWS CLI installed and accessible on the system.
3. Network access to AWS endpoints (no VPC restrictions blocking IAM API calls).
4. Optional: Access to an EC2 instance for metadata service queries if combining with IMDS.

## Defense

- Apply least privilege to IAM roles in instance profiles, regularly auditing attached policies.
- Enable and monitor AWS CloudTrail for IAM API calls, alerting on unusual list-instance-profiles activity.
- Use IMDSv2 on EC2 instances to restrict metadata access and implement network ACLs to limit API exposure.
- Implement AWS Organizations SCPs to constrain IAM actions across accounts.

## Objectives

1. Identify all available instance profiles in the target AWS account.
2. Extract associated IAM role ARNs and permissions for privilege analysis.
3. Facilitate escalation by targeting assumable roles with elevated privileges.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Ensure the AWS CLI is set up with credentials that have the necessary IAM permissions to avoid authentication errors during enumeration.

Run the AWS CLI configure command if not already set, or verify current configuration:

**Command** ([[commands/aws-iam-list-instance-profiles]] variant for testing):
```bash
aws sts get-caller-identity
```

This confirms your identity and permissions. If it succeeds without errors, proceed; otherwise, update credentials.

**Expected Output**: JSON response showing Account, UserId, and Arn, indicating valid access.

### Step 2: List All Instance Profiles

**Context**: Query the IAM service to retrieve a complete list of instance profiles, which reveals the roles available for EC2 instances and potential escalation paths.

Execute the primary enumeration command to fetch profiles:

**Command** ([[commands/aws-iam-list-instance-profiles]]):
```bash
aws iam list-instance-profiles
```

This returns details like profile names, ARNs, and associated role ARNs. Pipe to jq for parsing if needed (e.g., | jq '.InstanceProfiles[].Arn').

**Expected Output**: JSON array of instance profiles, e.g., {"InstanceProfiles": [{"Arn": "arn:aws:iam::123456789012:instance-profile/MyProfile", "Roles": [{"Arn": "arn:aws:iam::123456789012:role/MyRole"}]}]}.

### Step 3: Analyze Profile Roles and Permissions

**Context**: For each discovered profile, query the associated role's policies to understand granted permissions, identifying high-value actions like s3:* or ec2:RunInstances.

Use follow-up commands to describe roles (assuming from Step 2 output):

**Command** ([[commands/aws-iam-list-instance-profiles]] variant):
```bash
aws iam get-role --role-name $_ROLE_NAME
```
Replace $_ROLE_NAME with a role from the output, e.g., MyRole.

Then list attached policies:
```bash
aws iam list-attached-role-policies --role-name $_ROLE_NAME
```

**Expected Output**: Role details including AssumeRolePolicyDocument and list of policy ARNs, e.g., {"AttachedPolicies": [{"PolicyName": "AdminPolicy", "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"}]}.

### Step 4: Validate and Document Findings

**Context**: Cross-reference profiles with instance metadata if on an EC2 host, or save output for reporting to confirm escalation potential.

If on an EC2 instance, query IMDS for current profile:
```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

Compare with listed profiles to identify mismatches or over-privileges.

**Expected Output**: Instance role name or temporary credentials if profile attached.

Save output to file for analysis: aws iam list-instance-profiles > profiles.json.

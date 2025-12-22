---
id: 7a1bc42f-c7ba-4a19-abce-ec00d94cb5e7
name: List-Attached-Policies-for-AWS-IAM-Role
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.858163+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Accessing more credentials]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Listing all managed policies attached to the specific IAM role]]'
  - '[[tags/Persistence & Backdooring]]'
commands:
  - '[[commands/aws-iam-list-attached-role-policies]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# List-Attached-Policies-for-AWS-IAM-Role

## Summary

This procedure enumerates all managed policies attached to a specific AWS IAM role using the AWS CLI. It allows attackers or auditors to discover the permissions granted to the role, identifying potential privilege escalation paths by revealing access to sensitive resources like S3 buckets, EC2 instances, or other AWS services.

## Description

In an AWS environment, IAM roles define permissions for entities like EC2 instances, Lambda functions, or assumed user sessions. Enumerating attached policies reveals the full scope of privileges, such as read/write access to critical services. This technique is commonly used during cloud reconnaissance to map permissions and chain to further exploitation, like assuming the role for lateral movement. It requires the `iam:ListAttachedRolePolicies` permission on the target role and valid AWS credentials configured via access keys or IAM roles. The output is a JSON list of policy ARNs and names, which can be parsed to assess risks like overly permissive policies (e.g., AdministratorAccess).

## Requirements

1. AWS CLI installed and configured with credentials that have `iam:ListAttachedRolePolicies` permission for the target role.
2. Access to the AWS account or assumed role with read access to IAM metadata.
3. Network connectivity to AWS endpoints (no VPC restrictions blocking IAM API calls).

## Defense

- Implement the principle of least privilege for IAM roles and policies, regularly auditing attachments with tools like IAM Access Analyzer.
- Monitor and analyze AWS CloudTrail logs for `ListAttachedRolePolicies` API calls from unusual sources or IPs.
- Enable AWS Config rules to alert on role policy changes and enforce policy boundaries to limit enumeration scope.

## Objectives

1. Discover all managed policies attached to a specific IAM role.
2. Identify potential privilege escalation opportunities by analyzing policy permissions.
3. Gather intelligence on AWS resource access for further attack planning.

## Instructions

### Step 1: Configure AWS Credentials

**Context**: Ensure AWS CLI is set up with appropriate credentials to authenticate API calls. This step verifies access before enumeration.

Use environment variables or `aws configure` to set access key, secret key, and default region.

**Expected Output**: Successful `aws sts get-caller-identity` returns your current identity without errors.

### Step 2: Enumerate Attached Role Policies

**Context**: Query the IAM service to list all managed policies linked to the target role. This reveals the role's effective permissions for analysis.

**Command** ([[commands/aws-iam-list-attached-role-policies]]):
```bash
aws iam list-attached-role-policies --role-name $_ROLE_NAME
```

> Replace `$_ROLE_NAME` with the name of the IAM role (e.g., `MyEC2Role`). The command queries the IAM API and returns a JSON response. If the role has no policies, an empty list is returned. Parse the output using `jq` for easier reading: `aws iam list-attached-role-policies --role-name $_ROLE_NAME | jq '.AttachedPolicies[] | {PolicyName, PolicyArn}'`. This step succeeds if the API responds with HTTP 200 and lists policies without permission denied errors.

**Expected Output**:
```json
{
    "AttachedPolicies": [
        {
            "PolicyName": "AmazonS3ReadOnlyAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
        },
        {
            "PolicyName": "CustomAdminPolicy",
            "PolicyArn": "arn:aws:iam::123456789012:policy/CustomAdminPolicy"
        }
    ],
    "IsTruncated": false
}
```

### Step 3: Analyze Policy Permissions

**Context**: Review the listed policies to identify high-privilege ones. This manual step helps decide next actions, like fetching full policy details with `aws iam get-policy-version`.

If escalation is suspected (e.g., policies with `*:*` actions), note the PolicyARN for further enumeration. Use decision point: If `AdministratorAccess` is attached, proceed to role assumption; otherwise, check for specific service escalations like S3 to Lambda.

**Expected Output**: Documented list of policies with potential risks, such as full EC2 control or data exfiltration paths.

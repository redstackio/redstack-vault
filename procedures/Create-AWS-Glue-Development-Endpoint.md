---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Create Account|T1136 - Create Account]]'
  - '[[techniques/Cloud Account|T1136.003 - Cloud Account]]'
sub_techniques: []
tags:
  - AWS
  - Cloud
  - Privilege Escalation
  - Shadow Admin
  - Admin Equivalent Permission
commands:
  - '[[commands/aws-glue-create-dev-endpoint]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - AWS
validated: true
---

# Create-AWS-Glue-Development-Endpoint

## Summary

This procedure allows an attacker with admin-equivalent permissions in AWS to create a Glue Development Endpoint, providing a managed environment for running arbitrary code on AWS infrastructure. This can facilitate privilege escalation and access to sensitive data by enabling interactive sessions via SSH on the endpoint.

## Description

AWS Glue Development Endpoints are interactive environments for developing and testing ETL scripts, but they can be abused by attackers to execute commands and potentially pivot within the cloud environment. By creating an endpoint with a service role that has broad permissions, an attacker can connect via SSH and run code that interacts with other AWS resources, leading to data exfiltration or further compromise. This technique assumes the attacker has obtained credentials with permissions to create Glue resources and pass IAM roles, often through shadow admin access where a user has elevated privileges without full awareness.

The procedure uses the AWS CLI to issue the creation command, requiring a unique endpoint name, an IAM role ARN for Glue operations, and a public SSH key for access. Success grants the attacker a persistent compute resource in the victim's AWS account.

## Requirements

1. AWS credentials with `glue:CreateDevEndpoint` and `iam:PassRole` permissions (admin-equivalent access).
2. AWS CLI installed and configured with the compromised credentials.
3. An existing IAM role ARN for the Glue service with necessary permissions (e.g., GlueFullAccess policy attached).
4. A valid public SSH key pair generated for connecting to the endpoint.
5. Network access to AWS APIs (no specific ports beyond standard HTTPS for CLI).

## Defense

- Implement least privilege principles by restricting `glue:CreateDevEndpoint` and `iam:PassRole` to only necessary users and roles.
- Monitor CloudTrail logs for Glue API calls, especially creation of development endpoints, and alert on unusual activity from shadow admin accounts.
- Use AWS Organizations SCPs to deny creation of Glue endpoints in sensitive environments.
- Regularly audit IAM roles and permissions to identify and remove shadow admin access.
- Enable GuardDuty for cloud threat detection, which can flag anomalous resource creation.

## Objectives

1. Create a persistent development endpoint in AWS Glue for executing arbitrary code.
2. Establish SSH access to the endpoint for interactive sessions and privilege escalation.
3. Gain access to sensitive data or other AWS resources via the endpoint's compute environment.

## Instructions

### Step 1: Prepare IAM Role and SSH Key

**Context**: Before creating the endpoint, ensure an IAM role exists for Glue with appropriate permissions, and generate or prepare an SSH key pair for secure access. This step verifies prerequisites to avoid command failures.

Use [[commands/aws-iam-get-role]] or AWS Console to confirm the role ARN. Generate SSH key if needed:

```bash
generate_ssh_key_command_here # e.g., ssh-keygen -t rsa -b 2048 -f my_key
```

> Expected: A public key file (e.g., my_key.pub) and the role ARN noted for the next step. Verify the role has policies like AWSGlueServiceRole.

### Step 2: Create the Glue Development Endpoint

**Context**: Issue the AWS CLI command to create the endpoint, specifying a unique name, the Glue service role, and the public key. This deploys a managed Jupyter/Spark environment accessible via SSH or Zeppelin, allowing code execution.

**Command** ([[commands/aws-glue-create-dev-endpoint]]):

```powershell
aws glue create-dev-endpoint --endpoint-name $_ENDPOINT_NAME --role-arn $_ROLE_ARN --public-key file://$_PUBLIC_KEY_PATH
```

> This command provisions the endpoint, which may take several minutes to become available. The `--endpoint-name` must be unique in the account. The role must trust the Glue service and have execution permissions. The public key enables SSH tunneling. Expected output includes an EndpointName and creation status; poll with `aws glue get-dev-endpoint` to check readiness.

### Step 3: Verify Endpoint Creation and Connect

**Context**: Confirm the endpoint is active and test connectivity to ensure access for further exploitation. This validates success and prepares for code execution.

Use [[commands/aws-glue-get-dev-endpoint]]:

```powershell
aws glue get-dev-endpoint --endpoint-name $_ENDPOINT_NAME
```

> Expected: Response showing "Status": "READY". Then, connect via SSH: `ssh -i private_key.pem -L 8888:localhost:8888 glue@$_ENDPOINT_DNS`. Success allows browser access to Jupyter at localhost:8888 for running code against AWS resources.

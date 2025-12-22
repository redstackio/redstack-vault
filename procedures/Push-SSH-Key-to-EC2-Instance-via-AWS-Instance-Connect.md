---
id: 9c5d72c3-496e-4f27-af27-1c6204a67004
name: Push-SSH-Key-to-EC2-Instance-via-AWS-Instance-Connect
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.637114+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - '[[techniques/Valid Accounts/.001|T1078.001 - Default Accounts]]'
tags:
  - '[[tags/AWS]]'
  - '[[tags/EC2]]'
  - '[[tags/SSH]]'
  - '[[tags/Cloud]]'
  - '[[tags/Instance Connect]]'
commands:
  - '[[commands/aws-ec2-describe-instances]]'
  - '[[commands/aws-ec2-instance-connect-send-ssh-public-key]]'
platforms:
  - AWS
  - Linux
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Push-SSH-Key-to-EC2-Instance-via-AWS-Instance-Connect

## Summary

This procedure demonstrates how to use AWS EC2 Instance Connect to push a public SSH key to an EC2 instance, enabling secure SSH access without exposing port 22 to the internet or requiring a bastion host. It is useful in red team scenarios where an attacker with valid AWS credentials seeks to establish persistent remote access to compromised cloud instances.

## Description

AWS EC2 Instance Connect provides a temporary SSH access mechanism by pushing a public key to an instance on-demand. An attacker with IAM permissions (e.g., ec2:DescribeInstances and ec2-instance-connect:SendSSHPublicKey) can enumerate instances and inject their SSH key, allowing immediate SSH login as the specified OS user (e.g., ubuntu or ec2-user). This technique leverages legitimate AWS APIs for initial access or persistence, bypassing traditional SSH key management. It assumes the target instance runs a supported OS like Amazon Linux or Ubuntu and has the EC2 Instance Connect package installed. Success grants shell access for further post-exploitation, such as lateral movement or data exfiltration.

## Requirements

1. Valid AWS credentials with permissions for ec2:DescribeInstances and ec2-instance-connect:SendSSHPublicKey.
2. AWS CLI installed and configured with a profile containing the necessary credentials.
3. A public SSH key file (e.g., ~/.ssh/id_rsa.pub) generated for the attacker's machine.
4. Network access to AWS APIs (no direct instance connectivity needed initially).
5. Target EC2 instance in a supported region with Instance Connect enabled.

## Defense

- Implement least-privilege IAM policies to restrict ec2-instance-connect:SendSSHPublicKey to trusted users/roles.
- Enable AWS CloudTrail logging for API calls and monitor for unusual DescribeInstances or SendSSHPublicKey activity from unexpected IPs.
- Use AWS Config rules to audit EC2 instances for Instance Connect package and restrict SSH user access via instance metadata.
- Integrate with SIEM for alerts on SSH key pushes to production instances.

## Objectives

1. Enumerate target EC2 instances to identify accessible ones.
2. Push an attacker-controlled SSH public key to the instance for temporary access.
3. Establish SSH connection to the instance for command execution and persistence.

## Instructions

### Step 1: Enumerate EC2 Instances

**Context**: Use the AWS CLI to list EC2 instances in the target region, filtering for relevant details like InstanceId, KeyName, and State. This step identifies the target instance without alerting via direct access attempts. The jq filter parses the JSON response to show only essential fields.

**Command** ([[commands/aws-ec2-describe-instances]]):
```bash
aws ec2 describe-instances --profile $_PROFILE --region $_REGION | jq '.Reservations[].Instances[] | {InstanceId, KeyName, State}'
```

> This command queries the EC2 API for instance details. Replace $_PROFILE with your AWS CLI profile name and $_REGION with the target region (e.g., us-east-1). The output is a JSON array of instances; note the InstanceId of the target.

### Step 2: Push SSH Public Key to Instance

**Context**: Send the public SSH key to the selected instance using EC2 Instance Connect. This grants temporary (up to 60 seconds) SSH access. Specify the instance's availability zone, OS user, and key file. The key is pushed via the AWS API, authorizing the corresponding private key for login.

**Command** ([[commands/aws-ec2-instance-connect-send-ssh-public-key]]):
```bash
aws ec2-instance-connect send-ssh-public-key --region $_REGION --instance-id $_INSTANCE_ID --availability-zone $_AVAILABILITY_ZONE --instance-os-user $_OS_USER --ssh-public-key file://$_KEY_FILE --profile $_PROFILE
```

> Replace $_INSTANCE_ID with the InstanceId from Step 1, $_AVAILABILITY_ZONE with the instance's AZ (e.g., us-east-1a, query via describe-instances if needed), $_OS_USER with the target user (e.g., ubuntu for Ubuntu AMIs), and $_KEY_FILE with the path to your public key (e.g., shortkey.pub). If successful, the command returns a success message; the key is valid for SSH for 60 seconds.

### Step 3: Connect via SSH

**Context**: Immediately after pushing the key, connect to the instance using standard SSH with the private key corresponding to the pushed public key. This establishes the shell session for further actions.

**Instructions**: Use the ssh command with the instance's public DNS or IP, specifying the private key and user:
```bash
ssh -i $_PRIVATE_KEY_FILE $_OS_USER@$_INSTANCE_PUBLIC_DNS -o StrictHostKeyChecking=no
```

> Replace $_PRIVATE_KEY_FILE with the path to your private key (e.g., shortkey), $_OS_USER as before, and $_INSTANCE_PUBLIC_DNS with the instance's public DNS name (from describe-instances output). The -o StrictHostKeyChecking=no skips host key verification for automation. Expected: Successful login to the instance shell prompt.

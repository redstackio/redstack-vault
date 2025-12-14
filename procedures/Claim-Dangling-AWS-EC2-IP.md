---
id: proc-claim-dangling-ec2
tags:
  - aws
  - ec2
  - cloud
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Email Accounts]]'
updated_at: '2025-12-14T04:38:49.484Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Email Accounts]]'
---
# Claim-Dangling-AWS-EC2-IP

## Summary

This procedure claims a dangling AWS EC2 IP address by launching a new instance and associating it with the IP, thereby redirecting traffic from a misconfigured DNS record to attacker-controlled infrastructure.

## Description

When a DNS record points to a deleted EC2 instance's Elastic IP without removal, attackers with an AWS account can reclaim that IP by launching a new instance and associating it. In this case, the IP 52.214.138.192 was unused, allowing the attacker to set up a web server. The target environment is AWS EC2; prerequisites include an active AWS account with EC2 permissions. Outcomes include full control over inbound traffic to the subdomain.

## Requirements

1. Active AWS account with EC2 launch and Elastic IP association permissions
2. Knowledge of the dangling IP from prior DNS recon
3. Basic AWS CLI or console access

## Defense

Defensive measures and detection strategies:

- Disassociate and release Elastic IPs immediately upon instance deletion
- Use AWS Config rules to monitor for orphaned DNS entries
- Implement least-privilege IAM policies to limit IP reuse by unauthorized accounts

## Objectives

1. Associate the dangling IP with a new attacker-controlled EC2 instance
2. Redirect subdomain traffic to malicious server
3. Enable serving arbitrary content or obtaining certificates

## Instructions

### Step 1: Launch EC2 Instance

**Context**: Create a new EC2 instance in the appropriate region (e.g., eu-west-1 for the IP's location) to prepare for IP association.

**Command** (AWS CLI example):
```bash
aws ec2 run-instances --image-id ami-0abcdef1234567890 --count 1 --instance-type t2.micro --key-name MyKeyPair
```

> Replace with actual AMI and details. Wait for instance to launch, then note its ID.

### Step 2: Associate Elastic IP

**Context**: Allocate or associate the known dangling Elastic IP to the new instance, claiming control.

**Command** (AWS CLI):
```bash
aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id eipalloc-12345678
```

> If the IP is Elastic, use its allocation ID (discover via AWS console). Expected output: Association successful. Configure the instance with a web server (e.g., apt install nginx).

### Step 3: Configure Server

**Context**: Set up the instance to handle HTTP requests, simulating malicious content serving.

**Command** (On instance via SSH):
```bash
echo "<!-- hackerone.com/ian --> <h1>Takeover Successful</h1>" > /var/www/html/index.html
systemctl restart nginx
```

> This serves custom content when the subdomain is accessed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Email Accounts]] Compromise Infrastructure: Cloud Accounts/Infrastructure

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[aws]]
- [[ec2]]
- [[cloud]]
- [[subdomain-takeover]]

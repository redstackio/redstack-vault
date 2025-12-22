---
id: proc-claim-orphaned-ec2
name: Claim Orphaned AWS EC2 IP for Takeover
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.595Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - aws
  - ec2
  - subdomain-takeover
  - cloud-abuse
commands: []
platforms:
  - AWS
  - Cloud
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Claim Orphaned AWS EC2 IP for Takeover

## Summary

This procedure involves launching a new AWS EC2 instance on an orphaned IP address identified from a stale DNS record, granting control over the associated subdomain.

## Description

When an EC2 instance is terminated without removing its DNS entry, the IP becomes available for reuse. Attackers with an AWS account can launch a new instance on that IP, redirecting traffic from the subdomain. This enables serving malicious content, phishing, or certificate acquisition. Prerequisites include AWS credentials with EC2 permissions.

## Requirements

1. AWS account with EC2 launch and IP assignment permissions
2. Identified orphaned IP (e.g., 52.47.57.107)
3. AWS CLI installed or console access

## Defense

Defensive measures and detection strategies:

- Automate DNS cleanup on instance termination using AWS Lambda or CloudWatch
- Monitor for unauthorized EC2 launches on specific IPs
- Use AWS Config to track resource changes

## Objectives

1. Secure the orphaned IP by launching an instance
2. Redirect subdomain traffic to attacker-controlled server
3. Enable further exploitation like content serving

## Instructions

### Step 1: Launch EC2 on Orphaned IP

**Context**: Use AWS console or CLI to create an instance specifying the elastic IP or direct IP assignment.

**Command** (AWS CLI example):
```bash
aws ec2 run-instances --image-id ami-0abcdef1234567890 --instance-type t2.micro --subnet-id subnet-12345678 --private-ip-address 52.47.57.107 --associate-public-ip-address
```

> Adjust parameters for the region (e.g., eu-west-1 for France). Expected output: Instance ID and running status. Configure security groups to allow HTTP/HTTPS inbound.

### Step 2: Install Web Server

**Context**: SSH into the instance and set up a server to respond to the subdomain.

**Command** (On instance):
```bash
sudo apt update && sudo apt install apache2 -y
sudo systemctl start apache2
```

> Edit /var/www/html/index.html to include custom content. The server will now handle requests to fr1.vpn.zomans.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[aws]]
- [[ec2]]

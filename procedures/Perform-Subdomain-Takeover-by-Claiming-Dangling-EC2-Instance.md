---
tags:
  - subdomain-takeover
  - dns
  - aws
  - ec2
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:26.557Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: d6c20398-c334-4436-a86f-b442642beab0
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Perform Subdomain Takeover by Claiming Dangling EC2 Instance

## Summary

This procedure identifies a dangling DNS A record pointing to a terminated AWS EC2 instance and claims the resource to achieve subdomain takeover, allowing control over the subdomain for further exploitation.

## Description

In this attack scenario, a target's DNS configuration leaves an A record unresolved after terminating an EC2 instance, making the IP available for registration. The attacker queries DNS to find such records, then uses an AWS account to launch an EC2 instance that responds at that IP, hijacking the subdomain. This can occur in cloud environments where cleanup of DNS entries lags behind resource termination. Prerequisites include public DNS access and an AWS account for resource provisioning. Expected outcomes include full control over the subdomain, enabling hosting of malicious payloads.

## Requirements

1. Access to public DNS resolution tools (e.g., dig, nslookup)
2. An active AWS account with permissions to launch EC2 instances
3. Knowledge of the target's domain and subdomain structure

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records against active cloud resources using automated scripts
- Implement DNS monitoring for unresolved A records and alert on dangling entries
- Use AWS Config rules to enforce cleanup of DNS upon resource termination

## Objectives

1. Discover and verify the dangling DNS A record
2. Claim the EC2 IP/resource to resolve the subdomain to attacker-controlled instance
3. Establish persistent control over the subdomain

## Instructions

### Step 1: Enumerate and Identify Dangling DNS Record

**Context**: Query the target's DNS to find A records for subdomains that do not resolve to active services.

Use DNS lookup tools to check the subdomain's A record and verify if the IP responds to HTTP/HTTPS requests.

> Perform a DNS lookup:
> ```bash
dig subdomain.target.com
```
> Expected output: A record with IP, but no response on port 80/443.

### Step 2: Verify Non-Existence and Availability

**Context**: Confirm the EC2 instance at the IP is terminated and the resource is claimable.

Ping the IP and attempt connections; if unresponsive, proceed to AWS console to check for availability of the IP (e.g., Elastic IP).

> No specific command; use AWS CLI if authenticated, but since public, manual verification suffices.
> Expected output: No response from IP, confirming dangling status.

### Step 3: Claim the EC2 Resource

**Context**: Launch an EC2 instance configured to use the dangling IP.

In the AWS Management Console or via API, create a new EC2 instance and associate the available IP (if EIP) or launch at the public IP range.

> Use AWS console: Navigate to EC2 > Launch Instance > Configure network to match the dangling IP.
> Expected output: Instance running and accessible at the IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[aws]]
- [[ec2]]

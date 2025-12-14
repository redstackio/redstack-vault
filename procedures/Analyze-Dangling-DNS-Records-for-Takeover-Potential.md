---
id: proc-uuid-002
name: Analyze-Dangling-DNS-Records-for-Takeover-Potential
tags:
  - dns-misconfiguration
  - dangling-cname
  - aws
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-query-dns]]'
  - '[[commands/curl-aws-ip-check]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T05:32:31.187Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-Dangling-DNS-Records-for-Takeover-Potential

## Summary

This procedure analyzes DNS records to detect dangling CNAMEs resulting from terminated cloud instances, evaluating the risk of subdomain takeover where the IP can be reassigned to attacker-controlled resources.

## Description

When an EC2 instance is terminated, its public IP is released to the AWS pool without automatically updating associated DNS records. If a CNAME points to the instance's public DNS (e.g., ec2-*.compute.amazonaws.com), it becomes dangling. An attacker can then launch a new instance to claim the IP, redirecting traffic to the subdomain. This analysis involves re-querying records and cross-referencing with AWS IP data to confirm vulnerability.

## Requirements

1. Prior DNS query results showing EC2 CNAME
2. Access to AWS IP range APIs
3. Ability to monitor for IP changes over time

## Defense

Defensive measures and detection strategies:

- Use Elastic IPs for stable DNS associations
- Automate DNS cleanup on instance termination
- Scan for dangling records using tools like dnsdumpster

## Objectives

1. Confirm the CNAME targets a transient EC2 resource
2. Assess impact of IP release on subdomain control
3. Identify escalation paths like traffic hijacking

## Instructions

### Step 1: Re-Query for Changes

**Context**: Check if the record persists post-termination to confirm dangling status.

**Command** ([[commands/dig-query-dns]]):
```bash
dig @1.0.0.1 max1.liveplan.com CNAME +short
```

> If the CNAME remains unchanged, it indicates no update was made upon termination.

### Step 2: Validate IP Against AWS Ranges

**Context**: Confirm the IP's origin and reassignment potential.

**Command** ([[commands/curl-aws-ip-check]]):
```bash
curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq '.prefixes[] | select(.ip_prefix=="54.68.0.0/15")'
```

> Output shows the IP in us-west-2 region, highlighting pool reassignment risk.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/dig-query-dns]]
- [[commands/curl-aws-ip-check]]

## Tools Used


## Tags

- [[dns-misconfiguration]]
- [[dangling-cname]]

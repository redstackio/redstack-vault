---
tags:
  - subdomain-takeover
  - reconnaissance
  - dns
type: procedure
tools:
  - '[[tools/takeover-cyberint]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.797Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: cfe4a3b4-1b09-40d4-bd88-81bb15dcac21
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Monitor-for-Subdomain-Takeover-Vulnerabilities

## Summary

This procedure uses an online monitoring tool to scan a target domain for subdomain takeover vulnerabilities by detecting stale DNS records pointing to decommissioned cloud resources, such as Azure VMs.

## Description

In this attack scenario, attackers passively or actively monitor public domains for misconfigurations where subdomains resolve to dead cloud endpoints. The procedure targets environments like Azure where DNS entries (e.g., via Traffic Manager) are not properly cleaned up after decommissioning. Expected outcomes include a list of vulnerable subdomains ready for enumeration. Prerequisites include internet access and basic knowledge of DNS.

## Requirements

1. Internet access to web-based scanning tools
2. Target domain name (e.g., starbucks.com)
3. No special credentials; public DNS queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for stale entries using tools like Azure DNS cleanup scripts
- Implement monitoring for DNS changes and subdomain resolutions with services like Cloudflare or AWS Route 53 alerts
- Use certificate transparency logs to detect unauthorized subdomain usage

## Objectives

1. Identify potential subdomain takeover candidates
2. Flag issues like dead Azure CloudApp pointers
3. Prepare for deeper enumeration

## Instructions

### Step 1: Access Monitoring Tool

**Context**: Launch the web-based scanner to input the target and initiate the scan.

No command required; navigate to https://takeover.cyberint.com/ and enter the domain (e.g., starbucks.com).

> The tool performs automated DNS scans and returns flagged subdomains with issues, such as 2 problematic entries pointing to claimable resources.

### Step 2: Review Scan Results

**Context**: Analyze the output for vulnerable subdomains.

No command; inspect the dashboard for details like subdomain names and resource types (e.g., Azure trafficmanager.net).

> Expected: List of subdomains like svcardproxydevus.starbucks.com flagged as takeover-eligible.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/takeover-cyberint]]

## Tags

- [[subdomain-takeover]]
- [[Reconnaissance]]

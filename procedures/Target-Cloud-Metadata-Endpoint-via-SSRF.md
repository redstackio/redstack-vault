---
tags:
  - ssrf
  - cloud-metadata
  - aws
  - openstack
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - AWS
  - OpenStack
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.345Z'
sub_techniques: []
id: fa689055-6e60-4a28-88a4-5d932dc72eeb
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Target-Cloud-Metadata-Endpoint-via-SSRF

## Summary

This procedure directs the SSRF exploit to the link-local IP 169.254.169.254, where EC2 and OpenStack host metadata services accessible only from the instance itself, enabling internal reconnaissance without direct access.

## Description

Cloud providers like AWS EC2 and OpenStack expose instance metadata at http://169.254.169.254/latest/meta-data/, including configuration details. By using SSRF, an attacker can force the Phabricator server to query this endpoint, bypassing network restrictions. This targets multicast/link-local addresses not routable externally, highlighting the risk dismissed in prior reports.

## Requirements

1. Confirmed SSRF in target application
2. Server hosted on EC2 or OpenStack instance
3. Port 80 open internally for metadata service

## Defense

Defensive measures and detection strategies:

- Blacklist private IP ranges in SSRF-handling code
- Disable metadata service access or use IMDSv2 on AWS
- Log and alert on server-initiated requests to 169.254.169.254

## Objectives

1. Reach internal metadata service via SSRF
2. Perform discovery of instance details
3. Prepare for data exfiltration

## Instructions

### Step 1: Identify Metadata Endpoint

**Context**: Recognize the standard cloud metadata URL structure.

No command; note endpoints like /latest/meta-data/ and /latest/user-data.

> These are only resolvable from the instance's loopback or link-local interface.

### Step 2: Craft SSRF Payload for Metadata

**Context**: Input the metadata URL into the vulnerable field.

Use http://169.254.169.254/latest/meta-data/ as the URL in the meme feature.

> Server fetches and potentially embeds the metadata in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- metadata
- ec2

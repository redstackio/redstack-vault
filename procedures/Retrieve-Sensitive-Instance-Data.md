---
tags:
  - information-disclosure
  - cloud-metadata
  - credentials
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - AWS
  - OpenStack
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T04:39:02.337Z'
sub_techniques: []
id: 35e5bb51-10c9-423f-98d0-537690b12f2e
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Retrieve-Sensitive-Instance-Data

## Summary

This procedure uses SSRF to pull specific sensitive data from cloud metadata endpoints, such as hostnames, IP addresses, and user-data scripts that may contain passwords, private keys, or source code.

## Description

Once SSRF reaches the metadata service, targeted requests to paths like /latest/meta-data/hostname or /latest/user-data expose critical information. User-data often includes bootstrap scripts with secrets, leading to broader compromise like accessing localhost services (e.g., databases).

## Requirements

1. Active SSRF to 169.254.169.254
2. Knowledge of metadata API paths
3. Application that echoes or logs SSRF responses

## Defense

Defensive measures and detection strategies:

- Restrict metadata access with instance roles and policies
- Enable metadata token requirements (IMDSv2)
- Parse and sanitize SSRF responses to prevent echo

## Objectives

1. Collect instance configuration and network details
2. Extract credentials from user-data
3. Enable further lateral movement

## Instructions

### Step 1: Request Basic Metadata

**Context**: Fetch core instance identifiers.

Input http://169.254.169.254/latest/meta-data/hostname into SSRF.

> Output includes the instance's hostname.

### Step 2: Extract User Data Scripts

**Context**: Pull potentially secret-laden startup data.

Use http://169.254.169.254/latest/user-data for the payload.

> Reveals scripts with passwords, keys, or code if present.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- disclosure
- user-data
- keys

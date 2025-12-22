---
tags:
  - fastly
  - takeover
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.664Z'
sub_techniques: []
id: 821916c5-984e-4809-bcc7-e48abaabaa46
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Fastly-Service-for-Takeover

## Summary

This procedure creates a new Fastly service and adds an unconfigured subdomain to claim control via SNI routing.

## Description

Exploiting the gap, an attacker registers a free Fastly service, adds the target domain (e.g., registry.nodejs.org), and configures it to serve custom content. Fastly doesn't verify DNS ownership for additions, allowing instant takeover. Outcomes: Attacker controls all traffic to the subdomain.

## Requirements

1. Free Fastly account
2. Dashboard access
3. Basic VCL knowledge for custom responses

## Defense

Defensive measures and detection strategies:

- Monitor CDN logs for unauthorized domain additions
- Require DNS TXT records for domain verification in CDN policies
- Use subdomain lockdown tools to prevent dangling records

## Objectives

1. Register and configure a new Fastly service
2. Add the target subdomain without verification
3. Enable traffic interception

## Instructions

### Step 1: Create New Service

**Context**: Log into Fastly and start a new distribution.

Navigate to Fastly dashboard > Create a Service > Choose 'Blank' template.

### Step 2: Add Domain

**Context**: Claim the subdomain in the domains section.

In Service Settings > Domains > Add Domain: Enter 'registry.nodejs.org' > Save. No DNS proof needed.

**Expected Output**: Domain added successfully; service activates.

### Step 3: Configure Response

**Context**: Set up a backend or VCL to serve custom HTML.

Edit VCL: In vcl_recv, respond with synthetic content including a comment like '<!--You probably meant registry.npmjs.org-->'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[takeover]]
- [[fastly]]

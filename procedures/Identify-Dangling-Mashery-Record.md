---
tags:
  - dns-probing
  - service-identification
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:39.533Z'
sub_techniques: []
id: 3370ff4c-d084-43bb-bbc5-88c0aff936fb
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Dangling-Mashery-Record

## Summary

Probe a suspected subdomain to detect dangling DNS records pointing to third-party services like Mashery, indicated by specific server headers.

## Description

Visiting the subdomain http://developer.openapi.starbucks.com/ returns a 200 OK with a 'Mashery Proxy' header, signaling an unclaimed record after service discontinuation. This step confirms the vulnerability for takeover.

## Requirements

1. HTTP access to port 80
2. Browser for header inspection
3. Knowledge of common third-party services

## Defense

Defensive measures and detection strategies:

- Remove unused DNS records promptly
- Monitor for unexpected server headers
- Implement CNAME validation on services

## Objectives

1. Confirm dangling record existence
2. Identify the third-party service
3. Assess takeover feasibility

## Instructions

### Step 1: Access Subdomain URL

**Context**: Visit the subdomain to trigger DNS resolution and observe the response.

Open http://developer.openapi.starbucks.com/ in a browser.

**Expected Output**: 200 OK response with default Mashery page.

### Step 2: Inspect Response Headers

**Context**: Check for indicators of the service.

Use browser dev tools to view headers, looking for 'Server: Mashery Proxy'.

**Expected Output**: Confirmation of Mashery involvement.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- [[dns-probing]]
- [[service-identification]]

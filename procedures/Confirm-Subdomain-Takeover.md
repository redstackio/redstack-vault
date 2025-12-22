---
tags:
  - verification
  - takeover
  - web
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
  - '[[Web Protocols]]'
updated_at: '2025-12-14T04:51:26.659Z'
sub_techniques: []
id: 98b1f87d-df18-4ad7-99be-a9114844bc27
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Web Protocols]]'
---
# Confirm-Subdomain-Takeover

## Summary

This procedure validates subdomain control by serving and observing custom content on the hijacked domain.

## Description

After routing, serve a benign page with identifiable markers (e.g., HTML comment) and access the subdomain to confirm resolution to the attacker's service. In the vulnerability, this displayed a warning comment, proving interception. Outcomes: Proof of full control and traffic handling.

## Requirements

1. Configured Fastly service with custom response
2. Browser for testing
3. Access to the target URL

## Defense

Defensive measures and detection strategies:

- Set up content integrity checks for subdomains
- Monitor for unexpected responses or comments in served content
- Use browser extensions or scripts to alert on hijacked domains

## Objectives

1. Serve custom identifiable content
2. Access and verify the subdomain response
3. Confirm exclusive control

## Instructions

### Step 1: Configure Custom Content

**Context**: Update VCL to inject a unique marker.

In Fastly VCL editor: Add to vcl_deliver: synth(0, "<html><!--You probably meant registry.npmjs.org--></html>").

### Step 2: Test Access

**Context**: Visit the subdomain to check response.

Open https://registry.nodejs.org in a browser and view source.

**Expected Output**: Page source includes the custom comment, not official npm content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Web Protocols]] Application Layer Protocol: Web Protocols

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[confirmation]]
- [[html]]

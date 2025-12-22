---
id: proc-uuid-002
name: Identify-Delete-Endpoint-via-Interception
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.993Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - endpoint-discovery
  - interception
  - burp-suite
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Identify-Delete-Endpoint-via-Interception

## Summary

This procedure involves intercepting HTTP traffic during an album deletion to identify the vulnerable /mediagallery/delete/id/{album-id} endpoint, confirming the lack of CSRF protections.

## Description

To exploit the CSRF vulnerability, the attacker performs a legitimate delete action from their account while proxying traffic through Burp Suite. This reveals the GET request structure, which lacks token verification, making it forgeable. The scenario targets the DoD media gallery web application, assuming the attacker has an account and album. Prerequisites include Burp Suite setup as a proxy. Outcomes include endpoint details for PoC crafting.

## Requirements

1. Burp Suite configured as browser proxy
2. Authenticated session on the target site
3. Existing album to delete

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and monitor for proxy interception attempts
- Log all delete requests and alert on unusual patterns

## Objectives

1. Discover the vulnerable endpoint
2. Confirm absence of CSRF tokens
3. Gather parameters for exploitation

## Instructions

### Step 1: Configure Interception

**Context**: Set up Burp Suite to capture requests from the browser.

Launch Burp Suite and configure the browser to use its proxy (default 127.0.0.1:8080).

### Step 2: Perform Delete Action

**Context**: Trigger the delete to capture the request.

Navigate to the album, initiate deletion, and inspect the intercepted GET request to /mediagallery/delete/id/{album-id}.

**Expected Output**: Request details showing GET method and no tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[endpoint-discovery]]
- [[interception]]
- [[tools/Burp-Suite]]

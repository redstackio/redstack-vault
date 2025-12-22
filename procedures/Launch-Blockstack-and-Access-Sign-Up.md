---
tags:
  - launch
  - browser
  - sign-up
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:32:10.199Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b54aaf00-fd3a-4af5-9c16-ce0bdf281d4c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Launch-Blockstack-and-Access-Sign-Up

## Summary

This procedure launches the Blockstack Browser application on macOS and uses Firefox to access the local sign-up page, triggering network requests that may contain sensitive data for interception.

## Description

Blockstack Browser runs a local server on port 8888, serving pages like the sign-up endpoint. Accessing this via a proxied browser simulates user interaction and generates outbound requests to third-party services. The expected outcome is the initiation of traffic flows where the Core API Password is embedded in URLs. This requires the proxy to be active and Firefox configured accordingly.

## Requirements

1. Blockstack Browser installed
2. Burp Suite proxy configured and running
3. Firefox with proxy settings enabled

## Defense

Defensive measures and detection strategies:

- Implement Referer-Policy headers in applications to restrict leaks
- Monitor local port access and unexpected outbound connections
- Use browser extensions to block or log sensitive header transmissions

## Objectives

1. Start the local Blockstack server
2. Load the sign-up page to initiate requests
3. Confirm traffic routing through the proxy

## Instructions

### Step 1: Launch Blockstack Browser

**Context**: Start the application to activate its local server.

No command required; use the Applications folder.

> Double-click Blockstack Browser in /Applications to launch it.

### Step 2: Access Sign-Up Page in Firefox

**Context**: Use Firefox (version 66.0.3) with proxy to visit the local endpoint.

No command required; enter URL in address bar.

> Ensure Firefox is set to use the Burp proxy (127.0.0.1:8080), then navigate to http://localhost:8888/sign-up.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell (adapted for macOS app launch)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Burp-Suite]]

## Tags

- app-launch
- local-access
- firefox

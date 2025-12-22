---
id: proc-domain-http-redirect
tags:
  - misconfiguration
  - http-redirect
  - dos
  - domain-management
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Google Workspace
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:30:27.287Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Configure-Domain-HTTP-Redirect

## Summary

This procedure leverages unauthorized access to configure an HTTP redirect on a target domain (e.g., ubereats.com) via Google G Suite, pointing traffic to an invalid or disruptive location to cause temporary Denial of Service for users attempting to access the service.

## Description

Building on an authorization bypass, this procedure involves editing domain settings in G Suite to set up a redirect rule. The attack targets misconfigured domains where external control is possible. In the UberEats scenario, this disrupts web and app access by redirecting to a non-functional endpoint. Prerequisites include prior access to domain settings. Expected outcomes: Active redirect causing service unavailability, verifiable via HTTP requests.

## Requirements

1. Unauthorized access to G Suite domain settings (from prior bypass)
2. Knowledge of target domain's DNS propagation
3. Web browser for configuration and testing
4. Invalid target URL for redirect (e.g., http://nonexistent.example.com)

## Defense

Defensive measures and detection strategies:

- Lock down domain delegations in G Suite to verified owners only
- Implement DNS change monitoring and approval workflows
- Use web application firewalls (WAF) to detect anomalous redirects
- Regularly test domain configurations for redirect loops or invalid targets

## Objectives

1. Set up HTTP redirect to disruptive location
2. Propagate changes to affect user traffic
3. Induce DoS by preventing service access

## Instructions

### Step 1: Navigate to Redirect Settings

**Context**: Locate the URL forwarding or alias configuration in G Suite.

In the admin console, go to Apps > Google Workspace > Domains > Manage domains, then select URL redirects for ubereats.com.

> Ensure the interface allows edits without additional auth.

### Step 2: Define Redirect Rule

**Context**: Create a rule mapping the domain root or paths to an invalid endpoint.

Set the source as https://ubereats.com/* and target as http://disruptive.invalid/ (or similar). Choose permanent (301) redirect for persistence.

> Save the configuration; changes may take minutes to propagate via DNS.

### Step 3: Verify Redirect Activation

**Context**: Test the redirect to confirm DoS impact.

Use a browser or curl to access ubereats.com and observe the redirect. Check HTTP headers for Location: disruptive.invalid.

> Expected output: Traffic redirects, preventing access to UberEats; some users experience loading failures.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- misconfiguration
- http-redirect
- dos

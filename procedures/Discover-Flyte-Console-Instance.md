---
tags:
  - reconnaissance
  - flyte
  - discovery
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:53:38.206Z'
sub_techniques: []
id: a1b63219-cc3f-42ae-b992-827380fefbb7
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover Flyte Console Instance

## Summary

This procedure involves identifying and verifying the presence of a Flyte Console instance on a target domain, such as an internal Uber subdomain, to map the initial attack surface for potential vulnerabilities.

## Description

Flyte Console is a web-based UI for managing Flyte workflows. In this scenario, attackers scan or manually check domains for deployed instances, confirming accessibility without authentication. This step is crucial for targeting unauthenticated endpoints like CORS proxies. Expected outcomes include URL confirmation and basic functionality testing, setting up for code audits and exploitation.

## Requirements

1. Public or internal network access to the target domain (e.g., uberinternal.com)
2. Web browser for manual verification
3. Knowledge of Flyte deployment patterns from documentation

## Defense

Defensive measures and detection strategies:

- Implement domain monitoring for unauthorized Flyte deployments
- Use WAF rules to detect anomalous access to console paths
- Log and alert on unauthenticated UI access attempts

## Objectives

1. Confirm Flyte Console deployment on the target
2. Verify lack of authentication for initial access
3. Identify base URL for further probing

## Instructions

### Step 1: Identify Target Domain

**Context**: Start by selecting a domain known to host internal tools, such as uberinternal.com, based on OSINT or prior knowledge.

Navigate to potential subdomains like flyte-poc-us-east4.uberinternal.com using a browser.

> Look for Flyte branding or console elements on the page load.

### Step 2: Verify Instance Accessibility

**Context**: Ensure the console loads without login prompts, indicating unauthenticated routes.

Interact with the UI to check for proxy or API endpoints via developer tools (Network tab).

> Successful load confirms the instance is live and exploitable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[flyte]]
- [[Discovery]]

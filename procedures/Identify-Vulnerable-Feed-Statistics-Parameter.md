---
tags:
  - open-redirect
  - wordpress
  - recon
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:23.113Z'
sub_techniques: []
id: 680e0bed-e36c-4f9b-b1f7-c7f1acec7430
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-Feed-Statistics-Parameter

## Summary

This procedure involves examining WordPress sites running the Feed Statistics plugin to identify the ?feed-stats-url= parameter, which accepts arbitrary Base64-encoded URLs without validation, enabling open redirects.

## Description

In the context of testing WordPress 3.9.1 on Debian Linux, this step uses a web browser to inspect plugin behavior. The plugin's clickthrough tracking feature decodes and redirects to provided URLs without checking domains or requiring post IDs, affecting all versions and allowing attackers to phish users from legitimate sites.

## Requirements

1. Access to a WordPress site with Feed Statistics plugin installed
2. Web browser like Firefox for manual testing
3. Basic knowledge of URL parameters and Base64 encoding

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against whitelists of allowed domains
- Implement referrer checks or CSP headers to block unauthorized redirects
- Monitor access logs for suspicious ?feed-stats-url= parameters with external Base64 payloads

## Objectives

1. Confirm presence of vulnerable parameter on target site
2. Verify lack of validation in redirect handling
3. Prepare for payload crafting

## Instructions

### Step 1: Examine Plugin Installation

**Context**: Navigate to the target WordPress site and check for the Feed Statistics plugin via source code or known paths.

Use [[tools/Firefox]] to load the site and inspect network requests or plugin files at /wp-content/plugins/wordpress-feed-statistics/.

> Look for references to feed-stats-url in JavaScript or PHP endpoints.

### Step 2: Test Parameter Acceptance

**Context**: Probe the parameter to see if it accepts arbitrary inputs.

In the browser address bar, append ?feed-stats-url= followed by a simple Base64 string like aHR0cDovL3d3dy5leGFtcGxlLmNvbS8= and observe if it attempts a redirect.

> Expected behavior: Redirect to http://www.example.com/ without errors, confirming no validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- open-redirect
- wordpress

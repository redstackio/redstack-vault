---
id: proc-discover-encoded-slash-redirect
tags:
  - open-redirect
  - encoded-slash
  - phishing
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.334Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Encoded Slash Redirect

## Summary

This procedure identifies an open redirect vulnerability by accessing a URL with an encoded slash (%2F) in the path, causing the server to redirect to an external IP or domain without proper validation, enabling potential phishing.

## Description

In the context of testing hackerone.com, malformed URLs with encoded slashes exploit improper path parsing, allowing attackers to redirect users to arbitrary external sites. This step serves as the entry point for discovering the vulnerability, using a placeholder external IP like 1572395042 to confirm the redirect behavior. Prerequisites include a web browser and public access to the target site; expected outcomes are unauthorized redirects that could trick users into visiting malicious pages.

## Requirements

1. Web browser (e.g., Chrome) for URL testing
2. Network access to hackerone.com and external targets
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to reject encoded slashes in paths
- Use allowlists for redirect domains
- Monitor server logs for suspicious %2F usage and anomalous redirects

## Objectives

1. Confirm open redirect via encoded path manipulation
2. Establish baseline for further encoding bypasses
3. Demonstrate potential for phishing redirection

## Instructions

### Step 1: Construct and Access Malformed URL

**Context**: Build a URL with an encoded slash to test if the server treats it as a redirect trigger to an external endpoint.

No specific command; use browser navigation:

Navigate to: `https://hackerone.com/%2F1572395042`

> This URL encodes a slash (%2F) followed by a numeric placeholder representing an external IP (e.g., example.com). The server parses it as a redirect without validating the domain, leading to an external jump. Expected output: Browser location changes to the external site.

### Step 2: Verify Redirect

**Context**: Confirm the redirect occurs and note the destination to validate the vulnerability.

Observe browser behavior post-navigation.

> Successful execution shows a seamless redirect to the external IP/domain. If blocked, it indicates partial mitigation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- open-redirect
- encoded-slash

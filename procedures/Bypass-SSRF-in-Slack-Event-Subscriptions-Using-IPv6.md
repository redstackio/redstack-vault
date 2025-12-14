---
id: proc-slack-ssrf-ipv6
tags:
  - ssrf
  - slack
  - ipv6
  - localhost-bypass
  - internal-scanning
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:25.716Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-SSRF-in-Slack-Event-Subscriptions-Using-IPv6

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in Slack's Event Subscriptions feature by bypassing host validation using IPv6 localhost notation ([::]), enabling connections to internal services for port scanning and service banner retrieval.

## Description

Slack's Event Subscriptions allow apps to receive notifications via a user-specified URL. The API endpoint https://api.slack.com/apps/{app_code}/event-subscriptions validates hosts to prevent SSRF but fails to block IPv6 addresses like [::], which resolve to localhost (::1). Attackers with access to a Slack app can set the subscription URL to http://[::]:{port}/, causing Slack's servers to connect to internal ports and return responses. This enables reconnaissance of internal infrastructure, including service versions on ports like 22 (SSH) and 25 (SMTP), and potentially reading or updating internal resources. The attack requires app configuration access but no authentication bypass.

## Requirements

1. Valid Slack app code and permissions to configure event subscriptions.
2. Access to the Slack API or app management interface.
3. Optional: A redirector server (e.g., PHP script) to capture responses from internal connections.
4. Knowledge of target internal ports for scanning.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive URL validation that parses and blocks all localhost representations, including IPv6 notations like [::] and ::1.
- Use allowlists for permitted callback URLs instead of blocklists.
- Monitor API logs for suspicious subscription URLs containing IPv6 or localhost patterns.
- Deploy Web Application Firewalls (WAFs) to detect and block SSRF payloads in URL parameters.

## Objectives

1. Bypass SSRF protection to establish internal connections from Slack's servers.
2. Scan internal ports and retrieve service banners for reconnaissance.
3. Validate exploit by testing open and closed ports to confirm localhost resolution.

## Instructions

### Step 1: Access the Event Subscriptions Endpoint

**Context**: Identify the vulnerable endpoint and test basic SSRF blocks to understand validation behavior.

Configure your Slack app to access https://api.slack.com/apps/{app_code}/event-subscriptions. Attempt setting the callback URL to http://localhost:80/.

> This triggers a 500 error due to host validation, confirming protection exists but is incomplete.

### Step 2: Test IPv6 Bypass Payload

**Context**: Probe for bypasses by using IPv6 localhost, which evades string-based host checks.

Set the subscription URL to http://[::]:80/. Submit the configuration via the API or interface.

> If accepted without error, the bypass is successful; the server will attempt internal connections without blocking.

### Step 3: Exploit Specific Internal Ports

**Context**: Use the bypass to target known internal services, capturing responses via a redirector if direct observation is limited.

For port 22 (SSH): Set URL to http://[::]:22/. For port 25 (SMTP): Set to http://[::]:25/. Use a PoC like a PHP redirector (http://hacker.site/x.php/?u={payload}) to relay and observe the internal response.

> Expected: SSH banner 'SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4' or SMTP '220 squid-iad-ypfw.tinyspeck.com ESMTP Postfix'.

### Step 4: Validate with Closed Port

**Context**: Confirm internal routing by targeting a non-existent port, expecting a connection failure.

Set URL to http://[::]:9999/ and monitor for timeout or refusal errors.

> This verifies requests are processed internally, not externally resolved.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- slack
- ipv6
- localhost-bypass

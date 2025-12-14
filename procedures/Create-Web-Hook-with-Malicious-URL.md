---
tags:
  - webhook
  - ssrf
type: procedure
tools:
  - '[[tools/researchersservers]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-gitlabextssrf]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 0e5ac608-2e34-4def-8c83-aef08407dfc2
created_at: '2025-12-14T03:46:09.476Z'
updated_at: '2025-12-14T03:46:09.476Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Web-Hook-with-Malicious-URL

## Summary

Configures a GitLab webhook with a domain vulnerable to DNS rebinding, enabling ToCToU bypass for SSRF.

## Description

The webhook URL points to a custom domain that alternates resolutions between allowed and blocked IPs. Validation uses Addrinfo.getaddrinfo, but HTTParty re-resolves, allowing race exploitation. Requires custom DNS setup via researchersservers.

## Requirements

1. Authenticated access to repository settings
2. Custom DNS server running with alternating A records (0 TTL)
3. Domain gitlabextssrf.webhooks.pw configured

## Defense

Defensive measures and detection strategies:

- Implement consistent DNS resolution in validation and request
- Block low-TTL domains or monitor webhook URLs

## Objectives

1. Setup payload delivery vector
2. Verify DNS rebinding behavior
3. Prepare for race condition triggering

## Instructions

### Step 1: Configure Custom DNS

**Context**: Use researchersservers to alternate IPs: 198.211.125.160 (allowed) and 127.0.0.1 (blocked).

**Command** (Tool Setup):
No direct command; configure 41_gitlab.json for domain.

> Start the DNS server and point resolver to it.

### Step 2: Add Webhook

**Context**: In repo settings > Webhooks, add URL http://gitlabextssrf.webhooks.pw:9999/.

**Command** (Verify DNS):
Execute [[commands/dig-gitlabextssrf]] to confirm alternation:

```bash
dig +noall +answer gitlabextssrf.webhooks.pw
```

> Expected output: Alternating A records with 0 TTL.

### Step 3: Test Initial Hook

**Context**: Click 'Test' in UI; may fail with 500.

> Multiple attempts needed due to random resolution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/dig-gitlabextssrf]]

## Tools Used

- [[tools/researchersservers]]

## Tags

- [[webhook]]
- [[dns-rebinding]]

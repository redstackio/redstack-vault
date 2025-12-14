---
tags:
  - ssrf
  - ipv6
  - phabricator
  - blind-ssrf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/configure-phabricator-ssrf-integration-open-port]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.366Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b6d6915b-25ce-47b4-ab4e-67d4cc87e0ad
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Phabricator-Integration-for-Blind-SSRF

## Summary

This procedure updates Slack's Phabricator integration URL to an IPv6 loopback endpoint targeting an open internal port like SSH on 22, enabling blind SSRF where success is inferred from HTTP redirects.

## Description

Phabricator integrations in Slack allow URL configuration for Conduit API calls. By setting phabricator_url to http://[::]:22/, the backend attempts connection during validation or import, bypassing IPv4 filters. Open ports yield 302 redirects (success), while closed ones cause 500 errors. Useful for blind port scanning.

## Requirements

1. Access to Phabricator integration service ID (e.g., /services/4836378801)
2. Dummy credentials (conduit_user, conduit_cert)
3. Enabled import flags for triggering the request

## Defense

Defensive measures and detection strategies:

- Validate integration URLs against allowlists including IPv6
- Audit Phabricator config changes for loopback patterns
- Disable unused integrations

## Objectives

1. Set URL to target SSH port 22 via IPv6
2. Trigger blind connection during config save
3. Infer port openness from response codes

## Instructions

### Step 1: Update Integration URL

**Context**: POST to the services endpoint with IPv6 URL and import flags to force backend validation.

**Command** ([[commands/configure-phabricator-ssrf-integration-open-port]]):
```bash
curl -X POST https://agarri.slack.com/services/4836378801 \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "edit_service=1&edit_label=1&phabricator_url=http://[::]:22/&conduit_user=Yolo&conduit_cert=foobar&import_phriction=1&import_pastes=1"
```

> Response: 302 Found to updated page, with SSH protocol mismatch in backend logs (not visible). Success if no error.

### Step 2: Confirm Update

**Context**: Follow the redirect to verify configuration persistence.

**Command** (Follow redirect):
```bash
curl -L https://agarri.slack.com/services/4836378801?updated=1
```

> Check for updated URL in the form.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- None

## Commands Used

- [[commands/configure-phabricator-ssrf-integration-open-port]]

## Tools Used

- None

## Tags

- [[ssrf]]
- [[ipv6]]
- [[phabricator]]

---
id: proc-uuid-003
tags:
  - ssrf
  - image-retrieval
  - escalation
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.325Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Escalate SSRF to Retrieve Image Files

## Summary

This procedure escalates the blind SSRF to fetch arbitrary images from external or internal sources, incorporating them into the final emblem by hosting valid SVGs and testing ports.

## Description

By pointing the fill URL to a hosted valid SVG on an external server, the Rockstar server fetches it during publishing and uses the content if valid. Ports can be modified in the URL (e.g., :8080) to probe internal services. This enables potential data exfiltration or internal reconnaissance.

## Requirements

1. Control over external hosting for SVGs
2. Ability to listen on custom ports
3. Prior successful SSRF confirmation

## Defense

Defensive measures and detection strategies:

- Strip or proxy all external URL references in user-uploaded content
- Restrict server outbound connections to whitelisted domains/ports
- Analyze emblem images for unexpected embedded resources

## Objectives

1. Fetch and integrate external/internal images
2. Probe different ports for broader access
3. Demonstrate data incorporation impact

## Instructions

### Step 1: Host Valid SVG Externally

**Context**: Prepare a fetchable SVG on your server to confirm retrieval.

**Command** (Host via web server; no specific command):

> Place a simple SVG at http://yourserver.com/image.svg. Inject url(http://yourserver.com/image.svg#test) in fill.

### Step 2: Publish and Verify Fetch

**Context**: Republish emblem and monitor for request, checking if image is used.

**Command** (Use netcat to listen and capture):
```bash
nc -l 8080
```

> Expected: Server GET to your hosted path; emblem may show fetched content. Test ports by changing URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/netcat]]

## Tags

- ssrf
- image-retrieval

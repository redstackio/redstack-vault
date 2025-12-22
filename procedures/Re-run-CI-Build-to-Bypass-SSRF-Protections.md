---
id: proc-uuid-3
tags:
  - ssrf
  - bypass
  - re-run
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-fetch-digitalocean-metadata]]'
verified: false
platforms:
  - Cloud
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.561Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Re-run-CI-Build-to-Bypass-SSRF-Protections

## Summary

Re-execute the GitLab CI build to exploit the SSRF vulnerability, as protections are only applied on the first run, allowing the curl command to access and output internal metadata endpoints.

## Description

In GitLab CI runners, SSRF mitigations do not persist on re-runs, enabling arbitrary requests to local/metadata IPs like 169.254.169.254. The run.sh script's curl outputs metadata paths such as id, hostname, user-data, revealing internal instance details.

## Requirements

1. Completed initial build
2. Access to re-run jobs in GitLab UI
3. Ability to view detailed logs

## Defense

- Apply SSRF blocks consistently across all build iterations
- Detect re-runs with suspicious payloads in CI monitoring
- Block metadata IP access in runner network policies

## Objectives

1. Bypass initial protections
2. Expose internal metadata
3. Capture output for further exploitation

## Instructions

### Step 1: Re-run the Job

**Context**: Manually trigger re-run from GitLab CI interface.

No command; select the job and click "Re-run".

> This executes the pipeline again, bypassing protections.

### Step 2: Execute SSRF Curl and Capture Output

**Context**: The embedded curl in run.sh now succeeds.

**Command** ([[commands/curl-fetch-digitalocean-metadata]]):
```bash
curl -L http://169.254.169.254/metadata/v1/
```

> Expected output in logs: List of endpoints like id, hostname, user-data, vendor-data, public-keys, region, interfaces/, dns/, floating_ip/, tags/, features/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-digitalocean-metadata]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- bypass

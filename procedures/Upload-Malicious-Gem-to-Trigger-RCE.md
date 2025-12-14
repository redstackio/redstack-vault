---
tags:
  - rce
  - upload
  - exploit
  - curl
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-upload-malicious-gem]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 030030a0-2d3f-487c-bbbf-bfa33c470c56
created_at: '2025-12-14T17:23:53.951Z'
updated_at: '2025-12-14T17:23:53.951Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-Gem-to-Trigger-RCE

## Summary

This procedure uploads a malicious gem to the RubyGems /api/v1/gems endpoint using curl, triggering the deserialization vulnerability during checksum parsing and resulting in remote code execution on the server.

## Description

With the poc.gem prepared, the attacker POSTs it to the API with gzip content-type and authorization header. The server unpacks and calls read_checksums, loading the tainted YAML which deserializes to execute the payload (e.g., wget to attacker server). Demonstrates full RCE impact. Requires a valid API token and network access; may encounter UTF-8 errors but still executes.

## Requirements

1. Valid RubyGems API authorization token
2. poc.gem file with payload
3. Attacker server to receive exfiltration

## Defense

Defensive measures and detection strategies:

- Rate-limit and validate gem uploads
- Log and alert on deserialization attempts or anomalous system calls
- Deploy WAF rules to inspect gem contents for malicious patterns

## Objectives

1. Deliver the malicious gem to the vulnerable endpoint
2. Trigger parsing and deserialization
3. Confirm RCE via callback to attacker server

## Instructions

### Step 1: Prepare Upload Command

**Context**: Set up curl with necessary headers for binary POST.

No command; ensure Authorization token is ready (redacted as █████).

> Token obtained from RubyGems account.

### Step 2: Execute Gem Upload

**Context**: Pipe the gem file to curl for transmission.

Execute [[commands/curl-upload-malicious-gem]]:

```bash
cat poc.gem | curl -H 'Content-Type: application/gzip' --data-binary @- -H 'Authorization: █████' https://rubygems.org/api/v1/gems
```

> Sends binary data; server processes and executes payload.

### Step 3: Verify Execution

**Context**: Monitor for success indicators.

Check attacker server logs for wget request.

> Incoming connection confirms RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-malicious-gem]]

## Tools Used

- [[tools/curl]]

## Tags

- rce
- upload

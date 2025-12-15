---
tags:
  - api-exploit
  - dos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-create-oversized-playbook]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-12-14T10:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.494Z'
sub_techniques: []
id: b40fb8be-52a6-42fd-8548-537402d04190
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Create-Playbook-with-Oversized-Template

## Summary

This procedure submits an oversized JSON payload to the Mattermost Playbooks API to create a playbook with a 50MB run_summary_template, bypassing validation and setting up for DoS.

## Description

Targeting the /plugins/playbooks/api/v0/playbooks endpoint, this exploits the lack of attribute size validation, allowing large data storage. The created playbook can then be run to process the oversized template, causing resource exhaustion.

## Requirements

1. MMAUTHTOKEN and CSRF token from authentication
2. Generated payload.json file
3. curl or equivalent HTTP client
4. Target domain accessible

## Defense

Defensive measures and detection strategies:

- Implement request body size limits below nginx defaults
- Add server-side validation for playbook fields
- Log and alert on large POST requests to API endpoints

## Objectives

1. Successfully create playbook with oversized data
2. Avoid API rejection due to size
3. Confirm playbook visibility in UI

## Instructions

### Step 1: Prepare Headers and Token

**Context**: Gather authentication details for the request.

Extract CSRF token from UI or headers; use MMAUTHTOKEN from cookies.

> Ensure tokens are current to avoid 403 errors.

### Step 2: Submit Payload via API

**Context**: POST the oversized payload to create the playbook.

Execute [[commands/curl-create-oversized-playbook]]:

```bash
curl -X POST "http://<domain>/plugins/playbooks/api/v0/playbooks" -H 'Content-Type: application/json' -d @payload --cookie "MMAUTHTOKEN=<user-auth-token>" -H "X-CSRF-TOKEN: <csrf-token>"
```

> Expected output: JSON response with playbook ID, HTTP 200.

### Step 3: Verify in UI

**Context**: Confirm creation by navigating to Playbooks page.

In browser, go to Playbooks and select the new entry.

> Expected output: Playbook details load without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-create-oversized-playbook]]

## Tools Used


## Tags

- api-exploit
- dos

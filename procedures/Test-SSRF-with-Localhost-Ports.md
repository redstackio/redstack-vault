---
id: proc-test-localhost-ports
tags:
  - ssrf
  - port-scanning
  - localhost
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:39:02.177Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Test-SSRF-with-Localhost-Ports

## Summary

This procedure tests SSRF by submitting localhost URLs with specific ports to identify open services through cURL error responses.

## Description

By inputting URLs targeting localhost ports like 22 (SSH) or 21 (FTP), the Phabricator server performs server-side cURL fetches. Errors reveal port status: open ports may return recv errors, closed ones connection failures. This enables blind port scanning without direct access.

## Requirements

1. Access to the macro creation form
2. Knowledge of common internal ports to test
3. Ability to submit and observe form responses

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed URL schemes/hosts in cURL calls
- Sanitize error messages to prevent information leakage
- Log and alert on requests to localhost or private IPs

## Objectives

1. Confirm SSRF vulnerability
2. Map open ports on the server
3. Identify potential internal services

## Instructions

### Step 1: Prepare Test URLs

**Context**: Select ports based on common services.

Choose URLs such as `http://localhost:22/` for SSH or `http://localhost:21/` for FTP.

> These target standard services; adjust based on expected environment.

### Step 2: Submit and Observe

**Context**: Trigger the server-side request and capture response.

Enter the URL in the form field and submit. Note the error message returned by Phabricator.

> For open ports: Errors like CURLE_RECV_ERROR (56) indicate connection but failed read. For closed: CURLE_COULDNT_CONNECT (7).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[port-scanning]]

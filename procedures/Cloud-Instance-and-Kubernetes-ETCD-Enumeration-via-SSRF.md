---
type: procedure
tactics:
  - '[[tactics/Discovery]]'
techniques:
  - '[[techniques/System-Information-Discovery]]'
  - '[[techniques/Exploit-Public-Facing-Application]]'
sub_techniques: []
tags:
  - ssrf
  - cloud-metadata
  - kubernetes-etcd
  - discovery
commands:
  - '[[commands/curl-get-etcd-version]]'
  - '[[commands/curl-get-etcd-recursive-keys]]'
platforms:
  - Web
  - Cloud
  - Kubernetes
tools: []
verified: true
validated: true
---

# Cloud-Instance-and-Kubernetes-ETCD-Enumeration-via-SSRF

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in a web application to enumerate information about cloud instances and Kubernetes ETCD databases. By crafting malicious requests, an attacker can force the server to query internal metadata endpoints, revealing details such as ETCD versions, stored keys, and potentially cloud instance counts or configurations, which aids in further reconnaissance and lateral movement.

## Description

Server-Side Request Forgery (SSRF) allows attackers to manipulate a vulnerable application into making unauthorized requests to internal or external resources. In cloud and Kubernetes environments, this can target metadata services (e.g., AWS IMDS at 169.254.169.254) to enumerate instance details or ETCD endpoints (typically on port 2379) to extract configuration data, secrets, or cluster state. This procedure focuses on using SSRF to access these endpoints, assuming the application processes user-supplied URLs without validation. Success depends on the application's ability to reach localhost or internal network segments. Potential outcomes include discovering API keys, internal IPs, or cluster topology, enabling escalation to data exfiltration or privilege escalation.

## Requirements

1. Valid SSRF vulnerability in the target web application, allowing arbitrary URL requests.
2. Network access to the application (e.g., via browser or proxy like Burp Suite).
3. Knowledge of target environment (e.g., cloud provider like AWS/GCP, or Kubernetes cluster presence).
4. Tools for request crafting (e.g., curl, Burp Suite) and a listener if responses are reflected.

## Defense

- Implement strict URL validation and whitelisting to block internal IP ranges (e.g., 127.0.0.1, 169.254.169.254, 10.0.0.0/8).
- Use network segmentation and firewalls to isolate metadata services and ETCD from application servers.
- Enable application-level firewalls (WAF) to detect and block SSRF patterns, such as requests to localhost or private IPs.
- Monitor logs for anomalous internal requests and implement endpoint protection to restrict ETCD access.

## Objectives

1. Force the application to query internal ETCD endpoints for version and key enumeration.
2. Extract cloud instance metadata if applicable, such as instance IDs or user data.
3. Gather actionable intelligence on the environment for subsequent attacks.

## Instructions

### Step 1: Identify SSRF Endpoint and Test Basic Connectivity

**Context**: Locate the vulnerable input field (e.g., image URL, webhook, or import feature) that triggers server-side requests. Test with a harmless external URL to confirm SSRF, then pivot to internal targets like localhost.

Use a proxy tool to intercept and modify requests. For example, submit a URL like `http://127.0.0.1:2379` if the app reflects responses.

> This step verifies the SSRF payload delivery without exposing sensitive data.

### Step 2: Retrieve ETCD Version Information

**Context**: Query the ETCD version endpoint to identify the database version, which helps assess vulnerabilities or compatibility for further exploitation.

**Command** ([[commands/curl-get-etcd-version]]):
```bash
curl -L http://127.0.0.1:2379/version
```

> Submit this URL via the SSRF vulnerability (e.g., as a parameter in a POST request). The `-L` flag follows redirects if needed. Expected response includes JSON with ETCD and Go versions, confirming access to the internal service.

### Step 3: Enumerate ETCD Keys Recursively

**Context**: Fetch all keys and values from the ETCD store to discover secrets, configurations, or cluster state. This can reveal sensitive data like certificates, tokens, or pod information.

**Command** ([[commands/curl-get-etcd-recursive-keys]]):
```bash
curl http://127.0.0.1:2379/v2/keys/?recursive=true
```

> Craft the SSRF payload with this URL. The `recursive=true` parameter ensures sub-keys are included. Parse the JSON response for key-value pairs; success is indicated by a non-empty node list. Be cautious as this may expose high-value data.

### Step 4: Enumerate Cloud Instance Metadata (If Applicable)

**Context**: If the environment is cloud-based (e.g., AWS), target the Instance Metadata Service (IMDS) to count instances or retrieve details like instance ID, region, or IAM roles.

**Command** (Custom extension; use similar to Step 2):
```bash
curl http://169.254.169.254/latest/meta-data/
```

> Adapt the SSRF payload for cloud-specific endpoints (e.g., AWS IMDSv1). Expected output lists metadata paths; follow up with specific queries like `/latest/meta-data/instance-id`. This step assumes cloud deployment; skip if not detected.

### Step 5: Analyze and Validate Output

**Context**: Review responses for useful data and verify no alerts were triggered. Use tools like jq to parse JSON if responses are captured.

> Manually inspect for indicators like ETCD version strings or metadata fields. If data is reflected in the app response, document for chaining with other procedures (e.g., credential extraction).

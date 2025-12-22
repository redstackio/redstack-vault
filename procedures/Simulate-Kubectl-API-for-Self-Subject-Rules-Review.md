---
id: 0f6bad0e-061f-4cdb-9264-89444890113f
name: Simulate-Kubectl-API-for-Self-Subject-Rules-Review
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.123079+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Container Environment]]'
  - '[[tags/Kubernetes]]'
  - '[[tags/Simulating kubectl API Requests]]'
commands:
  - '[[commands/kubectl-verbose-auth-can-i-list]]'
  - '[[commands/curl-post-selfsubjectrulesreview]]'
platforms:
  - Kubernetes
  - Linux
tools:
  - '[[tools/kubectl]]'
validated: true
---

# Simulate-Kubectl-API-for-Self-Subject-Rules-Review

## Summary

This procedure simulates `kubectl` API requests to perform a Self Subject Rules Review in a Kubernetes cluster, allowing an attacker to enumerate the permissions and access levels associated with a specific Service Account token. By directly querying the Kubernetes API server, it reveals allowed actions on resources, helping identify privilege escalation paths or lateral movement opportunities without relying on the `kubectl` tool.

## Description

In a Kubernetes environment, Service Accounts provide identities for processes running in pods. A Self Subject Rules Review queries the API server to list the rules (verbs like get, list, create) applicable to the authenticated subject across namespaces. This is equivalent to running `kubectl auth can-i --list` but simulated via direct HTTP POST requests to the `/apis/authorization.k8s.io/v1/selfsubjectrulesreviews` endpoint. Attackers with a compromised Service Account token can use this to map permissions stealthily, especially in air-gapped or monitored setups where `kubectl` usage might be logged or restricted. The technique leverages the Kubernetes authorization API to introspect RBAC policies, potentially exposing over-privileged accounts for further exploitation. This maps to discovery tactics in containerized environments, where understanding permissions is key to navigation.

## Requirements

1. A valid Kubernetes Service Account token (JWT) obtained via pod mount, configmap, or secret compromise.
2. The Kubernetes API server endpoint URL (e.g., https://api.example.com:6443) and network access to it.
3. curl installed on the attacker's system or compromised host.
4. Optional: `kubectl` for initial observation of the API call structure.

## Defense

- Implement least-privilege principles for Service Accounts, using RBAC to restrict API access to only necessary verbs and resources.
- Regularly audit and rotate Service Account tokens, and use short-lived tokens where possible.
- Enable Kubernetes audit logging to monitor API requests to authorization endpoints, and integrate with SIEM for anomalous queries (e.g., frequent SelfSubjectRulesReviews from unexpected IPs).
- Deploy network policies to limit API server access and use tools like OPA Gatekeeper for policy enforcement.

## Objectives

1. Enumerate all permissions (rules) granted to the Service Account across the cluster.
2. Identify exploitable over-permissions for privilege escalation or lateral movement.
3. Gather intelligence on cluster structure without triggering `kubectl`-specific alerts.

## Instructions

### Step 1: Observe the API Request Using kubectl Verbose Mode

**Context**: If `kubectl` is available, run it in verbose mode to capture the exact API request structure, including the JSON payload and headers. This helps replicate the call manually. The output reveals the underlying curl equivalent for simulation.

**Command** ([[commands/kubectl-verbose-auth-can-i-list]]):
```bash
kubectl -v=9 auth can-i --list
```

This command authenticates with your kubeconfig or token and queries the API server. The verbose level 9 logs the full HTTP request details.

**Expected Output**: A table of permissions (e.g., "Resources nonempty" with verbs like [get list watch] for resources like [pods]), followed by verbose logs showing the POST request body and curl command. Look for lines starting with "I" indicating the request body JSON and the curl invocation.

### Step 2: Prepare the JSON Payload

**Context**: Extract or construct the SelfSubjectRulesReview object from the verbose output. This payload specifies the review scope (e.g., namespace). Save it to a file for the curl request. The status fields are set to null in the request; the API server populates them in the response.

**Code** ([[codes/self-subject-rules-review-request-body]]):

Use the following JSON as the request body, adjusting the namespace in spec if targeting a specific one (default is cluster-wide if omitted).

### Step 3: Send the Simulated API Request with curl

**Context**: Use curl to POST the payload directly to the API server, authenticating with the Service Account token as a Bearer header. This bypasses `kubectl` and simulates the request for stealth. The -k flag ignores TLS verification if self-signed certs are used.

**Command** ([[commands/curl-post-selfsubjectrulesreview]]):
```bash
curl -k -X POST \
  -H "Authorization: Bearer $_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"kind":"SelfSubjectRulesReview","apiVersion":"authorization.k8s.io/v1","metadata":{"creationTimestamp":null},"spec":{"namespace":"default"},"status":{"resourceRules":null,"nonResourceRules":null,"incomplete":false}}' \
  "$_API_SERVER/apis/authorization.k8s.io/v1/selfsubjectrulesreviews"
```

Replace $_TOKEN with your Service Account JWT and $_API_SERVER with the API endpoint. For better readability, save the JSON to payload.json and use -d @payload.json.

**Expected Output**: HTTP 201 Created response with JSON body containing the review status:

```json
{
  "kind": "SelfSubjectRulesReview",
  "apiVersion": "authorization.k8s.io/v1",
  "status": {
    "resourceRules": [
      {
        "verbs": ["get", "list", "watch"],
        "resources": ["pods"],
        "apiGroups": [""]
      }
    ],
    "nonResourceRules": [],
    "incomplete": false
  }
}
```

The resourceRules array lists allowed actions; incomplete=true indicates partial evaluation due to policy errors.

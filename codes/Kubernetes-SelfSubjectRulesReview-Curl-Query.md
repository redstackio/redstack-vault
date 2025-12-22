---
id: 97210164-eda2-45bd-abd8-465a3dd9a1a3
name: Kubernetes-SelfSubjectRulesReview-Curl-Query
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:01.145468+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - api-query
  - authorization
  - discovery
validated: true
---

# Kubernetes-SelfSubjectRulesReview-Curl-Query

## Code

```bash
NAMESPACE=$(cat "/var/run/secrets/kubernetes.io/serviceaccount/namespace")
MASTER_URL="https://${KUBERNETES_SERVICE_HOST}:${KUBERNETES_SERVICE_PORT}"
TOKEN=$(cat "/var/run/secrets/kubernetes.io/serviceaccount/token")
curl "${MASTER_URL}/apis/authorization.k8s.io/v1/selfsubjectrulesreviews" \
  --cacert "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt" \
  --header "Authorization: Bearer ${TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{"kind":"SelfSubjectRulesReview","apiVersion":"authorization.k8s.io/v1","spec":{"namespace":"'${NAMESPACE}'"}}'
```

## Description

This bash script queries the Kubernetes API server directly using curl to perform a SelfSubjectRulesReview, retrieving a comprehensive list of permissions for the current service account. It uses pod-mounted service account files for authentication and provides detailed JSON output on allowed API groups, resources, and verbs, useful for mapping privilege escalation paths.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $KUBERNETES_SERVICE_HOST | Kubernetes API server host from pod env | kubernetes.default.svc.cluster.local |
| $KUBERNETES_SERVICE_PORT | API server port from pod env | 443 |
| $TOKEN | Service account token from /var/run/secrets/.../token | eyJhbGciOiJSUzI1NiIsInR5cCI6... |
| $NAMESPACE | Current namespace from pod secret | default |

## Usage

Execute this script inside a compromised pod to enumerate permissions without relying on kubectl. Pipe the output to jq for parsing: `bash script.sh | jq '.status.rules'`. Commonly used in post-exploitation to identify exploitable RBAC misconfigurations.

## Detection

- API server audit logs showing POST to /apis/authorization.k8s.io/v1/selfsubjectrulesreviews.
- Unusual curl processes in pods or network traffic from pods to API server on non-standard paths.
- Anomalous service account token usage in authorization logs.

## Related

- [[procedures/Kubernetes-Service-Account-Permissions-Enumeration]]

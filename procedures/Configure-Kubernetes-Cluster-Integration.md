---
tags:
  - kubernetes
  - integration
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-13T23:52:44.265Z'
sub_techniques: []
id: f2c64d57-2b1a-43d0-926f-e4c451e528c1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Configure-Kubernetes-Cluster-Integration

## Summary

This procedure adds a Kubernetes cluster integration to the GitLab project using mock credentials, enabling the use of kubernetes: namespace in CI jobs which is necessary for injecting the XSS payload.

## Description

In the GitLab UI, navigate to the Kubernetes operations section and configure an existing cluster with placeholder values. This integration allows CI/CD jobs to reference Kubernetes resources without a real cluster, focusing on the rendering flaw in the job page.

## Requirements

1. Existing GitLab project
2. User permissions for integrations
3. Web browser access to GitLab

## Defense

Defensive measures and detection strategies:

- Validate Kubernetes API URLs and tokens during integration setup
- Audit cluster integrations for unauthorized additions
- Use GitLab's managed clusters to avoid manual configurations

## Objectives

1. Enable Kubernetes features in the project
2. Set up for namespace injection in CI YAML
3. Verify integration without real cluster dependency

## Instructions

### Step 1: Access Kubernetes Settings

**Context**: Locate the integration configuration in the project menu.

**Instructions**: Go to project sidebar > Operations > Kubernetes > "Add Kubernetes cluster".

### Step 2: Add Existing Cluster

**Context**: Provide mock details to simulate integration.

**Instructions**: Select "Add existing cluster" tab, set name: "cluster-example", API URL: "https://google.com/", service token: "token-example", uncheck "GitLab-managed cluster", and click "Add cluster".

> Expected output: Success message and cluster listed in integrations.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- kubernetes
- integration
- gitlab

---
id: proc-2255750-1
tags:
  - recon
  - ci-cd
  - nx-cloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Cloud
  - CI/CD
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:54.353Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Obtain Authorized Upload URL for NX Cloud Cache

## Summary

This procedure involves accessing a public Git repository integrated with NX Cloud to extract an authorized upload URL for CI build cache artifacts, enabling subsequent poisoning without authentication.

## Description

In the Mozilla fxa repository, NX Cloud handles distributed caching for builds. The procedure targets the public exposure of upload links in repository configurations or build artifacts. By inspecting public source code and CI setups, an attacker obtains a URL that authorizes uploads to specific cache namespaces. This URL lacks expiration or single-use checks, setting up cache poisoning. Prerequisites include public repo access; outcomes provide entry for supply chain attacks in CI/CD pipelines.

## Requirements

1. Public read access to the target Git repository (e.g., GitHub mozilla/fxa).
2. Basic knowledge of NX Cloud integration in monorepos.
3. HTTP client for URL interaction (e.g., browser or curl).

## Defense

Defensive measures and detection strategies:

- Enforce single-use or short-lived upload tokens in caching services.
- Monitor public repo for anomalous access patterns to CI configs.
- Use repository secrets scanning to avoid exposing cache URLs.

## Objectives

1. Acquire a valid, reusable upload URL for NX Cloud cache artifacts.
2. Identify the cache namespace tied to the target repository's CI pipeline.
3. Establish initial access for cache manipulation without credentials.

## Instructions

### Step 1: Inspect Repository Configuration

**Context**: Review the public source code to locate NX Cloud setup files that generate or reference cache upload links.

Navigate to the mozilla/fxa repository on GitHub and examine files like nx.json or CI workflow files (e.g., .github/workflows). Look for NX Cloud configuration that includes cache artifact references. The upload URL is often logged or derivable from build processes.

### Step 2: Extract Upload URL from Build Artifacts

**Context**: Simulate or observe a build to capture the authorized link.

If build logs are public, review recent CI runs for NX Cloud upload endpoints. The URL format typically includes a signed token for the specific cache key (e.g., based on repo hash). Copy the full URL for reuse.

**Expected Output**: A URL like https://cloud.nx.app/upload/... with authorization parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- ci-cd
- nx-cloud

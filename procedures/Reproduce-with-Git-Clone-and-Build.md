---
tags:
  - xss
  - reproduction
  - git
  - build
type: procedure
tools:
  - '[[tools/git]]'
  - '[[tools/npm]]'
  - '[[tools/webpack]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/git-clone-poc]]'
  - '[[commands/cd-poc-directory]]'
  - '[[commands/npm-install-poc]]'
  - '[[commands/npm-run-build]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:36.961Z'
sub_techniques: []
id: 53b490ec-da08-4488-b347-ca05271b5b10
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reproduce-with-Git-Clone-and-Build

## Summary

This procedure clones a POC repository, installs dependencies, and runs a webpack build to generate stats JSON with malicious module names, fully reproducing the XSS in a realistic third-party module scenario.

## Description

The POC repo demonstrates control over third-party module file/directory names (e.g., '<script>alert(1)</script>') during webpack compilation, injecting them into stats JSON. Building the project automatically runs the analyzer, serving the vulnerable interface. This targets a Node.js project environment, requiring git and npm, and results in XSS execution upon accessing the generated URL, confirming the attack vector.

## Requirements

1. Git installed and accessible
2. Node.js and npm for dependency management
3. Internet for cloning the repo

## Defense

Defensive measures and detection strategies:

- Vet third-party modules for malicious naming
- Use webpack plugins to sanitize stats output
- Integrate vulnerability scanners in CI/CD pipelines

## Objectives

1. Clone and setup the POC project
2. Build with malicious module structure
3. Trigger analyzer and XSS via generated stats

## Instructions

### Step 1: Clone POC Repository

**Context**: Downloads the example project for in-depth reproduction.

**Command** ([[commands/git-clone-poc]]):
```bash
git clone https://github.com/inkz/poc-webpack-bundle-analyzer.git
```

> Clones the repo into a local directory. Expected output: Progress logs and confirmation of download.

### Step 2: Change Directory

**Context**: Enters the project root for setup.

**Command** ([[commands/cd-poc-directory]]):
```bash
cd poc-webpack-bundle-analyzer/
```

> Changes working directory. Expected output: Shell prompt updates to project path.

### Step 3: Install Dependencies

**Context**: Installs webpack, analyzer, and other packages.

**Command** ([[commands/npm-install-poc]]):
```bash
npm install
```

> Installs from package.json. Expected output: Logs for webpack, analyzer, etc.

### Step 4: Run Build Script

**Context**: Compiles with malicious names, generating and analyzing stats.

**Command** ([[commands/npm-run-build]]):
```bash
npm run build
```

> Executes webpack build and starts analyzer. Expected output: Server at http://localhost:8888 with XSS trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/git-clone-poc]]
- [[commands/cd-poc-directory]]
- [[commands/npm-install-poc]]
- [[commands/npm-run-build]]

## Tools Used

- [[tools/git]]
- [[tools/npm]]
- [[tools/webpack]]

## Tags

- xss
- reproduction
- git
- build

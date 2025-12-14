---
id: proc-736522-init-app
tags:
  - installation
  - npm
  - authmagic
type: procedure
tools:
  - '[[tools/authmagic-cli]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/install-authmagic-cli-globally]]'
  - '[[commands/init-npm-project-default]]'
  - '[[commands/init-authmagic-example]]'
  - '[[commands/install-authmagic-dependencies]]'
  - '[[commands/start-authmagic-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:10.858Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initialize-and-Install-Authmagic-Example-App

## Summary

This procedure installs and configures the authmagic example application, including the vulnerable authmagic-timerange-stateless-core module (v0.0.9), to enable testing of the JWT token reissuance vulnerability at the POST /token endpoint.

## Description

The authmagic CLI tool facilitates quick setup of a Node.js web app that uses the stateless core module for JWT-based authentication. By initializing with the example flag (-e), the project includes the vulnerable dependency. Installation pulls in authmagic-timerange-stateless-core@0.0.9, where the checkRefreshToken function in core.js only verifies the refresh token, allowing payload tampering in the access token. Starting the server exposes http://localhost:3000 for authentication flows. Note: Avoid naming the project 'authmagic' to prevent circular dependency errors.

## Requirements

1. Node.js v14+ and npm
2. Global authmagic-cli (installed in prior steps)
3. Internet access for npm downloads
4. Port 3000 free

## Defense

Defensive measures and detection strategies:

- Pin dependencies to secure versions (e.g., update beyond 0.0.9)
- Scan for vulnerable npm packages using tools like npm audit
- Review source code for JWT validation (e.g., ensure jwt.verify on access tokens)

## Objectives

1. Install vulnerable module
2. Configure example app
3. Launch local server for testing

## Instructions

### Step 1: Install Authmagic CLI Globally

**Context**: Enables authmagic commands for project setup.

**Command** ([[commands/install-authmagic-cli-globally]]):
```bash
npm install -g authmagic-cli
```

> Installs the CLI tool system-wide. Expected output: Progress bars and 'added X packages'.

### Step 2: Initialize NPM Project

**Context**: Creates package.json with defaults, avoiding name conflicts.

**Command** ([[commands/init-npm-project-default]]):
```bash
npm init -y
```

> Skips prompts for quick setup. Expected output: package.json file created.

### Step 3: Init Authmagic Example

**Context**: Sets up the example app structure with vulnerable core.

**Command** ([[commands/init-authmagic-example]]):
```bash
authmagic init -e
```

> Uses -e for example mode. Expected output: Project files generated.

### Step 4: Install Dependencies

**Context**: Pulls in authmagic-timerange-stateless-core@0.0.9 and others.

**Command** ([[commands/install-authmagic-dependencies]]):
```bash
authmagic install
```

> Runs npm install for the project. Expected output: Dependencies installed, including vulnerable module.

### Step 5: Start Server

**Context**: Launches the web app for authentication testing.

**Command** ([[commands/start-authmagic-server]]):
```bash
authmagic
```

> Starts the development server. Expected output: 'Server running on http://localhost:3000'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/install-authmagic-cli-globally]]
- [[commands/init-npm-project-default]]
- [[commands/init-authmagic-example]]
- [[commands/install-authmagic-dependencies]]
- [[commands/start-authmagic-server]]

## Tools Used

- [[tools/authmagic-cli]]

## Tags

- installation
- npm
- authmagic

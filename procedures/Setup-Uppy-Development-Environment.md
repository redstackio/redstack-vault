---
tags:
  - setup
  - node.js
  - uppy
type: procedure
tools:
  - '[[tools/git]]'
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-uppy]]'
  - '[[commands/cd-uppy]]'
  - '[[commands/npm-install-uppy]]'
  - '[[commands/npm-start-uppy]]'
  - '[[commands/npm-run-dev-uppy]]'
platforms:
  - Node.js
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 64e400e9-d891-4a6f-961c-2b5cbcd4c474
created_at: '2025-12-14T03:16:14.094Z'
updated_at: '2025-12-14T03:16:14.094Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Setup-Uppy-Development-Environment

## Summary

This procedure clones the Uppy repository, installs dependencies, and starts the development server to enable testing of the file upload dashboard where the XSS vulnerability can be exploited.

## Description

Uppy is a Node.js module for file uploads using the TUS protocol. To reproduce the stored XSS, a local instance must be set up. This involves cloning from GitHub, installing npm packages, and running the dev server on port 3452. The dashboard provides an interface for uploading SVG files that will later trigger XSS when viewed.

## Requirements

1. Git installed on the system
2. Node.js and npm installed
3. Local port 3452 available
4. Internet access for cloning and installing packages

## Defense

Defensive measures and detection strategies:

- Use containerized environments to isolate development setups
- Monitor npm install logs for anomalous packages
- Firewall rules to restrict port 3452 access

## Objectives

1. Establish a functional Uppy dashboard for upload testing
2. Prepare environment for payload creation and exploitation
3. Verify server accessibility without errors

## Instructions

### Step 1: Clone the Repository

**Context**: Fetch the Uppy source code to begin local setup.

**Command** ([[commands/git-clone-uppy]]):
```bash
git clone https://github.com/transloadit/uppy
```

> Clones the repository into a local 'uppy' directory. Expected output: Progress messages ending with download completion.

### Step 2: Navigate to Directory

**Context**: Change into the cloned folder for subsequent operations.

**Command** ([[commands/cd-uppy]]):
```bash
cd uppy
```

> Switches working directory. Expected output: Prompt changes to /path/to/uppy.

### Step 3: Install Dependencies

**Context**: Install Node.js packages required for Uppy.

**Command** ([[commands/npm-install-uppy]]):
```bash
npm install
```

> Downloads and installs packages from package.json. Expected output: List of installed modules, no errors.

### Step 4: Start the Server

**Context**: Launch the basic server.

**Command** ([[commands/npm-start-uppy]]):
```bash
npm start
```

> Initiates the application server. Expected output: Server running message.

### Step 5: Run Development Mode

**Context**: Start the interactive dev server with dashboard.

**Command** ([[commands/npm-run-dev-uppy]]):
```bash
npm run dev
```

> Launches on port 3452. Expected output: Dashboard available at http://localhost:3452.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/git-clone-uppy]]
- [[commands/cd-uppy]]
- [[commands/npm-install-uppy]]
- [[commands/npm-start-uppy]]
- [[commands/npm-run-dev-uppy]]

## Tools Used

- [[tools/git]]
- [[tools/npm]]

## Tags

- setup
- node.js
- uppy

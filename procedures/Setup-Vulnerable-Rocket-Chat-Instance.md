---
id: proc-setup-rocket-chat
tags:
  - setup
  - rocket-chat
  - docker
type: procedure
tools:
  - '[[tools/Git]]'
  - '[[tools/Docker-Compose]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-rocket-chat]]'
  - '[[commands/cd-rocket-chat]]'
  - '[[commands/git-checkout-3-12-1]]'
  - '[[commands/docker-compose-up-detached]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:18.951Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Setup-Vulnerable-Rocket-Chat-Instance

## Summary

This procedure deploys a local instance of the vulnerable Rocket.Chat version 3.12.1 using Git and Docker Compose, enabling reproduction of the stored XSS and RCE exploit chain.

## Description

Rocket.Chat 3.12.1 contains a stored XSS vulnerability due to unsafe merging of extraData in room creation and unescaped error messages in toastr. This setup creates an isolated environment with MongoDB backend, accessible via http://localhost:3000, for testing the full attack without affecting production systems. Prerequisites include Docker and Git installed on a Linux host.

## Requirements

1. Docker and Docker Compose installed
2. Git version control system
3. Local network access for port 3000
4. No internet restrictions for cloning the repo

## Defense

Defensive measures and detection strategies:

- Run Rocket.Chat in containers with network isolation
- Monitor Docker logs for unauthorized clones or startups
- Use vulnerability scanners like Trivy on container images

## Objectives

1. Establish a reproducible vulnerable environment
2. Complete initial admin setup for testing
3. Verify instance accessibility before exploitation

## Instructions

### Step 1: Clone Repository

**Context**: Download the Rocket.Chat source code from GitHub.

**Command** ([[commands/git-clone-rocket-chat]]):
```bash
git clone git@github.com:RocketChat/Rocket.Chat.git
```

> Clones the official repository to a local directory named Rocket.Chat. Expected output: Progress messages ending with a local copy.

### Step 2: Navigate to Directory

**Context**: Change into the cloned folder for further operations.

**Command** ([[commands/cd-rocket-chat]]):
```bash
cd Rocket.Chat
```

> Updates the working directory. Expected output: Prompt changes to /path/to/Rocket.Chat.

### Step 3: Checkout Vulnerable Version

**Context**: Switch to tag 3.12.1, which contains the vulnerability.

**Command** ([[commands/git-checkout-3-12-1]]):
```bash
git checkout tags/3.12.1
```

> Detaches HEAD to the specified tag. Expected output: Confirmation of switch to tag 3.12.1.

### Step 4: Start Services

**Context**: Launch the application and database in detached mode.

**Command** ([[commands/docker-compose-up-detached]]):
```bash
docker-compose up -d
```

> Starts MongoDB and Rocket.Chat containers in background. Expected output: Services running, accessible at http://localhost:3000.

### Step 5: Initial Configuration

**Context**: Access the UI and set up the admin account with default settings.

**Instructions**: Open http://localhost:3000 in a browser and follow the setup wizard to create an admin user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/git-clone-rocket-chat]]
- [[commands/cd-rocket-chat]]
- [[commands/git-checkout-3-12-1]]
- [[commands/docker-compose-up-detached]]

## Tools Used

- [[tools/Git]]
- [[tools/Docker-Compose]]

## Tags

- setup
- rocket-chat
- docker


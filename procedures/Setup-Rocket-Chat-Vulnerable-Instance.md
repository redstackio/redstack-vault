---
id: 123e4567-e89b-12d3-a456-426614174001
name: Setup-Rocket-Chat-Vulnerable-Instance
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.430Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - setup
  - rocket-chat
  - docker
platforms:
  - Web
commands:
  - '[[commands/git-clone-rocket-chat]]'
  - '[[commands/cd-rocket-chat]]'
  - '[[commands/git-checkout-rocket-chat-3-12-1]]'
  - '[[commands/docker-compose-up-detached]]'
tools:
  - '[[tools/Git]]'
  - '[[tools/Docker-Compose]]'
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Setup-Rocket-Chat-Vulnerable-Instance

## Summary

This procedure sets up a local instance of Rocket.Chat version 3.12.1 using Git and Docker Compose to replicate the vulnerable environment for testing stored XSS and RCE exploits.

## Description

The setup involves cloning the Rocket.Chat repository, checking out the specific vulnerable tag (3.12.1), and launching the application with default configuration via Docker Compose. This creates a web-accessible instance on port 3000 with a connected database, allowing subsequent user creation and exploitation steps. The environment uses JavaScript/Meteor and the toastr library, which are key to the vulnerabilities.

## Requirements

1. Git installed on the host machine
2. Docker and Docker Compose installed
3. SSH access to GitHub or HTTPS alternative for cloning
4. Local network access to run services on port 3000

## Defense

Defensive measures and detection strategies:

- Use container scanning tools to detect outdated versions like 3.12.1
- Monitor Docker image pulls for known vulnerable tags
- Implement network segmentation to limit local instance exposure

## Objectives

1. Deploy a reproducible vulnerable Rocket.Chat instance
2. Ensure default configuration for accurate testing
3. Validate accessibility for further attack steps

## Instructions

### Step 1: Clone Repository

**Context**: Obtain the source code for the vulnerable version.

**Command** ([[commands/git-clone-rocket-chat]]):
```bash
git clone git@github.com:RocketChat/Rocket.Chat.git
```

> Clones the Rocket.Chat repository to a local directory named Rocket.Chat. Expected output: Progress messages ending with a local copy of the repo.

### Step 2: Navigate to Directory

**Context**: Enter the project folder for subsequent operations.

**Command** ([[commands/cd-rocket-chat]]):
```bash
cd Rocket.Chat
```

> Changes the current working directory to Rocket.Chat. Expected output: Prompt updates to show the new path.

### Step 3: Checkout Vulnerable Version

**Context**: Switch to the exact version containing the vulnerabilities.

**Command** ([[commands/git-checkout-rocket-chat-3-12-1]]):
```bash
git checkout tags/3.12.1
```

> Checks out the 3.12.1 tag. Expected output: Confirmation of switching to the release branch.

### Step 4: Start Services

**Context**: Launch the application and dependencies in the background.

**Command** ([[commands/docker-compose-up-detached]]):
```bash
docker-compose up -d
```

> Starts Docker services using the default docker-compose.yml. Expected output: Services running, accessible at http://localhost:3000.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/git-clone-rocket-chat]]
- [[commands/cd-rocket-chat]]
- [[commands/git-checkout-rocket-chat-3-12-1]]
- [[commands/docker-compose-up-detached]]

## Tools Used

- [[tools/Git]]
- [[tools/Docker-Compose]]

## Tags

- [[setup]]
- [[rocket-chat]]
- [[docker]]

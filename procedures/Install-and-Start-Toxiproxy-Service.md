---
tags:
  - setup
  - toxiproxy
  - installation
type: procedure
tools:
  - '[[tools/Homebrew]]'
  - '[[tools/toxiproxy]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/brew-update]]'
  - '[[commands/brew-install-toxiproxy]]'
  - '[[commands/brew-services-start-toxiproxy]]'
platforms:
  - macOS
techniques:
  - '[[PowerShell]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ae20f865-9aa2-40e8-ae45-065bbe5532b5
created_at: '2025-12-14T17:27:29.740Z'
updated_at: '2025-12-14T17:27:29.740Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
---
# Install-and-Start-Toxiproxy-Service

## Summary

This procedure installs Toxiproxy, an open-source tool for simulating network conditions via TCP proxies, using Homebrew on macOS and starts it as a background service to expose the vulnerable HTTP API on localhost:8474.

## Description

Toxiproxy is used in development to create unreliable network connections for testing. In this attack scenario, it runs locally on the victim's machine without authentication, making its API susceptible to CSRF. The procedure sets up the environment for subsequent exploitation steps, assuming the victim has Toxiproxy installed for development (e.g., a Shopify employee). Expected outcomes include a running server ready for CSRF manipulation.

## Requirements

1. macOS operating system with Homebrew installed
2. Administrative privileges for service management
3. Internet access for package download

## Defense

Defensive measures and detection strategies:

- Restrict Toxiproxy installation to air-gapped environments
- Monitor for unauthorized service starts via process auditing (e.g., auditd on macOS)
- Use firewall rules to block external access to localhost:8474

## Objectives

1. Establish a local Toxiproxy instance for vulnerability simulation
2. Ensure the HTTP API is accessible without authentication
3. Prepare for CSRF-based proxy creation

## Instructions

### Step 1: Update Homebrew

**Context**: Refresh package lists to ensure the latest version of Toxiproxy is available.

**Command** ([[commands/brew-update]]):
```bash
brew update
```

> This command fetches the latest formulae from Homebrew repositories. Expected output includes updated package lists and any available upgrades.

### Step 2: Install Toxiproxy

**Context**: Download and install the Toxiproxy server and CLI tools from the Shopify tap.

**Command** ([[commands/brew-install-toxiproxy]]):
```bash
brew install toxiproxy
```

> Installs toxiproxy-server and toxiproxy-cli binaries. Expected output is a summary of downloaded files and installation path.

### Step 3: Start Service

**Context**: Launch Toxiproxy as a background service managed by launchd.

**Command** ([[commands/brew-services-start-toxiproxy]]):
```bash
brew services start shopify/shopify/toxiproxy
```

> Starts the server on localhost:8474. Expected output confirms successful startup.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[PowerShell]]

### Sub-Techniques


## Commands Used

- [[commands/brew-update]]
- [[commands/brew-install-toxiproxy]]
- [[commands/brew-services-start-toxiproxy]]

## Tools Used

- [[tools/Homebrew]]
- [[tools/toxiproxy]]

## Tags

- setup
- toxiproxy
- installation

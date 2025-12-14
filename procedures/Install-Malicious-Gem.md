---
id: proc-uuid-3
tags:
  - gem-install
  - persistence
type: procedure
tools:
  - '[[tools/gem]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/gem-install-securitytest]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.026Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Install-Malicious-Gem

## Summary

This procedure installs the malicious .gem file into the local RubyGems environment, storing the XSS payload in the system's gem registry for exposure via the server UI.

## Description

The 'gem install' command deploys the built .gem, integrating its metadata (including the javascript: homepage) into the local gem index. Once installed, the gem appears in the gem server's listings, ready for XSS triggering. This step requires local access but no elevated privileges. Outcomes include the payload persisting in the environment until uninstalled.

## Requirements

1. Built .gem file (e.g., securitytest-0.1.0.gem) in current directory
2. RubyGems environment writable
3. No prior conflicting gem names

## Defense

Defensive measures and detection strategies:

- Verify gem sources and signatures before installation
- Block installations from local or untrusted .gem files
- Audit installed gems for malicious metadata post-install

## Objectives

1. Integrate the malicious gem into the local registry
2. Make the payload available for serving
3. Enable UI exposure without further modification

## Instructions

### Step 1: Perform Installation

**Context**: Install the local .gem file to add it to the RubyGems collection.

**Command** ([[commands/gem-install-securitytest]]):
```bash
gem install securitytest-0.1.0.gem
```

> This extracts and registers the gem, including metadata. Expected output: "Successfully installed securitytest-0.1.0" and entry in 'gem list'.

### Step 2: Verify Installation

**Context**: Confirm the gem is installed and metadata intact.

Run `gem list securitytest` to check.

> Expected output: Lists the gem version. Success if no errors and metadata queryable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/gem-install-securitytest]]

## Tools Used

- [[tools/gem]]

## Tags

- gem-install
- persistence

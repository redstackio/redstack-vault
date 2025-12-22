---
id: proc-uuid-2
tags:
  - gem-build
  - packaging
type: procedure
tools:
  - '[[tools/gem]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/gem-build-securitytest]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.037Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Build-Malicious-Gem

## Summary

This procedure builds an installable .gem package from the malicious Gemspec file, embedding the XSS payload in the metadata for later exploitation.

## Description

Using the RubyGems CLI, compile the 'securitytest.gemspec' into a .gem file. This step packages the metadata, including the tainted homepage field, without validating URI schemes. The resulting file can be installed locally, making the payload available to the gem server. Target environment is any Ruby system; expected outcome is a portable .gem with the stored XSS.

## Requirements

1. Malicious Gemspec file present in current directory
2. RubyGems CLI access
3. Write permissions in the working directory

## Defense

Defensive measures and detection strategies:

- Implement scheme validation in the 'gem build' process to block javascript: URIs
- Scan Gemspec files for suspicious content before building
- Log all gem builds and review for anomalies

## Objectives

1. Generate a .gem file with embedded malicious metadata
2. Preserve the JavaScript payload in the package
3. Prepare for installation and serving

## Instructions

### Step 1: Execute Gem Build

**Context**: Run the build command to package the Gemspec and associated files into a gem archive.

**Command** ([[commands/gem-build-securitytest]]):
```bash
gem build securitytest.gemspec
```

> This command reads the Gemspec, validates basic structure, and outputs 'securitytest-0.1.0.gem'. Expected output: Success message like "Successfully built RubyGem" and the .gem file created.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/gem-build-securitytest]]

## Tools Used

- [[tools/gem]]

## Tags

- gem-build
- packaging

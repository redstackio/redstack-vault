---
id: proc-browse-sql-config-leaked-keys
tags:
  - credential-leak
  - github
  - sql
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - GitHub
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:32:01.853Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Browse SQL Config for Additional Leaked Keys

## Summary

This procedure focuses on accessing and reviewing SQL configuration files in a public GitHub repository to uncover additional sensitive keys and secrets beyond initial findings.

## Description

SQL files like app-conf-defaults.sql often contain default configurations with embedded secrets. In public repos, these can expose a wide range of API keys. This procedure builds on prior discoveries, targeting specific commits or files to extract more credentials, increasing the attack surface for service compromises.

## Requirements

1. Direct URL to the SQL file.
2. Browser for file viewing.
3. Basic understanding of SQL config syntax.

## Defense

Defensive measures and detection strategies:

- Sanitize SQL files before committing and use database secret injection at runtime.
- Perform code reviews and use tools like git diff for secret detection.
- Set up alerts for repository access spikes.

## Objectives

1. Identify extra keys in SQL configs.
2. Expand credential collection.
3. Demonstrate broad exposure risks.

## Instructions

### Step 1: Navigate to Specific File

**Context**: Directly access the known vulnerable file.

Open https://github.com/liberapay/liberapay.com/blob/4419a95916f4af3bfd61361341776fce66bf7a6a/sql/app-conf-defaults.sql in a browser.

### Step 2: Scan for Secrets

**Context**: Look for unescaped sensitive data.

Review the file contents line-by-line for API keys, tokens, or secrets in INSERT or SET statements.

**Expected Output**: Additional credentials listed in plain text.

### Step 3: Compile Findings

**Context**: Aggregate with previous leaks.

Document all discovered items and note commit hash for reference.

**Expected Output**: Comprehensive list of leaks.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Hardware]] Gather Victim Identity Information: Credentials

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[credential-leak]]
- [[github]]
- [[sql]]

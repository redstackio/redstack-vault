---
id: proc-004
tags:
  - data-extraction
  - credentials
  - pii-leak
type: procedure
tools:
  - '[[tools/Eclipse-Memory-Analyzer]]'
  - '[[tools/VisualVM]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.360Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Sensitive-Information-from-Heap-Dump

## Summary

This procedure searches the analyzed heap dump for strings containing credentials, secrets, PII, and code snippets to enable account takeovers and further exploitation.

## Description

Within memory tools, string searches reveal plaintext secrets like API keys, passwords, JWT tokens, and database URLs stored in heap objects. This data can lead to severe impacts such as admin access, payment manipulation, and service disruption in the Stripo application.

## Requirements

1. Loaded heap dump in analysis tool
2. Knowledge of target data patterns (e.g., "password=", "secret_key")
3. Export capabilities in the tool

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive data in memory and avoid plaintext storage
- Implement memory obfuscation techniques
- Audit heap dumps in incident response to detect leaks

## Objectives

1. Locate and export exploitable secrets
2. Assess impact on customer data and accounts
3. Chain to additional attacks like token replay

## Instructions

### Step 1: Perform String Search

**Context**: Use the tool's query interface to find sensitive patterns.

**Command**:
```bash
# In Eclipse MAT: Query > Java Basics > Search for char[] or String with regex like .*secret.*
```

> Results show objects holding strings like "jwt.secret=abc123".

### Step 2: Export and Document Findings

**Context**: Save extracted data for use in exploits.

**Command**:
```bash
# In VisualVM: Right-click results > Export to text file
```

> Generates a report with PII, credentials, and code excerpts.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Eclipse-Memory-Analyzer]]
- [[tools/VisualVM]]

## Tags

- [[data-extraction]]
- [[Credentials]]

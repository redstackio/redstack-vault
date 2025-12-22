---
id: proc-setup-rust-poc
tags:
  - rust
  - poc-setup
  - client-development
type: procedure
tools:
  - '[[tools/cargo]]'
  - '[[tools/Rust]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Blockchain
  - Cosmos SDK
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:46.783Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Set-Up-Rust-POC-Project

## Summary

This procedure initializes a Rust project configured as a client for interacting with Cosmos SDK, enabling the creation of messages to exploit the lockup module vulnerability.

## Description

The POC uses Rust to build a client that crafts MsgExecute with arbitrary sender addresses, targeting the lockup.go validation flaw. It includes files like main.rs for attack logic and dependencies for Cosmos protobuf interactions.

## Requirements

1. Rust toolchain installed
2. Cargo package manager
3. Access to Cosmos SDK protobuf definitions

## Defense

Defensive measures and detection strategies:

- Scan for unauthorized Rust projects in development environments
- Monitor Cargo.toml for suspicious blockchain dependencies
- Enforce code reviews for client-side exploit code

## Objectives

1. Create project structure for attack client
2. Integrate Cosmos SDK interaction libraries
3. Prepare for message forging

## Instructions

### Step 1: Initialize Project

**Context**: Set up the basic Rust project structure.

**Command** (cargo init):
```bash
cargo init cosmos-poc
cd cosmos-poc
```

> Initializes a new Rust project. Expected output: Cargo.toml and src/main.rs created.

### Step 2: Configure Dependencies

**Context**: Add Cosmos SDK dependencies via Cargo.toml.

**Instructions**: Edit Cargo.toml to include crates for protobuf, gRPC, and Cosmos types (e.g., cosmrs, prost). Place .rs files (main.rs, types.rs, etc.) in src/.

**Command** (no direct command; manual edit):

> After editing, run `cargo check` to verify. Expected output: No compilation errors.

### Step 3: Verify Setup

**Context**: Ensure project is ready.

**Command** (cargo check):
```bash
cargo check
```

> Checks dependencies and code. Success if no errors reported.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (adapted for Rust scripting/client execution)

### Sub-Techniques


## Commands Used

- [[commands/cargo-init]]
- [[commands/cargo-check]]

## Tools Used

- [[tools/cargo]]
- [[tools/Rust]]

## Tags

- [[rust-poc]]
- [[client-setup]]

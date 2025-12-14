---
id: cmd-cargo-run
data: cargo run
tags:
  - rust-execute
  - poc-run
type: command
output: 'Creates locking account, locks funds, waits, and transfers to attacker'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:46.740Z'
verified: false
validated: true
submitted: true
---
---

# cargo-run

## Command

```bash
cargo run
```

## Description

Compiles and executes the Rust POC to perform the unauthorized transfer attack on the local Cosmos chain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs main.rs by default | No |

## Examples

### Basic Usage

```bash
cargo run
```

### Advanced Usage

```bash
cargo run --release
```

## Expected Output

Transaction hashes for account creation, lock, and transfer; balance changes confirming theft.

## Related

- [[Related Procedure: Execute-Unauthorized-Fund-Transfer]]

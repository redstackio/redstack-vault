---
id: cd-poc-001
data: cd jdbc-sqlite-jolokia-rce
tags:
  - navigation
  - poc
type: command
output: Current directory changed
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.287Z'
verified: false
validated: true
submitted: true
---
# CD to PoC Directory

## Command

```bash
cd jdbc-sqlite-jolokia-rce
```

## Description

Changes the current working directory to the folder containing the Kafka Connect RCE proof-of-concept script and assets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| jdbc-sqlite-jolokia-rce | Path to PoC directory | Yes |

## Examples

### Basic Usage

```bash
cd /path/to/jdbc-sqlite-jolokia-rce
```

### Advanced Usage

```bash
cd ~/exploits/jdbc-sqlite-jolokia-rce && ls
```

## Expected Output

Shell prompt updates to reflect new directory, e.g., "user@host:~/jdbc-sqlite-jolokia-rce$".

## Related

- [[Related Procedure: Execute-PoC-Script-for-Kafka-Connect-RCE]]

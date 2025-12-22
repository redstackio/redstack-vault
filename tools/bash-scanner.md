---
id: tool-bash-scanner
url: null
tags:
  - automation
  - scanning
  - bash
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:54.786Z'
validated: true
submitted: true
---
---

# bash-scanner

**Status**: Unverified

## Overview

Custom bash script (scanner.sh) for automating SSRF exploitation in Kubernetes by parallel templating and applying StorageClass/PVC YAML to scan internal networks.

## Description

The script uses sed for YAML templating, kubectl for applies/deletes, and parallel workers to probe IPs/ports without overwhelming the cluster. Configured for 15 workers targeting 172.16.0.0/12 and key ports like 10255.

## Features

- Feature 1: Parallel execution with workers
- Feature 2: YAML templating for dynamic URLs
- Feature 3: Event parsing for open service detection

## Installation

### Requirements

- Bash shell
- kubectl installed
- Template YAML files

### Install Commands

```bash
# Create scanner.sh
cat > scanner.sh << EOF
#!/bin/bash
# Logic for looping IPs/ports, sed replace {{URL}}, kubectl apply/delete
EOF
chmod +x scanner.sh
```

## Basic Usage

```bash
./scanner.sh
```

### Common Options

| Option | Description |
|--------|-------------|
| `-w, --workers` | Number of parallel workers (default: 15) |
| `-r, --range` | IP range to scan |

## Examples

### Example 1: Basic Usage

```bash
./scanner.sh -r 172.16.0.0/12
```

### Example 2: Advanced Usage

```bash
./scanner.sh -w 10 -p 10255,2379
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Discovery]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Rapid create/delete of StorageClasses/PVCs
- Event logs showing repeated provisioning failures
- High API server load from automation

## Related Procedures

- [[procedures/Automate-Internal-Network-Scanning-and-Escalation]]

## Related Tools

- [[tools/kubectl]]
- [[tools/masscan]]

## References

- Custom script based on HackerOne report

---

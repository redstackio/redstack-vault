---
id: cmd-burp-intruder-fuzz-001
data: >-
  Burp Suite Intruder: Configure positions with §port§ in URL, load payload
  list, start sniper attack
tags:
  - fuzzing
  - ssrf
  - scanning
type: command
output: null
executor: gui
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.719Z'
verified: false
validated: true
submitted: true
---
# burp-intruder-fuzz

## Command

```bash
# GUI-based: In Burp Suite, select request > Intruder > Positions: Add § before/after '9090' in url param > Payloads: Load ports.txt > Attack type: Sniper > Start attack
```

## Description

Uses Burp Intruder to fuzz the port in SSRF URL for timing-based scanning; not a shell command but GUI workflow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Positions | Mark fuzz point (e.g., §9090§) | Yes |
| Payloads | List of ports (e.g., 1-10000) | Yes |
| Attack Type | Sniper for single position | Yes |

## Examples

### Basic Usage

Mark url=http://127.0.0.1:§9090§/, payloads=8080\n9090, start attack.

### Advanced Usage

Cluster bomb for multiple params; grep results for response lengths >100.

## Expected Output

Table of requests with columns: #, Payload, Status, Length, Time; sort by Time descending for open ports.

## Related

- [[Related Procedure: Perform-Port-Scanning-via-Response-Timing]]

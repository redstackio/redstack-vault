---
id: cf87c077-7d28-482b-9ab7-7c3a40f8652a
name: nmap-run-default-scripts
type: command
executor: bash
data: nmap -sC $_TARGET
output: null
created_at: '2023-04-06T03:56:22.058664+00:00'
updated_at: '2023-04-10T20:25:05.094903+00:00'
platforms:
  - Linux
tags:
  - nmap
  - recon
  - discovery
verified: true
validated: true
---

# nmap-run-default-scripts

## Command

```bash
nmap -sC $_TARGET
```

## Description

Runs Nmap with the default NSE scripts (-sC) to perform automated discovery, including version detection and basic vulnerability checks on the target host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | IP address or hostname of the target | Yes |
| -sC | Enables default script scanning | Built-in |

## Examples

### Basic Usage

```bash
nmap -sC 192.168.1.100
```

### Advanced Usage

```bash
nmap -sC -p- 192.168.1.100
```

> Scans all ports with default scripts.

## Expected Output

Port scan results with script outputs, e.g.:

PORT   STATE SERVICE
80/tcp open  http
| http-title: Site title

## Related

- [[procedures/Network-Discovery-with-Nmap-Scripting-Engine]]
- [[tools/Nmap]]

---
data: nmap -sV -O -p 3478 stun.nextcloud.com
tags:
  - recon
  - os-detection
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.525Z'
id: ccedc2e4-3e91-4fce-9e9b-d6694d9bdc04
verified: false
validated: true
submitted: true
---
# nmap-os-detect

## Command

```bash
nmap -sV -O -p 3478 stun.nextcloud.com
```

## Description

This command uses nmap to perform service version detection and OS fingerprinting on a specific port of the target host, revealing the underlying Unix OS version for vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-sV` | Enable service version detection | Yes |
| `-O` | Enable OS detection | Yes |
| `-p 3478` | Scan specific port (STUN default) | Yes |
| `stun.nextcloud.com` | Target hostname | Yes |

## Examples

### Basic Usage

```bash
nmap -sV -O -p 3478 stun.nextcloud.com
```

### Advanced Usage

```bash
nmap -sV -O -p- stun.nextcloud.com --osscan-guess
```

## Expected Output

Nmap scan report for stun.nextcloud.com
Host is up (0.XXs latency).
PORT     STATE SERVICE VERSION
3478/udp open  stun     (unknown banner: Ubuntu 12.04)
OS details: Linux 3.2

## Related

- [[Related Procedure|procedures/Detect-End-of-Life-Operating-System]]

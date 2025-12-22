---
id: b6e925ad-40bc-4cd9-8c91-260d76e20a09
name: dockscan-basic-scan
type: command
executor: bash
data: 'dockscan unix:///var/run/docker.sock'
output: null
created_at: '2023-04-06T03:56:16.860177+00:00'
updated_at: '2023-04-10T20:33:48.514623+00:00'
platforms:
  - Linux
tags:
  - docker
  - scanning
verified: true
validated: true
---

# dockscan-basic-scan

## Command

```bash
dockscan unix:///var/run/docker.sock
```

## Description

This command performs a basic security audit of a local Docker installation by connecting to the Unix socket, identifying vulnerabilities in containers, images, and configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| unix:///var/run/docker.sock | Path to the local Docker socket for communication | Yes |

## Examples

### Basic Usage

```bash
dockscan unix:///var/run/docker.sock
```

### Advanced Usage

For remote scanning, use tcp://host:port instead of unix socket.

## Expected Output

Console output listing vulnerabilities, such as:
- Vulnerable images: e.g., "Image nginx:1.14 has CVE-2019-1234"
- Misconfigurations: e.g., "Container abc123 runs in privileged mode"
- Summary of risks and recommendations

## Related

- [[procedures/Docker-Security-Assessment]]
- [[commands/dockscan-generate-html-report]]

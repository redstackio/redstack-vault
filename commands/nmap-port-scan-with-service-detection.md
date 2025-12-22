---
data: sudo nmap -sSV -p- 104.131.159.88 -oA stage_ph -T4
tags:
  - scanning
  - recon
type: command
executor: bash
platforms:
  - Linux
id: b84fa5ad-cb28-40d9-bc43-30c4cddc7d52
created_at: '2025-12-14T03:16:37.263Z'
updated_at: '2025-12-14T03:16:37.263Z'
verified: false
validated: true
submitted: true
---
# nmap-port-scan-with-service-detection

## Command

```bash
sudo nmap -sSV -p- 104.131.159.88 -oA stage_ph -T4
```

## Description

This command performs a comprehensive port scan using nmap to detect all open ports and services on the target IP, including version detection, to identify exposed applications like NodeBB on port 4567.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-sSV` | Enables service and version detection | Yes |
| `-p-` | Scans all 65535 ports | Yes |
| `104.131.159.88` | Target IP address | Yes |
| `-oA stage_ph` | Saves output in all formats prefixed with 'stage_ph' | No |
| `-T4` | Aggressive timing template for faster scanning | No |
| `sudo` | Required for privileged scanning | Yes |

## Examples

### Basic Usage

```bash
sudo nmap -sSV -p- 104.131.159.88
```

### Advanced Usage

```bash
sudo nmap -sSV -p- 104.131.159.88 -oA stage_ph -T4 -v
```

## Expected Output

A list of open ports and services, e.g., "4567/tcp open tram? | http://nodebb...", with details on protocols and versions for vulnerability assessment.

## Related

- [[Related Procedure: Port-Scan-to-Discover-Exposed-Services]]

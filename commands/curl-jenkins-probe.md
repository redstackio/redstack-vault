---
data: 'curl -I https://jenkins.target.com'
tags:
  - recon
  - probe
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 6333d805-b009-49e5-a190-b747e0685bdb
created_at: '2025-12-11T03:47:56.619Z'
updated_at: '2025-12-11T03:47:56.619Z'
verified: false
validated: true
submitted: true
---
# curl-jenkins-probe

## Command

```bash
curl -I https://jenkins.target.com
```

## Description

This command probes a target URL for Jenkins-specific HTTP headers to confirm the presence of a Jenkins instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `https://jenkins.target.com` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://jenkins.target.com
```

### Advanced Usage

```bash
curl -I -k https://jenkins.target.com:8080
```

## Expected Output

HTTP headers including 'X-Jenkins: <version>' if Jenkins is present.

## Related

- #curl
- [[procedures/Discover-Open-Jenkins-Instance]]

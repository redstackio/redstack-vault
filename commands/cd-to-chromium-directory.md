---
data: cd ./x-pack/plugins/reporting/chromium/headless_shell-linux_x64/
tags:
  - navigation
  - chromium
type: command
output: bash-4.4# in the new directory
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.213Z'
id: 67938699-8275-4db5-9c93-85873d84e433
verified: false
validated: true
submitted: true
---
# cd-to-chromium-directory

## Command

```bash
cd ./x-pack/plugins/reporting/chromium/headless_shell-linux_x64/
```

## Description

Navigates inside the Kibana container to the directory containing the headless Chromium binary used by the reporting feature.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | ./x-pack/plugins/reporting/chromium/headless_shell-linux_x64/ | Yes |

## Examples

### Basic Usage

```bash
cd ./x-pack/plugins/reporting/chromium/headless_shell-linux_x64/
```

## Expected Output

Changes to the specified directory; prompt updates to reflect new path.

## Related

- [[commands/headless-shell-load-url]]
- [[procedures/Run-Kibana-Docker-Container-and-Test-Chromium]]

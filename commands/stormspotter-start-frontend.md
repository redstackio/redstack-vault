---
id: d00f6b60-16e3-4390-abbf-6124ea649ae8
type: command
executor: bash
data: quasar.cmd serve -p $_PORT --history
output: null
created_at: '2023-04-06T03:56:14.585426+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - stormspotter
  - frontend
verified: true
validated: true
---

# stormspotter-start-frontend

## Command

```bash
quasar.cmd serve -p $_PORT --history
```

## Description

Serves the StormSpotter web UI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p, $_PORT | Port (e.g., 9091) | Yes |
| --history | Enable history mode | Yes |

## Examples

### Basic Usage

```bash
quasar.cmd serve -p 9091 --history
```

## Expected Output

UI available at http://localhost:9091.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azure-StormSpotter]]

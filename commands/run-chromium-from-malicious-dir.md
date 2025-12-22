---
id: cmd-run-chromium
data: chromium
tags:
  - rce-trigger
  - snap-exploit
type: command
output: >-
  Triggers RCE via malicious library load, prints 'Got code execution running as
  itszn inside snap container!'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.802Z'
verified: false
validated: true
submitted: true
---
# run-chromium-from-malicious-dir

## Command

```bash
chromium
```

## Description

Launch Chromium browser snap package from malicious cwd, triggering RCE via libc.so.6 load from tls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
chromium
```

### Advanced Usage

```bash
chromium --no-sandbox
```

## Expected Output

Triggers RCE, prints 'Got code execution running as itszn inside snap container!' and launches browser.

## Related

- [[commands/write-test-file-in-container]]
- [[procedures/Trigger-RCE-in-Snap-Application]]

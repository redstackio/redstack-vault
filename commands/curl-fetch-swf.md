---
id: cmd-curl-fetch-swf
data: >-
  curl -s https://www.veris.in/wp-includes/js/mediaelement/flashmediaelement.swf
  -o flash.swf
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.626Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-swf

## Command

```bash
curl -s https://www.veris.in/wp-includes/js/mediaelement/flashmediaelement.swf -o flash.swf
```

## Description

This command fetches the flashmediaelement.swf file from a WordPress installation silently and saves it locally for inspection, useful for identifying potential XSS vectors in SWF parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `-o flash.swf` | Output file name | Yes |
| URL | Target SWF endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -s https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf -o flash.swf
```

### Advanced Usage

```bash
curl -s -L https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf?param=test -o flash.swf
```

## Expected Output

A binary SWF file saved as 'flash.swf' with size indicating successful download (e.g., several KB); no console output due to -s flag.

## Related

- [[commands/curl-test-parameter]]
- [[procedures/Identify-Vulnerable-Flash-Media-Element-Endpoint-in-WordPress]]

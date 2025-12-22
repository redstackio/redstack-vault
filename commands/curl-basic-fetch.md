---
type: command
executor: bash
data: curl $_URL
tags:
  - curl
  - fetch
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# curl-basic-fetch

## Command

```bash
curl $_URL
```

## Description

This command fetches the content from a specified URL using curl and outputs it to stdout. Use it to test basic connectivity or retrieve web content during reconnaissance or injection testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | The target URL to fetch (e.g., https://www.example.com) | Yes |

## Examples

### Basic Usage

```bash
curl https://www.google.com
```

### Advanced Usage

```bash
curl -s https://www.example.com  # Silent mode
```

## Expected Output

HTML content of the page, such as:
```
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information..."
```

## Related

- [[procedures/Curl-Argument-Injection-for-Arbitrary-Command-Execution]]
- [[commands/curl-download-file]]

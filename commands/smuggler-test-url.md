---
data: 'smuggler -u https://slackb.com'
tags:
  - http-request-smuggling
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 1f1d5304-9e0f-4648-b078-0502c0af4b84
created_at: '2025-12-13T09:01:26.218Z'
updated_at: '2025-12-13T09:01:26.218Z'
verified: false
validated: true
submitted: true
---
# Smuggler Test URL

## Command

```bash
smuggler -u https://slackb.com
```

## Description

This command runs the smuggler tool to test for HTTP Request Smuggling vulnerabilities on the specified URL, performing exhaustive checks for desyncs in header processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Specifies the target URL to test | Yes |

## Examples

### Basic Usage

```bash
smuggler -u https://slackb.com
```

### Advanced Usage

```bash
smuggler -u https://slackb.com --verbose
```

## Expected Output

Output indicating failures or successes in smuggling tests, such as the 'space1' test failure showing CL.TE desync.

## Related

- [[procedures/Perform-Reconnaissance-for-HTTP-Request-Smuggling]]
- [[tools/Smuggler]]

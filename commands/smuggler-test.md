---
data: 'smuggler -u https://slackb.com'
tags:
  - recon
  - smuggling
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.487Z'
id: d5beb6c5-b1d8-4f59-954a-7278d0f83db5
verified: false
validated: true
submitted: true
---
# smuggler-test

## Command

```bash
smuggler -u https://slackb.com
```

## Description

This command runs the smuggler tool to perform exhaustive HTTP Request Smuggling tests on the specified target URL, detecting vulnerabilities like CL.TE desync.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Specifies the target URL for testing | Yes |

## Examples

### Basic Usage

```bash
smuggler -u https://slackb.com
```

### Advanced Usage

```bash
smuggler -u https://example.com --tests all
```

## Expected Output

Detection report, e.g., "space1: vulnerable - CLTE desync detected with space in Transfer-Encoding header."

## Related

- [[Related Procedure]]

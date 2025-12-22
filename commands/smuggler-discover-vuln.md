---
data: 'smuggler -u https://slackb.com'
tags:
  - recon
  - http-request-smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 6d5a5d22-0156-48b5-8711-f31a7d4880f2
created_at: '2025-12-11T06:10:33.352Z'
updated_at: '2025-12-11T06:10:33.352Z'
verified: false
validated: true
submitted: true
---
# smuggler-discover-vuln

## Command

```bash
smuggler -u https://slackb.com
```

## Description

Runs the Smuggler tool to test for HTTP Request Smuggling vulnerabilities on the specified URL, performing exhaustive payload tests to identify desyncs.

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

Output indicating test results, such as failure in 'space1' test showing CL.TE desync.

## Related

- [[commands/http-smuggling-payload]]
- [[procedures/Discover-CL.TE-HTTP-Request-Smuggling-Vulnerability]]

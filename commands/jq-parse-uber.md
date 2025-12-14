---
id: c4g5h6i7-j8k9-0124-ghij-7890123456
data: 'jq ''.user.personalInfo, .mobileAuthToken'' response.json'
tags:
  - parsing
  - json
  - extraction
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:22.945Z'
verified: false
validated: true
submitted: true
---
# jq-parse-uber

## Command

```bash
jq '.user.personalInfo, .mobileAuthToken' response.json
```

## Description

Parses the Uber API response JSON to extract personal info and mobile auth token fields.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `.user.personalInfo` | Path to personal data | Yes (adjust as needed) |
| `.mobileAuthToken` | Path to auth token | Yes |
| `response.json` | Input file | Yes |

## Examples

### Basic Usage

```bash
jq '.user.personalInfo, .mobileAuthToken' response.json
```

### Advanced Usage

Pretty print all user data:
```bash
jq '.user | {personalInfo, mobileAuthToken}' response.json
```

## Expected Output

Extracted JSON objects showing PII and token.

## Related

- [[Related Procedure: Retrieve-Sensitive-User-Data-and-Token]]

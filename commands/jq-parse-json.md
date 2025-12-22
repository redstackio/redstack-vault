---
data: 'jq ''.[] | .authors[] | .email'' composer_data.json'
tags:
  - json
  - parsing
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.642Z'
id: e51956a4-4f12-404e-9ef5-6479cba9e28e
verified: false
validated: true
submitted: true
---
# jq-parse-json

## Command

```bash
jq '.[] | .authors[] | .email' composer_data.json
```

## Description

This command uses jq to parse a JSON file from the Nextcloud composer endpoint, extracting specific fields like author emails to reveal leaked sensitive information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Query | jq filter expression, e.g., '.[] | .authors[] | .email' | Yes |
| Input file | The JSON file to parse | Yes |

## Examples

### Basic Usage

```bash
jq '.[] | .authors[] | .email' composer_data.json
```

### Advanced Usage

```bash
jq '.[] | {name: .name, version: .version}' composer_data.json > versions.txt
```

> Outputs package names and versions to a file.

## Expected Output

List of email strings, e.g., "author@domain.com", or structured objects depending on the query.

## Related

- [[Related Procedure: Inspect-Leaked-Sensitive-Data]]

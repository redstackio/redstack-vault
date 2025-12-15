---
id: cmd-001
data: 'curl https://apps-staging.pingone.com/package.json'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.673Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-package-json

## Command

```bash
curl https://apps-staging.pingone.com/package.json
```

## Description

This command uses curl to fetch the publicly exposed package.json file from a staging web application, bypassing authentication controls to disclose Node.js dependencies and versions for reconnaissance purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint for the package.json file | Yes |

## Examples

### Basic Usage

```bash
curl https://apps-staging.pingone.com/package.json
```

### Advanced Usage

```bash
curl -s https://apps-staging.pingone.com/package.json | jq '.'
```

> Adds silent mode (-s) and pipes to jq for formatted JSON output.

## Expected Output

A JSON object detailing the application's package information, e.g.:

```json
{
  "name": "staging-app",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.17.1",
    "lodash": "^4.17.21"
  }
}
```

Inspect for vulnerable versions.

## Related

- [[Related Procedure: Bypass-Authentication-to-Access-Static-package.json-File]]

---
id: cmd-uuid-002
data: 'curl https://_domainkey.launchpad.37signals.com/sprockets.js -o sprockets.js'
tags:
  - reconnaissance
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.094Z'
verified: false
validated: true
submitted: true
---
# curl-access-sprockets-js

## Command

```bash
curl https://_domainkey.launchpad.37signals.com/sprockets.js -o sprockets.js
```

## Description

This command fetches the exposed sprockets.js file using curl, allowing inspection of JavaScript source code for reconnaissance on client-side logic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target JS endpoint | Yes |
| -o | Output file name | Yes |

## Examples

### Basic Usage

```bash
curl https://example.com/sprockets.js -o script.js
```

### Advanced Usage

```bash
curl -v https://_domainkey.launchpad.37signals.com/sprockets.js -o sprockets.js
```

## Expected Output

A JavaScript file (sprockets.js) with source code, including prototype pollution prevention scripts, loaded successfully.

## Related

- [[Related Procedure: Access-Exposed-Sprockets-Js-Source-Code]]

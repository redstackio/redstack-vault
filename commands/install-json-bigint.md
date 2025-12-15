---
id: cmd-uuid-1
data: npm install json-bigint@0.3.1
tags:
  - setup
  - npm
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.301Z'
verified: false
validated: true
submitted: true
---
# install-json-bigint

## Command

```bash
npm install json-bigint@0.3.1
```

## Description

Installs the vulnerable version 0.3.1 of the json-bigint Node.js module, which is required for exploiting CVE-2020-8237 prototype pollution leading to DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `json-bigint@0.3.1` | Specifies the exact vulnerable version to install | Yes |

## Examples

### Basic Usage

```bash
npm install json-bigint@0.3.1
```

### Advanced Usage

```bash
npm install json-bigint@0.3.1 --save
```

## Expected Output

Installation success: "added 1 package" or similar, with json-bigint in node_modules.

## Related

- [[Related Procedure]]

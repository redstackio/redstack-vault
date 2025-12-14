---
data: node redos-test.js
tags:
  - redos
  - test
  - dos
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.704Z'
id: c77569cf-8cdf-48ee-b819-fc8a758857b5
verified: false
validated: true
submitted: true
---
# node redos-test

## Command

```bash
node redos-test.js
```

## Description

This command executes a Node.js script to test the ReDoS vulnerability in 'is-my-json-valid' by validating a JSON object containing a malicious email input, measuring the time taken and demonstrating event loop blockage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `redos-test.js` | The script file path | Yes |

## Examples

### Basic Usage

```bash
node redos-test.js
```

### Advanced Usage

Run with timing flags for more details:

```bash
node --max-old-space-size=4096 redos-test.js
```

## Expected Output

Script output shows start time, validation attempt, and end time with a delay of ~10 seconds: "Validation started at [timestamp], completed at [timestamp + 10s]. CPU usage spiked."

## Related

- [[Related Procedure|Exploit-ReDoS-with-Malicious-Email-Input]]

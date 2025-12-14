---
data: runtests.pl 418
tags:
  - dos
  - curl
  - test
type: command
output: Test failure indicating memory exhaustion in curl header processing
executor: bash
platforms:
  - Linux
  - Unix
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.573Z'
id: fe307b71-2f46-4e10-8162-9c1f43f32a07
verified: false
validated: true
submitted: true
---
# runtests.pl-418

## Command

```bash
runtests.pl 418
```

## Description

Executes test case 418 in the curl project test suite to reproduce the CVE-2023-23916 DoS vulnerability, simulating an HTTP response with multiple Transfer-Encoding and Content-Encoding headers that cause unbounded buffer allocations and memory exhaustion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `418` | Test case number for the multi-header DoS reproduction | Yes |

## Examples

### Basic Usage

```bash
runtests.pl 418
```

### Advanced Usage

```bash
./tests/runtests.pl 418 -v
```

(Use -v for verbose output to see detailed allocation failures.)

## Expected Output

Test execution logs showing failure in curl's HTTP parsing, with indicators of excessive memory use, such as 'out of memory' errors or high RAM consumption during header processing.

## Related

- [[procedures/Run-curl-DoS-Reproduction-Test]]

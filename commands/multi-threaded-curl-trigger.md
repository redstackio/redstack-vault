---
data: ./curl_race_test
tags:
  - execution
  - race-condition
type: command
executor: bash
platforms:
  - Linux
  - Unix-like
id: cac861ec-6dcf-49d1-8328-4d6e1b63f887
created_at: '2025-12-14T17:24:18.797Z'
updated_at: '2025-12-14T17:24:18.797Z'
verified: false
validated: true
submitted: true
---
# multi-threaded-curl-trigger

## Command

```bash
./curl_race_test
```

## Description

Executes the compiled multi-threaded libcurl test program to trigger the synchronous resolver race condition, simulating concurrent DNS resolutions that corrupt the global buffer.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./curl_race_test` | Path to compiled binary | Yes |

## Examples

### Basic Usage

```bash
./curl_race_test
```

### Advanced Usage

```bash
ulimit -c unlimited && ./curl_race_test
```

## Expected Output

Program runs briefly then crashes with "Segmentation fault (core dumped)" or similar, indicating race-induced buffer corruption. No stdout if crash occurs early.

## Related

- [[Related Procedure|procedures/Trigger-libcurl-Resolver-Race-Condition]]

---
id: 97155918-9627-4aaa-8161-470be1e564bc
name: echo-test-content-to-file
type: command
executor: bash
data: echo "$TEST_CONTENT" > /tmp/test_file.txt
output: Silent success; file created
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.025Z'
platforms:
  - Linux
tags:
  - file-creation
  - test-data
verified: false
validated: true
submitted: true
---

# echo-test-content-to-file

## Command

```bash
echo "$TEST_CONTENT" > /tmp/test_file.txt
```

## Description

Writes the contents of the $TEST_CONTENT environment variable to a test file in /tmp, used to prepare detectable data for leakage verification in curl exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $TEST_CONTENT | Unique string like "http://LEAKED_DATA_$(date +%s).invalid" for DNS detection | Yes |
| > /tmp/test_file.txt | Redirects output to file | Yes |

## Examples

### Basic Usage

```bash
echo "$TEST_CONTENT" > /tmp/test_file.txt
```

### Advanced Usage

Set TEST_CONTENT first:
```bash
TEST_CONTENT="http://TEST_$(date +%s).invalid"; echo "$TEST_CONTENT" > /tmp/test_file.txt
```

## Expected Output

No stdout; the file /tmp/test_file.txt contains the echoed string. Verify with `cat /tmp/test_file.txt`.

## Related

- [[commands/ln-create-symlink]]
- [[procedures/Prepare-Test-File-for-curl-IPFS-Exploitation]]

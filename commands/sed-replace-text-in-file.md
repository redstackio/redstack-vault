---
id: 6a99b91f-da21-451e-b0b4-219c0c9a3302
name: sed-replace-text-in-file
type: command
executor: bash
data: sed 's/$_OLD_TEXT/$_NEW_TEXT/g' $_INPUT_FILE > $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:22.336269+00:00'
updated_at: '2023-04-10T20:25:09.843906+00:00'
platforms:
  - Linux
tags:
  - text-processing
  - mitm-modification
verified: true
validated: true
---

# sed-replace-text-in-file

## Command

```bash
sed 's/$_OLD_TEXT/$_NEW_TEXT/g' $_INPUT_FILE > $_OUTPUT_FILE
```

## Description

Uses sed to globally substitute (replace) all occurrences of one string with another in a file or stream. In MITM contexts, it's piped into interception pipelines to modify responses, e.g., injecting payloads or altering credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_OLD_TEXT | Text pattern to find and replace | Yes |
| $_NEW_TEXT | Replacement text | Yes |
| $_INPUT_FILE | Source file or stream | Yes |
| $_OUTPUT_FILE | Destination for modified content | Yes |
| g | Global flag (replace all occurrences) | Built-in |

## Examples

### Basic Usage

```bash
sed 's/password/protected/g' response.txt > modified.txt
```

### Piped Usage in MITM

```bash
... | sed 's/old_js/new_js/g' | tee log.txt
```

## Expected Output

Modified content written to $_OUTPUT_FILE, e.g., input "Enter password" becomes "Enter protected".

## Related

- [[procedures/SSL-MITM-Network-Discovery-with-OpenSSL]]
- [[codes/openssl-mitm-setup-pipeline]]

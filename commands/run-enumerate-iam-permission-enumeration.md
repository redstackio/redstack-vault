---
type: command
executor: bash
data: ./enumerate-iam.py --access-key $_ACCESS_KEY --secret-key $_SECRET_KEY
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - iam
  - enumeration
verified: true
validated: true
---

# run-enumerate-iam-permission-enumeration

## Command

```bash
./enumerate-iam.py --access-key $_ACCESS_KEY --secret-key $_SECRET_KEY
```

## Description

Executes the enumerate-iam Python script to probe AWS IAM permissions by attempting API calls across multiple services. It logs successful and failed permissions, helping identify credential scope. Run from the tool's directory after setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --access-key | AWS access key ID (e.g., AKIAIOSFODNN7EXAMPLE) | Yes |
| --secret-key | AWS secret access key (e.g., wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY) | Yes |

## Examples

### Basic Usage

```bash
./enumerate-iam.py --access-key AKIAEXAMPLE --secret-key wJalrXUtnFEMI
```

### With Output Redirection

```bash
./enumerate-iam.py --access-key $_ACCESS_KEY --secret-key $_SECRET_KEY > permissions_log.txt
```

## Expected Output

Log messages like "Starting permission enumeration for access-key-id 'AKIA...'" followed by service checks, e.g., "[INFO] gamelift.list_builds() worked!" for successes and failures for denied actions. Ends with a summary of accessible permissions if implemented.

## Related

- [[procedures/AWS-IAM-Permissions-Enumeration]]

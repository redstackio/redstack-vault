---
id: 570e7ac1-fb15-4de8-a6f3-4d16a67751a0
name: run-o365creeper-validate-emails
type: command
executor: bash
data: >-
  C:\Python27\python.exe C:\Tools\o365creeper\o365creeper.py -f
  C:\Tools\emails.txt -o C:\Tools\validemails.txt
output: null
created_at: '2023-05-28T04:04:52.995365+00:00'
updated_at: '2023-05-28T04:04:53.191028+00:00'
platforms:
  - Cloud
tags:
  - enumeration
  - email
  - o365
verified: true
validated: true
---

# run-o365creeper-validate-emails

## Command

```bash
C:\Python27\python.exe C:\Tools\o365creeper\o365creeper.py -f C:\Tools\emails.txt -o C:\Tools\validemails.txt
```

## Description

This command executes the o365creeper Python script to validate a batch of email addresses against an Azure O365 tenant, marking them as VALID or INVALID based on tenant responses. Use it during reconnaissance to identify active user accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f $_INPUT_FILE | Path to the input text file containing email addresses (one per line) | Yes |
| -o $_OUTPUT_FILE | Path to the output file where valid emails will be saved | Yes |
| C:\Python27\python.exe | Path to the Python 2.7 executable | Yes (adjust for environment) |
| C:\Tools\o365creeper\o365creeper.py | Path to the o365creeper script | Yes (adjust for installation) |

## Examples

### Basic Usage

```bash
C:\Python27\python.exe C:\Tools\o365creeper\o365creeper.py -f C:\Tools\emails.txt -o C:\Tools\validemails.txt
```

### Advanced Usage

For a different input/output path:

```bash
C:\Python27\python.exe C:\path\to\o365creeper.py -f C:\path\to\input.txt -o C:\path\to\output.txt
```

## Expected Output

Console output showing validation results for each email:

admin@contoso.onmicrosoft.com   - VALID
noob@contoso.onmicrosoft.com    - INVALID
jeff@contoso.onmicrosoft.com    - VALID
payroll@contoso.onmicrosoft.com - INVALID

Valid emails are also appended to the output file specified with -o.

## Related

- [[procedures/Enumerate-Valid-Emails-in-Azure-O365-Tenant]]
- [[tools/o365creeper]]

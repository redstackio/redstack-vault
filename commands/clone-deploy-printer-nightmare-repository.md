---
id: 3d6080b7-e38e-48c2-8150-5f1cecfd6ac2
name: clone-deploy-printer-nightmare-repository
type: command
executor: bash
data: 'git clone https://github.com/Flangvik/DeployPrinterNightmare'
output: null
created_at: '2023-04-06T03:56:29.867171+00:00'
updated_at: '2023-04-10T20:37:34.442831+00:00'
platforms:
  - Linux
  - Windows
tags:
  - recon
  - setup
verified: true
validated: true
---

# clone-deploy-printer-nightmare-repository

## Command

```bash
git clone https://github.com/Flangvik/DeployPrinterNightmare
```

## Description

Clones the DeployPrinterNightmare GitHub repository to obtain exploit files like FakePrinter.exe and malicious DLLs for PrinterNightmare privilege escalation. Use this as the first step on a system with git installed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/Flangvik/DeployPrinterNightmare | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/Flangvik/DeployPrinterNightmare
```

Clones to a local folder named 'DeployPrinterNightmare'.

## Expected Output

Cloning into 'DeployPrinterNightmare'...
remote: Enumerating objects: X, done.
remote: Counting objects: 100% (X/X), done.
... (successful clone messages)

## Related

- [[procedures/PrinterNightmare-Privilege-Escalation]]

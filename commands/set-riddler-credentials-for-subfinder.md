---
id: 2fd96662-58a7-4709-957a-e25ddbb1c4b8
name: set-riddler-credentials-for-subfinder
type: command
executor: bash
data: >-
  subfinder -update-config -set-config
  RiddlerEmail='$_EMAIL',RiddlerPassword='$_PASSWORD'
output: null
created_at: '2023-04-06T03:56:25.499402+00:00'
updated_at: '2023-04-10T20:25:39.525193+00:00'
platforms:
  - Linux
tags:
  - configuration
  - recon
verified: true
validated: true
---

# set-riddler-credentials-for-subfinder

## Command

```bash
subfinder -update-config -set-config RiddlerEmail='$_EMAIL',RiddlerPassword='$_PASSWORD'
```

## Description

Configures Riddler credentials for Subfinder to access their certificate-based subdomain search data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -update-config | Flag to modify config | Yes |
| -set-config | Sets email and password | Yes |
| RiddlerEmail='$_EMAIL' | Riddler account email | Yes |
| RiddlerPassword='$_PASSWORD' | Riddler account password | Yes |

## Examples

### Basic Usage

```bash
subfinder -update-config -set-config RiddlerEmail='user@example.com',RiddlerPassword='pass123'
```

## Expected Output

Configuration updated successfully.

## Related

- [[procedures/Subdomain-Enumeration-with-Subfinder]]
- [[tools/Subfinder]]

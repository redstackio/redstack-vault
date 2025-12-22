---
id: 7239a3b0-a0d5-4e5d-ae07-2eed1401ee4a
type: command
executor: bash
data: pipenv run python cloudmapper.py find_admins
output: null
created_at: '2023-04-06T03:56:08.940432+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - admins
  - roles
verified: true
validated: true
---

# Find AWS Admins Roles CloudMapper

## Command

```bash
pipenv run python cloudmapper.py find_admins
```

## Description

Identifies admin users and roles in AWS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| find_admins | Find admins mode | Yes |

## Examples

### Basic Usage

```bash
pipenv run python cloudmapper.py find_admins
```

## Expected Output

Admin users: root, admin-role

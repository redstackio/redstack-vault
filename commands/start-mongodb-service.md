---
data: sudo systemctl start mongod
tags:
  - setup
  - database
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.270Z'
id: 9a7b99fc-de47-465d-b2bb-bdcc415428f7
verified: false
validated: true
submitted: true
---
# start-mongodb-service

## Command

```bash
sudo systemctl start mongod
```

## Description

Starts the MongoDB daemon service on Ubuntu/Debian systems using systemd, enabling the database backend for applications like meemo.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Run with superuser privileges | Yes |
| systemctl | System service manager | Yes |
| start | Initiate service | Yes |
| mongod | MongoDB service name | Yes |

## Examples

### Basic Usage

```bash
sudo systemctl start mongod
```

### Check Status

```bash
sudo systemctl status mongod
```

## Expected Output

Service starts successfully with no output if already running; use status command for confirmation showing 'active (running)'.

## Related

- [[commands/install-npm-dependencies]]
- [[procedures/Setup-Meemo-Environment-with-LDAP]]

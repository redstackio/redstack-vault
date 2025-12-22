---
id: 511dd0db-a1b3-4197-9728-4f7dab98a4fa
type: command
executor: bash
data: who
output: null
created_at: '2023-04-06T03:56:21.852184+00:00'
updated_at: '2023-04-06T03:56:21.864145+00:00'
platforms:
  - Linux
tags:
  - discovery
  - users
verified: true
validated: true
---

# who-show-logged-in-users-linux

## Command

```bash
who
```

## Description

Displays information about currently logged-in users on a Linux system, including usernames, terminal IDs, login times, and originating hosts. Useful for reconnaissance to identify active sessions before messaging or targeting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; runs on current system | No |

## Examples

### Basic Usage

```bash
who
```

### With Output Filtering

```bash
who | grep root
```

## Expected Output

```
root     pts/0        2023-10-01 10:30 (192.168.1.100)
user1    pts/1        2023-10-01 11:15 (localhost)
```

Shows user, terminal, time, and source. Empty output indicates no remote sessions.

## Related

- [[procedures/Inter-User-Messaging]]

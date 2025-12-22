---
id: 081577dd-2d07-4144-8c22-27a265c13b86
name: mssql-connect-using-sqsh
type: command
executor: bash
data: sqsh -S $_MSSQL_IP -U $_USERNAME -P $_PASSWORD
output: null
created_at: '2023-04-06T03:56:33.953478+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
platforms:
  - Linux
tags:
  - mssql
  - connection
verified: true
validated: true
---

# mssql-connect-using-sqsh

## Command

```bash
sqsh -S $_MSSQL_IP -U $_USERNAME -P $_PASSWORD
```

## Description

Connects to an MSSQL server using the sqsh client, providing an interactive SQL shell for query execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -S $_MSSQL_IP | Target MSSQL server IP or hostname | Yes |
| -U $_USERNAME | Username for authentication (e.g., sa) | Yes |
| -P $_PASSWORD | Password for the user | Yes |

## Examples

### Basic Usage

```bash
sqsh -S 192.168.1.100 -U sa -P superPassword
```

### With Port Specification

```bash
sqsh -S 192.168.1.100:1433 -U sa -P superPassword
```

## Expected Output

Connection banner followed by SQL prompt:

```
Microsoft (R) SQL Server SQuirrel SHell
Version 1.0.0 (i386-redhat-linux-gnu)
Copyright (C) 1996-2000 by Michael R. Glad
This software is licensed under GPL v2

1> 
```

## Related

- [[procedures/MSSQL-Command-Execution-via-xp-cmdshell]]
- [[commands/mssql-connect-using-impacket-mssqlclient]]

---
id: c894cdf5-a01a-47dd-8e51-d8eda04e6ab0
name: run-bloodhound-application
type: command
executor: bash
data: ./bloodhound --no-sandbox
output: null
created_at: '2023-04-06T03:56:02.119900+00:00'
updated_at: '2023-10-10T20:26:14.196507+00:00'
platforms:
  - Linux
tags:
  - visualization
  - ad
verified: true
validated: true
---

# run-bloodhound-application

## Command

```bash
./bloodhound --no-sandbox
```

## Description

Launches BloodHound GUI for importing and querying AD data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ./bloodhound | Executable path | Yes |
| --no-sandbox | Disable sandbox for compatibility | No |

## Examples

### Basic Usage

```bash
./bloodhound --no-sandbox
```

## Expected Output

Electron window opens; connect to Neo4j and load data.

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/BloodHound]]

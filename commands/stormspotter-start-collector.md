---
id: 19c9cb48-35f0-4a96-a638-8b47c8d9d754
type: command
executor: bash
data: python $_COLLECTOR_PATH cli
output: null
created_at: '2023-04-06T03:56:14.585635+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - stormspotter
  - collector
verified: true
validated: true
---

# stormspotter-start-collector

## Command

```bash
python $_COLLECTOR_PATH cli
```

## Description

Starts the data collector for StormSpotter after az login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COLLECTOR_PATH | Path to sscollector.pyz | Yes |
| cli | Command-line mode | Yes |

## Examples

### Basic Usage

```bash
python C:\Tools\stormspotter\stormcollector\sscollector.pyz cli
```

## Expected Output

Data ingestion logs to Neo4j.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azure-StormSpotter]]

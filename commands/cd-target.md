---
id: cmd-cd-target
data: cd target
tags:
  - navigation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.669Z'
verified: false
validated: true
submitted: true
---
# cd-target

## Command

```bash
cd target
```

## Description

Changes directory to the Maven target folder containing the built ysoserial JAR.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| target | Maven build output directory | Yes |

## Examples

### Basic Usage

```bash
cd target
```

### Advanced Usage

N/A

## Expected Output

Current working directory set to ysoserial/target/ (silent).

## Related

- [[commands/mvn-build-ysoserial]]
- [[commands/java-generate-urldns-payload]]

---
id: babd5157-cbd3-4fb5-970e-58f8a023a81e
type: command
executor: bash
data: jar -cvf yaml-payload.jar -C src/ .
output: null
platforms:
  - Linux
  - macOS
tags:
  - jar
  - archive
  - java
created_at: '2023-04-06T03:55:59.656796+00:00'
updated_at: '2023-04-10T20:22:30.128005+00:00'
verified: true
validated: true
---

# jar-create-yaml-payload-archive

## Command

```bash
jar -cvf yaml-payload.jar -C src/ .
```

## Description

Creates a JAR archive containing the compiled AwesomeScriptEngineFactory class from the src directory, packaging it as the deserialization payload for remote loading.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c | Create new archive | Yes |
| -v | Verbose output | Yes |
| -f yaml-payload.jar | Output file name | Yes |
| -C src/ . | Change to src and include all files | Yes |

## Examples

### Basic Usage

```bash
jar -cvf yaml-payload.jar -C src/ .
```

### Without Verbose

```bash
jar -cf yaml-payload.jar -C src/ .
```

## Expected Output

added manifest
adding: artsploit/AwesomeScriptEngineFactory.class(in = 1234) (out= 567)(deflated 54%)

## Related

- [[procedures/Remote-Code-Execution-via-Spring-Boot-Actuator-Env]]

---
id: 62a82aae-dbe4-450f-8d4c-af280d6bd685
type: command
executor: bash
data: javac src/artsploit/AwesomeScriptEngineFactory.java
output: null
platforms:
  - Linux
  - macOS
tags:
  - javac
  - compile
  - java
created_at: '2023-04-06T03:55:59.656768+00:00'
updated_at: '2023-04-10T20:22:30.128005+00:00'
verified: true
validated: true
---

# javac-compile-awesome-script-engine-factory

## Command

```bash
javac src/artsploit/AwesomeScriptEngineFactory.java
```

## Description

Compiles the AwesomeScriptEngineFactory.java source file into bytecode, creating the deserialization gadget class for RCE in SnakeYAML exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src/artsploit/AwesomeScriptEngineFactory.java | Path to Java source file | Yes |

## Examples

### Basic Usage

```bash
javac src/artsploit/AwesomeScriptEngineFactory.java
```

### With Output Directory

```bash
javac -d classes src/artsploit/AwesomeScriptEngineFactory.java
```

## Expected Output

No output if successful; generates src/artsploit/AwesomeScriptEngineFactory.class. Errors if syntax issues or JDK not found.

## Related

- [[procedures/Remote-Code-Execution-via-Spring-Boot-Actuator-Env]]

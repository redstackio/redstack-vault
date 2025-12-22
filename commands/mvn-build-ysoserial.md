---
id: cmd-mvn-build
data: mvn clean package –DskipTests
tags:
  - build
  - maven
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.683Z'
verified: false
validated: true
submitted: true
---
# mvn-build-ysoserial

## Command

```bash
mvn clean package –DskipTests
```

## Description

Cleans previous build artifacts and packages the ysoserial project into a JAR file using Maven, skipping unit tests for faster execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| clean | Cleans previous build artifacts | Yes |
| package | Compiles and packages into JAR | Yes |
| –DskipTests | Skips running tests | Yes |

## Examples

### Basic Usage

```bash
mvn clean package –DskipTests
```

### Advanced Usage

```bash
mvn clean package –DskipTests -Dmaven.test.skip=true
```

## Expected Output

[INFO] BUILD SUCCESS
Build success with JAR file in target/ directory.

## Related

- [[commands/cd-ysoserial]]
- [[commands/cd-target]]

---
id: uuid-c1
data: gradle getDeps
tags:
  - build
  - dependencies
type: command
output: Creates 'runtime/' directory with JAR files like hive-jdbc-1.1.0.jar
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.615Z'
verified: false
validated: true
submitted: true
---
# gradle-getdeps

## Command

```bash
gradle getDeps
```

## Description

Executes a custom Gradle task to download and copy Hive JDBC 1.1.0 and Hadoop 1.1.0 dependencies to a runtime directory for classpath usage in Java clients.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| getDeps | Custom task defined in build.gradle | Yes |

## Examples

### Basic Usage

```bash
gradle getDeps
```

### Advanced Usage

Run in project dir with build.gradle configured for java plugin and dependencies.

## Expected Output

Creates 'runtime/' directory populated with JAR files such as hive-jdbc-1.1.0.jar and hadoop-client-1.1.0.jar.

## Related

- [[Related Procedure: Select-and-Configure-Hive-JDBC-Client]]

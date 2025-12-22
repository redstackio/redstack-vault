---
id: 01541feb-ae78-449f-8ad8-4a662762ba22
type: tool
verified: true
created_at: '2019-08-28T21:17:37.078836+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - java
  - dynamic-analysis
  - instrumentation
  - debugging
  - reverse-engineering
url: 'https://github.com/gkatzen/javasnoop'
validated: true
---

# javasnoop

**Status**: Unverified

## Overview

JavaSnoop is a dynamic instrumentation tool for Java applications, enabling security testers to attach to running JVM processes, intercept method calls, modify variables, inject custom code, and monitor runtime behavior without access to source code. It is particularly useful for analyzing and testing Java clients, applets, or server-side applications in black-box scenarios.

## Description

Testing the security of Java clients without original source code is challenging due to unpredictable decompilation and compilation processes. Traditional approaches like proxying HTTP traffic work only for configurable protocols, but fail for custom, encrypted, or serialized data. JavaSnoop addresses this by acting as a runtime debugger: it attaches to an existing Java process, allowing real-time tampering with method invocations, parameter alteration, and code execution. This facilitates identification of vulnerabilities in communication channels, authentication logic, or data handling in Java-based systems.

## Features

- Attach to local or remote JVM processes via Java Debug Wire Protocol (JDWP)
- Intercept and hook specific methods for monitoring or modification
- Inject custom Java code snippets at runtime
- Visualize call stacks and variable states
- Support for applet and standalone application analysis

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher
- Target application must be running with debugging enabled (e.g., -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005)

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install javasnoop

# Manual installation from source
sudo apt install default-jdk git
mkdir -p /opt/javasnoop
cd /opt/javasnoop
git clone https://github.com/gkatzen/javasnoop.git .
# Build if necessary (check repo for instructions)
```

For Windows/macOS, download the JAR from the repository and run with Java.

## Basic Usage

```bash
java -jar /usr/share/javasnoop/JavaSnoop.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show usage help |
| `--attach <PID>` | Directly attach to a process by PID |
| `-v, --verbose` | Enable verbose logging for debugging |

## Examples

### Example 1: Basic Usage

Launch the GUI and manually select a process:

```bash
java -jar /usr/share/javasnoop/JavaSnoop.jar
```

In the GUI, scan for Java processes, select one, and set hooks on methods like HTTP request handlers.

### Example 2: Advanced Usage

Attach directly to a known PID:

```bash
java -cp /usr/share/javasnoop/JavaSnoop.jar javasnoop.Attach 1234
```

This loads the instrumentation agent and opens the interface for method selection.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Injection]] Process Injection (for runtime code injection into Java processes)
- [[Hijack Execution Flow]] Hijack Execution Flow (by intercepting and altering method calls)

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual JDWP connections on non-standard ports (e.g., monitoring for dt_socket listeners)
- JVM processes with loaded agents showing 'javasnoop' in heap dumps or thread stacks
- Anomalous method invocations or variable modifications logged in application traces
- Increased CPU/memory usage in target JVM due to instrumentation overhead

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/jdb]] (Java Debugger)
- [[tools/Frida]] (Dynamic instrumentation framework)

## References

- Official GitHub Repository: https://github.com/gkatzen/javasnoop
- Kali Tools Documentation: https://www.kali.org/tools/javasnoop
- Java Instrumentation API Docs: https://docs.oracle.com/javase/8/docs/api/java/lang/instrument/package-summary.html

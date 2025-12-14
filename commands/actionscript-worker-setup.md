---
id: c2e3f4g5-h6i7-8902-efgh-567890123456
data: >-
  import flash.system.Worker; import flash.system.WorkerDomain; import
  flash.utils.ByteArray; var byteArray:ByteArray = new ByteArray();
  byteArray.shareable = true; var worker1:Worker =
  WorkerDomain.current.createWorker(); var worker2:Worker =
  WorkerDomain.current.createWorker(); worker1.setSharedProperty("byteArray",
  byteArray); worker2.setSharedProperty("byteArray", byteArray);
  worker1.start(); worker2.start();
tags:
  - setup
  - flash
type: command
output: null
executor: actionscript
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:18.605Z'
verified: false
validated: true
submitted: true
---
# actionscript-worker-setup

## Command

```actionscript
import flash.system.Worker;
import flash.system.WorkerDomain;
import flash.utils.ByteArray;

var byteArray:ByteArray = new ByteArray();
byteArray.shareable = true;
var worker1:Worker = WorkerDomain.current.createWorker();
var worker2:Worker = WorkerDomain.current.createWorker();
worker1.setSharedProperty("byteArray", byteArray);
worker2.setSharedProperty("byteArray", byteArray);
worker1.start();
worker2.start();
```

## Description

ActionScript code to initialize and share a ByteArray between two Flash Worker threads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ByteArray` | Shared data structure | Yes |
| `Worker` | Thread instances | Yes |

## Examples

### Basic Usage

```actionscript
var ba:ByteArray = new ByteArray(); ba.shareable = true;
```

### Advanced Usage

```actionscript
// With message passing
worker1.sendMessage("start");
```

## Expected Output

Workers start and share the ByteArray without errors.

## Related

- [[Related Procedure: Setup-Flash-Worker-Environment]]

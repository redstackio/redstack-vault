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
  - destruct
  - include
  - rce
validated: true
---

# Trigger-Phar-Unserialize-via-Class-Destruct-and-Include

## Code

```php
class AnyClass {
    function __destruct() {
        echo $this->data;
    }
}
// output: rips
include('phar://test.phar');
```

## Description

This code defines a PHP class 'AnyClass' with a __destruct magic method that outputs the 'data' property from the unserialized object. It then includes the Phar file via the phar:// wrapper, triggering unserialization and execution of __destruct. In exploits, this demonstrates how LFI can lead to RCE if the application loads this class before inclusion.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $this->data | Property from serialized metadata (set during Phar creation) | 'rips' or 'system("whoami");' |
| 'test.phar' | Path to the malicious Phar file | 'upload/malicious.phar' |

## Usage

Place this in a vulnerable PHP file or inject via another vuln to define the class. Trigger by including the Phar through an LFI parameter (e.g., vulnerable.php?file=phar://test.phar). Replace echo with malicious code like file_put_contents or system calls for RCE. Requires the Phar to be uploaded and accessible.

## Detection

- Application logs for include statements with phar:// or unserialize errors.
- Runtime analysis for __destruct invocations on user-controlled objects.
- Static code analysis to find classes with dangerous magic methods.
- Network/audit logs showing unexpected output from file inclusions.

## Related

- [[procedures/LFI-RFI-via-phar-Wrapper-with-Serialized-Object]]

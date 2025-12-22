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
  - file-exists
  - unserialize
validated: true
---

# Trigger-Phar-Unserialize-via-File-Exists

## Code

```php
file_exists('phar://test.phar');
```

## Description

This simple PHP code uses the file_exists function on a Phar file via the phar:// wrapper, which triggers unserialization of the file's metadata. If the metadata contains a serialized object with magic methods, they execute during the file operation, enabling RCE in LFI contexts where include is filtered but other file functions are not.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'test.phar' | Path to the malicious Phar file | 'upload/test.phar' |

## Usage

Integrate this into a vulnerable application's code or test via a parameter that calls file_exists internally (e.g., ?check=phar://test.phar). Useful as a bypass when direct includes are blocked. The function returns true if the Phar exists, but the side effect is the unserialization and code execution.

## Detection

- Log all file_exists calls with phar:// in parameters.
- PHP extensions like Phar can be monitored for metadata access.
- Error suppression (@file_exists) may hide issues; enable full logging.
- Behavioral detection: Unexpected code execution during file checks.

## Related

- [[procedures/LFI-RFI-via-phar-Wrapper-with-Serialized-Object]]

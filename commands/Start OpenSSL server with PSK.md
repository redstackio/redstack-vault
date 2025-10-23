---
id: 4567a331-d0d6-453b-81f1-3cd69129cdb2
name: Start OpenSSL server with PSK
type: command
executor: bash
data: export LHOST="*"; export LPORT="4242"; export PSK="replacewithgeneratedpskfromabove";
  openssl s_server -quiet -tls1_2 -cipher PSK-CHACHA20-POLY1305:PSK-AES256-GCM-SHA384:PSK-AES256-CBC-SHA384:PSK-AES128-GCM-SHA256:PSK-AES128-CBC-SHA256
  -psk $PSK -nocert -accept $LHOST:$LPORT
output: null
created_at: '2023-04-06T03:56:24.445000+00:00'
updated_at: '2023-04-10T20:25:34.183750+00:00'
---

# Start OpenSSL server with PSK

```bash
export LHOST="*"; export LPORT="4242"; export PSK="replacewithgeneratedpskfromabove"; openssl s_server -quiet -tls1_2 -cipher PSK-CHACHA20-POLY1305:PSK-AES256-GCM-SHA384:PSK-AES256-CBC-SHA384:PSK-AES128-GCM-SHA256:PSK-AES128-CBC-SHA256 -psk $PSK -nocert -accept $LHOST:$LPORT
```



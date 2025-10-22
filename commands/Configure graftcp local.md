---
id: e31b3217-815a-4ae9-a7b1-69d8f0adc82b
name: Configure graftcp local
type: command
executor: bash
data: '# https://github.com/hmgle/graftcp/blob/master/local/example-graftcp-local.conf

  ## Listen address (default ":2233")

  listen = :2233

  loglevel = 1

  ## SOCKS5 address (default "127.0.0.1:1080")

  socks5 = 127.0.0.1:1080

  # socks5_username = SOCKS5USERNAME

  # socks5_password = SOCKS5PASSWORD

  ## Set the mode for select a proxy (default "auto")

  select_proxy_mode = auto'
output: null
created_at: '2023-04-06T03:56:22.550365+00:00'
updated_at: '2023-04-10T20:25:14.782686+00:00'
---

# Configure graftcp local

```bash
# https://github.com/hmgle/graftcp/blob/master/local/example-graftcp-local.conf
## Listen address (default ":2233")
listen = :2233
loglevel = 1

## SOCKS5 address (default "127.0.0.1:1080")
socks5 = 127.0.0.1:1080
# socks5_username = SOCKS5USERNAME
# socks5_password = SOCKS5PASSWORD

## Set the mode for select a proxy (default "auto")
select_proxy_mode = auto
```

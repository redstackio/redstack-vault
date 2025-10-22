---
id: eb95573f-a11e-4cfc-96d7-c35ea2bfcc3d
name: Start SOCKS server on given port tunneling traffic through specified Beacon
type: command
executor: bash
data: 'beacon > socks [PORT]

  beacon > socks [port]

  beacon > socks [port] [socks4]

  beacon > socks [port] [socks5]

  beacon > socks [port] [socks5] [enableNoAuth|disableNoAuth] [user] [password]

  beacon > socks [port] [socks5] [enableNoAuth|disableNoAuth] [user] [password] [enableLogging|disableLogging]'
output: null
created_at: '2023-04-06T03:56:16.576262+00:00'
updated_at: '2023-04-10T20:36:22.875975+00:00'
---

# Start SOCKS server on given port tunneling traffic through specified Beacon

```bash
beacon > socks [PORT]
beacon > socks [port]
beacon > socks [port] [socks4]
beacon > socks [port] [socks5]
beacon > socks [port] [socks5] [enableNoAuth|disableNoAuth] [user] [password]
beacon > socks [port] [socks5] [enableNoAuth|disableNoAuth] [user] [password] [enableLogging|disableLogging]
```

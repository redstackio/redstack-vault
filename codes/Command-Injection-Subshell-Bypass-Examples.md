---
type: code
language: bash
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - command-injection
  - filter-bypass
  - subshell
validated: true
---

# Command-Injection-Subshell-Bypass-Examples

## Code

```bash
who$()ami
who$(echo am)i
who`echo am`i
```

## Description

This code snippet provides example payloads for bypassing command injection filters using subshell syntax ($() for bash command substitution) and backticks (legacy substitution). These patterns demonstrate how to split and inject into existing commands, such as turning 'whoami' into 'who am i' while embedding executable content. They are useful for evading filters that block spaces, semicolons, or direct command separators in vulnerable applications.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static injection strings; customize the embedded command (e.g., replace 'echo am' with 'whoami' or 'id') based on the target. | N/A |

## Usage

Inject these patterns into vulnerable user inputs, such as a web form field that executes shell commands (e.g., a 'ping' input: '127.0.0.1$(whoami)'). Test in contexts where the application runs the input via system() or similar. Start with simple empty subshells ($()) to confirm parsing, then escalate to full commands. Used in procedures like [[procedures/Command-Injection-with-Subshell-Filter-Bypass]] for filter evasion during exploitation.

## Detection

- Scan application logs and WAF rules for $(), `, or unusual command nesting.
- Monitor process arguments via tools like ps or auditd for embedded subshells in executed commands.
- Behavioral detection: Anomalous outputs combining legitimate and injected command results (e.g., ping data mixed with 'whoami').

## Related

- [[procedures/Command-Injection-with-Subshell-Filter-Bypass]]

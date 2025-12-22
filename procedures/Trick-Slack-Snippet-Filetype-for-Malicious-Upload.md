---
tags:
  - slack
  - rce
  - file-upload
  - unrestricted-upload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Desktop
techniques:
  - '[[Malicious File]]'
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 714a8d48-465c-4a26-93dd-117cd34d59e3
created_at: '2025-12-14T17:24:08.199Z'
updated_at: '2025-12-14T17:24:08.199Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
  - '[[Remote File Copy]]'
---
# Trick-Slack-Snippet-Filetype-for-Malicious-Upload

## Summary

This procedure exploits a flaw in Slack's Create Snippet feature where filetypes are displayed incorrectly, allowing attackers to upload malicious executables disguised as benign files (e.g., CSV), tricking users into downloading and executing them, resulting in remote code execution on the victim's machine.

## Description

The attack targets Slack's snippet creation process, which is intended for sharing code or text but can be manipulated to handle file uploads. By selecting an inappropriate syntax highlighting (e.g., CSV) and using misleading filenames or content embedding, the UI incorrectly presents dangerous files as safe. Victims, believing the file to be harmless, download and run it, enabling RCE. This occurs in Slack workspaces on web or desktop platforms, requiring only standard user access. The root cause is insufficient validation of actual file content against displayed type, leading to unrestricted upload of dangerous types.

## Requirements

1. Active Slack account with permission to create and share snippets in the target workspace
2. Prepared malicious executable file (e.g., .exe with payload for RCE)
3. Target victim who is a workspace member and likely to interact with shared content
4. Standard internet access for Slack connectivity

## Defense

Defensive measures and detection strategies:

- Enforce server-side validation of file content and extensions before allowing snippet creation or sharing
- Implement UI warnings for file downloads, prompting users to verify types via external tools
- Deploy endpoint detection and response (EDR) tools to scan and block execution of unexpected downloads from collaboration apps like Slack
- Conduct user training on recognizing disguised files and avoiding execution of unverified attachments

## Objectives

1. Upload a malicious file via Slack snippet without triggering type restrictions
2. Misrepresent the file's type to deceive the victim into safe assumption
3. Induce victim to download and execute the file, achieving RCE

## Instructions

### Step 1: Prepare the Malicious Payload

**Context**: Create or obtain an executable file containing the RCE payload, and prepare it for disguise.

Prepare a malicious .exe file (e.g., using a tool like msfvenom for a reverse shell). Rename it to end with a benign extension like "data.csv" or embed its binary content into a text format that can be pasted into the snippet editor. Ensure the payload executes upon download and run.

### Step 2: Initiate Snippet Creation in Slack

**Context**: Use Slack's interface to create a snippet, manipulating the type display.

Log into Slack (web or desktop app). Click the "+" in a channel or DM to create a message, then select "Create Snippet." In the editor, choose a syntax highlighter like "CSV" or "Plain Text" from the language dropdown, regardless of the actual content. Paste the executable's content (as hex or base64 if needed) or upload the file via any supported method in the snippet tool. Set the title to something innocuous like "Sample Data CSV."

### Step 3: Share the Snippet and Monitor Victim Interaction

**Context**: Distribute the disguised snippet to the target and observe execution.

Save the snippet and post it in a relevant channel or send via DM to the victim. The UI will display it as a CSV file due to the selected type. Encourage interaction (e.g., "Check this data export"). Monitor for download (via workspace logs if admin) and subsequent execution indicators like callback from the payload.

**Expected Output**: Snippet shares successfully, displays as CSV in Slack preview, and victim downloads the file, which saves as .csv but contains executable content that runs when opened.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Malicious File]]
- [[Remote File Copy]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[slack]]
- [[rce]]
- [[file-upload]]

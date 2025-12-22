---
data: >-
  /usr/bin/perl -w /opt/gitlab/embedded/bin/exiftool -all= --IPTC:all
  --XMP-iptcExt:all -tagsFromFile @ -ResolutionUnit -XResolution -YResolution
  -YCbCrSubSampling -YCbCrPositioning -BitsPerSample -ImageHeight -ImageWidth
  -ImageSize -Copyright -CopyrightNotice -Orientation -
tags:
  - metadata-processing
type: command
executor: bash
platforms:
  - Linux
id: 00e4fc64-cbf2-456f-bdd8-72ad69dba8b9
created_at: '2025-12-11T03:47:57.672Z'
updated_at: '2025-12-11T03:47:57.672Z'
verified: false
validated: true
submitted: true
---
# exiftool-process-image

## Command

```bash
/usr/bin/perl -w /opt/gitlab/embedded/bin/exiftool -all= --IPTC:all --XMP-iptcExt:all -tagsFromFile @ -ResolutionUnit -XResolution -YResolution -YCbCrSubSampling -YCbCrPositioning -BitsPerSample -ImageHeight -ImageWidth -ImageSize -Copyright -CopyrightNotice -Orientation -
```

## Description

Runs ExifTool to remove non-whitelisted metadata tags from images during GitLab upload processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-all=` | Remove all tags | Yes |
| `--IPTC:all` | Exclude all IPTC tags | Yes |
| `-tagsFromFile @` | Copy tags from source | Yes |

## Examples

### Basic Usage

```bash
/usr/bin/perl -w /opt/gitlab/embedded/bin/exiftool -all= --IPTC:all --XMP-iptcExt:all -tagsFromFile @ -ResolutionUnit -XResolution -YResolution -YCbCrSubSampling -YCbCrPositioning -BitsPerSample -ImageHeight -ImageWidth -ImageSize -Copyright -CopyrightNotice -Orientation -
```

## Expected Output

Processed file with metadata removed.

## Related

- [[procedures/Upload-Image-to-Trigger-ExifTool-RCE]]
- [[tools/ExifTool]]

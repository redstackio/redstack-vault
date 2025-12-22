---
type: command
executor: web
data: Click the 'Play' button on the video service interface for the processed file
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - exploits
  - playback
verified: true
validated: true
---

# Play Processed Video on Website

## Command

Manual web action: Access the processed video page on the website and click the play button to initiate streaming.

## Description

Plays the MP4 output from the server-side processing, which reloads the embedded malicious HLS playlist. This causes the server (or client player) to stream the target file contents, enabling exfiltration or viewing by the attacker.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Video URL | URL of the processed video on the site | Yes |
| Player Interface | The website's media player element | Yes |

## Examples

### Basic Usage

Navigate to https://example-videoservice.com/view/job123 and click Play.

### Advanced Usage

Use dev tools to intercept the HLS stream: Open Network tab, play, and capture .ts segments.

## Expected Output

The player starts streaming; instead of video, the target file contents appear in the stream data (e.g., text overlay or downloadable segments). Capture with Wireshark or browser tools for raw data.

## Related

- [[procedures/Exploit-FFmpeg-HLS-Vulnerability-via-Malicious-AVI-for-Arbitrary-File-Read]]

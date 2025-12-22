---
id: cmd-render-components-001
data: >-
  render(){ return ( <div className="App"> <input placeholder="Place your link
  here" type="text" onChange={this.changeState}/> <AutolinkerWrapper
  text={this.state.text}/> </div> ) }
tags:
  - render
  - react
type: command
output: JSX rendered to DOM.
executor: javascript
platforms:
  - Web
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.621Z'
verified: false
validated: true
submitted: true
---
# render-app-components

## Command

```javascript
render(){
  return (
    <div className="App">
      <input placeholder="Place your link here" type="text" onChange={this.changeState}/>
      <AutolinkerWrapper text={this.state.text}/>
    </div>
  )
}
```

## Description

Defines the render method to output input and AutolinkerWrapper based on state.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| this.state.text | Current text state | Yes |

## Examples

### Basic Usage

```javascript
render(){ /* as above */ }
```

## Expected Output

UI with input field and linked text display.

## Related

- [[commands/initialize-app-state]]

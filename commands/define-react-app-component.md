---
id: cmd-define-app-001
data: >-
  class App extends React.Component { constructor(){ super() this.state = {text:
  "fudge"} this.changeState = this.changeState.bind(this) } changeState(event){
  this.setState({text: event.target.value}) } render(){ return ( <div
  className="App"> <input placeholder="Place your link here" type="text"
  onChange={this.changeState}/> <AutolinkerWrapper text={this.state.text}/>
  </div> ) } } export default App;
tags:
  - react
  - component
type: command
output: Component defined and exported; ready for rendering in React app.
executor: javascript
platforms:
  - Web
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.623Z'
verified: false
validated: true
submitted: true
---
# define-react-app-component

## Command

```javascript
class App extends React.Component {
  constructor(){
    super()
    this.state = {text: "fudge"}
    this.changeState = this.changeState.bind(this)
  }

  changeState(event){
    this.setState({text: event.target.value})
  }

  render(){
    return (
      <div className="App">
        <input placeholder="Place your link here" type="text" onChange={this.changeState}/>
        <AutolinkerWrapper text={this.state.text}/>
      </div>
    )
  }
}

export default App;
```

## Description

Defines a complete React class component App that manages state for text input and renders an input field with the vulnerable AutolinkerWrapper.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Component definition body | Yes |

## Examples

### Basic Usage

```javascript
class App extends React.Component { /* full definition */ } export default App;
```

### Advanced Usage

Integrate into index.js:

```javascript
import App from './App';
ReactDOM.render(<App />, document.getElementById('root'));
```

## Expected Output

Component renders an input and wrapper; state updates on input.

## Related

- [[commands/import-react-and-autolinkerwrapper]]

import React from 'react';

import * as fs from 'fs'

import logo from './logo.svg';
import './App.css';

function App() {

  const fs = require('fs')

  const dir = 'C:/Users/jeffrey.moody/Documents/GitHub/etb/src/reactsrc/etb-ui/src'

  const files = fs.readdirSync(dir)


  for (const file of files) {
    console.log(file)
  }  

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

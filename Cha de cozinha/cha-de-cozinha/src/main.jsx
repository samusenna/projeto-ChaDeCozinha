import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './components/ui/App.css'
import App from './components/ui/App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
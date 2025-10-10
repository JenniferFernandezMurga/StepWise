import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { ShoeProvider } from './context/ShoeStore'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import LoginSingup from './pages/LoginSignup'
// import RecommendationForm from './pages/RecommendationForm'  // ← Nuevo nombre
// import About from './pages/About'
import './styles/App.css'

function App() {
  return (
    <ShoeProvider>
      <BrowserRouter>
        <div className="App">
          <Navbar />
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
              {/* <Route path="/recommend" element={<RecommendationForm />} />  ← Formulario
              <Route path="/shoe/:id" element={<ShoeDetail />} />
              <Route path="/about" element={<About />} /> */}
                <Route path="/login" element={<LoginSingup />} />

            </Routes>
          </main>
        </div>
      </BrowserRouter>
    </ShoeProvider>
  )
}

export default App
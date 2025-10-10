// import React from "react" 
// import { Link } from "react-router-dom"

// const Navbar = () => {
//     return(

// <nav className="navbar navbar-expand-lg navbar-light bg-light">
//   <div className="container-fluid">
//   <Link to="/" className="nav-logo">🏃 StepWise</Link>
//     <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
//       <span className="navbar-toggler-icon"></span>
//     </button>
//     <div className="collapse navbar-collapse" id="navbarSupportedContent">
//       <form className="d-flex">
//         <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
//         <button className="btn btn-outline-success" type="submit">Search</button>
//       </form>
//       <ul className="navbar-nav me-auto mb-2 mb-lg-0">
//         <li className="nav-item">
//           <a className="nav-link active" aria-current="page" href="#">Home</a>
//         </li>
//         <li className="nav-item">
//           <a className="nav-link" href="#">Link</a>
//         </li>
//         <li className="nav-item dropdown">
//           <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
//             Dropdown
//           </a>
//           <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
//             <li><a className="dropdown-item" href="#">Action</a></li>
//             <li><a className="dropdown-item" href="#">Another action</a></li>
//             <li><hr className="dropdown-divider"/></li>
//             <li><a className="dropdown-item" href="#">Something else here</a></li>
//           </ul>
//         </li>
//       </ul>
     
//     </div>
//   </div>
// </nav> 
//     )
// }

// export default Navbar

import React from "react" 
import { Link } from "react-router-dom"

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                
                {/* IZQUIERDA: Logo que lleva al Home */}
                <Link to="/" className="navbar-brand">
                <img 
                    src="/images/logoStepWise.png" 
                    alt="StepWise Logo" 
                    style={{ 
                        height: "10px",  // ← Reducir de 60px a 40px
                        border: "3px solid #000", 
                        borderRadius: "10px", 
                        padding: "2px"   // ← Reducir padding también
                    }} 
                />
            </Link>
                
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent">
                    <span className="navbar-toggler-icon"></span>
                </button>
                
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    
                    {/* CENTRO: Buscador */}
                    <form className="d-flex mx-auto">
                        <input 
                            className="form-control me-2" 
                            type="search" 
                            placeholder="Buscar zapatillas..." 
                            aria-label="Search"
                        />
                        <button className="btn btn-outline-primary" type="submit">
                            🔍
                        </button>
                    </form>
                    
                    {/* DERECHA: Navegación + Login */}
                    <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <Link to="/" className="nav-link">Inicio</Link>
                        </li>
                        <li className="nav-item">
                            <Link to="/recommend" className="nav-link">Encuentra tu zapatilla</Link>
                        </li>
                        <li className="nav-item">
                            <Link to="/about" className="nav-link">Cómo funciona</Link>
                        </li>
                        
                        {/* Login/Registro */}
                        <li className="nav-item">
                            <Link to="/loginSignup" className="btn btn-primary ms-2">Accede</Link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}

export default Navbar
// src/pages/ProductDetail.jsx
import React, { useState, useEffect } from "react"
import { useParams, Link } from "react-router-dom"

const ProductDetail = () => {
    const { id } = useParams()
    const [shoe, setShoe] = useState(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => {
        const fetchShoe = async () => {
            try {
                setLoading(true)
                setError(null)
                
                console.log("🔄 Buscando producto ID:", id)
                
                // ✅ URL CORRECTA - usa la misma estructura que tu search
                const response = await fetch(`http://localhost:5000/api/shoes/${id}`)
                
                console.log("📡 Response status:", response.status)
                
                if (!response.ok) {
                    throw new Error(`Error HTTP: ${response.status}`)
                }
                
                const data = await response.json()
                console.log("📦 Datos recibidos:", data)
                
                if (data.success) {
                    setShoe(data.shoe)
                
                } else {
                    throw new Error(data.error || 'Producto no encontrado')
                }
                
            } catch (error) {
                console.error("❌ Error cargando producto:", error)
                setError(`No se pudo cargar el producto: ${error.message}`)
            } finally {
                setLoading(false)
            }
        }

        if (id) {
            fetchShoe()
        }
    }, [id])

    if (loading) {
        return (
            <div className="container mt-4">
                <div className="text-center py-5">
                    <div className="spinner-border" role="status">
                        <span className="visually-hidden">Cargando...</span>
                    </div>
                    <p className="mt-2">Cargando producto...</p>
                </div>
            </div>
        )
    }

    if (error || !shoe) {
        return (
            <div className="container mt-4">
                <div className="alert alert-danger">
                    <h4>Error</h4>
                    <p>{error || "El producto que buscas no existe."}</p>
                    <p className="small text-muted">ID: {id}</p>
                    <Link to="/" className="btn btn-primary">Volver al inicio</Link>
                </div>
            </div>
        )
    }

    // Función para traducir valores
    const traducirValor = (valor) => {
        const traducciones = {
            "high": "alto", "medium": "medio", "low": "bajo",
            "maximum": "máxima", "minimal": "mínima", "standard": "estándar",
            "long": "larga", "short": "corta", "neutral": "neutral",
            "narrow": "estrecho", "road_running": "running en carretera",
            "gym": "gimnasio", "training": "entrenamiento", "marathon": "maratón",
            "light": "ligero", "heavy": "pesado"
        }
        return traducciones[valor] || valor
    }

    return (
        <div className="container mt-4">
            {/* Migas de pan */}
            <nav aria-label="breadcrumb">
                <ol className="breadcrumb">
                    <li className="breadcrumb-item"><Link to="/">Inicio</Link></li>
                    <li className="breadcrumb-item"><Link to="/search">Productos</Link></li>
                    <li className="breadcrumb-item active">{shoe.brand} {shoe.model}</li>
                </ol>
            </nav>

            <div className="row">
                {/* Imagen */}
                <div className="col-md-6">
                    <img 
                        src={shoe.image_url} 
                        alt={`${shoe.brand} ${shoe.model}`}
                        className="img-fluid rounded shadow"
                        style={{ maxHeight: "500px", objectFit: "contain", width: "100%" }}
                    />
                </div>

                {/* Información */}
                <div className="col-md-6">
                    <h1 className="h2">{shoe.brand} {shoe.model}</h1>
                    <span className="badge bg-secondary">{shoe.category}</span>
                    
                    <div className="my-4">
                        <h3 className="text-primary">{shoe.price}€</h3>
                        {shoe.affiliate_link && shoe.affiliate_link !== "#" && (
                            <a 
                                href={shoe.affiliate_link} 
                                target="_blank" 
                                rel="noopener noreferrer"
                                className="btn btn-success btn-lg mt-2"
                            >
                                🛒 Comprar ahora
                            </a>
                        )}
                    </div>

                    {/* Especificaciones */}
                    <div className="card">
                        <div className="card-header bg-light">
                            <h5 className="mb-0">📋 Especificaciones técnicas</h5>
                        </div>
                        <div className="card-body">
                            <div className="row">
                                <div className="col-md-6 mb-3">
                                    <strong>🏃 Actividad:</strong><br/>
                                    <span className="text-muted">{traducirValor(shoe.best_for_activity)}</span>
                                </div>
                                <div className="col-md-6 mb-3">
                                    <strong>📏 Distancia:</strong><br/>
                                    <span className="text-muted">{traducirValor(shoe.distance_capacity)}</span>
                                </div>
                                <div className="col-md-6 mb-3">
                                    <strong>🦶 Amortiguación:</strong><br/>
                                    <span className="text-muted">{traducirValor(shoe.cushioning)}</span>
                                </div>
                                <div className="col-md-6 mb-3">
                                    <strong>👣 Tipo de pisada:</strong><br/>
                                    <span className="text-muted">{traducirValor(shoe.footstrike_support)}</span>
                                </div>
                                <div className="col-md-6 mb-3">
                                    <strong>📐 Ancho:</strong><br/>
                                    <span className="text-muted">{traducirValor(shoe.width_fit)}</span>
                                </div>
                                <div className="col-md-6 mb-3">
                                    <strong>⚡ Placa de carbono:</strong><br/>
                                    <span className="text-muted">{shoe.carbon_plate ? "✅ Sí" : "❌ No"}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ProductDetail
// src/pages/RecommendationResults.jsx
import React from "react"
import { useLocation, Link } from "react-router-dom"
import ProductCard from "../components/ProductCard"

const RecommendationResults = () => {
    const location = useLocation()
    const { recommendations = [], userData } = location.state || {}

    if (!recommendations || recommendations.length === 0) {
        return (
            <div className="container mt-4">
                <div className="text-center py-5">
                    <h2>No se encontraron recomendaciones</h2>
                    <p>Intenta ajustar tus criterios de búsqueda.</p>
                    <Link to="/recommend" className="btn btn-primary">
                        Volver al formulario
                    </Link>
                </div>
            </div>
        )
    }

    return (
        <div className="container mt-4">
            {/* Header */}
            <div className="text-center mb-5">
                <h1 className="text-primary">🎯 Tus zapatillas ideales</h1>
                <p className="lead">Basado en tus características y preferencias</p>
            </div>

            {/* Resultados */}
            <div className="row">
                {recommendations.map((product, index) => (
                    <div key={product.id} className="col-lg-6 mb-4">
                        <div className="card h-100 border-0 shadow-sm">
                            <div className="card-body">
                                {/* Badge de posición */}
                                <div className="position-absolute top-0 start-0 m-3">
                                    <span className="badge bg-primary fs-6">#{index + 1}</span>
                                </div>
                                
                                {/* Score de compatibilidad */}
                                <div className="position-absolute top-0 end-0 m-3">
                                    <span className="badge bg-success fs-6">
                                        {product.match_percentage} compatible
                                    </span>
                                </div>

                                {/* Producto */}
                                <div className="mt-4">
                                    <ProductCard product={product} />
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </div>

            {/* Volver */}
            <div className="text-center mt-5">
                <Link to="/recommend" className="btn btn-outline-primary me-3">
                    🔄 Hacer otra recomendación
                </Link>
                <Link to="/" className="btn btn-secondary">
                    🏠 Volver al inicio
                </Link>
            </div>
        </div>
    )
}

export default RecommendationResults
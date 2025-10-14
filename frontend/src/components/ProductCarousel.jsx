// src/components/ProductCarousel.jsx
import React, { useState } from "react"
import ProductCard from "./ProductCard"

const ProductCarousel = ({ products, section }) => {
    const [currentIndex, setCurrentIndex] = useState(0)
    const productsPerView = 4 // Cuántos productos mostrar a la vez

    if (!products || products.length === 0) {
        return (
            <div className="text-center py-4">
                <p className="text-muted">No hay productos disponibles en esta sección</p>
            </div>
        )
    }

    const nextSlide = () => {
        setCurrentIndex(prev => 
            prev + productsPerView >= products.length ? 0 : prev + 1
        )
    }

    const prevSlide = () => {
        setCurrentIndex(prev => 
            prev === 0 ? Math.max(0, products.length - productsPerView) : prev - 1
        )
    }

    const visibleProducts = products.slice(currentIndex, currentIndex + productsPerView)

    return (
        <div className="product-carousel position-relative">
            {/* Controles de navegación */}
            {products.length > productsPerView && (
                <>
                    <button 
                        className="carousel-control prev btn btn-light position-absolute start-0 top-50 translate-middle-y z-3"
                        onClick={prevSlide}
                        style={{ left: '-20px' }}
                    >
                        ‹
                    </button>
                    <button 
                        className="carousel-control next btn btn-light position-absolute end-0 top-50 translate-middle-y z-3"
                        onClick={nextSlide}
                        style={{ right: '-20px' }}
                    >
                        ›
                    </button>
                </>
            )}

            {/* Indicadores */}
            {products.length > productsPerView && (
                <div className="text-center mt-3">
                    {Array.from({ length: Math.ceil(products.length / productsPerView) }).map((_, index) => (
                        <button
                            key={index}
                            className={`btn btn-sm mx-1 ${currentIndex === index * productsPerView ? 'btn-primary' : 'btn-outline-primary'}`}
                            onClick={() => setCurrentIndex(index * productsPerView)}
                        >
                            {index + 1}
                        </button>
                    ))}
                </div>
            )}

            {/* Grid de productos */}
            <div className="row g-3">
                {visibleProducts.map(product => (
                    <div key={product.id} className="col-lg-3 col-md-4 col-sm-6">
                        <ProductCard product={product} />
                    </div>
                ))}
            </div>

            {/* Estilos para el carrusel */}
            <style>{`
                .product-carousel {
                    padding: 0 10px;
                }
                .carousel-control {
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
                }
                .carousel-control:hover {
                    background-color: #e9ecef;
                }
                @media (max-width: 768px) {
                    .carousel-control {
                        display: none;
                    }
                }
            `}</style>
        </div>
    )
}

export default ProductCarousel
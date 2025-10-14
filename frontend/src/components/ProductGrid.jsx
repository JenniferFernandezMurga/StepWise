// frontend/src/components/ProductGrid.jsx
import React from "react"
import ProductCard from "./ProductCard"

const ProductGrid = ({ products = [], searchQuery, category }) => {
    return (
        <div className="container mt-4">
            {/* Search results header */}
            {searchQuery && (
                <div className="mb-4">
                    <h2>Results for: "{searchQuery}"</h2>
                    {category && category !== "todo" && (
                        <p className="text-muted">Filter: {category}</p>
                    )}
                    <p>{products.length} shoes found</p>
                </div>
            )}
            
            {/* Products grid */}
            <div className="row">
                {products.map(shoe => (
                    <div key={shoe.id} className="col-lg-4 col-md-6 mb-4">
                        <ProductCard product={shoe} />
                    </div>
                ))}
            </div>
            
            {products.length === 0 && searchQuery && (
                <div className="text-center py-5">
                    <h4>No shoes found</h4>
                    <p>Try with different search terms</p>
                </div>
            )}
        </div>
    )
}

export default ProductGrid
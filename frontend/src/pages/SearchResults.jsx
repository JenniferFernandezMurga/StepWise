import React, { useState, useEffect } from "react"
import { useLocation } from "react-router-dom"
import ProductGrid from "../components/ProductGrid"
import { shoesService } from "../services/api"

const SearchResults = () => {
    const [shoes, setShoes] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const location = useLocation()

    useEffect(() => {
        const searchParams = new URLSearchParams(location.search)
        const query = searchParams.get('q')
        const category = searchParams.get('category')

        performSearch(query, category)
    }, [location])

    const performSearch = async (query, category) => {
        setLoading(true)
        setError(null)
        
        try {
            console.log("🔄 Searching:", { query, category })
            
            const data = await shoesService.search(query || '', category || 'todo')
            
            console.log("📦 Results received:", data)
            
            setShoes(data.shoes || [])
            
        } catch (error) {
            console.error("❌ Search error:", error)
            setError("Could not load results. Check your connection.")
            setShoes([])
        } finally {
            setLoading(false)
        }
    }

    const searchParams = new URLSearchParams(location.search)
    const query = searchParams.get('q')
    const category = searchParams.get('category')

    if (loading) {
        return (
            <div className="container mt-4">
                <div className="text-center py-5">
                    <div className="spinner-border text-primary" role="status">
                        <span className="visually-hidden">Loading...</span>
                    </div>
                    <p className="mt-2">Searching shoes...</p>
                </div>
            </div>
        )
    }

    if (error) {
        return (
            <div className="container mt-4">
                <div className="alert alert-danger text-center">
                    <h5>Error</h5>
                    <p>{error}</p>
                    <button 
                        className="btn btn-primary" 
                        onClick={() => performSearch(query, category)}
                    >
                        Try Again
                    </button>
                </div>
            </div>
        )
    }

    return (
        <ProductGrid 
            products={shoes}
            searchQuery={query}
            category={category}
        />
    )
}

export default SearchResults
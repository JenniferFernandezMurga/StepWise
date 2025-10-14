// frontend/src/services/api.js
import { API_ENDPOINTS } from '../config/api'

export const shoesService = {
    search: async (query, category = 'todo') => {
        const url = `${API_ENDPOINTS.SEARCH}?q=${encodeURIComponent(query)}&category=${encodeURIComponent(category)}`
        
        console.log('🔍 Searching at:', url)
        
        const response = await fetch(url)
        
        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`)
        }
        
        const data = await response.json()
        
        if (!data.success) {
            throw new Error(data.error || 'Search error')
        }
        
        return data
    },

    getAll: async () => {
        const response = await fetch(API_ENDPOINTS.SHOES)
        
        if (!response.ok) {
            throw new Error('Error loading shoes')
        }
        
        const data = await response.json()
        return data
    }
}
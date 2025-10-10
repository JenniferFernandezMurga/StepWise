import React from 'react'
import HeroSection from '../components/HeroSection'
// import ProductGrid from '../components/ProductGrid'
// import ProductCarousel from '../components/ProductCarousel'
// import BrandShowcase from '../components/BrandShowcase'
// import HowItWorks from '../components/HowItWorks'

const Home = () => {
  return (
    <div className="home-page">
      {/* Sección Hero - Llamada a acción */}
      <HeroSection />
      
      {/* Sección Top Trail Running
      <section className="section">
        <ProductGrid 
          title="Top Trail Running"
          category="trail_running"
          limit={6}
        />
      </section>
      
      {/* Sección Más Vendidos */}
      {/* <section className="section bg-light">
        <ProductCarousel 
          title="Los Más Vendidos"
        />
      </section>
      
      {/* Sección Marcas */}
      {/* <section className="section">
        <BrandShowcase />
      </section>
      
      {/* Sección Cómo funciona */}
      {/* <section className="section bg-light">
        <HowItWorks />
      </section> */} 
    </div>
  )
}

export default Home
import React, { useState } from "react"
import { useNavigate } from "react-router-dom"

const RecommendationForm = () => {
    const [formData, setFormData] = useState({
        // ✅ NUEVO CAMPO
        gender: "",
        // Campos requeridos existentes
        foot_width: "",
        arch_type: "",
        weight: "",  // Se enviará como número
        activity_type: "",
        // Campos opcionales
        footstrike_type: "",
        target_distance: "",
        running_level: ""
    })
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState("")
    const navigate = useNavigate()

    const handleChange = (e) => {
        const { name, value } = e.target
        setFormData(prev => ({
            ...prev,
            [name]: value
        }))
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        setLoading(true)
        setError("")
        
        try {
            console.log("📤 Datos del formulario (original):", formData)
            
            // ✅ CONVERSIÓN SEGURA EN FRONTEND + NUEVO CAMPO
            const dataToSend = {
                gender: formData.gender,  // ✅ NUEVO
                foot_width: formData.foot_width,
                arch_type: formData.arch_type,
                weight: parseInt(formData.weight) || 70,  // ✅ CONVERTIDO A NÚMERO
                activity_type: formData.activity_type,
                footstrike_type: formData.footstrike_type,
                target_distance: formData.target_distance,
                running_level: formData.running_level
            }
            
            console.log("📤 Datos enviados al backend:", dataToSend)
            
            const response = await fetch('http://localhost:5000/api/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(dataToSend)
            })
            
            console.log("📡 Status de respuesta:", response.status)
            
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`)
            }
            
            const data = await response.json()
            console.log("📦 Respuesta recibida:", data)
            
            if (data.success) {
                navigate('/recommendation-results', { 
                    state: { 
                        recommendations: data.recommendations,
                        userData: formData
                    } 
                })
            } else {
                setError(data.error || "Error en la recomendación")
            }
        } catch (error) {
            console.error("❌ Error en recomendación:", error)
            setError("Error de conexión con el servidor: " + error.message)
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="container mt-4">
            <div className="row justify-content-center">
                <div className="col-lg-8">
                    <div className="card shadow">
                        <div className="card-header bg-primary text-white text-center py-4">
                            <h1 className="h3 mb-2">🎯 Encuentra tu zapatilla perfecta</h1>
                            <p className="mb-0">Responde estas preguntas para una recomendación personalizada</p>
                        </div>
                        
                        <div className="card-body p-4">
                            {error && (
                                <div className="alert alert-danger" role="alert">
                                    {error}
                                </div>
                            )}

                            <form onSubmit={handleSubmit}>
                                {/* ✅ NUEVO: Campo Género */}
                                <div className="mb-4">
                                    <label className="form-label h5">🚻 Género</label>
                                    <small className="text-muted d-block mb-2">Para ajustar mejor las recomendaciones</small>
                                    <select 
                                        name="gender"
                                        className="form-select form-select-lg"
                                        value={formData.gender}
                                        onChange={handleChange}
                                        required
                                    >
                                        <option value="">Selecciona tu género</option>
                                        <option value="female">Mujer</option>
                                        <option value="male">Hombre</option>
                                        <option value="other">Otro / Prefiero no decir</option>
                                    </select>
                                </div>

                                {/* Ancho del pie */}
                                <div className="mb-4">
                                    <label className="form-label h5">👟 Ancho de tu pie</label>
                                    <select 
                                        name="foot_width"
                                        className="form-select form-select-lg"
                                        value={formData.foot_width}
                                        onChange={handleChange}
                                        required
                                    >
                                        <option value="">Selecciona el ancho de tu pie</option>
                                        <option value="narrow">Estrecho</option>
                                        <option value="standard">Normal</option>
                                        <option value="wide">Ancho</option>
                                    </select>
                                </div>

                                {/* Tipo de arco */}
                                <div className="mb-4">
                                    <label className="form-label h5">🦶 Tipo de arco del pie</label>
                                    <select 
                                        name="arch_type"
                                        className="form-select form-select-lg"
                                        value={formData.arch_type}
                                        onChange={handleChange}
                                        required
                                    >
                                        <option value="">Selecciona tu tipo de arco</option>
                                        <option value="low">Arco bajo (pie plano)</option>
                                        <option value="neutral">Arco normal</option>
                                        <option value="high">Arco alto</option>
                                    </select>
                                </div>

                                {/* Peso corporal - ✅ VALORES NUMÉRICOS */}
                                <div className="mb-4">
                                    <label className="form-label h5">⚖️ Tu peso corporal</label>
                                    <select 
                                        name="weight"
                                        className="form-select form-select-lg"
                                        value={formData.weight}
                                        onChange={handleChange}
                                        required
                                    >
                                        <option value="">Selecciona tu peso</option>
                                        <option value="60">Menos de 70kg (Ligero)</option>
                                        <option value="80">70-90kg (Medio)</option>
                                        <option value="95">Más de 90kg (Pesado)</option>
                                    </select>
                                </div>

                                {/* Tipo de actividad - REQUERIDO */}
                                <div className="mb-4">
                                    <label className="form-label h5">🏃 Actividad principal</label>
                                    <small className="text-muted d-block mb-2">¿Para qué usarás principalmente las zapatillas?</small>
                                    <select 
                                        name="activity_type"
                                        className="form-select form-select-lg"
                                        value={formData.activity_type}
                                        onChange={handleChange}
                                        required
                                    >
                                        <option value="">Selecciona tu actividad</option>
                                        <option value="road_running">Running en carretera</option>
                                        <option value="trail_running">Trail running</option>
                                        <option value="gym">Gimnasio / CrossTraining</option>
                                        <option value="walking">Caminar</option>
                                    </select>
                                </div>

                                {/* Tipo de pisada - OPCIONAL pero recomendado */}
                                <div className="mb-4">
                                    <label className="form-label h5">👣 Tipo de pisada</label>
                                    <small className="text-muted d-block mb-2">
                                        ¿Sabes cómo pisas al correr? 
                                        <span className="text-muted"> (Si no sabes, déjalo en blanco)</span>
                                    </small>
                                    <select 
                                        name="footstrike_type"
                                        className="form-select form-select-lg"
                                        value={formData.footstrike_type}
                                        onChange={handleChange}
                                    >
                                        <option value="">No estoy seguro / Neutral</option>
                                        <option value="over_pronation">Pronación (pie hacia dentro)</option>
                                        <option value="under_pronation">Supinación (pie hacia fuera)</option>
                                        <option value="neutral">Neutra</option>
                                    </select>
                                </div>

                                {/* Distancia objetivo - OPCIONAL */}
                                <div className="mb-4">
                                    <label className="form-label h5">📏 Distancia objetivo</label>
                                    <small className="text-muted d-block mb-2">¿Qué distancia sueles recorrer?</small>
                                    <select 
                                        name="target_distance"
                                        className="form-select form-select-lg"
                                        value={formData.target_distance}
                                        onChange={handleChange}
                                    >
                                        <option value="training">Entrenamiento general</option>
                                        <option value="5k">5K</option>
                                        <option value="10k">10K</option>
                                        <option value="half_marathon">Media maratón (21K)</option>
                                        <option value="marathon">Maratón (42K)</option>
                                    </select>
                                </div>

                                {/* Nivel de running - OPCIONAL */}
                                <div className="mb-4">
                                    <label className="form-label h5">🚀 Nivel de experiencia</label>
                                    <small className="text-muted d-block mb-2">¿Cómo te consideras como corredor?</small>
                                    <select 
                                        name="running_level"
                                        className="form-select form-select-lg"
                                        value={formData.running_level}
                                        onChange={handleChange}
                                    >
                                        <option value="beginner">Principiante</option>
                                        <option value="intermediate">Intermedio</option>
                                        <option value="advanced">Avanzado</option>
                                        <option value="competitive">Competitivo</option>
                                    </select>
                                </div>

                                {/* Botón de envío */}
                                <div className="text-center mt-5">
                                    <button 
                                        type="submit" 
                                        className="btn btn-primary btn-lg px-5 py-3"
                                        disabled={loading}
                                        style={{ fontSize: '1.2rem' }}
                                    >
                                        {loading ? (
                                            <>
                                                <span className="spinner-border spinner-border-sm me-2" role="status"></span>
                                                Analizando tus respuestas...
                                            </>
                                        ) : (
                                            "🎯 Encontrar mis zapatillas ideales"
                                        )}
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default RecommendationForm
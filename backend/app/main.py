"""
FastAPI Application Entry Point
This is where everything starts!
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.config import settings

# Create FastAPI application instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="P2P Rental Platform API for Lagos and Abuja",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS Middleware (allows frontend to call backend from different domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Root endpoint - health check
    Returns basic API information
    """
    return {
        "message": "Welcome to Lagos-Abuja Rentals API",
        "version": settings.VERSION,
        "status": "operational",
        "docs": f"{settings.API_V1_STR}/docs"
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    Used by load balancers and monitoring systems
    """
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME
    }


@app.get(f"{settings.API_V1_STR}/properties")
async def list_properties():
    """
    List all properties (mock data for now)
    We'll connect to database in next lesson
    """
    # Mock data - we'll replace with real database queries
    mock_properties = [
        {
            "id": 1,
            "title": "3 Bedroom Flat in Lekki",
            "location": "Lekki Phase 1, Lagos",
            "price": 1500000,
            "bedrooms": 3,
            "bathrooms": 2,
            "description": "Modern apartment with 24/7 security"
        },
        {
            "id": 2,
            "title": "2 Bedroom Apartment in Abuja",
            "location": "Wuse 2, Abuja",
            "price": 1200000,
            "bedrooms": 2,
            "bathrooms": 2,
            "description": "Serviced apartment in prime location"
        }
    ]
    
    return {
        "total": len(mock_properties),
        "properties": mock_properties
    }

"""Script to list all FastAPI routes in the application."""
import sys
import os

# Add the kyber-vpn-backend directory to Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(script_dir, "kyber-vpn-backend")
sys.path.insert(0, backend_dir)

try:
    from app.main import app
    
    print("\n=== API ROUTES ===\n")
    
    # Print all direct routes
    for route in app.routes:
        if not hasattr(route, "routes"):  # Skip router objects
            methods = ", ".join(route.methods) if hasattr(route, "methods") and route.methods else "N/A"
            print(f"{route.path} [{methods}]")
    
    print("\n=== INCLUDED ROUTER ENDPOINTS ===\n")
    
    # Find routers in app.routes first
    routers = [r for r in app.routes if hasattr(r, "routes")]
    
    # Print router endpoints
    for router in routers:
        prefix = router.prefix
        print(f"\nRouter with prefix '{prefix}':")
        for route in router.routes:
            methods = ", ".join(route.methods) if hasattr(route, "methods") and route.methods else "N/A"
            full_path = f"{prefix}{route.path}"
            print(f"  {full_path} [{methods}]")

except ImportError as e:
    print(f"Error: {e}")
    print(f"\nCurrent working directory: {os.getcwd()}")
    print(f"Script directory: {script_dir}")
    print(f"Backend directory: {backend_dir}")
    print(f"Python path: {sys.path}")
    print("\nPlease make sure the kyber-vpn-backend directory exists and contains the app module.")
    
    # List directory contents to help diagnose the issue
    print("\nContents of script directory:")
    for item in os.listdir(script_dir):
        print(f"  {item}")
    
    if os.path.exists(backend_dir):
        print(f"\nContents of backend directory:")
        for item in os.listdir(backend_dir):
            print(f"  {item}")
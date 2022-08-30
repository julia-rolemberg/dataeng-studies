import os
from src.app import create_app  


try:
    print("INITIALIZING APP")
    app = create_app(os.getenv('ENV') or 'DEV') 
except Exception as exc:
    # Intercept exception to record it and re-raise it
    print(f"ERROR INITIALIZING APP: {exc}")
    raise exc

import os
from d2draftnet_app import create_app

app = create_app()

if __name__ == "__main__":
    # Get the port from the environment (Render assigns this dynamically)
    port = int(os.getenv("PORT", 10000))  # Default to 10000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=False)

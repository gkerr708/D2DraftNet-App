import os
from d2draftnet_app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Render assigns a dynamic port
    app.run(host="0.0.0.0", port=port, debug=True)

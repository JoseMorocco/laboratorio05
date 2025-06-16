import os

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Agrega esto al inicio
    # ...otros middlewares...
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
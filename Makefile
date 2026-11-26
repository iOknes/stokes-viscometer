all:
    uv add . --dev
    pip install . --break-system-packages
    pipx install . --force

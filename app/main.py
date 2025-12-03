from fastapi import FastAPI
from app.routers import auth, lines, settings, events

app = FastAPI(title="Delay Certificate API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(lines.router, prefix="/lines", tags=["lines"])
app.include_router(settings.router, prefix="/settings", tags=["settings"])
app.include_router(events.router, prefix="/events", tags=["events"])
app.include_router(events.router, prefix="/certificates", tags=["certificates"])
app.include_router(events.router, prefix="/verify", tags=["verify"])

@app.get("/health")
def health():
    return {"ok": True}
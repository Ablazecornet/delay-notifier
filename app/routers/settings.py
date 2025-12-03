from fastapi import APIRouter

router = APIRouter()

@router.get("/v1/commute-profiles")
async def get_commute_profiles():
    pass

@router.post("/v1/commute-profiles/")
async def create_commute_profile():
    pass

@router.delete("/v1/commute-profiles/{profile_id}")
async def delete_commute_profile(profile_id: int):
    pass
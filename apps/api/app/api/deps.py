from typing import Annotated

from fastapi import Depends, HTTPException, status


def get_current_user_id() -> str:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Google OAuth is implemented in Module 2.",
    )


CurrentUserId = Annotated[str, Depends(get_current_user_id)]

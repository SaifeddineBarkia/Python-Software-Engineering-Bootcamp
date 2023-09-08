from pydantic import BaseModel, Field
from typing import List

class User(BaseModel):
    name: str = Field(
        title="The username",
        description="This is the username of the user",
        min_length=1,
        default=None
    )
    liked_posts: List[int] = Field(
        description = "Array of post ids the user liked"
    )

class UserProfileInfo(BaseModel):
    short_description: str
    long_bio: str

class FullUserProfile(User, UserProfileInfo):
    pass

class MultipleUsersResponse(BaseModel):
    users: List[FullUserProfile]
    total: int

class CreateUserResponse(BaseModel):
    user_id: int
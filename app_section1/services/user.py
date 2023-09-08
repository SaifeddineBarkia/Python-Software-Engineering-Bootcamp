from typing import Optional, List
from app.schemas.user import (
    FullUserProfile,
    UserProfileInfo,
    User
)
from app.exceptions import UserNotFound

profile_infos = {
    0:{
        "short_description":"This is short",
        "long_bio": "This longer"
    }
}

users_content = {
    0: {
        "name": "A",
        "liked_posts": [1,2,3],
    }
}

class UserService:

    def __init__(self):
        pass

    async def get_all_users_with_pagination(self, start: int, limit: int) -> (List[FullUserProfile], int):
        list_of_users = []
        keys = list(profile_infos.keys())
        total = len(keys)
        for index in range(start, start+limit, 1):
            if index not in keys:
                continue
            current_key = keys[index]
            user = await self.get_user_info(current_key)
            list_of_users.append(user)

        return list_of_users, total

    @staticmethod
    async def get_user_info( user_id : int = 0) -> FullUserProfile:

        if user_id not in profile_infos:
            raise UserNotFound(user_id=user_id)

        profile_info = profile_infos[user_id]
        user_content = users_content[user_id]

        user = User(**user_content)

        full_user_profile = {
            **profile_info,
            **user.dict()
        }

        return FullUserProfile(**full_user_profile)

    @staticmethod
    async def create_update_user(full_profile_info: FullUserProfile, new_user_id: Optional[int]=None)-> int :
        global profile_infos
        global users_content

        if new_user_id is None:
            new_user_id = len(profile_infos)

        liked_posts = full_profile_info.liked_posts
        short_description = full_profile_info.short_description
        long_bio = full_profile_info.long_bio
        name = full_profile_info.name

        # print("before:")
        # print("users_content:", users_content)
        # print("profile_infos:", profile_infos)

        users_content[new_user_id] = {
            "name": name,
            "liked_posts": liked_posts
            }
        profile_infos[new_user_id] = {
            "short_description": short_description,
            "long_bio": long_bio
        }

        # print("after:")
        # print("users_content:", users_content)
        # print("profile_infos:", profile_infos)

        return new_user_id

    @staticmethod
    async def delete_user (user_id: int) -> None:
        global profile_infos
        global users_content

        if user_id not in profile_infos:
            raise UserNotFound(user_id)

        del profile_infos[user_id]
        del users_content[user_id]

    @staticmethod
    async def update_user_only(full_user_profile: UserProfileInfo, user_id: int) -> FullUserProfile:
        global profile_infos
        global users_content

        short_description = full_user_profile.short_description
        long_bio = full_user_profile.long_bio

        profile_infos[user_id] = {
            "short_description": short_description,
            "long_bio": long_bio
        }

        user_content = users_content[user_id]
        profile_info = profile_infos[user_id]

        user = User(**user_content)

        full_user_profile = {
            **profile_info,
            **user.dict()
        }

        return FullUserProfile(**full_user_profile)

import asyncio
import aiohttp

json_example = {
  "short_description": "string",
  "long_bio": "string",
  "name": "string",
  "liked_posts": [
    0,2,3,4
  ]
}

async def sample_request_async(base_url:str,endpoint_prefix:str ,user_id:int):
    url = base_url + endpoint_prefix + str(user_id)
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json =json_example ) as response :
            # print(response.status) #it is different in this case
            # print(response.headers)
            # print(await response.json())
            return response.status, await response.json()


# for i in range(1000):
#     asyncio.run(sample_request_async(i))
#     print('xxxxxxxxxx',i)
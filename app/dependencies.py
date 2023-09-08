from fastapi import Response, HTTPException
import time


count = 0
limit = 500
start_time = time.time()
reset_interval = 10

def rate_limit(response: Response) -> Response:

    global count
    global start_time

    if time.time() > start_time + reset_interval:
        count = 0
        start_time = time.time()

    if count >= limit:
        raise HTTPException(status_code=429, detail={'error':"You have passed your limit",
                                                     "timeout": round(start_time + reset_interval - time.time(), 2) + 0.01})

    count += 1
    response.headers['X-app-rate-limit'] = f"{count}:{limit}"

    return Response
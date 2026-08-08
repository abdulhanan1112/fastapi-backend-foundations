import time
from typing import Annotated
from fastapi import APIRouter,Query
import asyncio
from app.core.timing import measure_time

router=APIRouter(
    prefix="/experiments",
    tags=['experiments']
)

@router.get('/non_blocking')
async def non_blocking_wait(
    delay: Annotated[
        float,
        Query(ge=0,le=10),

    ] = 2.0
) -> dict[str,object]:
    
    with measure_time("non_blocking"):
        asyncio.sleep(delay)

    return {
        "experiment" : "non_blocking",
        "delay" : delay
    }



@router.get('/threadpool_wait')
def threadpool_wait(
    delay: Annotated[
        float,
        Query(ge=0,le=10),

    ] = 2.0
) -> dict[str,object]:
    
    with measure_time("threadpool_wait"):
        time.sleep(delay)

    return {
        "experiment" : "threadpool_wait",
        "delay" : delay
    }
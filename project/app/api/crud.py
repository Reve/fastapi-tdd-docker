from typing import List, Optional

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id


async def get(id: int) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).first().values()

    if summary:
        return summary[0]

    return None


async def get_all() -> List:
    summamries = await TextSummary.all().values()
    return summamries


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).update(
        url=payload.url, summary=payload.summary
    )

    if summary:
        update_summary = await TextSummary.filter(id=id).first().values()
        return update_summary[0]

    return None

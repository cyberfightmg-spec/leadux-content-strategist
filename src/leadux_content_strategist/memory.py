from __future__ import annotations
import re
from datetime import datetime, timezone

def normalize(text: str) -> set[str]:
    return {t for t in re.findall(r"[\wа-яё]+", (text or "").lower(), flags=re.I) if len(t)>2}

def similarity(a: str, b: str) -> float:
    sa,sb=normalize(a),normalize(b)
    if not sa or not sb: return 0.0
    return len(sa&sb)/len(sa|sb)

def find_near_duplicates(candidate: dict, memory: dict, threshold: float=0.55) -> list[dict]:
    ctext=" ".join(str(candidate.get(k) or "") for k in ("title","topic","angle"))
    out=[]
    for item in memory.get("published_content",[]):
        itext=" ".join(str(item.get(k) or "") for k in ("title","topic","angle"))
        s=similarity(ctext,itext)
        if s>=threshold:
            out.append({"content_id":item.get("content_id"),"similarity":round(s,3),"published_at":item.get("published_at")})
    return sorted(out,key=lambda x:x["similarity"],reverse=True)

def empty_memory(memory_id: str="mem_default") -> dict:
    return {"memory_id":memory_id,"updated_at":datetime.now(timezone.utc).isoformat(),"published_content":[],"performance_patterns":[],"strategy_versions":[]}

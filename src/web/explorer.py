# APIRouter 적용
from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service

router = APIRouter(prefix='/explorer')

@router.get("/")
def get_all() -> list[Explorer]:
    # 탐험가 목록 반환"
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer | None:
    # 검색한 탐험가 반환
    return service.get_one(name)

# 탐험가를 추가, 수정, 교체, 삭제
@router.post("/")
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)

@router.patch("/{name}")
def modify(name, explorer: Explorer) -> Explorer:
    return service.modify(name, explorer)

@router.put("/{name}")
def replace(name, explorer: Explorer) -> Explorer:
    return explorerservice.replace(name, replace)

@router.delete("/{name}")
def delete(name: str):
    return None

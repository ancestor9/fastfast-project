# APIRouter 적용
from fastapi import APIRouter
from model.creature import Creature
import fake.creature as service

router = APIRouter(prefix='/creature')

@router.get("/")
def get_all() -> list[Creature]:
    # 탐험가 목록 반환"
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Creature | None:
    # 검색한 탐험가 반환
    return service.get_one(name)

# 탐험가를 추가, 수정, 교체, 삭제
@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)

@router.patch("/{name}")
def modify(name, creature: Creature) -> Creature:
    return service.modify(name, creature)

@router.put("/{name}")
def replace(name, creature: Creature) -> Creature:
    return service.replace(name, replace)

@router.delete("/{name}")
def delete(name: str):
    return None
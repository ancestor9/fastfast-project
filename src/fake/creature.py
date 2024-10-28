from model.creature import Creature

# 데이터베이스와 SQL로 변경전
_creatures: list[Creature] = [
    Creature(name = "yeti",
             aka = "Abominable Snowman",
             country = 'CN',
             area = "Himalayas",
             description = "Hairsuite Hymalayans"),
    
    Creature(name = "sasquatch",
             description = "Yett's cousin Eddie",
             country = 'US',
             area = "*",
             aka = "Big Foot")
]

def get_all() -> list[Creature]:
    # 생명체 목록 반환
    return _creatures

def get_one(name:str) -> Creature | None :
    # 검색한 생명체를 반환
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

# 탐험가를 추가, 수정, 교체, 삭제
def create(creature: Creature) -> Creature:
    return creature

def modify(name: str, creature: Creature) -> Creature:
    return creature

def replace(name: str, creature: Creature) -> Creature:
    return creature

def delete(name: str) -> bool:
    for _creature in _creatures:
        if _creature.name == name:
            return True
    return False
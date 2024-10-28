from model.explorer import Explorer

# fake data, 실제 DB와 SQL로 대체
_explorers = [
    Explorer(name = "Claude Handle",
             country = "FR",
             description = "Shall we meet at the day of Fulll Moon?"),
    
    Explorer(name = "Noah Weiser",
             country = "DE",
             description = "Weak eyesight woth carring Axes"),
]

def get_all() -> list[Explorer]:
    # 탐험가 목록 반환"
    return _explorers

def get_one(name:str) -> Explorer:
    # 검색한 탐험가 반환
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

# 탐험가를 추가, 수정, 교체, 삭제
def create(explorer: Explorer) -> Explorer:
    return explorer

def modify(name: str, explorer: Explorer) -> Explorer:
    return explorer

def replace(name: str, explorer: Explorer) -> Explorer:
    return explorer

def delete(name: str) -> bool:
    for _explorer in explorers:
        if _explorer.name == name:
            return True
    return False
    
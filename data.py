from model import Creature

creatures: list[Creature] = [
    Creature(name = "yeti",
             country = 'CN',
             area = "Himalayas",
             description = "Hairsuite Hymalayans",
             aka = "Abominable Snowman"
             ),
    Creature(name = "sasquatch",
             country = 'US',
             area = "*",
             description = "Yett's cousin Eddie",
             aka = "Big Foot"
             )  
]

def get_creatures() -> list[Creature]:
    return creatures

if __name__ == '__main__':
    results = get_creatures()

# print(results)
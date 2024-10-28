from pydantic import BaseModel 

class Creature(BaseModel):
    name : str
    country : str
    area : str
    description : str
    aka : str
    
thing = Creature(
    name = "yeti",
    country = 'CN',
    area = "Himalayas",
    description = "Hairsuite Hymalayans",
    aka = "Abominable Snowman"
)

if __name__ == '__main__':
    print("Name is", thing.name)
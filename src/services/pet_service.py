from src.models.pet_model import Pet
from src import db
from src.schemas.pet_schema import PetSchema

class PetService:
    def __init__(self):
        self.schema = PetSchema()
        self.schema_many = PetSchema(many=True)

    def criar_pet(self, data):
        pet = Pet(
            nome=data.get("nome"),
            descricao=data.get("descricao"),
            imagem=data.get("imagem")
        )
        db.session.add(pet)
        db.session.commit()
        return self.schema.dump(pet)

    def listar_pets(self):
        pets = Pet.query.all()
        return self.schema_many.dump(pets)

    def buscar_por_id(self, pet_id):
        pet = Pet.query.get(pet_id)
        if not pet:
            return None
        return self.schema.dump(pet)

    def atualizar_pet(self, pet_id, data):
        pet = Pet.query.get(pet_id)
        if not pet:
            return None
        pet.nome = data.get("nome", pet.nome)
        pet.descricao = data.get("descricao", pet.descricao)
        pet.imagem = data.get("imagem", pet.imagem)
        db.session.commit()
        return self.schema.dump(pet)

    def deletar_pet(self, pet_id):
        pet = Pet.query.get(pet_id)
        if not pet:
            return False
        db.session.delete(pet)
        db.session.commit()
        return True

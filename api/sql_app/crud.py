from sqlalchemy.orm import Session

from . import models, schemas

def get_recetas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Recetas).offset(skip).limit(limit).all()


def get_recetas_id(db: Session, receta_id: int):
    return db.query(models.Recetas).filter(models.Recetas.id == receta_id).first()


def get_receta_por_nombre(db: Session, nombre: str):
    return db.query(models.Recetas).filter(models.Recetas.nombre == nombre).first()


def create_recetas(db: Session, receta: schemas.RecetaCreate):
    db_item = models.Recetas(**receta.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_recetas(db: Session, receta_id: int):
    receta_delete = models.Receta.filter_by(id=receta_id).one()
    db.delete(receta_delete)
    db.commit()
    return receta_delete
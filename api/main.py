from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/recetas/", response_model=list[schemas.Receta])
def get_recetas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retorna una lista de todas las recetas
    """
    recetas = crud.get_recetas(db, skip=skip, limit=limit)
    return recetas


@app.get("/recetas/{receta_id}", response_model=schemas.Receta)
def get_receta(receta_id: int, db: Session = Depends(get_db)):
    """
    Retorna la receta identificada con el receta_id
    """
    db_receta = crud.get_recetas_id(db, receta_id=receta_id)
    if db_receta is None:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    return db_receta


@app.post("/recetas/", response_model=schemas.Receta)
def create_receta(receta: schemas.RecetaCreate, db: Session = Depends(get_db)):
    db_receta = crud.get_receta_por_nombre(db, nombre=receta.nombre)
    if db_receta:
        raise HTTPException(status_code=400, detail="La receta ya existe")
    return crud.create_recetas(db=db, receta=receta)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate, add_pagination
from typing import List, Optional
from .. import crud, models, schemas, database

router = APIRouter(
    prefix="/atletas",
    tags=["atletas"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Atleta)
def create_atleta(atleta: schemas.AtletaCreate, db: Session = Depends(database.get_db)):
    db_atleta = crud.get_atleta_by_cpf(db, cpf=atleta.cpf)
    if db_atleta:
        raise HTTPException(status_code=303, detail="Já existe um atleta cadastrado com o cpf: {}".format(atleta.cpf))
    return crud.create_atleta(db=db, atleta=atleta)

@router.get("/", response_model=List[schemas.Atleta])
def read_atletas(skip: int = 0, limit: int = 10, nome: Optional[str] = None, cpf: Optional[str] = None, db: Session = Depends(database.get_db)):
    atletas = crud.get_atletas(db, skip=skip, limit=limit, nome=nome, cpf=cpf)
    return atletas

add_pagination(router)

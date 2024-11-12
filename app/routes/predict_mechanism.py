from typing import List
from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

predict_mechanism_route = APIRouter()

class PredictMechanism(BaseModel):
    ndep_proce: str
    nmun_proce: str
    semana: int
    ano: int
    sexo_: str
    area_: int
    pac_hos_: int
    con_fin_: int
    edad_: int
    inten_prev: int
    prob_parej: int
    enfermedad_cronica: int
    prob_econo: int
    muerte_fam: int
    esco_educ: int
    prob_legal: int
    suici_fm_a: int
    maltr_fps: int
    prob_labor: int
    prob_famil: int
    prob_consu: int
    hist_famil: int
    idea_suici: int
    plan_suici: int
    antec_tran: int
    tran_depre: int
    trast_personalidad: int
    trast_bipolaridad: int
    esquizofre: int
    antec_v_a: int
    abuso_alco: int
    ahorcamien: int
    arma_corto: int
    arma_fuego: int
    inmolacion: int
    lanz_vacio: int
    lanz_vehic: int
    lanz_agua: int
    intoxicaci: int
    ndep_resi: str



@predict_mechanism_route.post('/predict')
async def predict_mechanism(columns: List[PredictMechanism]):
    pass
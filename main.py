from fastapi import FastAPI
from fastapi.responses import FileResponse
from typing import Optional
from pydantic import BaseModel
from app import contract as contract_gn
from json import loads


class Item(BaseModel):
    nome_locador: Optional[str] = "{'nome_locador'}"
    nacionalidade_locador: Optional[str] = "{'nacionalidade_locador'}"
    status_civil_locador: Optional[str] = "{'status_civil_locador'}"
    emprego_locador: Optional[str] = "{'emprego_locador'}"
    rg_locador: Optional[str] = "{'rg_locador'}"
    orgao_emissor_locador: Optional[str] = "{'orgao_emissor_locador'}"
    cpf_locador: Optional[str] = "{'cpf_locador'}"
    celular_locador: Optional[str] = "{'celular_locador'}"
    rua_locador: Optional[str] = "{'rua_locador'}"
    cep_locador: Optional[str] = "{'cep_locador'}"
    nome_locatario: Optional[str] = "{'nome_locatario'}"
    nacionalidade_locatario: Optional[str] = "{'nacionalidade_locatario'}"
    status_civil_locatario: Optional[str] = "{'status_civil_locatario'}"
    emprego_locatario: Optional[str] = "{'emprego_locatario'}"
    rg_locatario: Optional[str] = "{'rg_locatario'}"
    orgao_emissor_locatario: Optional[str] = "{'orgao_emissor_locatario'}"
    cpf_locatario: Optional[str] = "{'cpf_locatario'}"
    celular_locatario: Optional[str] = "{'celular_locatario'}"
    rua_locatario: Optional[str] = "{'rua_locatario'}"
    cep_locatario: Optional[str] = "{'cep_locatario'}"
    descricao_imovel: Optional[str] = "{'descricao_imovel'}"
    endereco_imovel: Optional[str] = "{'endereco_imovel'}"
    valor_aluguel: Optional[str] = "{'valor_aluguel'}"
    impostos_status: Optional[str] = "{'impostos_status'}"
    cod_agua: Optional[str] = "{'cod_agua'}"
    cod_luz: Optional[str] = "{'cod_luz'}"
    imovel_ref: Optional[str] = "{'imovel_ref'}"
    qtd_calcao: Optional[str] = "{'qtd_calcao'}"
    dia_vencimento: Optional[str] = "{'dia_vencimento'}"
    primeiro_vencimento: Optional[str] = "{'primeiro_vencimento'}"



app = FastAPI()

@app.post("/comercial")
async def comercial_contract(item: Item):
    response = loads(item.json())
    # with open('test.txt', 'a') as file:
    #     file.write(f"\n{type(response)}, {response}")
    _ = contract_gn(
            nome_locador=response['nome_locador'],
            nacionalidade_locador=response['nacionalidade_locador'],
            status_civil_locador=response['status_civil_locador'],
            emprego_locador=response['emprego_locador'],
            rg_locador=response['rg_locador'],
            orgao_emissor_locador=response['orgao_emissor_locador'],
            cpf_locador=response['cpf_locador'],
            celular_locador=response['celular_locador'],
            rua_locador=response['rua_locador'],
            cep_locador=response['cep_locador'],
            nome_locatario=response['nome_locatario'],
            nacionalidade_locatario=response['nacionalidade_locatario'],
            status_civil_locatario=response['status_civil_locatario'],
            emprego_locatario=response['emprego_locatario'],
            rg_locatario=response['rg_locatario'],
            orgao_emissor_locatario=response['orgao_emissor_locatario'],
            cpf_locatario=response['cpf_locatario'],
            celular_locatario=response['celular_locatario'],
            rua_locatario=response['rua_locatario'],
            cep_locatario=response['cep_locatario'],
            descricao_imovel=response['descricao_imovel'],
            endereco_imovel=response['endereco_imovel'],
            valor_aluguel=response['valor_aluguel'],
            impostos_status=response['impostos_status'],
            cod_agua=response['cod_agua'],
            cod_luz=response['cod_luz'],
            imovel_ref=response['imovel_ref'],
            qtd_calcao=response['qtd_calcao'],
            dia_vencimento=response['dia_vencimento'],
            primeiro_vencimento=response['primeiro_vencimento'],
    )
    return FileResponse("contrato-comercial.docx")

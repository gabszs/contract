from docxtpl import DocxTemplate
from PySimpleGUI import PySimpleGUI as sg
from datetime import (datetime, timedelta)
from tkinter import filedialog


FULL_MONTHS = {'01': 'janeiro', '02': 'fevereiro', '03': 'março', '04': 'abril',
               '05': 'maio', '06': 'junho', '07': 'julho', '08': 'agosto',
               '09': 'setembro', '010': 'outubro',  '011': 'novembro', '012': 'dezembro'}

def contract(
    nome_locador,
    nacionalidade_locador,
    status_civil_locador,
    emprego_locador,
    rg_locador,
    orgao_emissor_locador,
    cpf_locador,
    celular_locador,
    rua_locador,
    cep_locador,
    nome_locatario,
    nacionalidade_locatario,
    status_civil_locatario,
    emprego_locatario,
    rg_locatario,
    orgao_emissor_locatario,
    cpf_locatario,
    celular_locatario,
    rua_locatario,
    cep_locatario,
    descricao_imovel,
    endereco_imovel,
    valor_aluguel,
    impostos_status,
    cod_agua,
    cod_luz,
    imovel_ref,
    qtd_calcao,
    dia_vencimento,
    primeiro_vencimento,
):
    data_start = (datetime.today().strftime(f"%d/%m/%Y")).split('/')
    data_end = ((datetime.today() + timedelta(days=1095)
                 ).strftime("%d/%m/%Y")).split('/')
    data_start = f"{data_start[0]} de {FULL_MONTHS[data_start[1]]} de {data_start[2]}"
    data_end = f"{data_end[0]} de {FULL_MONTHS[data_end[1]]} de {data_end[2]}"

    # data_start,
    # data_end
    doc = DocxTemplate('contrato_base_comercial.docx')

    context = {
        'nome_locador': nome_locador,
        'nacionalidade_locador': nacionalidade_locador,
        'status_civil_locador': status_civil_locador,
        'emprego_locador': emprego_locador,
        'rg_locador': rg_locador,
        'orgao_emissor_locador': orgao_emissor_locador,
        'cpf_locador': cpf_locador,
        'celular_locador': celular_locador,
        'rua_locador': rua_locador,
        'cep_locador': cep_locador,
        'nome_locatario': nome_locatario,
        'nacionalidade_locatario': nacionalidade_locatario,
        'status_civil_locatario': status_civil_locatario,
        'emprego_locatario': emprego_locatario,
        'rg_locatario': rg_locatario,
        'orgao_emissor_locatario': orgao_emissor_locatario,
        'cpf_locatario': cpf_locatario,
        'celular_locatario': celular_locatario,
        'rua_locatario': rua_locatario,
        'cep_locatario': cep_locatario,
        'descricao_imovel': descricao_imovel,
        'endereco_imovel': endereco_imovel,
        'valor_aluguel': valor_aluguel,
        'impostos_status': impostos_status,
        'cod_agua': cod_agua,
        'cod_luz': cod_luz,
        'data_start': data_start,
        'data_end': data_end,
        'qtd_calcao': qtd_calcao,
        'dia_vencimento': dia_vencimento,
        'primeiro_vencimento': primeiro_vencimento,
    }

    doc.render(context)
    doc.save('contrato-comercial.docx')

    # file_path = filedialog.askdirectory()
    #
    # doc.save(str(file_path) +
    #          f"/CONTRATO LOCADOR= {nome_locador}, LOCATARIO= {nome_locatario}, REF= {imovel_ref}.docx")



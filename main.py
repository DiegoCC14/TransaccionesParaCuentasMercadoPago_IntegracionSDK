import mercadopago , json

# ####################################
ACCESS_TOKEN_PRD = "BUSCAR TOKEN EN MERCADO PAGO DEVELOPERS"

fecha_inicio = "2025-11-22T00:00:00Z"
fecha_final = "2025-11-23T23:59:59Z"
# ####################################

filters = {
    "range": "date_created",
    "begin_date": fecha_inicio,
    "end_date":   fecha_final
}

sdk = mercadopago.SDK(ACCESS_TOKEN_PRD)
result = sdk.payment().search(filters)
dicc_result = []
for data_dicc in result["response"]["results"]:
    data_dicc["transaction_details"]["operation_type"] = data_dicc["operation_type"] #Agregando campos a Transaccion

    dicc_data_tratado = { 
        "tipo_operacion" : data_dicc["operation_type"],
        "estado_operacion" : data_dicc["status"],
        "descripcion" : data_dicc["description"],
        "monto_operacion" : data_dicc["transaction_details"]["total_paid_amount"],
        "monto_neto_operacion" : data_dicc["transaction_details"]["net_received_amount"]
    }
    dicc_result.append( dicc_data_tratado )

with open(f"transaccionesMP{fecha_inicio[0:10]}_{fecha_final[0:10]}.json", "w", encoding="utf-8") as f:
    json.dump( dicc_result , f, ensure_ascii=False, indent=4)

#Diccionarios
#{"clave": "valor",}

teacher = {
    "name": "Francisco",
    "l_name": "Lopez",
    "phone": "2471234567",
    "groups": ["3ADSM", "3BDSM"]
}

print(type(teacher))
print(teacher)
print(teacher["name"])
print(teacher["gruops"])
teacher["groups"].append("3CDSM")
teacher["PHONE"]= "234723644"
teacher["City"] = "Huamantla"
print(teacher)
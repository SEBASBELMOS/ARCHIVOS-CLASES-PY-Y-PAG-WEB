def seleccion(dic):
    dicc = dict()
    for estudiante in dic:
        key = estudiante
        nombres = dic[estudiante]["nombres"]
        apellidos = dic[key]["apellidos"]
        documento = dic[key]["documento"]
        programa = dic[key]["programa"]
        materias = dic[key]["materias"]
        dicc[key] = {
            'nombres' : nombres,
            'apellidos' : apellidos,
            'documento' : documento,
            'programa' : programa,
            'materias' : materias 
        }
    return dicc

print(seleccion({
    20170136837:{
        "nombres" : "Jorge Juan",
        "apellidos" : "Moreno López",
        "documento" : 88481595,
        "programa" : "ARQU",
        "materias" : [
                        {
                        "facultad" : "Arquitectura",
                        "codigo" : "ARQU-2113",
                        "nota" : 2.97,
                        "creditos" : 2,
                        "retirada" : "Si",
                        },
                        {
                        "facultad" : "Arquitectura",
                        "codigo" : "ARQU-5048",
                        "nota" : 4.26,
                        "creditos" : 0,
                        "retirada" : "No",
                        },
                    ]
                },
    20130225137:{
                "nombres" : "Sara Carolina",
                "apellidos" : "Gómez Fernández",
                "documento" : 58770043,
                "programa" : "ARQD",
                "materias" : [
                                {
                                "facultad" : "Arquitectura",
                                "codigo" : "ARQD-7738",
                                "nota" : 3.36,
                                "creditos" : 3,
                                "retirada" : "No",
                                },
                                {
                                "facultad" : "Arquitectura",
                                "codigo" : "ARQD-7698",
                                "nota" : 1.59,
                                "creditos":4,
                                "retirada" : "Si",
                                },
                            ]
                } }))
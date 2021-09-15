def Seleccion(info: dict) -> list:
    ganador={}
    mayorPromedio=0
    
    for a in info:
        
        participante={}#{'nombre':'', 'apellido':'', 'documento': , 'programa':'' ,'materias':[] }
        participante=info[a]
        participante.setdefault('promedio',0)
        participante.setdefault('correo','')
        participante.setdefault('codigo',a)
        materias= participante.pop('materias')
        sumatoria=0
        cantidad=0
        
        
        
        for m in materias:
            if m['retirada']=='No':
                sumatoria+=m['nota']*m['creditos'] # = es igual a 8.92
                cantidad+=m['creditos'] # = es igual a 2
                
                
                
                
        if cantidad >0 and sumatoria>0:
            participante['promedio']=sumatoria/cantidad # se asigna el promedio el resultado de dividir sumatoria con cantidad
            
            
          
            
            
        if participante['promedio']>mayorPromedio:
            ganador=participante
            mayorPromedio=participante['promedio']
            
            
        elif participante['promedio']==mayorPromedio: #and not(participante['promedio']==0):
            añoGanador=int(str(ganador['codigo'])[0:4])
            añoParti=int(str(participante['codigo'])[0:4])
            periodoGanador=int(str(ganador['codigo'])[4:6])
            periodoParti=int(str(participante['codigo'])[4:6])
            
            if añoParti< añoGanador:
                ganador=participante
                mayorPromedio=participante['promedio']
                
                
            elif añoParti== añoGanador:
                if periodoParti< periodoGanador:
                    ganador=participante
                    mayorPromedio=participante['promedio']
    
    
    
    
    # Tenemos que avisar a la persona que ganó
    corteNombre=ganador['nombres'].find(' ')
    corteApellido=ganador['apellidos'].find(',')
   
    if not(ganador['nombres'].find(' ')==-1):
        c=ganador['nombres'][:1]+ganador['nombres'][corteNombre+1:corteNombre+2]+"."+ganador['apellidos'][:corteApellido]+str(ganador['documento'])[-2:]
    else:
        c= ganador['nombres'][:1] + ganador['apellidos'][:1]+"."+ganador['apellidos'][corteApellido+2:]+str(ganador['documento'])[-2:]
    c=c.lower()
    for u in range(0,len(c)):
       y=c[u:u+1]
       if y =='á':
            c=c[0:u]+'a'+c[u+1:]
       elif y =='é':
            c=c[0:u]+'e'+c[u+1:]
       elif y =='ì':
            c=c[0:u]+'i'+c[u+1:]
       elif y =='ó':
            c=c[0:u]+'o'+c[u+1:]
       elif y =='ù':
            c=c[0:u]+'u'+c[u+1:]
    ganador['correo']=c
    return [ganador['codigo'], ganador['nombres'], ganador['apellidos'], ganador['documento'], ganador['programa'], ganador['promedio'],ganador['correo']]
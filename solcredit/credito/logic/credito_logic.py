from ..models import Credito

def get_creditos():
    return Credito.objects.all()

def get_credito(credito_pk):
    measurement=Credito.objects.get(pk=credito_pk)
    return measurement

def create_credito(new_credito):
    estadof = "Denegado"
    if new_credito["valor"]%35>10: estadof="Aprobado" 
    credito = Credito(name=new_credito["name"],valor=new_credito["valor"],
           estado=estadof)
    credito.save()
    return credito
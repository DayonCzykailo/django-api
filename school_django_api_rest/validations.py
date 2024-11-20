import re
from validate_docbr import CPF

def validate_phone_is_brazil_format(phone) -> bool: # exemple: 55 11 91234-1234
    return not re.findall(r'^[0-9]{2} [0-9]{2} [0-9]{5}-[0-9]{4}$', phone)
    
def validate_cpf_value(cpf) -> bool:
    return CPF().validate(cpf)
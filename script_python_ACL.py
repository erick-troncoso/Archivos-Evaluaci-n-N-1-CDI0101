def tipo_acl(numero_acl):
	if numero_acl >= 1 and numero_acl <=99:
		return "ACL Estandar"
	elif numero_acl >= 100 and numero_acl <=199:
		return "ACL Extendida"
	else:
		return "ninguna lista de acceso"

try:
	numero_acl = int(input("introduce el numero de ACL IPv4: "))
	tipo = tipo_acl(numero_acl)
	print("El numero", numero_acl, "corresponde a ", tipo)
except ValueError:
	print("Por favor, introduce un numero valido.")

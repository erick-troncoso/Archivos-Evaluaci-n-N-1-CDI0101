import json
from datetime import datetime, timedelta

#ruta del archivo .json
ruta_archivo = "/home/devasc/labs/devnet-src/parsing/myfile.json"

try:
	with open(ruta_archivo) as archivo:
		ourjson = json.load(archivo)
		print ("Archivo JSON CARGADO CORRECTAMENTE." )

		if "expires_in" in ourjson:
			tiempo_expiracion_segundos = int(ourjson["expires_in"])

			fecha_expiracion = datetime.now() + timedelta(seconds=tiempo_expiracion_segundos)


			print("valor del token:", ourjson.get("access_token"))
			print("fecha de expiracion del token:" , fecha_expiracion)
		else:
			print("la clave expires_in no esta presente en el archivo JSON.")
except FileNotFoundError:
	print("el archivo json no se encontro en la ruta especificada.")
except json.JSONDecodeError:
	print("error al decodificar el archivo JSON.")


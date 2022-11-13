# Scraping and crawling
Web scraping y Web crawling con Python para obtener 
noticias relacionadas a medidas gubernamentales en el 
Perú durante la pandemia por COVID-19.

![img.png](images/politic_image.png)

## Justificación
Nuestro compañero necesita datos para su tesis

## Páginas evaluadas
Noticias MINSA:
> https://www.gob.pe/institucion/minsa/noticias?filter%5Bterms%5D=covid&amp;filter%5Btype%5D=&amp;sheet=

Para buscar los elementos de interés, filtraremos los enlaces relacionados a covid:
> soup.select("a[href*='covid']")

## Ejecutar localmente

Asegurarse de tener python instalado
> py --version

Crear un entorno virtual
> py -m venv .venv

Instalar dependencias 
> pip install -r requirements

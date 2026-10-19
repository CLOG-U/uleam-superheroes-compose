"""Genera el informe académico. Requiere reportlab; ejecutar desde la raíz del proyecto."""
from pathlib import Path
from xml.sax.saxutils import escape
import json
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/Informe_Superheroes_Carlos_Ortiz.pdf'
STATUS=json.loads((ROOT/'docs/resultado_validacion.json').read_text(encoding='utf-8'))
FONT=ROOT/'app/src/main/res/font'
pdfmetrics.registerFont(TTFont('Cabin',str(FONT/'cabin_regular.ttf')))
pdfmetrics.registerFont(TTFont('Cabin-Bold',str(FONT/'cabin_bold.ttf')))
pdfmetrics.registerFontFamily('Cabin',normal='Cabin',bold='Cabin-Bold',italic='Cabin',boldItalic='Cabin-Bold')
W,H=595.276,841.89
INK=colors.HexColor('#202A29'); GREEN=colors.HexColor('#466800'); RED=colors.HexColor('#B42837')
MUTED=colors.HexColor('#53615F'); PALE=colors.HexColor('#F0F4EA')
c=canvas.Canvas(str(OUT),pagesize=(W,H))
c.setTitle('PEA: App de superhéroes - Carlos Luis Ortiz García - ULEAM')
c.setAuthor('Carlos Luis Ortiz García')
styles={
 'body':ParagraphStyle('body',fontName='Cabin',fontSize=11,leading=16,textColor=INK,spaceAfter=9),
 'small':ParagraphStyle('small',fontName='Cabin',fontSize=9,leading=12,textColor=MUTED),
 'cell':ParagraphStyle('cell',fontName='Cabin',fontSize=9.5,leading=13,textColor=INK),
 'headcell':ParagraphStyle('headcell',fontName='Cabin-Bold',fontSize=9.5,leading=13,textColor=colors.white),
 'center':ParagraphStyle('center',fontName='Cabin',fontSize=12,leading=18,textColor=INK,alignment=1),
}
def para(text,x,y,width=W-104,kind='body'):
    p=Paragraph(text,styles[kind]); _,h=p.wrap(width,H); p.drawOn(c,x,y-h); return y-h-9
def heading(text,y):
    c.setFillColor(GREEN); c.setFont('Cabin-Bold',15); c.drawString(52,y,text); return y-22
def page(n,title,subtitle):
    c.setFillColor(GREEN); c.rect(0,H-8,W,8,fill=1,stroke=0)
    c.setFont('Cabin-Bold',9); c.setFillColor(MUTED); c.drawString(52,H-39,'ULEAM  /  APLICACIONES MÓVILES')
    c.setFont('Cabin-Bold',25); c.setFillColor(INK); c.drawString(52,H-85,title)
    para(subtitle,52,H-100,kind='small')
    c.setStrokeColor(colors.HexColor('#DDE4DB')); c.line(52,52,W-52,52)
    c.setFont('Cabin',8); c.setFillColor(MUTED); c.drawString(52,36,'Carlos Luis Ortiz García  |  18 de octubre de 2026')
    c.drawRightString(W-52,36,f'{n} / 6')
def table(rows,widths,y):
    data=[[Paragraph(escape(str(cell)),styles['headcell' if i==0 else 'cell']) for cell in row] for i,row in enumerate(rows)]
    t=Table(data,colWidths=widths,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),GREEN),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,0),(-1,0),0.5,GREEN)]))
    _,h=t.wrap(W-104,H); t.drawOn(c,52,y-h); return y-h-18
def code(text,y):
    lines=text.splitlines(); h=18+len(lines)*12
    c.setFillColor(PALE); c.roundRect(52,y-h,W-104,h,7,fill=1,stroke=0)
    c.setFillColor(INK); c.setFont('Courier',8.3)
    for i,line in enumerate(lines): c.drawString(64,y-17-i*12,line)
    return y-h-16

# 1. Portada
c.setFillColor(PALE); c.rect(0,0,W,H,fill=1,stroke=0)
c.setFillColor(RED); c.rect(0,H-15,W,15,fill=1,stroke=0)
c.setFillColor(RED); c.setFont('Cabin-Bold',57); c.drawCentredString(W/2,H-142,'ULEAM')
y=para('UNIVERSIDAD LAICA<br/><b>ELOY ALFARO DE MANABÍ</b>',70,H-164,W-140,'center')
c.setStrokeColor(RED); c.line(W/2-50,y-16,W/2+50,y-16)
c.setFillColor(INK); c.setFont('Cabin-Bold',28); c.drawCentredString(W/2,H-297,'PEA: App de superhéroes')
para('Desarrollo de una aplicación Android<br/>con Kotlin, Jetpack Compose y Material 3',70,H-315,W-140,'center')
y=H-416
for label,value in [('ESTUDIANTE','Carlos Luis Ortiz García'),('CARRERA','Ingeniería en Software'),('ASIGNATURA','Aplicaciones Móviles'),('DOCENTE','Ing. Edgardo Panchana'),('FECHA','18 de octubre de 2026')]:
    c.setFont('Cabin-Bold',9); c.setFillColor(RED); c.drawCentredString(W/2,y,label)
    c.setFont('Cabin',13); c.setFillColor(INK); c.drawCentredString(W/2,y-21,value); y-=58
c.setFont('Cabin',9); c.setFillColor(MUTED); c.drawCentredString(W/2,62,'Informe técnico y evidencias de la implementación')
c.showPage()

# 2. Alcance
page(2,'Objetivo y requisitos','Correspondencia entre la consigna y el proyecto entregado.')
y=heading('1. Objetivo',H-153)
y=para('Implementar una aplicación Android que presente seis superhéroes mediante una lista desplazable. La práctica permite aplicar composición de interfaces, recursos externos, reutilización de componentes y personalización visual con Material 3.',52,y)
y=heading('2. Cumplimiento del ejercicio',y-8)
y=table([
 ['Requisito','Evidencia en el proyecto'],
 ['Base Android y API mínima 24','ComponentActivity, módulo app y minSdk = 24.'],
 ['Modelo y datos locales','Hero.kt y HeroesDataSource.kt dentro de model; seis registros.'],
 ['Textos, imágenes e icono','strings.xml, seis vectores android_superhero e iconos mipmap oficiales.'],
 ['Fuente Cabin y Material 3','Cabin Regular/Bold; Color.kt, Type.kt, Shape.kt y Theme.kt.'],
 ['Tarjeta de héroe','Elevación 2 dp; forma 16 dp; padding 16 dp; imagen 72 dp y radio 8 dp.'],
 ['Lista y barra superior','LazyColumn; CenterAlignedTopAppBar centrada dentro de Scaffold.'],
 ['Claro, oscuro y bordes','Tema según el sistema; padding de Scaffold y ajuste de barras.'],
], [170,W-274],y)
y=para('<b>Interpretación de la altura:</b> los 72 dp corresponden al contenido mínimo de la fila y al tamaño de la ilustración. El padding se agrega por fuera del contenido; la tarjeta puede crecer si el nombre o la descripción ocupan más líneas.',52,y)
y=para('Se mantienen en inglés los nombres y las descripciones del conjunto de datos del ejercicio para conservar la referencia visual del codelab.',52,y)
c.showPage()

# 3. Implementación
page(3,'Diseño e implementación','Separación de datos, componentes y sistema visual.')
y=heading('3. Organización del código',H-153)
y=para('<b>Datos:</b> Hero almacena tres identificadores de recursos: nombre, descripción e imagen. Las anotaciones @StringRes y @DrawableRes hacen explícito el tipo de recurso esperado. HeroesRepository reúne la lista fija y evita repetir datos en la interfaz.',52,y)
y=para('<b>Presentación:</b> MainActivity configura Compose; SuperheroesApp coordina Scaffold y la barra superior. HeroesList crea los elementos bajo demanda con LazyColumn. HeroListItem concentra la tarjeta, la columna de textos y la ilustración.',52,y)
y=code('''SuperheroesTheme {
    SuperheroesApp(heroes = HeroesRepository.heroes)
}

Scaffold(topBar = { SuperheroesTopAppBar() }) { padding ->
    HeroesList(heroes = heroes, contentPadding = padding)
}''',y)
y=heading('4. Decisiones técnicas',y-2)
y=para('La pantalla recibe los héroes como parámetro, lo que facilita su reutilización y las pruebas. Cada elemento usa nameRes como clave estable. Los textos se obtienen con stringResource y las imágenes con painterResource; todos los recursos funcionan sin conexión.',52,y)
y=para('Las tarjetas conservan la animación de entrada de la solución oficial: aparición de la lista y desplazamiento vertical escalonado. Las imágenes se recortan con esquinas de 8 dp. Su descripción accesible es nula porque el nombre del héroe ya está presente como texto y la ilustración es decorativa.',52,y)
y=para('El tema usa paletas fijas clara y oscura, sin color dinámico por defecto. Cabin define los títulos y el cuerpo. WindowCompat permite dibujar de borde a borde; el Scaffold aporta los márgenes necesarios para que el contenido no invada las barras.',52,y)
y=para('<b>Alcance:</b> la aplicación es un catálogo de datos locales. La actividad no exige autenticación, almacenamiento remoto ni una API de superhéroes.',52,y)
c.showPage()

# 4. Pantallas
page(4,'Interfaz y evidencias','Renderizado de la aplicación y comportamiento de la lista de héroes.')
y=H-152
screens=[('tema_claro.png','Tema claro'),('tema_oscuro.png','Tema oscuro')]
if all((ROOT/'docs/evidencias'/f).exists() for f,_ in screens):
    for x,(file,label) in zip([72,326],screens):
        path=ROOT/'docs/evidencias'/file
        img=Image(str(path)); h=360; w=img.imageWidth/img.imageHeight*h
        img.drawHeight=h; img.drawWidth=w; img.drawOn(c,x+(197-w)/2,y-h)
        c.setFont('Cabin-Bold',11); c.setFillColor(GREEN); c.drawCentredString(x+98,y-h-22,label)
    y-=410
    y=para('Las capturas muestran la barra centrada, las tarjetas con tipografía Cabin y las ilustraciones oficiales. El tema sigue la configuración del sistema; la disposición mantiene la misma estructura en ambos modos.',52,y)
else:
    y=para(STATUS['ejecucion_detalle'],52,y)
    y=para('Las vistas previas @Preview de MainActivity.kt y HeroesScreen.kt permiten inspeccionar las dos paletas desde Android Studio. Las capturas de ejecución no se sustituyen por imágenes simuladas.',52,y)
y=heading('5. Comportamiento esperado',y-16)
y=para('Al abrir la app se muestra Superheroes y el primer registro, Nick the Night and Day. Al desplazar hacia arriba se llega a Dynamic Yasmine. Las descripciones largas aumentan la altura de la tarjeta sin imponer un recorte fijo.',52,y)
y=para('Para revisar el modo oscuro se cambia el tema del dispositivo y se vuelve a la app. Los fondos, textos y superficies adoptan la paleta oscura; el contenido de los héroes se conserva.',52,y)
c.showPage()

# 5. Validación
page(5,'Validación y ejecución','Resultados observados y pasos para reproducir la entrega.')
y=heading('6. Comprobaciones realizadas',H-153)
y=table([['Comprobación','Resultado'],['Compilación y APK',STATUS['compilacion']],['Android Lint',STATUS['lint']],['Pruebas instrumentadas',STATUS['pruebas']],['Ejecución y capturas',STATUS['ejecucion']],['Versionado',STATUS['git']]], [162,W-266],y)
y=para(STATUS['limitaciones'],52,y)
y=heading('7. Reproducción en Android Studio',y-12)
for text in [
 '1. Clonar el repositorio o descomprimir el proyecto y abrir la carpeta SuperheroesULEAM.',
 '2. Configurar el JDK de Gradle. La entrega se verifica con JBR 25, Gradle 9.6.0, AGP 9.4.0 y el plugin Compose 2.2.10.',
 '3. Instalar SDK Platform 37, sincronizar Gradle y conectar un dispositivo Android API 24 o superior. local.properties se genera con la ruta del SDK de cada equipo.',
 '4. Ejecutar app, desplazar hasta el sexto héroe y cambiar el tema del sistema para revisar ambas paletas.'
]: y=para(text,52,y)
y=code('''.\\gradlew.bat assembleDebug lintDebug assembleDebugAndroidTest
.\\gradlew.bat connectedDebugAndroidTest''',y)
y=para('El segundo comando requiere un emulador o dispositivo conectado. El APK de depuración se incluye en entrega/SuperheroesULEAM-debug.apk; el código fuente y los recursos están en el mismo repositorio.',52,y,kind='small')
c.showPage()

# 6. Cierre
page(6,'Repositorio y conclusiones','Trazabilidad del repositorio y cierre de la práctica.')
y=heading('8. Control de versiones y entrega',H-153)
y=para('Se creó el repositorio y se realizó un primer commit del proyecto Android. Los siguientes cambios incorporan la documentación, el APK y las evidencias. Los archivos temporales, cachés, rutas locales y claves de firma no forman parte del código versionado.',52,y)
y=para('<b>Repositorio:</b><br/><link href="https://github.com/CLOG-U/uleam-superheroes-compose" color="#466800">github.com/CLOG-U/uleam-superheroes-compose</link>',52,y)
y=code('''git clone https://github.com/CLOG-U/uleam-superheroes-compose.git
cd uleam-superheroes-compose
git log --oneline''',y)
y=heading('9. Conclusiones',y-12)
y=para('La práctica integra datos locales con una interfaz declarativa. La separación entre modelo, repositorio, componentes y tema facilita localizar cada responsabilidad. LazyColumn ofrece una lista desplazable y MaterialTheme mantiene coherencia de color, forma y tipografía.',52,y)
y=para('El tratamiento de padding, alturas mínimas y barras del sistema evita que una medida rígida o el borde de la pantalla oculte información. Las pruebas incluidas verifican la presencia del encabezado y el acceso al último héroe en ambos temas.',52,y)
c.showPage(); c.save(); print(OUT)

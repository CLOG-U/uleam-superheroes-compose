# Superheroes - ULEAM

[![Android](https://github.com/CLOG-U/uleam-superheroes-compose/actions/workflows/android.yml/badge.svg)](https://github.com/CLOG-U/uleam-superheroes-compose/actions/workflows/android.yml)

Proyecto de la actividad **PEA: App de superhéroes**, basado en el codelab de Android Developers [Practice: Build Superheroes app](https://developer.android.com/codelabs/basic-android-kotlin-compose-practice-superheroes).

- Estudiante: Carlos Luis Ortiz García.
- Universidad: Universidad Laica Eloy Alfaro de Manabí (ULEAM).
- Carrera: Ingeniería en Software.
- Asignatura: Aplicaciones Móviles.
- Docente: Ing. Edgardo Panchana.
- Fecha académica: 18 de octubre de 2026.
- Repositorio: https://github.com/CLOG-U/uleam-superheroes-compose

## Archivos de entrega

- [Informe explicativo en PDF](docs/Informe_Superheroes_Carlos_Ortiz.pdf).
- [APK de depuración](entrega/SuperheroesULEAM-debug.apk).
- [Resultados y límites de la validación](docs/VALIDACION.md).
- [Capturas de pantalla](docs/evidencias/).

## Funcionalidad

Aplicación Android nativa con Kotlin, Jetpack Compose y Material 3. Muestra los seis héroes del ejercicio en tarjetas dentro de una `LazyColumn`. Incluye imágenes vectoriales, fuente Cabin Regular/Bold, barra superior centrada, animación de entrada, temas claro y oscuro según el sistema y tratamiento de las barras del sistema para dibujar de borde a borde. Los datos son locales; no requiere servicios web ni permisos de Internet.

## Abrir y ejecutar

1. Clonar este repositorio o descomprimir el proyecto.
2. Abrir esta carpeta desde Android Studio y configurar su JDK de Gradle. La verificación de esta entrega usa JBR 25, Gradle 9.6.0 y Android Gradle Plugin 9.4.0 (Kotlin integrado con plugin Compose 2.2.10).
3. Instalar Android SDK Platform 37. Android Studio debe generar `local.properties` con la ruta del SDK de cada equipo.
4. Sincronizar Gradle y ejecutar el módulo `app` en Android 7.0/API 24 o superior. `targetSdk` es 35; `minSdk` es 24.
5. Cambiar el tema del dispositivo para comprobar las dos paletas. Desplazar la lista hasta Dynamic Yasmine.

En PowerShell, con `JAVA_HOME` apuntando al JDK:

```powershell
.\gradlew.bat assembleDebug lintDebug assembleDebugAndroidTest
.\gradlew.bat connectedDebugAndroidTest
```

El segundo comando requiere un dispositivo o emulador conectado. El APK se genera en `app/build/outputs/apk/debug/app-debug.apk`. La copia de entrega está en `entrega/SuperheroesULEAM-debug.apk`.

## Estructura

```text
app/src/main/java/com/example/superheroes/
  MainActivity.kt        # Activity, Scaffold y barra superior
  HeroesScreen.kt        # Lista animada y tarjeta reutilizable
  model/Hero.kt          # Modelo con identificadores de recursos
  model/HeroesDataSource.kt # Repositorio de seis héroes
  ui/theme/              # Paletas, tipografía Cabin, formas y tema
app/src/main/res/        # Textos, vectores, iconos y fuentes
app/src/androidTest/    # Pruebas de renderizado y desplazamiento
docs/                   # Informe PDF y evidencias de validación
entrega/                # APK de depuración para evaluación
```

## Decisiones de implementación

La tarjeta tiene elevación de 2 dp y forma de 16 dp. El contenido interior tiene altura mínima de 72 dp más 16 dp de relleno; no se fija toda la tarjeta a 72 dp, pues eso recortaría el contenido. La imagen mide 72 dp, se recorta con radio de 8 dp y queda separada 16 dp del texto. La altura puede crecer para respetar textos largos y tamaños de fuente mayores.

La pantalla recibe la lista como parámetro. Los elementos usan el identificador del nombre como clave estable. El padding del `Scaffold` se transmite a la lista para respetar las barras del sistema. Las ilustraciones se consideran decorativas porque el nombre del héroe se muestra en texto.

## Procedencia y licencias

Esta entrega es una **adaptación de la solución oficial** de [google-developer-training/basic-android-kotlin-compose-training-superheroes](https://github.com/google-developer-training/basic-android-kotlin-compose-training-superheroes). Se conservaron el modelo, los datos, las ilustraciones, los iconos, las fuentes, la base de los temas y la lista animada. Se adaptaron la configuración de compilación, la composición de la pantalla, las claves y formas de las tarjetas y el tratamiento de barras; se añadieron pruebas instrumentadas, documentación y evidencias.

Se conserva `LICENSE` (Apache 2.0) y `ASSETS_LICENSE.txt` (fuentes bajo SIL Open Font License y demás recursos bajo Apache 2.0). La procedencia se declara para no atribuir como originales los materiales de Google.

El archivo `docs/VALIDACION.md` describe las comprobaciones efectivamente realizadas y sus límites.

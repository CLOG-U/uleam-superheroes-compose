# Validación de la entrega

Fecha académica: **18 de octubre de 2026**, zona America/Guayaquil.

## Código verificado

- Commit de la app y pruebas: `bde9d5e234da50cab0bac86db201f1038c5880a7`.
- Ejecución de GitHub Actions: https://github.com/CLOG-U/uleam-superheroes-compose/actions/runs/39180874219
- Entorno de ejecución: Ubuntu, emulador Android 11/API 30 x86_64 con aceleración KVM.
- Compilación local: Windows, JBR 25.0.3, Gradle 9.6.0, Android Gradle Plugin 9.4.0 y SDK Platform 37.0.

## Comprobaciones completadas

1. `assembleDebug`: APK generado correctamente tanto localmente como en CI.
2. `assembleDebugAndroidTest`: pruebas instrumentadas compiladas.
3. `lintDebug`: sin errores; el reporte local registra 12 advertencias. No se desactivaron errores ni se creó un baseline para ocultarlos.
4. `connectedDebugAndroidTest`: **2 pruebas aprobadas, 0 fallidas**.
5. Capturas reales de la app instalada: tema claro, tema oscuro y lista desplazada hasta el último héroe.

La prueba del tema claro comprueba el encabezado, el primer héroe y el acceso completo a la descripción del sexto héroe. La prueba del tema oscuro comprueba la navegación entre los extremos de la lista y fuerza la captura de su renderizado.

## Evidencias

- `evidencias/tema_claro.png`
- `evidencias/tema_oscuro.png`
- `evidencias/lista_desplazada.png`
- `evidencias/jerarquia_lista.xml`
- `evidencias/resultados_pruebas.xml`
- `evidencias/lint-resumen.txt`
- `resultado_validacion.json`: resultados utilizados para generar el PDF.

## Límites observados

El emulador local no pudo arrancar de forma estable en este equipo, por lo que la ejecución y las capturas se obtuvieron en GitHub Actions. Las pruebas de ejecución cubren API 30; no se afirma haber probado API 24, todas las orientaciones ni todos los tamaños de fuente/pantalla.

Las advertencias locales de Lint corresponden a targetSdk 35, bibliotecas con versiones más recientes disponibles, tamaño nominal de los vectores oficiales y una etiqueta redundante del manifiesto. La app conserva las versiones compiladas y comprobadas. El APK de entrega es una compilación de depuración para evaluación, no una versión firmada para Google Play.

El informe y los demás archivos de documentación se incorporan después del commit verificado; no cambian el comportamiento de la aplicación.

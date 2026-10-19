# Correspondencia con el codelab

| Paso | Implementación |
| --- | --- |
| Proyecto Empty Activity y API mínima 24 | Una ComponentActivity con Compose; minSdk 24 en app/build.gradle.kts |
| Imágenes e icono oficiales | res/drawable/android_superhero1.xml a android_superhero6.xml y mipmap |
| Fuente Cabin | res/font/cabin_regular.ttf y cabin_bold.ttf |
| Modelo Hero en model | model/Hero.kt con @StringRes y @DrawableRes |
| Datos de héroes | model/HeroesDataSource.kt, objeto HeroesRepository |
| Cadenas externas | res/values/strings.xml |
| Color, forma y tipografía | ui/theme/Color.kt, Shape.kt, Type.kt y Theme.kt |
| Tarjeta | HeroesScreen.kt: elevación 2 dp, radio 16 dp, padding 16 dp, imagen 72 dp y radio 8 dp |
| Lista desplazable | LazyColumn e itemsIndexed con clave estable |
| Barra superior centrada | MainActivity.kt: CenterAlignedTopAppBar dentro de Scaffold |
| Edge-to-edge | Theme.kt: WindowCompat y colores/iconos de barras del sistema |
| Tema claro y oscuro | isSystemInDarkTheme, paletas fijas y previews para ambos modos |

Fuente: https://developer.android.com/codelabs/basic-android-kotlin-compose-practice-superheroes

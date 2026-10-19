package com.example.superheroes

import android.content.res.Configuration
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.CenterAlignedTopAppBar
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.tooling.preview.Preview
import com.example.superheroes.model.Hero
import com.example.superheroes.model.HeroesRepository
import com.example.superheroes.ui.theme.SuperheroesTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            SuperheroesTheme { SuperheroesApp() }
        }
    }
}

/** La lista se recibe como parámetro para poder reutilizar y probar la pantalla. */
@Composable
fun SuperheroesApp(heroes: List<Hero> = HeroesRepository.heroes) {
    Scaffold(
        modifier = Modifier.fillMaxSize(),
        topBar = { SuperheroesTopAppBar() }
    ) { padding ->
        HeroesList(heroes = heroes, contentPadding = padding)
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SuperheroesTopAppBar(modifier: Modifier = Modifier) {
    CenterAlignedTopAppBar(
        title = {
            Text(stringResource(R.string.app_name), style = MaterialTheme.typography.displayLarge)
        },
        modifier = modifier
    )
}

@Preview(name = "Tema claro", showBackground = true)
@Preview(name = "Tema oscuro", uiMode = Configuration.UI_MODE_NIGHT_YES, showBackground = true)
@Composable
private fun SuperheroesPreview() {
    SuperheroesTheme { SuperheroesApp() }
}

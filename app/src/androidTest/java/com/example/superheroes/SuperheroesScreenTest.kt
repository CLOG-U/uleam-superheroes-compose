package com.example.superheroes

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.onRoot
import androidx.compose.ui.test.captureToImage
import androidx.compose.ui.test.performScrollTo
import androidx.compose.ui.test.performScrollToNode
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.hasText
import androidx.test.ext.junit.runners.AndroidJUnit4
import com.example.superheroes.model.HeroesRepository
import com.example.superheroes.ui.theme.SuperheroesTheme
import org.junit.Assert.assertEquals
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class SuperheroesScreenTest {
    @get:Rule val compose = createComposeRule()

    @Test fun lightTheme_displaysTitleAndScrollsToLastHero() {
        compose.setContent { SuperheroesTheme(darkTheme = false) { SuperheroesApp() } }
        compose.onNodeWithText("Superheroes").assertIsDisplayed()
        compose.onNodeWithText("Nick the Night and Day").assertIsDisplayed()
        compose.onNodeWithTag("heroes_list").performScrollToNode(hasText("Ability to shift to any form and energize"))
        compose.onNodeWithText("Dynamic Yasmine").assertIsDisplayed()
        compose.onNodeWithText("Ability to shift to any form and energize").assertIsDisplayed()
    }

    @Test fun darkTheme_rendersAndKeepsAllHeroesReachable() {
        compose.setContent { SuperheroesTheme(darkTheme = true) { SuperheroesApp() } }
        compose.onNodeWithText("Superheroes").assertIsDisplayed()
        compose.onNodeWithTag("heroes_list").performScrollToNode(hasText("Dynamic Yasmine"))
        compose.onNodeWithText("Dynamic Yasmine").assertIsDisplayed()
        compose.onNodeWithTag("heroes_list").performScrollToNode(hasText("Nick the Night and Day"))
        compose.onNodeWithText("Nick the Night and Day").assertIsDisplayed()
        // Capturar fuerza el renderizado de la raíz en el tema oscuro.
        compose.onRoot().captureToImage()
        assertEquals(6, HeroesRepository.heroes.size)
        assertEquals(6, HeroesRepository.heroes.map { it.imageRes }.distinct().size)
    }
}

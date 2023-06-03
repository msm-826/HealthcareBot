package com.project.healthcarebot

sealed class ScreenList(val route: String) {
    object LoginScreen: ScreenList("login_screen")
    object MainScreen: ScreenList("main_screen")
}

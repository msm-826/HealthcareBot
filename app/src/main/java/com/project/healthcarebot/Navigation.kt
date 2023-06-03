package com.project.healthcarebot

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.project.healthcarebot.database.MessageViewModel
import com.project.healthcarebot.ui.screens.LoginScreen
import com.project.healthcarebot.ui.screens.MainScreen
import com.project.healthcarebot.speechtotext.InputViewModel

@Composable
fun Navigation(messageViewModel: MessageViewModel, inputViewModel: InputViewModel) {
    val navController = rememberNavController()
    NavHost(
        navController = navController,
        startDestination = ScreenList.LoginScreen.route
    ) {
        composable(route = ScreenList.LoginScreen.route) {
            LoginScreen(navController = navController)
        }
        composable(route = ScreenList.MainScreen.route) {
            MainScreen(messageViewModel = messageViewModel, inputViewModel = inputViewModel)
        }
    }
}
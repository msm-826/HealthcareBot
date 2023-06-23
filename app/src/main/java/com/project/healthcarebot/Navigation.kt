package com.project.healthcarebot

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.project.healthcarebot.database.MessageViewModel
import com.project.healthcarebot.observeconnectivity.ConnectivityViewModel
import com.project.healthcarebot.realtimedatabase.RealtimeDatabaseViewModel
import com.project.healthcarebot.ui.screens.LoginScreen
import com.project.healthcarebot.ui.screens.MainScreen
import com.project.healthcarebot.speechtotext.InputViewModel

@Composable
fun Navigation(
    messageViewModel: MessageViewModel,
    inputViewModel: InputViewModel,
    connectivityViewModel: ConnectivityViewModel,
    realtimeDatabaseViewModel: RealtimeDatabaseViewModel
) {
    val navController = rememberNavController()
    NavHost(
        navController = navController,
        startDestination = ScreenList.LoginScreen.route
    ) {
        composable(route = ScreenList.LoginScreen.route) {
            LoginScreen(
                navController = navController,
                connectivityViewModel = connectivityViewModel
            )
        }
        composable(route = ScreenList.MainScreen.route) {
            MainScreen(
                messageViewModel = messageViewModel,
                inputViewModel = inputViewModel,
                connectivityViewModel = connectivityViewModel,
                realtimeDatabaseViewModel = realtimeDatabaseViewModel
            )
        }
    }
}
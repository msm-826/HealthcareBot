package com.project.healthcarebot

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.room.Room
import com.project.healthcarebot.database.MessageDatabase
import com.project.healthcarebot.database.MessageViewModel
import com.project.healthcarebot.observeconnectivity.ConnectivityViewModel
import com.project.healthcarebot.observeconnectivity.NetworkConnectivityObserver
import com.project.healthcarebot.realtimedatabase.RealtimeDatabaseRepository
import com.project.healthcarebot.realtimedatabase.RealtimeDatabaseViewModel
import com.project.healthcarebot.speechtotext.InputViewModel
import com.project.healthcarebot.speechtotext.RealSpeechToText
import com.project.healthcarebot.ui.theme.HealthcareBotTheme

class MainActivity : ComponentActivity() {
    //initializing the database and passing the dao to MessageViewModel
    private val db by lazy {
        Room.databaseBuilder(
            applicationContext,
            MessageDatabase::class.java,
            "message_db"
        ).build()
    }

    private val messageViewModel by viewModels<MessageViewModel> (
        factoryProducer = {
            object : ViewModelProvider.Factory {
                override fun <T : ViewModel> create(modelClass: Class<T>): T {
                    return MessageViewModel(db.messageDao()) as T
                }
            }
        }
    )

    //Speech to text
    private val inputViewModel by viewModels<InputViewModel> (
        factoryProducer = {
            object : ViewModelProvider.Factory {
                override fun <T : ViewModel> create(modelClass: Class<T>): T {
                    return InputViewModel(RealSpeechToText(applicationContext)) as T
                }
            }
        }
    )

    //Connectivity Manager
    private val connectivityViewModel by viewModels<ConnectivityViewModel> (
        factoryProducer = {
            object : ViewModelProvider.Factory {
                override fun <T : ViewModel> create(modelClass: Class<T>): T {
                    return ConnectivityViewModel(NetworkConnectivityObserver(applicationContext)) as T
                }
            }
        }
    )

    //Firebase Realtime Database
    private val repository = RealtimeDatabaseRepository()
    private val realtimeDatabaseViewModel by viewModels<RealtimeDatabaseViewModel> (
        factoryProducer = {
            object : ViewModelProvider.Factory {
                override fun <T : ViewModel> create(modelClass: Class<T>): T {
                    return RealtimeDatabaseViewModel(repository = repository) as T
                }
            }
        }
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        installSplashScreen().apply {
            setKeepOnScreenCondition {
                messageViewModel.isLoading.value
            }
        }

        setContent {
            HealthcareBotTheme {
                Navigation(
                    messageViewModel = messageViewModel,
                    inputViewModel = inputViewModel,
                    connectivityViewModel = connectivityViewModel,
                    realtimeDatabaseViewModel = realtimeDatabaseViewModel
                )
            }
        }
    }
}
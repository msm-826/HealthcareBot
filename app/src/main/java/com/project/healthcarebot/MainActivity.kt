package com.project.healthcarebot

import android.Manifest
import android.app.Activity
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.provider.Settings
import androidx.activity.ComponentActivity
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.compose.setContent
import androidx.activity.result.contract.ActivityResultContracts
import androidx.activity.viewModels
import androidx.compose.runtime.LaunchedEffect
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.room.Room
import com.project.healthcarebot.database.MessageDatabase
import com.project.healthcarebot.database.MessageViewModel
import com.project.healthcarebot.permission.InternetPermissionTextProvider
import com.project.healthcarebot.permission.PermissionDialog
import com.project.healthcarebot.permission.PermissionViewModel
import com.project.healthcarebot.permission.RecordAudioPermissionTextProvider
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

    //permissions for the application
    private val permissionViewModel by viewModels<PermissionViewModel>()
    private val permissionsToRequest = arrayOf(
        Manifest.permission.RECORD_AUDIO,
        Manifest.permission.INTERNET,
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

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)


        installSplashScreen().apply {
            setKeepOnScreenCondition {
                messageViewModel.isLoading.value
            }
        }

        setContent {
            HealthcareBotTheme {
                val dialogQueue = permissionViewModel.visiblePermissionDialogQueue
                val multiplePermissionResultLauncher = rememberLauncherForActivityResult(
                    contract = ActivityResultContracts.RequestMultiplePermissions(),
                    onResult = { perms ->
                        permissionsToRequest.forEach { permission ->
                            permissionViewModel.onPermissionResult(
                                permission = permission,
                                isGranted = perms[permission] == true
                            )
                        }
                    }
                )

                LaunchedEffect(Unit) {
                    multiplePermissionResultLauncher.launch(permissionsToRequest)
                }

                dialogQueue
                    .reversed()
                    .forEach { permission ->
                        PermissionDialog(
                            permissionTextProvider = when (permission) {
                                Manifest.permission.RECORD_AUDIO -> {
                                    RecordAudioPermissionTextProvider()
                                }

                                Manifest.permission.INTERNET -> {
                                    InternetPermissionTextProvider()
                                }

                                else -> return@forEach
                            },
                            isPermanentlyDeclined = !shouldShowRequestPermissionRationale(
                                permission
                            ),
                            onDismiss = permissionViewModel::dismissDialog,
                            onOkClick = {
                                permissionViewModel.dismissDialog()
                                multiplePermissionResultLauncher.launch(
                                    arrayOf(permission)
                                )
                            },
                            onGoToAppSettingsClick = ::openAppSettings
                        )
                    }

                Navigation(messageViewModel = messageViewModel, inputViewModel = inputViewModel)
            }
        }
    }
}

fun Activity.openAppSettings() {
    Intent(
        Settings.ACTION_APPLICATION_DETAILS_SETTINGS,
        Uri.fromParts("package", packageName, null)
    ).also(::startActivity)
}
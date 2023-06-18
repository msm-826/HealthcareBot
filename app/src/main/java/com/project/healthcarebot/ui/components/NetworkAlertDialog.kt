package com.project.healthcarebot.ui.components

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.WifiOff
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.State
import androidx.compose.ui.window.DialogProperties

@Composable
fun NetworkStateAlertDialog(
    onRetry: () -> Unit,
    onDismiss: () -> Unit,
    showDialog: State<Boolean>,
) {
    if (showDialog.value) {
        AlertDialog(
            onDismissRequest = { onDismiss() },
            icon = {
                   Icon(imageVector = Icons.Default.WifiOff, contentDescription = null)
            },
            title = { Text(text = "No Internet Connection") },
            text = { Text(text = "Please check your internet connection and try again.") },
            confirmButton = {
                TextButton(
                    onClick = { onRetry() }
                ) {
                    Text("Retry")
                }
            },
            dismissButton = {
                TextButton(
                    onClick = { onDismiss() }
                ) {
                    Text("Close")
                }
            },
            properties = DialogProperties(
                dismissOnBackPress = false,
                dismissOnClickOutside = false
            )
        )
    }
}

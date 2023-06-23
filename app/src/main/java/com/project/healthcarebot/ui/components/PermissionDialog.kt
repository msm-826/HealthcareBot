package com.project.healthcarebot.ui.components

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Mic
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.window.DialogProperties
import com.project.healthcarebot.R

@Composable
fun PermissionDialog(
    onRequest: () -> Unit,
    onDismiss: () -> Unit,
    text: String,
    showDialog: Boolean,
) {
    if (showDialog) {
        AlertDialog(
            onDismissRequest = { onDismiss() },
            icon = {
                Icon(imageVector = Icons.Default.Mic, contentDescription = null)
            },
            title = { Text(text = stringResource(R.string.microphone_permission)) },
            text = { Text(text = text) },
            confirmButton = {
                TextButton(
                    onClick = { onRequest() }
                ) {
                    Text(stringResource(R.string.request_permission))
                }
            },
            dismissButton = {
                TextButton(
                    onClick = { onDismiss() }
                ) {
                    Text(stringResource(R.string.close))
                }
            },
            properties = DialogProperties(
                dismissOnBackPress = true,
                dismissOnClickOutside = true
            )
        )
    }
}
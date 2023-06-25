package com.project.healthcarebot.ui.components

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Warning
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.window.DialogProperties
import com.project.healthcarebot.R

@Composable
fun ClearChatDialog(
    onConfirm: () -> Unit,
    onDismiss: () -> Unit,
    showDialog: Boolean,
) {
    if (showDialog) {
        AlertDialog(
            onDismissRequest = { onDismiss() },
            icon = {
                Icon(imageVector = Icons.Default.Warning, contentDescription = null)
            },
            title = { Text(text = stringResource(R.string.clear_chat)) },
            text = { Text(text = stringResource(R.string.clicking_on_yes_will_clear_all_the_chat_content)) },
            confirmButton = {
                TextButton(
                    onClick = { onConfirm() }
                ) {
                    Text(stringResource(R.string.yes))
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
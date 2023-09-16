package com.project.healthcarebot.ui.screens

import android.util.Log
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.Edit
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.DrawerState
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Dialog
import com.project.healthcarebot.R
import com.project.healthcarebot.database.Contacts
import com.project.healthcarebot.database.MessageViewModel
import kotlinx.coroutines.CoroutineScope

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ContactScreen(
    messageViewModel: MessageViewModel,
    drawerState: DrawerState,
    scope: CoroutineScope,
) {
    val contacts by messageViewModel.getFullContacts().collectAsState(initial = emptyList())
    val (showAddContactDialog, setShowAddContactDialog) = remember { mutableStateOf(false) }
    val (showUpdateContactDialog, setShowUpdateContactDialog) = remember { mutableStateOf(false) }

    val nameForDialog = remember { mutableStateOf("") }
    val numberForDialog = remember { mutableStateOf("") }
    val idForDialog = remember { mutableStateOf(-1) }

    Scaffold(
        topBar = { AppBar("Medicare" ,drawerState, scope) },
    ) {paddingValues->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
        ) {
            Row {
                Text(
                    text = "Saved Contacts",
                    style = MaterialTheme.typography.headlineLarge,
                    modifier = Modifier
                        .padding(16.dp)
                        .weight(1f)
                )
                IconButton(
                    onClick = { setShowAddContactDialog(true) },
                    modifier = Modifier
                        .padding(end = 18.dp)
                        .align(Alignment.CenterVertically)
                ) {
                    Icon(
                        imageVector = Icons.Default.Add,
                        contentDescription = null,
                        modifier = Modifier.size(32.dp)
                    )
                }
            }

            LazyColumn(
                verticalArrangement = Arrangement.spacedBy(16.dp),
                modifier = Modifier.padding(16.dp)
            ) {
                items(contacts) { contact ->
                    Card(
                        modifier = Modifier.fillMaxWidth(),
                        shape = RoundedCornerShape(32.dp)
                    ) {
                        Row {
                            Icon(
                                painter = painterResource(id = R.drawable.user),
                                contentDescription = null,
                                modifier = Modifier
                                    .size(50.dp)
                                    .align(Alignment.CenterVertically)
                                    .padding(start = 16.dp)
                                    .clip(CircleShape)
                            )
                            Column(
                                modifier = Modifier
                                    .padding(16.dp)
                                    .weight(1f)
                            ) {
                                Text(
                                    text = contact.name,
                                    style = MaterialTheme.typography.bodyMedium
                                )
                                Text(
                                    text = contact.contactNumber.toString(),
                                    style = MaterialTheme.typography.bodyMedium
                                )
                            }
                            IconButton(
                                onClick = {
                                    nameForDialog.value = contact.name
                                    numberForDialog.value = contact.contactNumber.toString()
                                    idForDialog.value = contact.id!!
                                    setShowUpdateContactDialog(true)
                                },
                                modifier = Modifier
                                    .align(Alignment.CenterVertically)
                                    .padding(2.dp)
                            ) {
                                Icon(
                                    imageVector = Icons.Default.Edit,
                                    contentDescription = null,
                                )
                            }
                            IconButton(
                                onClick = {
                                    contact.id?.let { messageViewModel.deleteContact(it) }
                                },
                                modifier = Modifier
                                    .align(Alignment.CenterVertically)
                                    .padding(2.dp)
                            ) {
                                Icon(
                                    imageVector = Icons.Default.Delete,
                                    contentDescription = null,
                                )
                            }
                        }
                    }
                }
            }
        }
    }

    ContactDialog(
        dialogHeading = "Add Contact",
        dialogActionButton = "Add",
        showDialog = showAddContactDialog,
        onProceed = { _, name, number ->
            messageViewModel.addContact(
                Contacts(name = name, contactNumber = number.toLong())
            )
        },
        onDismissRequest = { setShowAddContactDialog(false) }
    )

    ContactDialog(
        dialogHeading = "Update Contact",
        dialogActionButton = "Update",
        showDialog = showUpdateContactDialog,
        onProceed = { id, name, number ->
            Log.d("contact", "name: $name, number: $number")
            if (id != null) {
                messageViewModel.updateContact(
                    id,name, number.toLong()
                )
            }
        },
        onDismissRequest = { setShowUpdateContactDialog(false) },
        nameFromColumn = nameForDialog.value,
        numberFromColumn = numberForDialog.value,
        idFromColumn = idForDialog.value
    )
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ContactDialog(
    dialogHeading: String,
    dialogActionButton: String,
    showDialog: Boolean,
    onProceed: (Int?, String, String) -> Unit,
    onDismissRequest: () -> Unit,
    nameFromColumn: String = "",
    numberFromColumn: String = "",
    idFromColumn: Int = -1,
) {
    if(showDialog) {
        Dialog(
            onDismissRequest = onDismissRequest
        ) {
            Column(
                modifier = Modifier
                    .clip(RoundedCornerShape(32.dp))
                    .background(MaterialTheme.colorScheme.onPrimary)
                    .padding(16.dp)
            ) {
                Text(dialogHeading, style = MaterialTheme.typography.headlineSmall)
                Spacer(modifier = Modifier.height(16.dp))

                val (name, setName) = remember { mutableStateOf(nameFromColumn) }
                val (number, setNumber) = remember { mutableStateOf(numberFromColumn) }
                val id = remember { mutableStateOf(idFromColumn) }

                OutlinedTextField(
                    value = name,
                    onValueChange = { setName(it) },
                    label = { Text("Name") },
                    singleLine = true,
                    shape = RoundedCornerShape(32.dp),
                    modifier = Modifier.fillMaxWidth()
                )
                Spacer(modifier = Modifier.height(8.dp))
                OutlinedTextField(
                    value = number,
                    onValueChange = { setNumber(it) },
                    label = { Text(text = "Ph. Number") },
                    singleLine = true,
                    shape = RoundedCornerShape(32.dp),
                    keyboardOptions = KeyboardOptions(
                        keyboardType = KeyboardType.Phone
                    ),
                    modifier = Modifier.fillMaxWidth()
                )
                Spacer(modifier = Modifier.height(16.dp))

                Row(horizontalArrangement = Arrangement.End) {
                    Button(onClick = { onDismissRequest() }) {
                        Text("Cancel")
                    }
                    Spacer(modifier = Modifier.width(8.dp))
                    Button(onClick = {
                        onProceed(id.value, name, number)
                        onDismissRequest()
                    }) {
                        Text(dialogActionButton)
                    }
                }
            }
        }
    }
}
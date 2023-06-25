package com.project.healthcarebot.ui.screens

import android.util.Log
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.spring
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.imePadding
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ClearAll
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Menu
import androidx.compose.material.icons.filled.Mic
import androidx.compose.material.icons.filled.Send
import androidx.compose.material3.Card
import androidx.compose.material3.CenterAlignedTopAppBar
import androidx.compose.material3.DrawerState
import androidx.compose.material3.DrawerValue
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.LocalContentColor
import androidx.compose.material3.LocalTextStyle
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.ModalDrawerSheet
import androidx.compose.material3.ModalNavigationDrawer
import androidx.compose.material3.NavigationDrawerItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.rememberDrawerState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.MutableState
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.scale
import androidx.compose.ui.focus.onFocusChanged
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.graphics.SolidColor
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalFocusManager
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.google.accompanist.permissions.ExperimentalPermissionsApi
import com.google.accompanist.permissions.isGranted
import com.google.accompanist.permissions.rememberPermissionState
import com.project.healthcarebot.R
import com.project.healthcarebot.database.Message
import com.project.healthcarebot.database.MessageViewModel
import com.project.healthcarebot.observeconnectivity.ConnectivityObserver
import com.project.healthcarebot.observeconnectivity.ConnectivityViewModel
import com.project.healthcarebot.realtimedatabase.RealtimeDatabaseViewModel
import com.project.healthcarebot.speechtotext.InputViewModel
import com.project.healthcarebot.speechtotext.RecordState
import com.project.healthcarebot.ui.components.ClearChatDialog
import com.project.healthcarebot.ui.components.LoadingAnimation
import com.project.healthcarebot.ui.components.NetworkStateAlertDialog
import com.project.healthcarebot.ui.components.PermissionDialog
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.launch
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MainScreen(
    messageViewModel: MessageViewModel,
    inputViewModel: InputViewModel,
    connectivityViewModel: ConnectivityViewModel,
    realtimeDatabaseViewModel: RealtimeDatabaseViewModel,
    modifier: Modifier = Modifier
){
    val drawerState = rememberDrawerState(initialValue = DrawerValue.Closed)
    val scope = rememberCoroutineScope()

    ModalNavigationDrawer(
        drawerState = drawerState,
        drawerContent = {
            DrawerContentOfModalDrawer(
                messageViewModel = messageViewModel,
                drawerState = drawerState,
                scope = scope,
                modifier = modifier
            )
        },
        content = {
            MainContentOfModalDrawer(
                messageViewModel = messageViewModel,
                inputViewModel = inputViewModel,
                connectivityViewModel = connectivityViewModel,
                realtimeDatabaseViewModel = realtimeDatabaseViewModel,
                drawerState = drawerState,
                scope = scope,
                modifier = modifier
            )
        }
    )
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MainContentOfModalDrawer(
    messageViewModel: MessageViewModel,
    inputViewModel: InputViewModel,
    connectivityViewModel: ConnectivityViewModel,
    realtimeDatabaseViewModel: RealtimeDatabaseViewModel,
    drawerState: DrawerState,
    scope: CoroutineScope,
    modifier: Modifier = Modifier
) {
    Scaffold(
        topBar = { AppBar("Medicare" ,drawerState, scope) },
        modifier = modifier,
    ) {paddingValues ->
        BoxWithConstraints {
            // height calculated based on text field and mic button height (initially -> max-height - 72 - 100)
            // for making the lazy column only span up to text-field and not overlap
            ChatContent(
                messageViewModel = messageViewModel,
                modifier = modifier
                    .padding(paddingValues)
                    .height(this.maxHeight - 180.dp)
            )
            Column(
                modifier = modifier
                    .fillMaxHeight()
                    .navigationBarsPadding()
                    .imePadding(),
                verticalArrangement = Arrangement.Bottom,
            ) {
                UserInputTextField(
                    messageViewModel = messageViewModel,
                    inputViewModel = inputViewModel,
                    connectivityViewModel = connectivityViewModel,
                    realtimeDatabaseViewModel = realtimeDatabaseViewModel
                )
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DrawerContentOfModalDrawer(
    messageViewModel: MessageViewModel,
    drawerState: DrawerState,
    scope: CoroutineScope,
    modifier: Modifier = Modifier,
) {
    ModalDrawerSheet(
        drawerShape = RectangleShape,
        modifier = modifier
    ) {
        val selectedItemId = remember { mutableIntStateOf(1) }
        var showClearChatDialog by remember { mutableStateOf(false) }

        Column(modifier = Modifier.fillMaxSize()) {
            Spacer(modifier = Modifier.height(16.dp))
            DrawerItem(
                id = 1,
                selectedItemId = selectedItemId,
                label = stringResource(R.string.home),
                icon = Icons.Default.Home,
                drawerState = drawerState,
                scope = scope
            )
            DrawerItem(
                id = 2,
                selectedItemId = selectedItemId,
                label = stringResource(R.string.clearAll),
                icon = Icons.Default.ClearAll,
                drawerState = drawerState,
                scope = scope,
                onSelect = {
                    showClearChatDialog = true
                }
            )
        }

        ClearChatDialog(
            onConfirm = {
                messageViewModel.clearAllMessages()
                showClearChatDialog = false
            },
            onDismiss = { showClearChatDialog = false },
            showDialog = showClearChatDialog
        )
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DrawerItem(
    id: Int,
    selectedItemId: MutableState<Int>,
    label: String,
    icon: ImageVector,
    drawerState: DrawerState,
    scope: CoroutineScope,
    modifier: Modifier = Modifier,
    onSelect: () -> Unit = {}
) {
    val isSelected = id == selectedItemId.value
    NavigationDrawerItem(
        label = { Text(text = label) },
        selected = isSelected,
        icon = { Icon(imageVector = icon, contentDescription = null) },
        onClick = {
            scope.launch { drawerState.close() }
            selectedItemId.value = when (id) {
                2 -> 1 // when clicked on Clear Chat history no need for navigation
                else -> id
            }
            onSelect()
        },
        modifier = modifier.padding(vertical = 4.dp, horizontal = 16.dp)
    )
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AppBar(
    title: String,
    drawerState: DrawerState,
    scope: CoroutineScope,
    modifier: Modifier = Modifier
) {
    CenterAlignedTopAppBar(
        modifier = modifier,
        title = { Text(text = title) },
        navigationIcon = {
            Box(
                modifier = Modifier
                    .size(64.dp)
                    .clickable(onClick = {
                        scope.launch {
                            if (drawerState.isOpen) {
                                drawerState.close()
                            } else {
                                drawerState.open()
                            }
                        }
                    })
                    .padding(16.dp)
            ) {
                Icon(Icons.Filled.Menu, contentDescription = null)
            }
        }
    )
}

@Composable
fun ChatContent(
    messageViewModel: MessageViewModel,
    modifier: Modifier = Modifier
) {
    val messages by messageViewModel.getFullMessage().collectAsState(initial = emptyList())
    val scrollState = rememberLazyListState()

    LazyColumn(
        modifier = modifier
            .fillMaxSize()
            .padding(horizontal = 8.dp),
        verticalArrangement = Arrangement.spacedBy(32.dp),
        state = scrollState,
    ) {
        items(messages) {message ->
            Spacer(modifier = Modifier.height(8.dp))
            Row(modifier = Modifier
                .fillMaxSize()
                .padding(end = 32.dp), horizontalArrangement = Arrangement.Start) {
                Card(shape = RoundedCornerShape(0.dp, 32.dp, 32.dp, 32.dp)) {
                    Column(
                        modifier = Modifier.padding(16.dp)
                    ) {
                        Text(
                            text = message.messageText,
                            style = MaterialTheme.typography.bodyLarge
                        )
                        Text(
                            text = convertTimestampToDateTime(message.messageTimeStamp),
                            style = MaterialTheme.typography.bodyLarge
                        )
                    }
                }
            }
            Spacer(modifier = Modifier.height(8.dp))
            if (message.replyText == null || message.replyTimeStamp == null) {
                Spacer(modifier = Modifier.height(16.dp))
                Row(
                    modifier = Modifier.fillMaxSize(),
                    horizontalArrangement = Arrangement.End
                ) {
                    LoadingAnimation(modifier = Modifier.padding(bottom = 16.dp))
                }
            } else {
                Row(modifier = Modifier
                    .fillMaxSize()
                    .padding(start = 32.dp), horizontalArrangement = Arrangement.End) {
                    Card(shape = RoundedCornerShape(32.dp, 0.dp, 32.dp, 32.dp)) {
                        Column(
                            modifier = Modifier.padding(16.dp),
                        ) {
                            Text(
                                text = message.replyText,
                                style = MaterialTheme.typography.bodyLarge
                            )
                            Text(
                                text = convertTimestampToDateTime(message.replyTimeStamp),
                                style = MaterialTheme.typography.bodyLarge
                            )
                        }
                    }
                }
            }
        }
    }

    if (messages.isNotEmpty()) {
        LaunchedEffect(messages) {
            Log.d("scrollTag", "scrolled")
            scrollState.animateScrollToItem(messages.size - 1)
        }
    }
}

private fun convertTimestampToDateTime(timestamp: Long): String {
    val sdf = SimpleDateFormat("dd/M/yyyy hh:mm:ss", Locale.getDefault())
    val dateTime = sdf.format(Date(timestamp))
    return "Sent at: $dateTime"
}

@OptIn(ExperimentalPermissionsApi::class)
@Composable
fun MicrophoneButton(
    inputViewModel: InputViewModel,
    connectivityViewModel: ConnectivityViewModel,
    modifier: Modifier = Modifier
) {
    val networkStatus by connectivityViewModel.networkStatus.collectAsState()
    val micPermissionState = rememberPermissionState(android.Manifest.permission.RECORD_AUDIO)
    var showPermissionDialog by remember { mutableStateOf(false) }

    var pressed by remember { mutableStateOf(false) }
    val buttonScale by animateFloatAsState(
        targetValue = if (pressed) 0.8f else 1f,
        animationSpec = spring(
            stiffness = Spring.StiffnessLow,
            dampingRatio = Spring.DampingRatioMediumBouncy,
            visibilityThreshold = 0.001f
        ),
        label = "Button Scale"
    )

    Box(
        modifier = modifier
            .size(72.dp)
            .scale(buttonScale)
            .clip(CircleShape)
            .background(color = MaterialTheme.colorScheme.primary)
            .pointerInput(Unit) {
                detectTapGestures(
                    onPress = {
                        when (networkStatus) {
                            ConnectivityObserver.Status.Losing,
                            ConnectivityObserver.Status.Lost,
                            ConnectivityObserver.Status.Unavailable -> {
                                connectivityViewModel.toggleDialog(true)
                            }

                            else -> {
                                Log.d(
                                    "permissionTag",
                                    "Permission Status: ${micPermissionState.status}"
                                )
                                if (micPermissionState.status.isGranted) {
                                    showPermissionDialog = false
                                    pressed = true
                                    inputViewModel.send(RecordState.StartRecord)
                                    awaitRelease()
                                    pressed = false
                                    inputViewModel.send(RecordState.EndRecord)
                                } else {
                                    showPermissionDialog = true
                                }
                            }
                        }
                    }
                )
            },
        contentAlignment = Alignment.Center
    ) {
        Icon(
            imageVector = Icons.Filled.Mic,
            contentDescription = stringResource(id = R.string.mic)
        )
    }

    PermissionDialog(
        onRequest = {
            micPermissionState.launchPermissionRequest()
            showPermissionDialog = false
        },
        onDismiss = { showPermissionDialog = false },
        text = stringResource(R.string.request_microphone_permission),
        showDialog = showPermissionDialog
    )

    NetworkStateAlertDialog(
        onRetry = {
            if (networkStatus == ConnectivityObserver.Status.Available) {
                connectivityViewModel.toggleDialog(false)
            }
        },
        onDismiss = { connectivityViewModel.toggleDialog(false)},
        showDialog = connectivityViewModel.showDialog
    )
}

@Composable
fun UserInputTextField(
    messageViewModel: MessageViewModel,
    inputViewModel: InputViewModel,
    connectivityViewModel: ConnectivityViewModel,
    realtimeDatabaseViewModel: RealtimeDatabaseViewModel,
    modifier: Modifier = Modifier
) {
    var textFieldFocusState by remember { mutableStateOf(false) }
    val focusManager = LocalFocusManager.current
    val sendButtonStatus = messageViewModel.replyFetched.value && inputViewModel.inputTextState.inputText.isNotBlank()
    val networkStatus by connectivityViewModel.networkStatus.collectAsState()
    val replyStatus by realtimeDatabaseViewModel.replyStatus.collectAsState(null)
    val context = LocalContext.current

    LaunchedEffect(Unit) {
        messageViewModel.initializeTextToSpeech(context)
    }

    Row {
        Surface(
            tonalElevation = 2.dp,
            shape = RoundedCornerShape(32.dp),
            modifier = modifier
                .fillMaxWidth()
                .weight(1f)
                .padding(start = 8.dp, bottom = 8.dp)
        ) {
            Row(modifier = modifier.height(104.dp)) {
                BasicTextField(
                    decorationBox = {
                            innerTextField ->
                        Row {
                            if (inputViewModel.inputTextState.inputText.isEmpty()) {
                                Text("Message : ")
                            }
                            innerTextField()
                        }
                    },
                    value = inputViewModel.inputTextState.inputText,
                    onValueChange = { newValue -> inputViewModel.onTextValueChange(newValue) },
                    keyboardOptions = KeyboardOptions(
                        keyboardType = KeyboardType.Text,
                        imeAction = ImeAction.Send
                    ),
                    keyboardActions = KeyboardActions(
                        onSend = {
                            Log.d("NetworkTag", "network status in keyboard send: $networkStatus")
                            if (sendButtonStatus) {
                                when (networkStatus) {
                                    ConnectivityObserver.Status.Losing,
                                    ConnectivityObserver.Status.Lost,
                                    ConnectivityObserver.Status.Unavailable -> {
                                        connectivityViewModel.toggleDialog(true)
                                    }

                                    else -> {
                                        messageViewModel.addMessage(
                                            Message(
                                                messageText = inputViewModel.inputTextState.inputText,
                                                messageTimeStamp = System.currentTimeMillis(),
                                                id = messageViewModel.currentMessageIndex.value
                                            )
                                        )

                                        //sending to firebase realtime database
                                        realtimeDatabaseViewModel.addEntry(inputViewModel.inputTextState.inputText)

                                        focusManager.clearFocus()
                                        textFieldFocusState = false
                                        inputViewModel.onTextValueChange("")
                                    }
                                }
                            }
                        }
                    ),
                    maxLines = 4,
                    cursorBrush = SolidColor(LocalContentColor.current),
                    textStyle = LocalTextStyle.current.copy(color = LocalContentColor.current),
                    modifier = modifier
                        .padding(start = 16.dp)
                        .align(Alignment.CenterVertically)
                        .onFocusChanged { state ->
                            textFieldFocusState = state.isFocused
                        }
                        .weight(1f)
                )

                IconButton(
                    onClick = {
                        Log.d("NetworkTag", "network status in send: $networkStatus")
                        when (networkStatus) {
                            ConnectivityObserver.Status.Losing,
                            ConnectivityObserver.Status.Lost,
                            ConnectivityObserver.Status.Unavailable -> {
                                connectivityViewModel.toggleDialog(true)
                            }

                            else -> {
                                //adding to local database
                                messageViewModel.addMessage(
                                    Message(
                                        messageText = inputViewModel.inputTextState.inputText,
                                        messageTimeStamp = System.currentTimeMillis(),
                                        id = messageViewModel.currentMessageIndex.value
                                    )
                                )

                                //sending to firebase realtime database
                                realtimeDatabaseViewModel.addEntry(inputViewModel.inputTextState.inputText)

                                focusManager.clearFocus()
                                textFieldFocusState = false
                                inputViewModel.onTextValueChange("")
                            }
                        }
                    },
                    enabled = sendButtonStatus,
                    modifier = modifier
                        .align(Alignment.CenterVertically)
                        .padding(8.dp)
                ) {
                    Icon(
                        imageVector = Icons.Filled.Send,
                        contentDescription = stringResource(id = R.string.send),
                        modifier = modifier.size(24.dp)
                    )
                }
            }
        }

        LaunchedEffect(replyStatus) {
            replyStatus?.reply?.let {reply ->
                messageViewModel.updateMessage(
                    id = messageViewModel.currentMessageIndex.value,
                    replyText = reply,
                    replyTimeStamp = System.currentTimeMillis()
                )
                messageViewModel.speakText(reply)
            }
        }

        MicrophoneButton(
            inputViewModel = inputViewModel,
            connectivityViewModel = connectivityViewModel,
            modifier = modifier
                .align(Alignment.CenterVertically)
                .padding(start = 8.dp, top = 16.dp, end = 8.dp, bottom = 16.dp)
        )
    }
    NetworkStateAlertDialog(
        onRetry = {
            if (networkStatus == ConnectivityObserver.Status.Available) {
                connectivityViewModel.toggleDialog(false)
            }
        },
        onDismiss = { connectivityViewModel.toggleDialog(false)},
        showDialog = connectivityViewModel.showDialog
    )
}
package com.project.healthcarebot.ui.screens

import android.util.Log
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.ElevatedButton
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.project.healthcarebot.R
import com.project.healthcarebot.ScreenList
import com.project.healthcarebot.observeconnectivity.ConnectivityObserver
import com.project.healthcarebot.observeconnectivity.ConnectivityViewModel
import com.project.healthcarebot.ui.components.NetworkStateAlertDialog

@Composable
fun LoginScreen(
    navController: NavController,
    connectivityViewModel: ConnectivityViewModel,
    modifier: Modifier = Modifier
) {
    val networkStatus by connectivityViewModel.networkStatus.collectAsState()

    Surface {
        Column(
            modifier = modifier
                .fillMaxSize(),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Spacer(modifier = Modifier.weight(1f))
            ElevatedButton(
                onClick = {
                    Log.d("NetworkTag", "networkStatus: $networkStatus")
                    when (networkStatus) {
                        ConnectivityObserver.Status.Losing,
                        ConnectivityObserver.Status.Lost,
                        ConnectivityObserver.Status.Unavailable -> {
                            connectivityViewModel.toggleDialog(true)
                        }
                        else -> {
                            navController.navigate(ScreenList.MainScreen.route)
                        }
                    }
                },
                shape = RoundedCornerShape(8.dp),
                elevation = ButtonDefaults.buttonElevation(defaultElevation = 6.dp),
                modifier = modifier
                    .padding(32.dp)

            ) {
                Icon(
                    painter = painterResource(id = R.drawable.google_logo),
                    contentDescription = null,
                    modifier = modifier
                        .size(16.dp)
                )
                Spacer(modifier = Modifier.size(12.dp))
                Text(
                    text = stringResource(id = R.string.get_started),
                    style = MaterialTheme.typography.titleLarge
                )
            }
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
}
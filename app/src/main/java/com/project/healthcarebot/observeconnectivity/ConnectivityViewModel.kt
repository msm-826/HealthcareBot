package com.project.healthcarebot.observeconnectivity

import androidx.compose.runtime.State
import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class ConnectivityViewModel(
    private val connectivityObserver: ConnectivityObserver
) : ViewModel() {

    private val _showDialog = mutableStateOf(false)
    val showDialog: State<Boolean> get() = _showDialog

    fun toggleDialog(show: Boolean) {
        _showDialog.value = show
    }

    private val _networkStatus = MutableStateFlow(ConnectivityObserver.Status.Unavailable)
    val networkStatus: StateFlow<ConnectivityObserver.Status> = _networkStatus

    init {
        viewModelScope.launch {
            connectivityObserver.observe().collect() { status ->
                _networkStatus.value = status
            }
        }
    }
}
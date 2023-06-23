package com.project.healthcarebot.realtimedatabase

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.launch

class RealtimeDatabaseViewModel(private val repository: RealtimeDatabaseRepository): ViewModel() {
    private val _replyStatus = MutableStateFlow<MessageRealtimeDatabaseModel?>(null)
    val replyStatus: Flow<MessageRealtimeDatabaseModel?> = _replyStatus

    init {
        viewModelScope.launch {
            repository.listenForReplies().collect { newStatus ->
                _replyStatus.value = newStatus
            }
            Log.d("realtimeDatabase", "reply status in init block: $replyStatus")
        }
    }

    fun addEntry(query: String) {
        viewModelScope.launch {
            repository.insertMessageModel(MessageRealtimeDatabaseModel(query, ""))
        }
    }
}
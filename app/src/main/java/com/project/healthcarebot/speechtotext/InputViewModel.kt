package com.project.healthcarebot.speechtotext

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch

data class InputTextState(
    var inputText: String = ""
)

sealed class RecordState {
    object StartRecord : RecordState()
    object EndRecord : RecordState()
    data class Update(val text: String): RecordState()
}

class InputViewModel(private val stt: SpeechToText): ViewModel() {
    // Text field input
    var inputTextState by mutableStateOf(InputTextState())
        private set

    fun onTextValueChange(newValue: String) {
        inputTextState = inputTextState.copy(inputText = newValue)
    }

    init {
        viewModelScope.launch {
            with(stt) {
                text.collect { result ->
                    send(RecordState.Update(result))
                }
            }
        }
    }

    fun send(action: RecordState) {
        when (action) {
            RecordState.StartRecord -> {
                stt.start()
            }
            RecordState.EndRecord -> {
                stt.stop()
            }
            is RecordState.Update -> {
                inputTextState = inputTextState.copy(inputText = inputTextState.inputText + action.text)
            }
        }
    }
}
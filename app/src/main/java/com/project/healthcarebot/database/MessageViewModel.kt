package com.project.healthcarebot.database

import android.content.Context
import android.speech.tts.TextToSpeech
import android.util.Log
import androidx.compose.runtime.MutableState
import androidx.compose.runtime.State
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.async
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import java.util.Locale

class MessageViewModel(
    private val messageDao: MessageDao
) : ViewModel() {
    fun getFullMessage(): Flow<List<Message>> = messageDao.getAllMessages()

    private val _currentMessageIndex: MutableState<Int> = mutableIntStateOf(0)
    val currentMessageIndex: State<Int>
        get() = _currentMessageIndex

    //initially set as true for enabling the send button
    private val _replyFetched: MutableState<Boolean> = mutableStateOf(true)
    val replyFetched: State<Boolean>
        get() = _replyFetched

    private val _isLoading = MutableStateFlow(true)
    val isLoading = _isLoading.asStateFlow()

    init {
        viewModelScope.launch {
            val deferred = async { setIndex(messageDao.getLastMessageIndex() + 1) }
            deferred.await()
            val deferred1 = async {delay(1500) }
            deferred1.await()
            _isLoading.value = false
        }
    }

    private fun setIndex(index: Int) {
        _currentMessageIndex.value = index
    }

    fun addMessage(message: Message) {
        viewModelScope.launch {
            val deferred = async { messageDao.insertMessage(message) }
            deferred.await()
            _replyFetched.value = false
        }
    }

    fun updateMessage(id: Int, replyText: String, replyTimeStamp: Long) {
        viewModelScope.launch {
            val deferred = async { messageDao.updateMessage(id, replyText, replyTimeStamp) }
            deferred.await()
            setIndex(_currentMessageIndex.value + 1)
            _replyFetched.value = true
        }
    }

    fun clearAllMessages() {
        viewModelScope.launch {
            val deferred = async { messageDao.clearMessage() }
            deferred.await()
            setIndex(0)
            _replyFetched.value = true
        }
    }

    private var textToSpeech: TextToSpeech? = null
    fun initializeTextToSpeech(context: Context) {
        textToSpeech = TextToSpeech(context) { status ->
            if (status == TextToSpeech.SUCCESS) {
                Log.d("tts", "initialized successfully")
                textToSpeech?.language = Locale.UK
                textToSpeech?.setSpeechRate(1.0f)
            } else {
                Log.d("tts", "failed to initialize")
            }
        }
    }

    fun speakText(text: String) {
        textToSpeech?.speak(text, TextToSpeech.QUEUE_FLUSH, null, null)
    }

    override fun onCleared() {
        super.onCleared()
        textToSpeech?.stop()
        textToSpeech?.shutdown()
    }
}
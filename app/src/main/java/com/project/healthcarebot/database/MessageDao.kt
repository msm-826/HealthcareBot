package com.project.healthcarebot.database

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query
import kotlinx.coroutines.flow.Flow

@Dao
interface MessageDao {
    @Insert
    suspend fun insertMessage(message: Message)

    @Query("SELECT * FROM message")
    fun getAllMessages(): Flow<List<Message>>

    @Query("UPDATE message SET replyText = :replyText, replyTimeStamp = :replyTimeStamp WHERE id = :messageIndex")
    suspend fun updateMessage(messageIndex: Int, replyText: String, replyTimeStamp: Long)

    @Query("DELETE FROM message")
    suspend fun clearMessage()

    @Query("SELECT MAX(id) FROM message")
    suspend fun getLastMessageIndex(): Int
}

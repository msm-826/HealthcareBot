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

@Dao
interface ContactDao {
    @Insert
    suspend fun insertContact(contacts: Contacts)

    @Query("UPDATE contacts SET name = :name, contactNumber = :number WHERE id = :id")
    suspend fun updateContact(id: Int, name: String, number: Long)

    @Query("SELECT * FROM contacts")
    fun getAllContacts(): Flow<List<Contacts>>

    @Query("DELETE FROM contacts where id = :id")
    suspend fun deleteContact(id: Int)

    @Query("SELECT contactNumber from contacts where name = :name")
    suspend fun getNumber(name: String): Long
}

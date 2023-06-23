package com.project.healthcarebot.realtimedatabase

import android.util.Log
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.ValueEventListener
import com.google.firebase.database.ktx.database
import com.google.firebase.ktx.Firebase
import kotlinx.coroutines.channels.awaitClose
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.callbackFlow
import kotlinx.coroutines.tasks.await

class RealtimeDatabaseRepository {
    private val database =
        Firebase.database("https://healthcarebot-901fa-default-rtdb.asia-southeast1.firebasedatabase.app/")
    private lateinit var databaseListener: ValueEventListener

    suspend fun insertMessageModel(entry: MessageRealtimeDatabaseModel) {
        database.getReference("entries")
            .setValue(entry)
            .addOnCompleteListener {
                if (it.isSuccessful) {
                    Log.d("realtimeDatabase", "Item added to the realtime database")
                }
            }
            .addOnFailureListener {
                Log.d("realtimeDatabase", "Failed to add item to the realtime database")
            }
            .await()
    }

    fun listenForReplies(): Flow<MessageRealtimeDatabaseModel?> = callbackFlow {
        databaseListener = object : ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {
                val entry = snapshot.getValue(MessageRealtimeDatabaseModel::class.java)
                if (entry != null) {
                    if (entry.reply?.isNotBlank() == true) {
                        trySend(entry)
                        Log.d("realtimeDatabase", "reply ready in the the server: ${entry.reply}")
                    }
                }
            }

            override fun onCancelled(error: DatabaseError) {
                Log.d("realtimeDatabase", "Failed to listen for replies from the server: ${error.message}")
            }
        }

        database.getReference("entries")
            .addValueEventListener(databaseListener)
        Log.d("realtimeDatabase", "Started listening for replies from the server")

        awaitClose {
            database.getReference("entries")
                .removeEventListener(databaseListener)
        }
    }
}
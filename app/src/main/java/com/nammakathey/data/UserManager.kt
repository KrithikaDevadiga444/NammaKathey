package com.nammakathey.data

import android.content.Context
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken

data class UserProfile(
    val id: String,
    val name: String,
    val avatarResId: Int,
    val earnedBadges: MutableList<String> = mutableListOf()
)

object UserManager {
    private const val PREFS_NAME = "multi_user_prefs"
    private const val KEY_USERS = "users_list"
    private const val KEY_CURRENT_USER_ID = "current_user_id"

    private val gson = Gson()

    fun getUsers(context: Context): List<UserProfile> {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        val json = prefs.getString(KEY_USERS, null)
        return if (json != null) {
            val type = object : TypeToken<List<UserProfile>>() {}.type
            gson.fromJson(json, type)
        } else {
            emptyList()
        }
    }

    fun deleteUser(context: Context, userId: String) {
        val users = getUsers(context).toMutableList()
        users.removeAll { it.id == userId }
        saveUsers(context, users)
    }

    fun saveUsers(context: Context, users: List<UserProfile>) {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        prefs.edit().putString(KEY_USERS, gson.toJson(users)).apply()
    }

    fun getCurrentUser(context: Context): UserProfile? {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        val currentId = prefs.getString(KEY_CURRENT_USER_ID, null) ?: return null
        return getUsers(context).find { it.id == currentId }
    }

    fun setCurrentUser(context: Context, userId: String) {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        prefs.edit().putString(KEY_CURRENT_USER_ID, userId).apply()
    }

    fun addUser(context: Context, name: String, avatarResId: Int): UserProfile {
        val users = getUsers(context).toMutableList()
        val newUser = UserProfile(
            id = System.currentTimeMillis().toString(),
            name = name,
            avatarResId = avatarResId
        )
        users.add(newUser)
        saveUsers(context, users)
        setCurrentUser(context, newUser.id)
        return newUser
    }

    fun addBadgeToCurrentUser(context: Context, badgeId: String) {
        val currentUser = getCurrentUser(context) ?: return
        if (!currentUser.earnedBadges.contains(badgeId)) {
            currentUser.earnedBadges.add(badgeId)
            val users = getUsers(context).toMutableList()
            val index = users.indexOfFirst { it.id == currentUser.id }
            if (index != -1) {
                users[index] = currentUser
                saveUsers(context, users)
            }
        }
    }

    fun hasBadge(context: Context, badgeId: String): Boolean {
        return getCurrentUser(context)?.earnedBadges?.contains(badgeId) == true
    }

    fun isLoggedIn(context: Context): Boolean {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        return prefs.getString(KEY_CURRENT_USER_ID, null) != null
    }

    fun logout(context: Context) {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        prefs.edit().remove(KEY_CURRENT_USER_ID).apply()
    }
}

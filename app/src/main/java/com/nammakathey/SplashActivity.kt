package com.nammakathey

import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import androidx.appcompat.app.AppCompatActivity
import com.nammakathey.data.DataProvider
import com.nammakathey.data.UserManager

class
SplashActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // Load data in background
        Thread {
            DataProvider.loadData(applicationContext)
            
            Handler(Looper.getMainLooper()).postDelayed({
                val users = UserManager.getUsers(applicationContext)
                if (users.isNotEmpty()) {
                    startActivity(Intent(this, SelectProfileActivity::class.java))
                } else {
                    startActivity(Intent(this, LoginActivity::class.java))
                }
                finish()
            }, 1500)
        }.start()
    }
}
